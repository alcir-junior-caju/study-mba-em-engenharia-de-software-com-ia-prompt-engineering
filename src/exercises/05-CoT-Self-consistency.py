import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

msg1 = """
Questão: Em um endpoint de API que retorna uma lista de usuários e suas postagens, o desenvolvedor escreveu:

users := db.FindAllUsers()
for _, u := range users {
    u.Posts = db.FindPostsByUserID(u.ID)
}

Quantas consultas ao banco de dados esse código executará se houver N usuários?

Gere 3 caminhos de raciocínio diferentes passo a passo.
No final, resuma as respostas e escolha a mais consistente, ignorando outliers.
Se houver 3 respostas diferentes, APENAS responda: "Não consigo encontrar uma resposta consistente".
"""


# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
print_llm_result(msg1, response1)
