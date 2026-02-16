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
class CodeReviewRequest:
    """Request model for code review."""
    code_diff: str
    language: str = "python"
    repo_rules: str = "Apply general best practices"
    security_level: str = "standard"
    review_focus: str = "general"

request = CodeReviewRequest(
    code_diff="""
    + def calculate_total(items):
    +     total = 0
    +     for item in items:
    +         total = total + item['price'] * item['quantity']
    +     return total
    """,
    language="python",
    repo_rules="Use type hints and docstrings",
    security_level="standard",
    review_focus="quality and performance"
)

prompt = registry.get_prompt("agent-code-reviewer")
from langchain_core.prompts.loading import load_prompt
prompt_template = load_prompt(prompt.path)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke(prompt_template.format(**asdict(request)))
print_llm_result(prompt_template.format(**asdict(request)), result)
