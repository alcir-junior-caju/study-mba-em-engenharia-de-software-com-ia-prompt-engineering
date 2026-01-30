<img alt="Infografico" src="infografico.png" style="margin: 15px 0" />

## Tree of Thought (ToT)

**Tree of Thought (ToT)** é uma extensão da técnica **Chain of Thought (CoT)** que permite que o modelo explore **múltiplos caminhos de raciocínio paralelos ou alternativos** antes de tomar uma decisão final. Em vez de um raciocínio linear, o **ToT** incentiva o modelo a **ramificar ideias** e **avaliar alternativas**, como se estivesse construído uma árvore de decisões.

**Estudo**

A técnica foi formalizada por **Yao et al. (2023)**, no paper **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**, mostrando ganhos significativos em tarefas complexas como jogos de lógica, planejamento e raciocínio analítico estruturado.

**Quando utilizar**

- A tarefa é ambígua ou tem **múltiplas soluções possíveis**
- É necessário **comparar estratégias ou caminhos distintos**
- A decisão final depende de **múltiplos critérios ou trade-offs**
- Deseja-se simular **raciocínio humano deliberado** com ponderações

**[Link do Paper](https://arxiv.org/abs/2305.10601)**

**Exemplo**

> Você é um engenheiro de software especialista em sistemas distribuídos. Um cliente quer limitar o acesso à sua API que recebe até 100 mil requisições por segundo. Gere múltiplas abordagens (caminhos de raciocínio) para resolver esse problema. Para cada abordagem, exponha os prós e contras. Ao final, selecione a mais adequada com base em escalabilidade, confiabilidade e latência.

**Resposta esperada**

Caminho 1: Token Bucket com Redis

- Permite bursts controlados
- Fácil de implementar
- Redis pode ser uma gargalo sob carga intensa
- Exige replicação e scripts atômicos

Caminho 2: Leaky Bucket com cache local

- Boa regularização de tráfego
- Alta previsibilidade de latência
- Menos flexível para bursts
- Cache local pode divergir entre instâncias

Caminho 3: Algoritmo Sliding Window Log

- Precisão de tempo real por requisição
- Alta granularidade
- Alto consumo de memória e custo computacional
- Difícil de escalar sem otimizações

**Avaliação dos caminhos**

- **Escalabilidade**: Caminhos 1 e 2 são melhores
- **Baixa latência**: Caminho 2 se destaca
- **Facilidade de manutenção**: Caminho 1 é o mais indicado

**Escolha final**

Token Bucket com Redis + buffer local representa o melhor equilíbrio entre simplicidade, performance e tolerância a falhas.

**Técnicas auxiliares**

**Expansão controlada de caminhos**: limite a profundidade e número de alternativas para evitar dispersão.

`"Apresente no máximo 3 caminhos distintos para resolver este problema e desenvolva até 2 níveis de sub-etapas para cada um"`

**Critérios de decisão explícitos**: guie o modelo com parâmetros como "menor custo", "maior confiabilidade", etc.

`"Para cada abordagem proposta, avalie com base em custo, latência e escalabilidade. Escolha a melhor com base nesses critérios"`

**Reavaliação iterativa**: o modelo pode revisar suas escolhas se uma nova ramificação se mostrar superior.

`"Depois de explorar todas as opções, reavalie as decisões com base nos resultados observados em cada caminho e corrija se necessário"`

**Combinação com outras técnicas: ToT + CoT + SoT**

Tree of Thought é altamente compatível com outras estratégias de prompting, resultando em maior controle, completude e explicabilidade. Abaixo está um exemplo que combina Tree of Thought com Chain of Thought e Skeleton of thought.

**Prompt combinado (ToT + CoT + SoT)**

> Você é um engenheiro de software especialista em sistemas distribuídos. Sua tarefa é projetar uma solução de rate limiting para uma API que suporta 100 mil requisições por segundo. Apresente 3 estratégias distintas, usando o seguinte esqueleto para cada uma:
>
> - Visão geral da abordagem
> - **Etapas detalhadas do raciocínio (pense passo a passo, como um engenheiro resolveria isso em produção)**
> - Principais vantagens
> - Quando usar essa abordagem
>
> Ao final, decida qual abordagem representa o melhor equilíbrio para o caso proposto.

**Resposta esperada**

Estratégia 1: Token Bucket com Redis distribuído

- **Visão geral**: Permite pequenos bursts, boa tolerância à falha
- **Etapas**: Descrever uso de token bucket, scripts LUA atômicos, cache local
- **Vantagens**: Popular, flexível, boa documentação
- **Desvantagens**: Requer Redis de alta disponibilidade
- **Uso ideal**: Quando se deseja flexibilidade e controle individualizado

Estratégia 2: Leaky Bucket com armazenamento local

- **Visão geral**: Regulariza fluxo de forma constante
- **Etapas**: Descrever de que local, fallback em caso de falha
- **Vantagens**: Mais simples, previsível
- **Desvantagens**: Cache local pode gerar inconsistência
- **Uso ideal**: Quando a estabilidade de fluxo é mais importante que burst handling

Estratégia 3: Sliding Window Log com shard por API key

- **Visão geral**: Rastreia cada requisição
- **Etapas**: Uso de logs temporais por cliente
- **Vantagens**: Alta precisão temporal
- **Desvantagens**: Alto custo de memória
- **Uso ideal**: Quando a justiça de tempo real é indispensável

**Escolha final**

A estratégia 1 oferece o melhor equilíbrio entre performance, controle e robustez para a maioria dos cenários em produção com cargas elevadas.

## Comparativo

| Tipo de Prompt         | Requer Estrutura | Raciocínio Passo a Passo | Múltiplas Alternativas | Ideal para                                              |
|------------------------|------------------|---------------------------|-------------------------|---------------------------------------------------------|
| Zero-Shot              | Não              | Não                       | Não                     | Consultas diretas, respostas factuais                   |
| Few-Shot               | Parcial          | Opcional                  | Não                     | Repetir padrões de exemplo com precisão                 |
| Chain of Thought       | Não              | Sim                       | Não                     | Diagnóstico, debugging, raciocínio técnico              |
| Skeleton of Thought    | Sim              | Opcional                  | Não                     | Respostas organizadas, documentações, especificações    |
| Tree of Thought        | Parcial          | Sim                       | Sim                     | Decisão entre estratégias, brainstorming estruturado    |

## Resumo comparativo: CoT, SoT, ToT

| Tipo de Prompt       | Situação Ideal                     | Justificativa                                                | Exemplo |
|----------------------|------------------------------------|---------------------------------------------------------------|---------|
| Chain of Thought (CoT) | Explicar Bugs                     | Raciocínio encadeado com lógica explicada                     | “Explique passo a passo por que o código abaixo pode gerar um panic em GO. Analise como um engenheiro faria o debug em produção.” |
| Skeleton of Thought (SoT) | Especificar módulos com seções fixas | Exige consistência e organização por tópicos               | “Crie uma especificação técnica para um módulo de autenticação JWT usando os seguintes tópicos: requisitos funcionais, modelo de dados, fluxos, validações, segurança e integração.” |
| Tree of Thought (ToT) | Comparar opções (Ex.: cache)      | Exploração de alternativas e decisão justificada              | “Considere três formas de aplicar cache em um sistema web: in-memory, Redis e CDN. Para cada uma descreva a estratégia, vantagens, desvantagens e cenário ideal de uso. Ao final, selecione a melhor com base em latência, custo e simplicidade.” |
| SoT + CoT            | Planejamento de arquitetura        | Organização por tópicos com raciocínio detalhado              | “Estruture a arquitetura de um sistema de Todo List com autenticação, API REST e persistência. Responda por tópicos: visão geral, autenticação, banco de dados, fluxos principais, escalabilidade. Em cada tópico, pense passo a passo com um arquiteto de software.” |
| ToT + SoT + CoT      | Definir melhor stack tecnológica   | Estrutura, múltiplas alternativas e raciocínio interno        | “Compare as stacks GO, Node.js e Python para microserviços. Para cada uma, siga os tópicos: performance, ecossistema, produtividade, complexidade de deploy e casos de uso recomendados. Dentro de cada tópico, pense passo a passo. Ao final, recomende a stack ideal para um sistema com 10 microserviços interconectados.” |
| ToT + SoT            | Comparação de bancos de dados      | Análise comparativa organizada por critérios                  | “Compare os tipos de banco de dados SQL, NoSQL e NewSQL para uma aplicação de leitura intensiva. Para cada um, responda usando os tópicos: modelo de dados, escalabilidade, latência, consistência e custo operacional. Ao final, indique qual abordagem é mais indicada para esse cenário.” |

## Casos de uso abordados

| Tipo de Prompt           | Situação Ideal                                                       | Justificativa                                                                       |
|--------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Chain of Thought (CoT)   | Explicar porque um bug ocorre                                        | Precisa de raciocínio encadeado com lógica explicada                                  |
| Skeleton of Thought (SoT)| Especificar um módulo de autenticação com seções fixas               | Exige consistência e organização por tópicos                                        |
| Tree of Thought (ToT)    | Comparar 3 formas de aplicar cache (in-memory, Redis, CDN)           | Exige exploração de alternativas e decisão final justificada                        |
| SoT + CoT                | Planejar arquitetura de um sistema com API, banco e autenticação       | Exige estrutura e raciocínio técnico dentro de cada seção                           |
| ToT + SoT + CoT          | Definir melhor stack entre GO, Node.js e Python para microserviços     | Requer estrutura, múltiplas alternativas e raciocínio interno completo                |
| ToT + SoT                | Comparar bancos SQL, NoSQL e NewSQL para leitura intensiva             | Múltiplas estratégias com análise técnica estruturada, sem exigir CoT                 |

## Conclusão

Cada técnica possuí forças complementares:

- **CoT** - Raciocínio Lógico
- **SoT** - Organização e completude
- **ToT** - Comparação e tomada de decisão

### [Assista ao resumo em vídeo](https://github.com/user-attachments/assets/527138e1-789b-4382-9741-5e7e2e0c2792)
