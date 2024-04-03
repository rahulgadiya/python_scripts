"""
To run the provided script `text_extractor.py`, follow these steps:

1. **Install Dependencies**:
   Ensure you have the necessary libraries installed. You can install them using pip:

>>>> pip install PyPDF2 Pillow pytesseract

2. **Prepare Input File**:
Have the input file ready. It should be either a PDF file or an image file containing text (supported formats include JPG, JPEG, PNG, BMP, and GIF).

3. **Execute the Script**:
Open a terminal or command prompt and navigate to the directory where the script `text_extractor.py` is located.

4. **Run the Script**:
Execute the script by running the following command:

>>>  python text_extractor.py input.pdf output_text

This command will extract text from the PDF file `input.pdf` and save the extracted text to two files: `output_text.txt` and `output_text.md`.

5. **Check Output**:
After running the script, you should see a confirmation message indicating that the text has been extracted and saved. You can then check the output files (`output_text.txt` and `output_text.md`) to view the extracted text.

By following these steps, you can run the `text_extractor.py` script to extract text from PDF and image files. If you encounter any issues or have further questions, feel free to ask!
"""

# Your script code goes here

import sys
import os
import PyPDF2
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_file_path):
    """
    Extract text from a PDF file.
    """
    try:
        with open(pdf_file_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            text = ''
            for page in range(pdf_reader.getNumPages()):
                text += pdf_reader.getPage(page).extractText()
            return text
    except FileNotFoundError:
        print("Error: PDF file not found.")
        sys.exit(1)
    except PyPDF2.utils.PdfReadError:
        print("Error: Unable to read the PDF file.")
        sys.exit(1)

def extract_text_from_image(image_file_path):
    """
    Extract text from an image file using OCR.
    """
    try:
        text = pytesseract.image_to_string(Image.open(image_file_path))
        return text
    except FileNotFoundError:
        print("Error: Image file not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Unable to extract text from image. {e}")
        sys.exit(1)

def save_text_to_file(text, output_file):
    """
    Save extracted text to a text file and a Markdown file.
    """
    try:
        # Save text to .txt file
        with open(output_file + ".txt", 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text extracted and saved to {output_file}.txt.")
        
        # Save formatted text to .md file
        markdown_text = format_markdown_text(text)
        with open(output_file + ".md", 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        print(f"Text extracted and saved to {output_file}.md.")
    except IOError:
        print("Error: Unable to save text to file.")
        sys.exit(1)

def format_markdown_text(text):
    """
    Format text for Markdown file.
    """
    # Escape special characters
    markdown_text = text.replace("_", "\\_").replace("*", "\\*").replace("[", "\\[").replace("]", "\\]").replace("(", "\\(").replace(")", "\\)")
    return markdown_text

if __name__ == "__main__":
    # Check if correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python convert_pdf_to_md_txt.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if output files already exist
    if os.path.exists(output_file + ".txt") or os.path.exists(output_file + ".md"):
        print("Error: Output file already exists. Please provide a different output file name.")
        sys.exit(1)

    # Determine file type and extract text accordingly
    if input_file.lower().endswith('.pdf'):
        text = extract_text_from_pdf(input_file)
    elif input_file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        text = extract_text_from_image(input_file)
    else:
        print("Error: Unsupported file format. Supported formats are PDF, JPG, JPEG, PNG, BMP, and GIF.")
        sys.exit(1)

    # Save extracted text to files
    save_text_to_file(text, output_file)






