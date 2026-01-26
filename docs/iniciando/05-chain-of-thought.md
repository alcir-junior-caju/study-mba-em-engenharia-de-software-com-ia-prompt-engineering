## Chain of Thought (CoT)

**Chain of Thought (CoT)** é uma técnica de engenharia de prompt que instrui o modelo a externalizar seu raciocínio **passo a passo**, permitindo que ele resolva tarefas que exigem lógica, múltiplas etapas ou operações intermediárias. Em vez de apenas dar a resposta final, o modelo mostra seu processo de pensamento.

**Estudo**

A técnica foi formada no paper **”Chain-of-Thought Prompting Elicits Reasoning in Large Models”** de **Wei et al. (2020)**, demonstrando que grandes modelos como PaLM e GPT-3 apresentam desempenho significativamente superior em tarefas de raciocínio lógico e aritmético quando induzidos a pensar de forma encadeada.

**Advanced Reasoning**

- O CoT é a **fundação para os recursos de Advanced Reasoning em LLMs**, como GPT-4, Claude e Gemini. Esses modelos foram treinados com instruções e exemplos que incentivam raciocínio multietapas, explicações lógicas e reflexões auditáveis.
- Chain of Thought permite que o modelo não apenas **chegue a resposta**, mas também **demonstre como chegou até la**, oferecendo transparência, confiabilidade e contexto técnico.

**Quando Utilizar**

- Diagnóstico de falhas e bugs
- Planejamento lógico de processos
- Argumentações comparativas entre abordagens

