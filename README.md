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

- [Introdução](./docs/01-introducao.md)
- [Role Prompting](./docs/02-role-prompting.md)
- [Zero Shot](./docs/03-zero-shot.md)
- [One/Few Shot](./docs/04-one-few-shot.md)
- [Chain of Thought](./docs/05-chain-of-thought.md)
- [Skeleton of Thought](./docs/06-skeleton-of-thought.md)
- [Tree of Thought](./docs/07-tree-of-thought.md)
- [Self Consistency](./docs/08-self-consistency.md)
- [Directional Stimulus](./docs/09-directional-stimulus.md)
- [React](./docs/10-react.md)

---

## 📄 Licença

MIT License - Criado por Alcir Junior [Caju]
