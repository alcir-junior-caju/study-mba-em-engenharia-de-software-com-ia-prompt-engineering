import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
llm2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
llm3 = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)


spec_to_schema = PromptTemplate.from_template(
    """Você é um engenheiro de backend sênior.
A partir da seguinte especificação de produto, extraia um esquema JSON mínimo com campos e tipos.
Retorne apenas JSON. Sem comentários.

Escreva todo o código usando blocos de código markdown.

Especificação:
{spec}
"""
) | llm1 | StrOutputParser()

schema_to_routes = PromptTemplate.from_template(
    """Você é um desenvolvedor Go sênior.
Dado o esquema JSON abaixo, projete rotas REST e esboce handlers Go idiomáticos para CRUD.
Mantenha conciso, orientado para produção e mostre snippets de código.

Escreva todo o código usando blocos de código markdown.

Esquema JSON:
{schema_json}
"""
) | llm2 | StrOutputParser()

commit_message = PromptTemplate.from_template(
    """Você é um desenvolvedor pragmático.
Escreva uma mensagem de commit convencional de uma única linha resumindo a nova API baseada no esquema e rotas.

Esquema:
{schema_json}

Rotas e handlers:
{routes}
"""
) | llm3 | StrOutputParser()


spec_text = """Precisamos de uma API de Produtos.
Campos: id (uuid), name (string, obrigatório), description (string), price (float, > 0), stock (int, >= 0).
Devemos suportar listagem com paginação, criação, busca por id, atualização e exclusão.
"""

schema_json = spec_to_schema.invoke({"spec": spec_text})
routes = schema_to_routes.invoke({"schema_json": schema_json})
commit = commit_message.invoke({"schema_json": schema_json, "routes": routes})


result_content = f"""# Resultado do Encadeamento de Prompts

## ESQUEMA (Gerado por gemini-2.5-flash)
{schema_json}

## ROTAS & HANDLERS (Go) (Gerado por gemini-2.5-flash)
{routes}

## COMMIT (Gerado por gemini-2.5-flash)
{commit}

---
**Modelos do Pipeline:**
- Passo 1: gemini-2.5-flash
- Passo 2: gemini-2.5-flash
- Passo 3: gemini-2.5-flash

"""

with open("prompt_chaining_result.md", "w", encoding="utf-8") as f:
    f.write(result_content)

print("Resultado salvo em prompt_chaining_result.md")
