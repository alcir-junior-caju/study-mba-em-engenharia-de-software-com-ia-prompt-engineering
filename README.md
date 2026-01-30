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
├── src/
│   ├── runner.py         # CLI interativa
│   ├── cli_utils.py      # Utilitários
│   └── exercises/        # Seus scripts Python
│       ├── 01.py
│       ├── 02.py
│       └── 03.py
└── pyproject.toml        # Configuração do projeto
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

---

## 📄 Licença

MIT License - Criado por Alcir Junior [Caju]
