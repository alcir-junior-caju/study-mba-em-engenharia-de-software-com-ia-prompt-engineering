import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

msg1 = "Qual é a capital do Brasil?"

msg2 = """
Encontre a intenção do usuário no seguinte texto:
Estou procurando um restaurante em São Paulo que tenha boa avaliação para comida japonesa.
"""

msg3 = "Qual é a capital do Brasil? Responda apenas com o nome da cidade."

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
