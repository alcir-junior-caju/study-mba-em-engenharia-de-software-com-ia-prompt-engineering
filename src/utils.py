from rich.console import Console
from rich.text import Text


def print_llm_result(prompt, response):
    """
    Print LLM prompt, response and token usage with colored         formatting
    """
    console = Console()

    # Print prompt
    console.print(Text("USER PROMPT:", style="bold green"))
    console.print(Text(prompt, style="bold blue"), end="\n\n")

    # Print response
    console.print(Text("LLM RESPONSE:", style="bold green"))
    console.print(Text(response.content, style="bold blue"), end="\n\n")

    # Print token usage
    usage = response.response_metadata.get('token_usage', {})
    if usage:
        # OpenAI format
        console.print(f"[bold white]Input tokens:[/bold white] [bright_black]{usage.get('prompt_tokens', 'N/A')}[/bright_black]")
        console.print(f"[bold white]Output tokens:[/bold white] [bright_black]{usage.get('completion_tokens', 'N/A')}[/bright_black]")
        console.print(f"[bold white]Total tokens:[/bold white] [bright_black]{usage.get('total_tokens', 'N/A')}[/bright_black]")
    elif hasattr(response, 'usage_metadata') and response.usage_metadata:
        # Gemini format (LangChain v0.2+)
        usage_meta = response.usage_metadata
        console.print(f"[bold white]Input tokens:[/bold white] [bright_black]{usage_meta.get('input_tokens', 'N/A')}[/bright_black]")
        console.print(f"[bold white]Output tokens:[/bold white] [bright_black]{usage_meta.get('output_tokens', 'N/A')}[/bright_black]")
        console.print(f"[bold white]Total tokens:[/bold white] [bright_black]{usage_meta.get('total_tokens', 'N/A')}[/bright_black]")
        # Mostrar detalhes adicionais se disponíveis
        if 'output_token_details' in usage_meta and usage_meta['output_token_details'].get('reasoning'):
            console.print(f"[bold white]Reasoning tokens:[/bold white] [bright_black]{usage_meta['output_token_details']['reasoning']}[/bright_black]")
    elif 'usage_metadata' in response.response_metadata:
        # Gemini format alternativo (versões antigas)
        usage_meta = response.response_metadata['usage_metadata']
        console.print(f"[bold white]Input tokens:[/bold white] [bright_black]{usage_meta.get('prompt_token_count', 'N/A')}[/bright_black]")
        console.print(f"[bold white]Output tokens:[/bold white] [bright_black]{usage_meta.get('candidates_token_count', 'N/A')}[/bright_black]")
        console.print(f"[bold white]Total tokens:[/bold white] [bright_black]{usage_meta.get('total_token_count', 'N/A')}[/bright_black]")
    console.print(f"[yellow]{'-'*50} [/yellow]")
