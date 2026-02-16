import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_core.prompts.loading import load_prompt
from langsmith import Client

try:
    from prompt_registry import registry
except ImportError:
    from ..prompt_registry import registry

load_dotenv()

prompt = registry.get_prompt("agent-pull-request-creator")
prompt_template = load_prompt(prompt.path)

client = Client()
url = client.push_prompt(
    "agent-pull-request-creator",
    object=prompt_template,
    tags=[
        f"v{prompt.version}",
        f"model: {prompt.model}",
    ],
    description=prompt.description,
)
print("Prompt pushed to LangSmith:", url)
