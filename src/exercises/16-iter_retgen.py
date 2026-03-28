from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from langchain_google_genai import ChatGoogleGenerativeAI
from utils import print_llm_result

# Initialize Gemini model wrapper
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# ========= Enhanced Prompt Templates =========

# Prompt to generate initial draft with MANY specific gaps
draft_prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are an expert assistant with limited initial knowledge.\n"
        "Answer the following question, but you MUST mark MANY specific details as missing.\n"
        "Use [MISSING: ...] markers for:\n"
        "- Specific version numbers and release dates\n"
        "- Technical specifications and parameters\n"
        "- Performance metrics and benchmarks\n"
        "- Comparison data between different versions\n"
        "- Implementation details and code examples\n"
        "- Real-world use cases and case studies\n"
        "- Limitations and known issues\n"
        "- Future roadmap and upcoming features\n\n"
        "Be thorough in identifying what specific information would make the answer complete.\n"
        "Start with a basic overview but mark MANY specific details as missing.\n\n"
        "Do not generate more than 5 MISSING Markers."
        "Question: {question}\n\n"
        "Answer:"
    ),
)

# Prompt to generate queries from gaps - now more specific
query_prompt = PromptTemplate(
    input_variables=["draft"],
    template=(
        "You received the following draft with gaps:\n{draft}\n\n"
        "For each [MISSING: ...] marker, provide information to fill that gap.\n"
        "Format each as: 'For [MISSING: topic]: provide the actual information'\n"
        "Be specific and provide real data when possible.\n"
        "Example: 'For [MISSING: version numbers]: LangChain is at version 0.1.0, LangGraph at 0.2.0'\n"
        "List information for each gap, maximum 5 items."
    ),
)

# Prompt to fill gaps gradually based on complexity
fill_prompt = PromptTemplate(
    input_variables=["question", "draft", "queries", "iteration"],
    template=(
        "Original question: {question}\n\n"
        "Current draft (iteration {iteration}):\n{draft}\n\n"
        "Information to help fill the gaps:\n{queries}\n\n"
        "CRITICAL INSTRUCTIONS:\n"
        "1. You MUST replace AT LEAST 1-2 [MISSING: ...] markers with concrete information\n"
        "2. ACTUALLY REPLACE the text '[MISSING: xyz]' with real content - don't keep the marker\n"
        "3. Use the information above to guide what content to add\n"
        "4. Do NOT add any new [MISSING:] markers - only fill or keep existing ones\n"
        "5. If you cannot fill a gap with certainty, keep it as [MISSING: ...]\n\n"
        "Example of what to do:\n"
        "- WRONG: '[MISSING: version numbers and release dates]' (keeping the marker)\n"
        "- RIGHT: 'LangChain version 0.1.0 was released in January 2024' (replacing with content)\n\n"
        "Important: This is iteration {iteration}. You MUST make progress by filling gaps.\n\n"
        "Rewrite the ENTIRE answer with the [MISSING:] markers replaced:"
    ),
)

# New prompt to identify additional gaps after filling
expansion_prompt = PromptTemplate(
    input_variables=["draft"],
    template=(
        "Review this draft answer:\n{draft}\n\n"
        "Identify areas that could benefit from MORE specific information.\n"
        "Add new [MISSING: ...] markers for:\n"
        "- Technical details that were glossed over\n"
        "- Specific examples that would clarify concepts\n"
        "- Comparative data that would add context\n"
        "- Implementation specifics that developers would need\n\n"
        "Return the same text but with ADDITIONAL [MISSING: ...] markers for deeper details:"
    ),
)


def run_prompt(prompt_template, **kwargs):
    text = prompt_template.format(**kwargs)
    res = llm.invoke(text)
    content = res.content if hasattr(res, 'content') else str(res)
    return content, text, res

# ========= Enhanced Main Function =========

