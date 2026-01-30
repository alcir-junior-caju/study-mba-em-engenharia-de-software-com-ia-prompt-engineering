<img alt="Infografico" src="infografico.png" style="margin: 15px 0" />

## Skeleton of Thought (SoT)

**Skeleton of Thought Prompting** é uma variação de **Chain of Thought** onde o modelo é instruído a seguir uma **estrutura lógica pré-definida (um esqueleto)**, com marcadores claros de seções ou ideias centrais que devem ser preenchidas com raciocínio. Essa técnica é ideal quando o desenvolvedor deseja que a IA produza respostas **organizadas**, **completas** e **sem fugir da estrutura** desejada.

**Estudo**

A técnica foi inspirada diretamente em um estudo acadêmico publicado por **Zhang et al. (2023)** no paper *"Skeleton-of-Thought: Large Language Models Can Do Parallel Decoding"*. Nesse trabalho, os autores mostraram que é possível separar a geração do **esqueleto estrutural da resposta** da geração de conteúdo detalhado de cada parte, promovendo paralelismo e coerência. Embora o foco técnico do paper seja a melhoria de desempenho por decodificação paralela, o mesmo princípio é aplicável a prompting estrutural em diversos contextos como documentações, arquitetura de software, etc.

**Quando utilizar**

- Resumos técnicos com seções fixas
- Documentações, ADRs, Templates
- Quando há necessidade de controlar a saída e formato de uma resposta

**[Link do Paper](https://arxiv.org/abs/2307.15337)**

**Exemplos**

> Você é um engenheiro de software especializado em performance e escalabilidade. Sua tarefa é propor uma solução para implementar um rate limiter robusto que limite a taxa de requisições por cliente. Estruture sua resposta com os seguintes tópicos:
>
> - Contexto do problema
> - Requisitos funcionais e não funcionais
> - Estratégia de rate limiting
> - Stack tecnológica sugerida
> - Considerações de concorrência e escalabilidade
> - Conclusão técnica

**Resposta esperada**

**Contexto do problema**: A API será utilizada por centenas de clientes simultaneamente e precisa garantir que nenhum cliente ultrapasse o limite de 1000 requisições por minuto. O Sistema seve suportar até 100 mil requisições por segundo em picos e evitar sobrecarga no backend. É necessário garantir que o rate limiter funcione em ambiente distribuído.

**Requisitos funcionais e não funcionais**:

- Cada cliente de ter limites de requisição individuais
- Os limites devem ser reiniciados por janela deslizante (sliding window)
- O sistema deve ser resiliente, com baixa latência (<5ms)
- Suporte a múltiplas instâncias e execução concorrente

**Estratégia de rate limiting**: A técnica ideal é o uso de **Token Bucket** com sliding window e sincronização via Redis. Cada cliente terá um bucket virtual com capacidade e taxa de preenchimento ajustável. A cada requisição, será feita uma tentativa de consumir um token. Se o token não estiver disponível, a requisição será rejeitada com HTTP 429.

**Stack tecnológica sugerida:**

- Linguagem GO
- Middleware HTTP; Echo ou Fiber
- Rate limiting core: implementação própria ou uso do pacote rate
- Armazenamento distribuído: Redis Cluster para controle de tokens sincronizados entre instâncias
- Monitoramento: Prometheus + Grafana

**Considerações de concorrência e escalabilidade**:

- Redis deve usar LUA scripts atômicos para evitar race conditions
- Shard de clientes por chave (hash) pode distribuir melhor a carga
- Uso de buffers internos no processo local para operações de leitura rápidas em cache
- Evitar chamadas de rede por requisição usando prefetching de tokens

**Conclusão técnica**: O uso de Token Bucket com Redis distribuído e implementação em GO atende aos requisitos de latência e escalabilidade. A estrutura modular permite reuso em outros serviços. É necessário fazer testes de carga com Locust e simulação de falhas para validar a robustez da solução em produção.

**Quando usar SoT vs CoT puro**

| Quando                                     | Skeleton of Thought |
|-------------------------------------------|----------------------|
| Você quer controle total do formato       | Sim                  |
| A resposta deve ser dividida por tópicos  | Sim                  |
| A tarefa exige checklist estruturado      | Sim                  |
| A IA costuma se perder na estrutura       | Sim                  |
| A lógica for altamente exploratória       | Não                  |

## Comparativo

| Tipo de Prompt         | Requer Estrutura | Raciocínio Passo a Passo | Ideal para                                    |
|------------------------|------------------|---------------------------|-----------------------------------------------|
| Zero-Shot              | Não              | Não                       | Consultas diretas, respostas factuais         |
| One-Shot / Few-Shot    | Parcial          | Opcional                  | Repetir padrões de exemplo com precisão       |
| Chain of Thought       | Não              | Sim                       | Diagnóstico, debugging, raciocínio técnico    |
| Skeleton of Thought    | Sim              | Opcional                  | Documentações, especificações                 |

### [Assista ao resumo em vídeo](https://github.com/user-attachments/assets/b0213fa9-c75b-4fdc-a6ee-4b223db5b6fc)
