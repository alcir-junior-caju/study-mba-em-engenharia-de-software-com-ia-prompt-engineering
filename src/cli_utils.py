"""Utilidades para CLI com Rich."""

import logging
from collections.abc import Generator
from contextlib import contextmanager

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.theme import Theme

# Tema customizado
custom_theme = Theme(
    {
        "info": "cyan",
        "warning": "yellow",
        "error": "red bold",
        "success": "green bold",
    }
)

# Console global com tema
console = Console(theme=custom_theme)


def print_header(title: str, subtitle: str = ""):
    """Exibe um cabeçalho bonito."""
    console.print()
    console.rule(f"[bold cyan]{title}[/bold cyan]")
    if subtitle:
        console.print(f"[dim]{subtitle}[/dim]", justify="center")
    console.print()


def print_success(message: str):
    """Exibe mensagem de sucesso."""
    console.print(f"[success]✓[/success] {message}")


def print_error(message: str):
    """Exibe mensagem de erro."""
    console.print(f"[error]✗[/error] {message}")


def print_info(message: str):
    """Exibe mensagem informativa."""
    console.print(f"[info](i)[/info] {message}")


def print_panel(content: str, title: str = "", style: str = "cyan"):
    """Exibe conteúdo em um painel."""
    panel = Panel(content, title=title, border_style=style)
    console.print(panel)


def create_table(title: str = "") -> Table:
    """Cria uma tabela formatada."""
    table = Table(title=title, show_header=True, header_style="bold magenta")
    return table


def setup_logging() -> logging.Logger:
    """Configura e retorna um logger."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(__name__)


@contextmanager
def progress_spinner() -> Generator[Progress, None, None]:
    """Context manager para spinner de progresso."""
    progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    )
    try:
        progress.start()
        yield progress
    finally:
        progress.stop()
