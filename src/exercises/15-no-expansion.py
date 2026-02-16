import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

# Initialize Gemini model wrapper
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    input_variables=["question"],
    template=(
        "You are a technology assistant.\n"
        "Answer the following question:\n\n"
        "{question}"
    ),
)

question = "Explain about the LangChain and LangGraph"

# Render prompt and invoke Gemini
prompt_text = prompt.format(question=question)
result = llm.invoke(prompt_text)

print_llm_result(prompt_text, result)
print(len(result.content) if hasattr(result, 'content') else 0)
