from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import sys

def display_menu(non_interactive=False):
    console = Console()

    menu_text = Text.assemble(
        ("PDF Manager\n\n", "bold magenta"),
        "1. Encrypt PDF\n",
        "2. Decrypt PDF\n",
        "3. Extract Metadata\n",
        "4. Merge PDFs\n",
        "5. Split PDF\n",
        "6. Rotate Pages\n",
        "7. PDF to Word\n",
        "8. Word to PDF\n",
        "9. Images to PDF\n",
        "10. PDF to Images\n",
        "11. Create Sample PDFs\n",
        "12. Exit\n\n",
        ("Choose an option (1-12): ", "cyan")
    )

    console.print(Panel(menu_text, title="Menu", border_style="blue"))

    if non_interactive:
        # In non-interactive mode, read from stdin if available
        try:
            choice = sys.stdin.readline().strip()
            if choice in [str(i) for i in range(1, 13)]:
                return choice
            return '12'  # Exit if invalid input
        except (EOFError, KeyboardInterrupt):
            return '12'  # Exit on EOF or interrupt

    while True:
        try:
            choice = console.input("")
            if choice in [str(i) for i in range(1, 13)]:
                return choice
            console.print("[red]Invalid choice. Please select 1-12.[/red]")
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Exiting...[/yellow]")
            return '12'