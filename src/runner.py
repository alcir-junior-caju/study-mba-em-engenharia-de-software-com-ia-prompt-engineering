"""CLI principal usando Typer e Rich."""

import subprocess
import sys
from pathlib import Path
from typing import Annotated

import questionary
import typer

from src.cli_utils import (
    console,
    create_table,
    print_error,
    print_header,
    print_info,
    print_success,
)

app = typer.Typer(
    name="script-runner",
    help="CLI para listar e executar scripts Python",
    add_completion=False,
)


def find_scripts(path: Path) -> list[tuple[int, str, Path]]:
    """Encontra todos os scripts Python em uma pasta.

    Args:
        path: Caminho da pasta para buscar scripts

    Returns:
        Lista de tuplas (número, nome_arquivo, caminho_completo)
    """
    scripts = []
    for idx, script_file in enumerate(sorted(path.rglob("*.py")), start=1):
        scripts.append((idx, script_file.name, script_file))
    return scripts


def get_script_path(scripts: list[tuple[int, str, Path]], identifier: int | str) -> Path | None:
    """Obtém o caminho completo de um script.

    Args:
        scripts: Lista de scripts encontrados
        identifier: Número ou nome do script

    Returns:
        Path do script ou None se não encontrado
    """
    if isinstance(identifier, int):
        # Buscar por número
        for num, _name, full_path in scripts:
            if num == identifier:
                return full_path
    else:
        # Buscar por nome
        for _num, name, full_path in scripts:
            if name == identifier:
                return full_path
    return None


@app.command()
def list(
    path: Annotated[
        str,
        typer.Option("--path", "-p", help="Pasta para buscar scripts"),
    ] = "./src/exercises",
):
    """Lista todos os scripts Python disponíveis."""
    scripts_path = Path(path)

    if not scripts_path.exists():
        print_error(f"Pasta não encontrada: {path}")
        raise typer.Exit(code=1)

    scripts = find_scripts(scripts_path)

    if not scripts:
        print_info(f"Nenhum script Python encontrado em: {path}")
        return

    print_header("Scripts Disponíveis", f"Pasta: {path}")

    table = create_table()
    table.add_column("#", style="cyan", justify="center", width=6)
    table.add_column("Nome do Script", style="green")
    table.add_column("Caminho Relativo", style="dim")

    for num, name, full_path in scripts:
        rel_path = full_path.parent.relative_to(scripts_path)
        table.add_row(str(num), name, str(rel_path))

    console.print(table)
    print_success(f"Total: {len(scripts)} script(s) encontrado(s)")


@app.command()
def run(
    script_id: Annotated[
        int | None,
        typer.Argument(help="Número do script para executar"),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", "-n", help="Nome do script para executar"),
    ] = None,
    path: Annotated[
        str,
        typer.Option("--path", "-p", help="Pasta onde estão os scripts"),
    ] = "./src/exercises",
    interactive: Annotated[
        bool,
        typer.Option("--interactive", "-i", help="Modo interativo com seleção por setas"),
    ] = True,
):
    """Executa um script Python."""
    scripts_path = Path(path)

    if not scripts_path.exists():
        print_error(f"Pasta não encontrada: {path}")
        raise typer.Exit(code=1)

    scripts = find_scripts(scripts_path)

    if not scripts:
        print_error(f"Nenhum script encontrado em: {path}")
        raise typer.Exit(code=1)

    # Modo interativo se nenhum identificador foi fornecido
    if script_id is None and name is None:
        if interactive:
            # Seleção interativa com setas
            choices = [f"{num}. {script_name}" for num, script_name, _ in scripts]

            selection = questionary.select(
                "Escolha um script para executar:",
                choices=choices,
                instruction="(Use as setas ↑↓ e Enter para confirmar)",
            ).ask()

            if selection is None:  # Usuário cancelou (Ctrl+C)
                print_info("Operação cancelada")
                raise typer.Exit(code=0)

            # Extrair número do script da seleção
            script_id = int(selection.split(".")[0])
        else:
            print_header("Executar Script", "Escolha um script da lista")

            table = create_table()
            table.add_column("#", style="cyan", justify="center", width=6)
            table.add_column("Nome do Script", style="green")

            for num, script_name, _ in scripts:
                table.add_row(str(num), script_name)

            console.print(table)

            script_id = questionary.text(
                "Digite o número do script:",
                default="1",
            ).ask()

            if script_id is None:
                print_info("Operação cancelada")
                raise typer.Exit(code=0)

            script_id = int(script_id)

    # Encontrar o script
    identifier = name if name else script_id
    script_path = get_script_path(scripts, identifier)  # type: ignore[arg-type]

    if not script_path:
        print_error(f"Script não encontrado: {identifier}")
        raise typer.Exit(code=1)

    # Executar o script
    print_header("Executando Script", f"Arquivo: {script_path.name}")
    console.print()

    try:
        result = subprocess.run(
            [sys.executable, str(script_path.absolute())],
            cwd=script_path.parent.absolute(),
            check=False,
        )

        console.print()
        if result.returncode == 0:
            print_success(f"Script executado com sucesso! (código: {result.returncode})")
        else:
            print_error(f"Script finalizado com erro (código: {result.returncode})")
            raise typer.Exit(code=result.returncode)

    except FileNotFoundError:
        print_error("Python não encontrado no sistema")
        raise typer.Exit(code=1) from None
    except Exception as e:
        print_error(f"Erro ao executar script: {e}")
        raise typer.Exit(code=1) from e


