
import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

system = ("system",
"""Você é um professor universitário de ciência da computação que é muito técnico e explica
conceitos com definições formais e pseudocódigo.""")

system2 = ("system", """Você é um estudante do ensino médio que está começando a aprender programação.
Você não é muito técnico e prefere explicar conceitos com palavras simples e exemplos.""")

user = ("user", "Explique recursão em 50 palavras.")

chat_prompt = ChatPromptTemplate([system, user])
chat_prompt2 = ChatPromptTemplate([system2, user])
messages = chat_prompt.format_messages()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
result = model.invoke(messages)
print_llm_result(str(system), result)

result2 = model.invoke(chat_prompt2.format_messages())
print_llm_result(str(system2), result2)
