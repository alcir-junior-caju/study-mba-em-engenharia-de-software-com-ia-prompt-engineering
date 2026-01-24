### Zero-Shot

Zero-Shot Prompting é uma técnica onde o modelo de linguagem recebe apenas a descrição da tarefa, **sem nenhum exemplo** anterior. O objetivo é avaliar a capacidade do modelo de generalizar e resolver o problema com base na instrução textual.

**Estudo**

Essa abordagem ganhou destaque com o paper **"Language Models are Few-Shot Learners”** de Brown et al. (2020), publicado pela OpenAI. Nesse estudo, os pesquisadores demostraram que modelos como o GPT-3 conseguem realizar tarefas complexas apenas com uma boa descrição da tarefa no prompt, mesmo sem exemplos anteriores.

**Quando Utilizar**

- A tarefa é simples e bem conhecida pelo modelo (por exemplo, perguntas factuais).
- Não há tempo ou espaço para adicionar exemplos.
- Deseja se testar a capacidade base do modelo de interpretar a tarefa.
- É preciso processar uma grande quantidade de tarefas distintas e breves com o menor custo de tokens.

**[Link do Paper](https://arxiv.org/abs/2005.14165)**

**Vantagens**

- Baixo custo de preparação do prompt.
- Alta escalabilidade.
- Rápido para experimentação.

**Limitações**

- Pode falhar em tarefas mais complexas ou menos frequentes para o modelo.
- Não oferece controle sobre o formato da resposta.
- Dependente da compreensão implícita do modelo sobre a tarefa.
- Alucinação de respostas: o modelo pode gerar conteúdo incorreto com alta confiança.
- Variação com pequenas mudanças na formatação: prompts semanticamente equivalentes podem gerar resultados diferentes.
- Dificuldade em tarefas de raciocínio lógico, análises comparativas ou inferência fora do contexto factual.

### Estratégias de Mitigação

Mesmo mantendo a proposta de não fornecer exemplos, algumas práticas ajudam a melhorar resultados com Zero-Shot Prompting:

**Especificidade:**

Instruções claras, que detalhem o que se espera, aumentam a precisão.

- Exemplo ruim: “Analise esse código”
- Melhorado: “Explique o que esse código GO faz e liste possíveis problemas de performance”

**Linguagem declarativa e orientada à Tarefa:**

Preferência por comandos diretos a perguntas abertas.

- Exemplo: “Liste os principais motivos para erros de memória da linguagem GO”

**Sinalização do formato esperado:**

Solicitação explicita de listas, tópicos, parágrafos curtos, etc.

- Exemplo: "Responda em forma de tópicos” ou “Escreva uma explicação de 3 parágrafos”

### In-Context Instruction Learning

Mesmo sem exemplos, prompts estruturados com clareza (persona, formato, objetivo) ajudam o modelo a responder melhor. Instruções mais detalhadas melhoram a performance Zero-Shot.

- Antes: “Explique o que é uma goRoutine”
- Depois: “Você é um especialista em GO. Escreva dois parágrafos explicando o que é uma goRoutine, como ela é usada e quais são suas limitações. Seja claro, técnico e direto”

### Boas práticas da Microsoft

- Especificar o papel do modelo (”Você é um especialista em …”)
- Especificar a saída desejada ("Responda em tópicos” ou “Formato JSON”)
- Garantir que o modelo compreende a meta ("Seu objetivo é …“)

**Exemplo:** "Você é um consultor técnico. Seu trabalho é analisar este trecho de código e sugerir melhorias de performance. Responda em tópicos e justifique cada sugestão”

**Importante:**

Apesar desse exemplo fornecer instruções estruturadas, **não apresenta nenhum exemplo anterior**. O modelo precisa inferir a tarefa com base apenas na instrução natural.

*[Link do codex pagina da microsoft](https://microsoft.github.io/prompt-engineering/)*
