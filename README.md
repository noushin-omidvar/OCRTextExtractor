# OCR Text Extractor

OCR Text Extractor is a Python-based automation tool that significantly enhances productivity by monitoring a specified folder for new images, extracting text using Tesseract OCR, and copying it directly to the clipboard. This tool is particularly useful for documentation, note-taking, or any situation requiring efficient extraction of text from images. Designed to work best with simple, non-artistic images, it offers a straightforward solution for automating text extraction tasks.

## Features

- **Automatic Monitoring**: Watches a specified folder for new images.
- **Text Extraction**: Utilizes Tesseract OCR to extract text from images.
- **Clipboard Integration**: Automatically copies the extracted text to the clipboard for easy pasting.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or newer installed on your system.
- Tesseract OCR installed and configured. [Tesseract OCR Installation Guide](https://github.com/tesseract-ocr/tesseract/wiki)

## Installation

Follow these steps to install OCR Text Extractor:

1. Clone the repository:
```
git clone https://github.com/noushin-omidvar/OCRTextExtractor.git
```
2. Navigate to the project directory:

```cd OCRTextExtractor```

3. Install the required dependencies:

```pip install -r requirements.txt```

## Usage
To use OCR Text Extractor, follow these steps:

1. Update the ocr_watchdog.py script with the path to the folder you want to monitor.
2. Run the script:
```python ocr_watchdog.py```

Place any image in the specified folder, and the extracted text will automatically be copied to your clipboard.

## Configuration
**Customizing the Watch Folder:** Edit the `ocr_watchdog.py` script to set the `path` variable to your target directory.
**Tesseract Path:** If necessary, specify the path to the Tesseract executable in the ocr_watchdog.py script.


## Contributing to OCR Text Extractor
To contribute to OCR Text Extractor, follow these steps:

1. Fork this repository.
2. Create a branch: git checkout -b branch_name.
3. Make your changes and commit them: git commit -m 'commit_message'.
4. Push to the original branch: git push origin OCRTextExtractor/branch_name.
5. Create the pull request.

Alternatively, see the GitHub documentation on creating a pull request.

## Contact
If you want to contact me, you can reach me at noush-omidvar@gmail.com.



