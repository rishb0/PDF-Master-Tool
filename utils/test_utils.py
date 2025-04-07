from PyPDF2 import PdfWriter
from rich.console import Console
import os
from PIL import Image

def create_test_pdf(output_path, num_pages=1):
    """Create a test PDF file with specified number of pages"""
    console = Console()
    writer = PdfWriter()

    for i in range(num_pages):
        # Create a new page (blank, but with size)
        page = writer.add_blank_page(width=612, height=792)  # Standard letter size

    try:
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        console.print(f"[green]Created test PDF: {output_path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error creating test PDF: {str(e)}[/red]")
        return False

def create_test_image(output_path, width=800, height=600):
    """Create a test image file"""
    console = Console()
    try:
        # Create a new image with a white background
        image = Image.new('RGB', (width, height), 'white')
        # Add some shapes to make it visible
        from PIL import ImageDraw
        draw = ImageDraw.Draw(image)
        # Draw a rectangle
        draw.rectangle([100, 100, 700, 500], outline='black', width=2)
        # Draw some text
        draw.text((400, 300), "Test Image", fill='black')

        image.save(output_path)
        console.print(f"[green]Created test image: {output_path}[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error creating test image: {str(e)}[/red]")
        return False

def create_sample_pdfs():
    """Create sample PDFs for testing"""
    console = Console()
    console.print("[yellow]Creating sample PDFs for testing...[/yellow]")

    # Create test directory if it doesn't exist
    if not os.path.exists('test_files'):
        os.makedirs('test_files')

    # Create a single page PDF for basic operations
    create_test_pdf("test_files/test_single.pdf")

    # Create a multi-page PDF for splitting
    create_test_pdf("test_files/test_multi.pdf", num_pages=3)

    # Create additional PDFs for merging
    create_test_pdf("test_files/test_merge1.pdf")
    create_test_pdf("test_files/test_merge2.pdf")

    # Create test images for image-to-PDF conversion
    create_test_image("test_files/test_image1.png")
    create_test_image("test_files/test_image2.png")

    console.print("[green]Sample files created successfully![/green]")