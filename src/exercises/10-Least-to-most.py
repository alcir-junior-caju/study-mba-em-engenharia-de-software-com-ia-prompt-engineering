import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

msg = """
Você é um engenheiro de backend Go sênior.

Problema: Precisamos projetar um serviço encurtador de URLs em Go.

Use o método Least-to-Most Prompting:
1. Comece listando os subproblemas que precisam ser resolvidos como uma lista de tarefas. Use checkboxes markdown: [ ] para pendente, [x] para concluído.
2. Conforme resolver cada subproblema, atualize a lista de tarefas marcando como [x] e escreva a solução logo abaixo.
3. Continue até que todos os itens estejam resolvidos.
4. No final, combine todas as soluções em um design integrado final para o encurtador de URLs.

Restrições:
- O serviço deve ser implementado em Go.
- URLs curtas devem ser únicas e fáceis de gerar.
- Deve suportar endpoints: encurtar uma URL, recuperar a URL original.
- Use um armazenamento em memória inicialmente, mas mencione como poderia escalar com um banco de dados.
- Inclua validação mínima e tratamento de erros.
- Mantenha as explicações concisas e estruturadas.

Formato de saída:
- Lista de tarefas com checkboxes (atualizando conforme o progresso)
- Cada subproblema resolvido explicado com raciocínio e snippets mínimos de código Go
- Design final combinado

"""

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke(msg)
print_llm_result(msg, result)