def iter_retgen_multi(question: str, max_iters: int = 10):
    """
    Perform iterative retrieval and generation with multiple natural rounds.
    Continues until all gaps are filled or max iterations reached.

    Args:
        question: The question to answer
        max_iters: Maximum number of iterations to refine the answer

    Returns:
        The final refined answer
    """

    # Generate initial draft with many gaps
    draft, draft_text, draft_res = run_prompt(draft_prompt, question=question)
    print("\n=== Initial Draft (with many gaps) ===")
    print_llm_result(draft_text, draft_res)

    # Count initial gaps
    initial_gaps = draft.count("[MISSING:")
    print(f"\n Initial gaps identified: {initial_gaps}")

    actual_iterations = 0
    consecutive_no_progress = 0

    # Iterative refinement - continue until complete or max iterations
    for iteration in range(max_iters):
        actual_iterations = iteration + 1
        current_gaps = draft.count("[MISSING:")

        # Check if we've reached completion
        if current_gaps == 0:
            print("\n All gaps filled!")

            # Only expand in early iterations, not indefinitely
            if iteration < 2:  # Only expand in first couple iterations
                print("Checking for areas to expand...")
                new_draft, expansion_text, expansion_res = run_prompt(expansion_prompt, draft=draft)
                print_llm_result(expansion_text, expansion_res)
                draft = new_draft
                current_gaps = draft.count("[MISSING:")

                if current_gaps == 0:
                    print(" Answer is comprehensive and complete!")
                    break
                else:
                    print(f" Identified {current_gaps} new areas for expansion")
                    consecutive_no_progress = 0  # Reset counter
            else:
                print("✅ Answer is complete after multiple refinements!")
                break  # Stop after filling all gaps in later iterations

        print(f"\n{'='*60}")
        print(f" ITERATION {iteration + 1}")
        print(f" Current gaps to address: {current_gaps}")
        print('='*60)

        # Generate queries for missing information
        queries, queries_text, queries_res = run_prompt(query_prompt, draft=draft)
        print("\n=== Generated Queries ===")
        print_llm_result(queries_text, queries_res)

        # Fill gaps with new information (gradual filling based on iteration)
        fill_input = {
            "question": question,
            "draft": draft,
            "queries": queries,
            "iteration": iteration + 1
        }
        new_draft, fill_text, fill_res = run_prompt(fill_prompt, **fill_input)
        draft = new_draft

        # Show refined answer
        print("\n=== Refined Answer ===")
        print_llm_result(fill_text, fill_res)

        # Report progress
        new_gaps = draft.count("[MISSING:")
        gaps_filled = current_gaps - new_gaps
        print(f"\nProgress: Filled {gaps_filled} gaps, {new_gaps} remaining")

        # Check if we're making progress
        if gaps_filled == 0:
            consecutive_no_progress += 1
            if consecutive_no_progress >= 3:
                print("\nNo progress in 3 consecutive iterations. Stopping.")
                break
        else:
            consecutive_no_progress = 0

    print(f"\n{'='*60}")
    print(f" REFINEMENT COMPLETE after {actual_iterations} iterations")
    print(f"{'='*60}")

    return draft


# ========= Main Execution =========

if __name__ == "__main__":
    # Using a complex technical question that naturally requires multiple iterations
    demonstration_question = (
        "Explain about the LangChain and LangGraph"
    )

    print(f"'{demonstration_question}'")
    print("#"*60)

    # Run with more iterations to ensure completion
    final_answer = iter_retgen_multi(demonstration_question, max_iters=10)

    print("\n" + "="*60)
    print("FINAL COMPLETE ANSWER:")
    print("="*60)
    print(final_answer)

    # Final statistics
    final_gaps = final_answer.count("[MISSING:")
    initial_length = len(demonstration_question)
    final_length = len(final_answer)

    print("\n" + "="*60)
    print(f"FINAL STATISTICS:")
    print(f"   - Remaining gaps: {final_gaps}")
    print(f"   - Answer expansion: {final_length / initial_length:.1f}x original question length")
    print("="*60)