**[Link do Paper](https://arxiv.org/abs/2201.11903)**

**Vantagens**

- **Raciocínio explícito**: permite que o modelo demonstre seu processo de pensar passo a passo
- **Maior resolução de problemas complexos**: melhora significativamente o desempenho em tarefas que exigem múltiplas etapas de raciocínio
- **Transparência e auditabilidade**: torna o processo decisório do modelo visível, facilitando a verificação da lógica utilizada

**Limitações**

- Gera saídas mais longas, o que pode ser custoso em prompts com limite de tokens
- Pode introduzir ruído se o modelo gerar cadeias de pensamento incorretas
- Requer modelo suficiente treinado para compreender e aplicar o passo a passo com qualidade
- Se não combinado com critérios de parada, pode prolongar desnecessariamente o raciocínio
    - “Pense passo a passo até chegar a uma conclusão única final”
    - “Pare quando tiver certeza da resposta”
    - “Após concluir as etapas, retorne apenas a resposta final”

**Estrutura e exemplos**

> Você é um engenheiro de software com 20 anos de experiência em sistemas concorrentes e distribuídos. Seu trabalho é revisar o código a seguir e identificar falhas ou melhorias. Pense passo a passo, justificando cada ponto com base nas práticas recomendadas em GO. Ao final, revise a sequência de etapas e forneça uma conclusão objetiva.
>
> Use a seguinte estrutura:
>
> Etapa 1: <descrição>
>
> Etapa 2: <descrição>
>
> Resultado final: <conclusão>

**Debugging com raciocínio lógico**

Prompt:

> Você é um desenvolvedor GO. Analise o seguinte código e explique, passo a passo, por que ele pode causar um erro:

```go
var list []string
fmt.Println(list[0])
```

**Resposta esperada**

- **Etapa 1**: A variável `list` é declarada como slice de strings, mas não foi inicializada.
- **Etapa 2**: Um slice não inicializado tem tamanho zero `(len(list) == 0)`
- **Etapa 3**: Acessar um `list[0]` viola o limite do slice, pois não há elementos.
- **Resultado final**: O programa entra em pânico (panic) por acesso fora dos limites.

**Refatoração com justificativas técnicas**

Prompt:

> Reescreva a função abaixo seguindo o padrão `early return` e explique cada modificação passo a passo.

```go
func Validate(u User) error {
	var err error
	if u.Email == "" {
		err = errors.New("Required Email")
	} else {
		if u.Senha == "" {
			err = errors.New("Required Password")
		} else {
		 err = nil
		}
	}
	return err
}
```

**Resposta esperada**

- **Etapa 1**: Segue a versão reescrita da função utilizando o padrão `early return`, seguida da explicação detalhada de cada modificação:

```go
func Validate(u User) error {
	if u.Email == "" {
		return errors.New("Required Email")
	}
	if u.Senha == "" {
		return errors.New("Required Password")
	}
	return nil
}
```

- **Etapa 2**: Identificar o uso de lógica encadeada desnecessária, a função original usava blocos `if/else` aninhados que resultavam em múltiplas verificações antes de decidir qual erro retornar. Isso torna o fluxo mais difícil de seguir.
- **Etapa 3**: Aplicar `early return` para as condições de erro, a técnica de `early return` consiste em  retornar o mais cedo possível quando uma condição de erro é satisfeita.
- **Etapa 4**: Eliminar a variável `err`, como cada caso de erro é retornado diretamente, não há necessidade de declarar uma variável intermediária para armazenar o erro. Isso reduz o escopo da variável e torna o código mais direto e limpo.

**Planejamento básico**

Prompt:

> Descreva todas as etapas na migração de uma aplicação monolítica para microserviços baseados em eventos. Para cada etapa, inclua pré-requisitos, riscos e validações. Organize o raciocínio em sequência lógica e valide antes de concluir.

**Resposta esperada**

- **Etapa 1**: Identificação dos domínios de negócio.
- **Etapa 2**: Definição de fronteiras de contexto (bounded contexts).
- **Etapa 3**: Extração de serviços mais isolados com menor acoplamento.
- **Etapa 4**: Implementação de mensageria (ex.: RabbitMQ) com fallback e DLQs.
- **Etapa 5**: Implementação de observabilidade: logs, métricas e tracing.
- **Etapa 6**: Testes de regressão antes de redirecionar o tráfego.
- **Resultado final**: Arquitetura distribuída validada com ganhos e resiliência e escalabilidade.

### Estratégias inspiradas na Anthropic Prompt Library

- **Persona + Objetivo + Estrutura clara**: contextualiza a função do modelo e define o tom da resposta.
- **Chamado à reflexão lógica**: “Pense passo a passo”, “Justifique cada etapa”.
- **Formato de saída padronizado**: etapas numeradas + conclusão objetiva.
- **Autoavaliação embutida**: "Verifique se todos os passos estão consistentes”.
- **Critério de parada lógica**: Encerrar ao atingir o raciocínio final.

**Técnicas avançadas de CoT com delimitações estruturais (Anthropic-style)**

Modelos como Claude e GPT respondem melhor quando o prompt apresenta **delimitações estruturais explicitas**. Uma técnica bastante utilizada pela Anthropic, segundo sua própria Claude Prompt Library, é o uso de **delimitadores XML-like** como `<thought>`, `<reasoning>`, `<answer>`, etc., **separar raciocínio da resposta final**, melhorar a legibilidade, e tornar o prompt mais auditável.

**Variações comuns de marcadores**

- `<context>` - delimita contexto inicial ou sistema.
- `<thought>` ou `<reasoning>` - contém raciocínio lógico.
- `<step>` - pode ser usado para dividir em etapas internas.
- `<answe>` - resposta direta, sem explicações.
- `<final_decision>` - quando há múltiplas alternativas sendo avaliadas.

**Motivação para usar marcadores estruturais**

- Reduz ambiguidade entre raciocínio e resposta.
- Permite que o modelo organize suas ideias de maneira hierárquica.
- Facilita análises posteriores do output por humanos ou outros sistemas.
- Ajuda o modelo a se manter dentro de um fluxo lógico, sem saltos.

**Exemplos**

Prompt:

> Você é um engenheiro de software especialista em arquitetura de sistemas web. Sua tarefa é pensar passo a passo sobre os requisitos técnicos para construir um backend de uma aplicação de Todo List colaborativa com autenticação de usuários, categorias personalizáveis e suporte a tarefas compartilhadas entre times.
>
> Escreva seu raciocínio entre `<thought>` e o resumo final entre `<answer>` e também `<step>` para dividir o pensamento por área de responsabilidade.

**Resposta esperada**

```
<thought>
	<step>
		<title>1. Autenticação e gerenciamento de usuários</title>
		A aplicação deve suportar login via e-mail e senha com autenticação baseada em tokens JWT. Usuários precisam ser persistidos em um banco relacional com campos como email, senha hash, nome e data de criação.
	</step>
	<step>
		<title>2. Modelagem de tarefas</title>
		Cada tarefa deve conter título, descrição, status (pendente, concluída), data de vencimento, categoria e ID do criador. As tarefas devem poder ser atribuídas a múltiplos usuários.
	</step>
	<step>
		<title>3. Compartilhamento e permissões</title>
		O sistema precisa de um controle de permissões onde usuários podem ser organizados em times, com permissões como leitura, escrita e administração de tarefas dentro de projetos ou categorias.
	</step>
	<step>
		<title>4. Armazenamento e tecnologia</title>
		Uma stack adequada seria: backend em Go com Echo ou Fiber, banco PostgreSQL, autenticação com JWT e middleware para RBAC (role-based access control).
	</step>
</thought>
<answer>
	O backend da aplicação Todo List deve ser construído em Go, com suporte a JWT para autenticação, PostgreSQL para persistência e estrutura multiusuário com times e permissões de acesso. As tarefas são entidades colaborativas atribuídas a múltiplos usuários com categorias personalizadas e status gerenciável.
</answer>
```

## Comparativo

| Tipo de Prompt         | Requer Exemplos | Gera Raciocínio | Ideal para                           |
|------------------------|-----------------|------------------|---------------------------------------|
| Zero-Shot              | Nenhum          | Média            | Uso genérico                          |
| One-Shot / Few-Shot    | Sim             | Opcional         | Imitar formato, estilo ou padrões     |
| Chain of Thought       | Indiferente     | Sim              | Lógica, planejamento, análise, debugging |
