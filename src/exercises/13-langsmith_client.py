import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langsmith import Client
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

client = Client()

prompt = client.pull_prompt("agent-pull-request-creator:dev")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
inputs = {
    "changes_summary": "Implementation of cache system to improve performance",
    "files_changed": "src/cache.py, tests/test_cache.py, README.md",
    "issue_number": "42",
    "branch_name": "feature/add-cache-system",
    "breaking_changes": "No",
    "testing_done": "Unit tests added with 95% coverage",
}
prompt_str = prompt.format(**inputs)
result = model.invoke(prompt_str)
print_llm_result(prompt_str, result)
