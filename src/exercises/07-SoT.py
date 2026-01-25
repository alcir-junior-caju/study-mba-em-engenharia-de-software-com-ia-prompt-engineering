import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

msg1 = """
Você é um engenheiro de backend sênior. Um desenvolvedor júnior perguntou como otimizar consultas SQL para melhor desempenho.
Siga a abordagem Skeleton of Thought:

Passo 1: Gere apenas o esqueleto da sua resposta em 3–5 tópicos concisos.
Passo 2: Expanda cada tópico em uma explicação clara e detalhada com exemplos.
Certifique-se de que a resposta final seja estruturada e fácil de seguir.
"""

msg2 = f"""
Você é um arquiteto de software. Quero que você produza um Architecture Decision Record (ADR) sobre escolher PostgreSQL ao invés de MongoDB.

Siga a abordagem Skeleton of Thought:
Passo 1: Primeiro, retorne apenas o esqueleto do ADR como cabeçalhos de seção (sem explicações ainda).
Use a estrutura padrão de ADR com 5 seções: Contexto, Decisão, Alternativas Consideradas, Consequências, Referências.
Passo 2: Após mostrar o esqueleto, expanda cada seção com conteúdo claro e detalhado.
Mantenha o ADR final profissional, estruturado e fácil de ler.
"""

msg3 = f"""
Você é um desenvolvedor Go sênior. Quero que você me ajude a planejar uma API REST para gerenciar produtos em Go.

Siga a abordagem Skeleton of Thought:

Passo 1: Retorne apenas o esqueleto da solução em 6–8 tópicos concisos.
O esqueleto deve cobrir: definição do modelo de dados em Go (structs), escolha do framework HTTP ou net/http, roteamento, handlers, validações, camada de banco de dados, tratamento de erros e estrutura do projeto. Não expanda ainda.

Passo 2: Expanda cada tópico com detalhes técnicos claros, exemplos e boas práticas de Go.
Inclua snippets de código de exemplo em Go (structs, handlers, routes) e considerações sobre pacotes (por exemplo, chi, ou net/http), tratamento de erros com Go idiomático e como organizar o projeto em pacotes (handlers, models, db).
Use linguagem concisa e profissional.

A API deve implementar operações CRUD para produtos com os campos: id, name, description, price, stock.
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
# response2 = llm.invoke(msg2)
# response3 = llm.invoke(msg3)

print_llm_result(msg1, response1)
# print_llm_result(msg2, response2)
# print_llm_result(msg3, response3)
