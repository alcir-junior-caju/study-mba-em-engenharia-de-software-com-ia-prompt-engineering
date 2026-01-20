import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

msg1 = """
EXEMPLO:
Pergunta: Qual é a capital da França?
Resposta: Paris

Pergunta: Qual é a capital do Brasil?
Resposta:
"""

msg2 = """
Exemplo:
Entrada: "Conexão com banco de dados perdida às 10:34."
Saída: ERROR

Agora classifique:
Entrada: "Uso de disco em 85%."
Saída:
"""


msg3 = """
Classifique a severidade do log.

Exemplo 1:
Entrada: "Conexão com banco de dados perdida às 10:34."
Saída: ERROR

Exemplo 2:
Entrada: "Uso de disco em 85%."
Saída: WARNING

Exemplo 3:
Entrada: "Tempo de resposta do banco de dados está acima do limite em 30ms"
Saída: WARNING

Exemplo 4:
Entrada: "Usuário logado com sucesso."
Saída: INFO

Agora classifique:
Entrada: "Tempo de resposta da API está acima do limite."
Saída:
"""

msg4 = """
Classifique a severidade do log.

Exemplo 1:
Entrada: "Conexão com banco de dados perdida às 10:34."
Saída: ERROR

Exemplo 2:
Entrada: "Uso de disco em 85%."
Saída: WARNING

Exemplo 3:
Entrada: "Usuário logado com sucesso."
Saída: INFO

Exemplo 4:
Entrada: "Arquivo não encontrado: config.yaml"
Saída: ERROR

Exemplo 5:
Entrada: "Alto uso de memória detectado: 75%"
Saída: WARNING

Exemplo 6:
Entrada: "Tarefa em segundo plano finalizada"
Saída: INFO

Exemplo 7:
Entrada: "Tentando novamente requisição ao gateway de pagamento"
Saída: ERROR

Exemplo 8:
Entrada: "Uso de disco em 90%"
Saída: ERROR   // ambíguo: poderia ser WARNING

Exemplo 9:
Entrada: "Latência da API está acima do limite"
Saída: WARNING

Exemplo 10:
Entrada: "Backup agendado concluído"
Saída: INFO

Exemplo 11:
Entrada: "Pouco espaço em disco: 15% restante"
Saída: WARNING

Exemplo 12:
Entrada: "Pouco espaço em disco: 5% restante"
Saída: ERROR   // ambíguo: WARNING ou ERROR?

Exemplo 13:
Entrada: "Aquecimento de cache concluído"
Saída: INFO

Exemplo 14:
Entrada: "Tempo limite de conexão, tentando novamente..."
Saída: WARNING   // ambíguo: poderia ser ERROR

Exemplo 15:
Entrada: "Falha de autenticação para usuário admin"
Saída: ERROR

Agora classifique:
Entrada: "Uso de CPU está em 95%."
Saída:
"""

# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
print_llm_result(msg4, response4)
# print(response2)
