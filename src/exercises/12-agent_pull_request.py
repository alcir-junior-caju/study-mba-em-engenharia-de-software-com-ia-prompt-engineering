import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

try:
    from prompt_registry import registry
except ImportError:
    from ..prompt_registry import registry

load_dotenv()

from dataclasses import dataclass, asdict

@dataclass
class PullRequestRequest:
    """Request model for pull request creation."""
    changes_summary: str
    files_changed: str
    issue_number: str = ""
    branch_name: str = ""
    breaking_changes: str = "No"
    testing_done: str = ""

request = PullRequestRequest(
    changes_summary="Implementation of cache system to improve performance",
    files_changed="src/cache.py, tests/test_cache.py, README.md",
    issue_number="42",
    branch_name="feature/add-cache-system",
    breaking_changes="No",
    testing_done="Unit tests added with 95% coverage"
)

prompt = registry.get_prompt("agent-pull-request-creator")
from langchain_core.prompts.loading import load_prompt
prompt_template = load_prompt(prompt.path)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke(prompt_template.format(**asdict(request)))
print_llm_result(prompt_template.format(**asdict(request)), result)
