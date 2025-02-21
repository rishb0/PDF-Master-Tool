import sys
from rich.console import Console
from utils.menu import display_menu
from utils.pdf_operations import PDFOperations
from utils.test_utils import create_sample_pdfs

def main():
    console = Console()
    pdf_ops = PDFOperations()

    # Check if running in non-interactive mode
    non_interactive = not sys.stdin.isatty()

    while True:
        try:
            choice = display_menu(non_interactive)

            if choice == '1':
                input_pdf = console.input("[cyan]Enter PDF path to encrypt: [/cyan]")
                password = console.input("[cyan]Enter password for encryption: [/cyan]")
                pdf_ops.encrypt_pdf(input_pdf, password)

            elif choice == '2':
                input_pdf = console.input("[cyan]Enter PDF path to decrypt: [/cyan]")
                password = console.input("[cyan]Enter password: [/cyan]")
                pdf_ops.decrypt_pdf(input_pdf, password)

            elif choice == '3':
                input_pdf = console.input("[cyan]Enter PDF path to extract metadata: [/cyan]")
                pdf_ops.extract_metadata(input_pdf)

            elif choice == '4':
                pdfs = []
                while True:
                    try:
                        pdf_path = console.input("[cyan]Enter PDF path (or 'done' to finish): [/cyan]")
                        if pdf_path.lower() == 'done':
                            break
                        pdfs.append(pdf_path)
                    except (EOFError, KeyboardInterrupt):
                        break
                if pdfs:
                    output_path = console.input("[cyan]Enter output PDF path: [/cyan]")
                    pdf_ops.merge_pdfs(pdfs, output_path)

            elif choice == '5':
                input_pdf = console.input("[cyan]Enter PDF path to split: [/cyan]")
                output_dir = console.input("[cyan]Enter output directory: [/cyan]")
                pdf_ops.split_pdf(input_pdf, output_dir)

            elif choice == '6':
                input_pdf = console.input("[cyan]Enter PDF path to rotate pages: [/cyan]")
                try:
                    page_num = int(console.input("[cyan]Enter page number to rotate: [/cyan]"))
                    rotation = int(console.input("[cyan]Enter rotation angle (90, 180, 270): [/cyan]"))
                    pdf_ops.rotate_pages(input_pdf, page_num, rotation)
                except ValueError as e:
                    console.print("[red]Please enter valid numbers for page and rotation.[/red]")

            elif choice == '7':
                input_pdf = console.input("[cyan]Enter PDF path to convert to Word: [/cyan]")
                pdf_ops.convert_pdf_to_word(input_pdf)

            elif choice == '8':
                input_word = console.input("[cyan]Enter Word document path to convert to PDF: [/cyan]")
                pdf_ops.convert_word_to_pdf(input_word)

            elif choice == '9':
                images = []
                while True:
                    try:
                        image_path = console.input("[cyan]Enter image path (or 'done' to finish): [/cyan]")
                        if image_path.lower() == 'done':
                            break
                        images.append(image_path)
                    except (EOFError, KeyboardInterrupt):
                        break
                if images:
                    output_path = console.input("[cyan]Enter output PDF path: [/cyan]")
                    pdf_ops.convert_images_to_pdf(images, output_path)

            elif choice == '10':
                input_pdf = console.input("[cyan]Enter PDF path to convert to images: [/cyan]")
                output_dir = console.input("[cyan]Enter output directory for images: [/cyan]")
                pdf_ops.convert_pdf_to_images(input_pdf, output_dir)

            elif choice == '11':
                console.print("[yellow]Creating sample PDF files for testing...[/yellow]")
                create_sample_pdfs()

            elif choice == '12':
                console.print("[yellow]Thank you for using PDF Manager![/yellow]")
                break

            if not non_interactive:
                console.print("\n[green]Press Enter to continue...[/green]")
                try:
                    input()
                except (EOFError, KeyboardInterrupt):
                    break

        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/red]")
            if not non_interactive:
                console.print("\n[green]Press Enter to continue...[/green]")
                try:
                    input()
                except (EOFError, KeyboardInterrupt):
                    break

if __name__ == "__main__":
    main()