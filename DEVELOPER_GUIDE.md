# PDF Master Tool - Developer Guide

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Code Structure](#code-structure)
4. [Development Setup](#development-setup)
5. [Contributing Guidelines](#contributing-guidelines)

## Project Overview

The PDF Master Tool is a Python-based command-line interface (CLI) application for comprehensive PDF management. It provides a suite of tools for manipulating PDF files, including encryption, merging, splitting, and format conversion.

### Technology Stack
- Python 3.8+
- Libraries:
  - PyPDF2 (PDF manipulation)
  - rich (CLI interface)
  - pdf2docx (PDF to Word conversion)
  - docx2pdf (Word to PDF conversion)
  - pillow (Image processing)
  - pdf2image (PDF to image conversion)

## System Architecture

### Component Overview
```
PDFMasterTool/
├── pdf_manager.py         # Main application entry point
├── utils/                 # Utility modules
│   ├── __init__.py       # Package marker
│   ├── menu.py           # Menu system
│   ├── pdf_operations.py # Core PDF operations
│   └── test_utils.py     # Testing utilities
├── test_files/           # Generated test files
├── USER_GUIDE.md         # End-user documentation
└── DEVELOPER_GUIDE.md    # Developer documentation
```

### File Descriptions

1. **pdf_manager.py**
   - Application entry point
   - Handles user interaction
   - Manages the main program loop
   - Error handling and input validation

2. **utils/menu.py**
   - Implements the CLI menu system
   - Uses rich library for formatted output
   - Handles both interactive and non-interactive modes

3. **utils/pdf_operations.py**
   - Core PDF manipulation functionality
   - Class: PDFOperations
     - PDF encryption/decryption
     - Metadata extraction
     - PDF merging/splitting
     - Page rotation
     - Format conversions

4. **utils/test_utils.py**
   - Testing utilities
   - Sample file generation
   - Test PDF creation
   - Test image creation

## Code Structure

### Core Classes

#### PDFOperations (pdf_operations.py)
```python
class PDFOperations:
    def __init__(self):
        self.console = Console()

    def _validate_pdf(self, pdf_path)
    def _validate_word(self, word_path)
    def _validate_image(self, image_path)
    def encrypt_pdf(self, input_pdf, password)
    def decrypt_pdf(self, input_pdf, password)
    def extract_metadata(self, input_pdf)
    def merge_pdfs(self, pdf_list, output_path)
    def split_pdf(self, input_pdf, output_dir)
    def rotate_pages(self, input_pdf, page_num, rotation)
    def convert_pdf_to_word(self, input_pdf)
    def convert_word_to_pdf(self, input_word)
    def convert_images_to_pdf(self, image_list, output_path)
    def convert_pdf_to_images(self, input_pdf, output_dir)
```

### Control Flow
1. User runs pdf_manager.py
2. Main loop displays menu (menu.py)
3. User selects operation
4. Input validation
5. Operation execution (pdf_operations.py)
6. Result display
7. Return to menu

## Development Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install rich PyPDF2 pdf2docx docx2pdf pillow pdf2image
```
3. Create test files:
```bash
python pdf_manager.py
# Select option 11
```

### Development Environment
- Python 3.8+ required
- IDE with Python support recommended
- Git for version control

## Contributing Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include type hints where appropriate

### Adding New Features
1. Create feature branch
2. Implement feature in utils/pdf_operations.py
3. Add menu option in utils/menu.py
4. Update main program in pdf_manager.py
5. Add test cases
6. Update documentation

### Testing
1. Use test_utils.py to generate test files
2. Test in both interactive and non-interactive modes
3. Verify error handling
4. Check output file quality

### Error Handling
- Use try-except blocks
- Validate input files
- Provide clear error messages
- Log errors appropriately

### Documentation
- Update USER_GUIDE.md for user-facing changes
- Update DEVELOPER_GUIDE.md for technical changes
- Include docstrings in code
- Comment complex logic

## Development Workflow

1. **Planning**
   - Feature specification
   - API design
   - User interface planning

2. **Implementation**
   - Code development
   - Unit testing
   - Integration testing

3. **Testing**
   - Functional testing
   - Error handling
   - Edge cases
   - Performance testing

4. **Documentation**
   - Code documentation
   - User guide updates
   - Developer guide updates

5. **Maintenance**
   - Bug fixes
   - Performance improvements
   - Feature enhancements
