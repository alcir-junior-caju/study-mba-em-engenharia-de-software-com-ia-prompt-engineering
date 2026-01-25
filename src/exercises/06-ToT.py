import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils import print_llm_result

load_dotenv()

msg1 = """
Você é um engenheiro de software sênior.
Um usuário relata que uma requisição de API para o endpoint `/users` está demorando 5 segundos para responder, o que é muito lento.
Pense de forma Tree of Thought:
- Gere pelo menos 3 causas possíveis diferentes para essa latência.
- Para cada causa, raciocine passo a passo sobre quão provável ela é e como você a verificaria.
- Em seguida, compare as ramificações e escolha a mais plausível como hipótese principal.
- Finalize com uma ação recomendada para depurar ou corrigir o problema.
"""

msg2 = f"""
Você está projetando um serviço que processa milhões de imagens diariamente.
Pense de forma Tree of Thought:
- Gere pelo menos 3 opções de arquitetura diferentes.
- Para cada opção, raciocine passo a passo sobre escalabilidade, custo e complexidade.
- Compare as opções.
- Escolha o melhor trade-off e explique por que é superior às outras.
- Finalize com "Resposta Final: " + a opção escolhida.
"""

msg3 = f"""
Você está projetando um serviço que processa milhões de imagens diariamente.
Pense de forma Tree of Thought:
- Pense em pelo menos 3 opções de arquitetura diferentes.
- Para cada opção, raciocine passo a passo sobre escalabilidade, custo e complexidade.
- Compare as opções.
- Escolha o melhor trade-off e explique por que é superior às outras.
- Finalize com "Resposta Final: " + a opção escolhida com 6 palavras ou menos.

- RETORNE APENAS A RESPOSTA FINAL, SEM QUALQUER OUTRO TEXTO.
"""

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


# response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
# response3 = llm.invoke(msg3)

# print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
# print_llm_result(msg3, response3)
