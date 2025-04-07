import os
from PyPDF2 import PdfReader, PdfWriter
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image
from pdf2image import convert_from_path

class PDFOperations:
    def __init__(self):
        self.console = Console()

    def _validate_pdf(self, pdf_path):
        """Validate if PDF file exists and is accessible"""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        if not pdf_path.lower().endswith('.pdf'):
            raise ValueError("File must be a PDF")

    def _validate_word(self, word_path):
        """Validate if Word file exists and is accessible"""
        if not os.path.exists(word_path):
            raise FileNotFoundError(f"Word file not found: {word_path}")
        if not word_path.lower().endswith('.docx'):
            raise ValueError("File must be a Word document (.docx)")

    def _validate_image(self, image_path):
        """Validate if image file exists and is accessible"""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        valid_extensions = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')
        if not image_path.lower().endswith(valid_extensions):
            raise ValueError(f"File must be an image {valid_extensions}")

    def encrypt_pdf(self, input_pdf, password):
        """Encrypt PDF with password"""
        self._validate_pdf(input_pdf)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Encrypting PDF...", total=None)

            reader = PdfReader(input_pdf)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.encrypt(password)
            output_path = input_pdf.replace('.pdf', '_encrypted.pdf')

            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

        self.console.print(f"[green]PDF encrypted successfully: {output_path}[/green]")

    def decrypt_pdf(self, input_pdf, password):
        """Decrypt PDF with password"""
        self._validate_pdf(input_pdf)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Decrypting PDF...", total=None)

            reader = PdfReader(input_pdf)
            writer = PdfWriter()

            if reader.is_encrypted:
                reader.decrypt(password)
            else:
                raise ValueError("PDF is not encrypted")

            for page in reader.pages:
                writer.add_page(page)

            output_path = input_pdf.replace('.pdf', '_decrypted.pdf')
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

        self.console.print(f"[green]PDF decrypted successfully: {output_path}[/green]")

    def extract_metadata(self, input_pdf):
        """Extract metadata from PDF"""
        self._validate_pdf(input_pdf)

        reader = PdfReader(input_pdf)
        metadata = reader.metadata

        if metadata:
            self.console.print("\n[yellow]PDF Metadata:[/yellow]")
            for key, value in metadata.items():
                if value:
                    self.console.print(f"[cyan]{key}:[/cyan] {value}")
        else:
            self.console.print("[yellow]No metadata found in the PDF[/yellow]")

    def merge_pdfs(self, pdf_list, output_path):
        """Merge multiple PDFs into one"""
        if not pdf_list:
            raise ValueError("No PDFs provided for merging")

        writer = PdfWriter()

        with Progress() as progress:
            task = progress.add_task("[cyan]Merging PDFs...", total=len(pdf_list))

            for pdf_path in pdf_list:
                self._validate_pdf(pdf_path)
                reader = PdfReader(pdf_path)
                for page in reader.pages:
                    writer.add_page(page)
                progress.update(task, advance=1)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        self.console.print(f"[green]PDFs merged successfully: {output_path}[/green]")

    def split_pdf(self, input_pdf, output_dir):
        """Split PDF into individual pages"""
        self._validate_pdf(input_pdf)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        reader = PdfReader(input_pdf)

        with Progress() as progress:
            task = progress.add_task("[cyan]Splitting PDF...", total=len(reader.pages))

            for page_num in range(len(reader.pages)):
                writer = PdfWriter()
                writer.add_page(reader.pages[page_num])

                output_path = os.path.join(output_dir, f'page_{page_num + 1}.pdf')
                with open(output_path, 'wb') as output_file:
                    writer.write(output_file)

                progress.update(task, advance=1)

        self.console.print(f"[green]PDF split successfully into {output_dir}[/green]")

    def rotate_pages(self, input_pdf, page_num, rotation):
        """Rotate specific page in PDF"""
        self._validate_pdf(input_pdf)

        if rotation not in [90, 180, 270]:
            raise ValueError("Rotation must be 90, 180, or 270 degrees")

        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        if page_num < 1 or page_num > len(reader.pages):
            raise ValueError(f"Invalid page number. PDF has {len(reader.pages)} pages")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Rotating page...", total=None)

            for i in range(len(reader.pages)):
                page = reader.pages[i]
                if i == page_num - 1:
                    page.rotate(rotation)
                writer.add_page(page)

            output_path = input_pdf.replace('.pdf', f'_rotated_{rotation}.pdf')
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

        self.console.print(f"[green]Page {page_num} rotated successfully: {output_path}[/green]")

    def convert_pdf_to_word(self, input_pdf):
        """Convert PDF to Word document"""
        self._validate_pdf(input_pdf)

        output_path = input_pdf.replace('.pdf', '.docx')

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Converting PDF to Word...", total=None)

            cv = Converter(input_pdf)
            cv.convert(output_path)
            cv.close()

        self.console.print(f"[green]PDF converted to Word successfully: {output_path}[/green]")

    def convert_word_to_pdf(self, input_word):
        """Convert Word document to PDF"""
        self._validate_word(input_word)

        output_path = input_word.replace('.docx', '.pdf')

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Converting Word to PDF...", total=None)

            convert(input_word, output_path)

        self.console.print(f"[green]Word document converted to PDF successfully: {output_path}[/green]")

    def convert_images_to_pdf(self, image_list, output_path):
        """Convert images to PDF"""
        if not image_list:
            raise ValueError("No images provided for conversion")

        images = []
        with Progress() as progress:
            task = progress.add_task("[cyan]Converting images to PDF...", total=len(image_list))

            for image_path in image_list:
                self._validate_image(image_path)
                image = Image.open(image_path)
                if image.mode == 'RGBA':
                    image = image.convert('RGB')
                images.append(image)
                progress.update(task, advance=1)

            if images:
                images[0].save(output_path, save_all=True, append_images=images[1:])

        self.console.print(f"[green]Images converted to PDF successfully: {output_path}[/green]")

    def convert_pdf_to_images(self, input_pdf, output_dir):
        """Convert PDF to images"""
        self._validate_pdf(input_pdf)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Converting PDF to images...", total=None)

            images = convert_from_path(input_pdf)

            for i, image in enumerate(images):
                image_path = os.path.join(output_dir, f'page_{i + 1}.png')
                image.save(image_path, 'PNG')

        self.console.print(f"[green]PDF converted to images successfully in: {output_dir}[/green]")