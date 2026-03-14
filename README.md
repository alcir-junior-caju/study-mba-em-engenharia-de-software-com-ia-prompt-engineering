# MBA em Engenharia de Software com IA - Prompt Engineering

<div>
    <img alt="Criado por Alcir Junior [Caju]" src="https://img.shields.io/badge/criado%20por-Alcir Junior [Caju]-%23f08700">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-%23f08700">
</div>

---

## 📋 Pré-requisitos

- **Python 3.11+** (recomendado 3.13)
- **[uv](https://docs.astral.sh/uv/)** - Gerenciador de pacotes Python

### Instalação do uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## 🚀 Como Usar

```bash
# 1. Instalar dependências
uv sync

# 2. Executar a CLI interativa
uv run runner start
```

**Navegue com ↑↓ e confirme com Enter**

---

## 📁 Estrutura


```
.
├── pyproject.toml                  # Configuração do projeto
├── README.md                       # Documentação principal
├── test_cli.sh                     # Script de teste da CLI
├── _images/                        # Imagens do projeto
├── docs/                           # Documentação
│   ├── 01-iniciando/
│   │   ├── 01-introducao/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 02-role-prompting/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 03-zero-shot/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 04-one-few-shot/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 05-chain-of-thought/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 06-skeleton-of-thought/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 07-tree-of-thought/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 08-self-consistency/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 09-directional-stimulus/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   │   ├── 10-react/
│   │   │   ├── post.md
│   │   │   └── resumo.md
│   └── 02-conceitos/
│       ├── 01-context-window/
│       │   ├── post.md
│       │   └── resumo.md
│       ├── 02-truncamento/
│       │   ├── post.md
│       │   └── resumo.md
│       ├── 03-sumarizacao/
│       │   ├── post.md
│       │   └── resumo.md
│       ├── 04-sliding-window/
│       │   ├── post.md
│       │   └── resumo.md
│       ├── 05-prompt-caching/
│       │   ├── post.md
│       │   └── resumo.md
│       ├── 06-batch-prompting/
│       │   ├── post.md
│       │   └── resumo.md
├── gerenciamento-e-versionamento-de-prompts/
│   └── prompts/
│       ├── registry.yaml
│       ├── agent-code-reviewer/
│       │   └── v1.0.0/
│       │       ├── prompt.tests.yaml
│       │       └── prompt.yaml
│       └── agent-pull-request-creator/
│           ├── v1.0.0/
│           │   ├── prompt.tests.yaml
│           │   └── prompt.yaml
│           └── v1.0.1/
│               ├── prompt.tests.yaml
│               └── prompt.yaml
├── prompts-e-workflow-de-agentes/
│   ├── agents/
│   │   ├── architectural-analyzer.md
│   │   ├── component-deep-analyzer.md
│   │   ├── dependency-auditor.md
│   │   └── orchestrator.md
│   └── commands/
│       └── run-project-state-full-report.md
├── src/
│   ├── cli_utils.py
│   ├── prompt_registry.py
│   ├── runner.py
│   ├── utils.py
│   └── exercises/
│       ├── 01-Role-prompting.py
│       ├── 02-zero-shot.py
│       ├── 03-one-few-shot.py
│       ├── 04-CoT.py
│       ├── 05-CoT-Self-consistency.py
│       ├── 06-ToT.py
│       ├── 07-SoT.py
│       ├── 08-ReAct.py
│       ├── 09-Prompt-channing.py
│       ├── 10-Least-to-most.py
│       ├── 11-agent_code_reviewer.py
│       ├── 12-agent_pull_request.py
│       ├── 13-langsmith_client.py
│       └── 14-langsmith_push.py
```

---

## 🔧 Desenvolvimento

```bash
# Verificar código
uv run ruff check src/

# Formatar código
uv run ruff format src/

# Verificar tipos
uv run pyright
```

---

## 📖 Tecnologias

- **Python 3.13** - Linguagem
- **Typer** - Framework CLI
- **Rich** - Interface colorida
- **Questionary** - Seleção interativa
- **uv** - Gerenciador de pacotes

---

## 📄 Docs

### Iniciando com Prompt Engineering

- [Introdução](./docs/01-iniciando/01-introducao/resumo.md)
- [Role Prompting](./docs/01-iniciando/02-role-prompting/resumo.md)
- [Zero Shot](./docs/01-iniciando/03-zero-shot/resumo.md)
- [One/Few Shot](./docs/01-iniciando/04-one-few-shot/resumo.md)
- [Chain of Thought](./docs/01-iniciando/05-chain-of-thought/resumo.md)
- [Skeleton of Thought](../docs/01-iniciando/06-skeleton-of-thought/resumo.md)
- [Tree of Thought](./docs/01-iniciando/07-tree-of-thought/resumo.md)
- [Self Consistency](./docs/01-iniciando/08-self-consistency/resumo.md)
- [Directional Stimulus](./docs/01-iniciando/09-directional-stimulus/resumo.md)
- [React](./docs/01-iniciando/10-react/resumo.md)

### Conceitos importantes

- [Context Window](./docs/02-conceitos/01-context-window/resumo.md)
- [Truncamento](./docs/02-conceitos/02-truncamento/resumo.md)
- [Sumarização](./docs/02-conceitos/03-sumarizacao/resumo.md)
- [Sliding Window](./docs/02-conceitos/04-sliding-window/resumo.md)
- [Prompt Caching](./docs/02-conceitos/05-prompt-caching/resumo.md)
- [Batch Prompting](./docs/02-conceitos/06-batch-prompting/resumo.md)

### Estruturação
- [Estruturação de prompts e estratégias de utilização](./docs/03-estruturacao/resumo.md)

### Versionamento
- [Versionamento e Gestão de Prompts na Engenharia de Software](./docs/04-versionamento/resumo.md)

### Enrichment
- [Prompt Enrichment e Query Reformulation](./docs/05-query-reformulation-prompt-enrichment/resumo.md)

### Evaluation
- [Prompt Evaluation ](./docs/06-evaluation/resumo.md)

---

## 📄 Licença

MIT License - Criado por Alcir Junior [Caju]
