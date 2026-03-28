"""
Correctness evaluation: Comparing predictions against reference outputs.

Demonstrates labeled evaluators that use reference outputs for comparison.
"""
from langsmith import evaluate
from langsmith.evaluation import LangChainStringEvaluator
from pathlib import Path
import sys

EVAL_DIR = Path(__file__).parent.parent.parent / "evaluation"
sys.path.insert(0, str(EVAL_DIR))

from shared.clients import get_openai_client
from shared.prompts import load_yaml_prompt, execute_text_prompt
from shared.evaluators import prepare_with_reference

# Configuration
DATASET_NAME = "evaluation_basic_dataset"
PROMPTS_DIR = EVAL_DIR / "01-basic" / "prompts"

# Setup
oai_client = get_openai_client()
prompt = load_yaml_prompt("correctness_eval.yaml", prompts_dir=PROMPTS_DIR)


def run_correctness_evaluation(inputs: dict) -> dict:
    """Target function for evaluate()."""
    return execute_text_prompt(prompt, inputs, oai_client, input_key="code")


# Labeled evaluators with reference outputs
evaluators = [
    LangChainStringEvaluator(
        "labeled_score_string",
        config={"criteria": "correctness", "normalize_by": 10},
        prepare_data=prepare_with_reference
    ),
    LangChainStringEvaluator(
        "labeled_score_string",
        config={"criteria": "relevance", "normalize_by": 10},
        prepare_data=prepare_with_reference
    )
]

# Run evaluation
results = evaluate(
    run_correctness_evaluation,
    data=DATASET_NAME,
    evaluators=evaluators,
    experiment_prefix="CorrectnessEval",
    max_concurrency=2
)

print("="*80)
print(f"EXPERIMENT: {results.experiment_name}")
print("="*80)
