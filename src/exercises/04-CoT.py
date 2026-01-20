import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()
msg1 = """
Classifique a severidade do log.

Entrada: "Uso de disco em 85%."
Responda apenas com INFO, WARNING, ou ERROR.
"""

msg2 = """
Classifique a severidade do log.

Entrada: "Uso de disco em 85%."
Pense passo a passo sobre por que isso é INFO, WARNING ou ERROR.
No final, dê apenas a resposta final após "Resposta:".
"""


msg3 = """
Pergunta: Quantos "r" existem na palavra "strawberry"?
Responda apenas com o número de "r".
"""

msg4 = """
Pergunta: Quantos "r" existem na palavra "strawberry"?
Explique passo a passo, decompondo cada letra em marcadores, apontando os "r" antes de dar a resposta final.
Dê o resultado final após "Resposta:".
"""

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model

response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
print_llm_result(msg4, response4)
# print(response2)