@app.command()
def start(
    path: Annotated[
        str,
        typer.Option("--path", "-p", help="Pasta onde estão os scripts"),
    ] = "./src/exercises",
):
    """Inicia a CLI interativa: lista e executa scripts com seleção por setas."""
    scripts_path = Path(path)

    if not scripts_path.exists():
        print_error(f"Pasta não encontrada: {path}")
        raise typer.Exit(code=1)

    scripts = find_scripts(scripts_path)

    if not scripts:
        print_error(f"Nenhum script encontrado em: {path}")
        raise typer.Exit(code=1)

    # Loop principal - permite executar múltiplos scripts
    while True:
        console.print()
        print_header("Script Runner", f"📂 Pasta: {path}")

        # Criar opções com informação adicional
        choices = []
        for num, script_name, full_path in scripts:
            rel_path = full_path.parent.relative_to(scripts_path)
            if str(rel_path) == ".":
                choices.append(f"{num}. {script_name}")
            else:
                choices.append(f"{num}. {script_name} ({rel_path})")

        choices.append("❌ Sair")

        # Seleção interativa
        selection = questionary.select(
            "Escolha um script para executar:",
            choices=choices,
            instruction="(Use ↑↓ e Enter para confirmar)",
        ).ask()

        if selection is None or selection == "❌ Sair":
            console.print()
            print_info("Encerrando Script Runner...")
            break

        # Extrair número do script
        script_id = int(selection.split(".")[0])
        script_path = get_script_path(scripts, script_id)

        if not script_path:
            print_error(f"Script não encontrado: {script_id}")
            continue

        # Executar o script
        console.print()
        print_header("Executando Script", f"📄 {script_path.name}")
        console.print()

        try:
            result = subprocess.run(
                [sys.executable, str(script_path.absolute())],
                cwd=script_path.parent.absolute(),
                check=False,
            )

            console.print()
            if result.returncode == 0:
                print_success(f"Script executado com sucesso! (código: {result.returncode})")
            else:
                print_error(f"Script finalizado com erro (código: {result.returncode})")

            # Perguntar se quer executar outro script
            if not questionary.confirm(
                "Deseja executar outro script?",
                default=True,
            ).ask():
                break

        except FileNotFoundError:
            print_error("Python não encontrado no sistema")
            break
        except Exception as e:
            print_error(f"Erro ao executar script: {e}")
            if not questionary.confirm(
                "Deseja tentar outro script?",
                default=True,
            ).ask():
                break


@app.command()
def info():
    """Mostra informações sobre a CLI."""
    from rich.markdown import Markdown

    doc = """
# Script Runner CLI

## Descrição
CLI interativa para listar e executar scripts Python de uma pasta com seleção por setas.

## Comandos Disponíveis

### 🚀 Modo Interativo (Recomendado)
```bash
uv run runner start
```
Interface completa com seleção por setas (↑↓) e execução contínua de scripts.

### 1. Listar Scripts
```bash
uv run runner list
uv run runner list --path ./minha-pasta
```

### 2. Executar Scripts
```bash
# Modo interativo com seleção por setas (padrão)
uv run runner run

# Por número
uv run runner run 1

# Por nome
uv run runner run --name 01.py

# Desabilitar modo interativo
uv run runner run --no-interactive

# Com pasta customizada
uv run runner run 1 --path ./minha-pasta
```

### 3. Ver Informações
```bash
uv run runner info
```

### 4. Ver Ajuda
```bash
uv run runner --help
uv run runner start --help
uv run runner list --help
uv run runner run --help
```

## Recursos

✅ Seleção interativa com setas do teclado (↑↓)
✅ Execução contínua de múltiplos scripts
✅ Interface bonita com cores e tabelas
✅ Busca recursiva em subpastas
✅ Suporte para pastas customizadas

## Exemplos

A pasta `src/exercises/` contém scripts de exemplo prontos para uso.
"""

    console.print(Markdown(doc))


if __name__ == "__main__":
    app()
