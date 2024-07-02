PDF Color Inverter

This Python script allows you to invert the colors of PDF documents. It converts each page of a PDF into an image, inverts the colors of the image, and then converts it back to PDF format.
Requirements

    Python 3.x
    PyMuPDF (fitz)
    Pillow (PIL fork)
    PyPDF2
    ReportLab

Install dependencies using pip:

bash

pip install PyMuPDF Pillow PyPDF2 reportlab

Usage

    Clone the repository:

    bash

git clone https://github.com/Deadlydav/bulkpdfcolorinverter.git
cd pdf-color-inverter

Run the script:

Modify the input_folder and output_folder variables in invert_pdf_colors.py to specify your input PDF directory and desired output directory.

python

# Define input and output directories
input_folder = '/path/to/your/input/folder'
output_folder = '/path/to/your/output/folder'

# Invert colors of PDFs from input folder and save to output folder with a DPI suitable for a Kindle
invert_pdf_colors(input_folder, output_folder, dpi=300)  # Use 167 if targeting older models

Execute the script:

bash

    python3 bulkpdfinverter.py

    The script will process each PDF file in the input_folder, invert the colors of each page, and save the processed PDFs in corresponding subfolders within the output_folder.

Customization

    DPI Setting: Adjust the dpi parameter in invert_pdf_colors.py for different output quality. Higher DPI values result in better quality but larger file sizes.
    Output Subfolders: The script preserves the subfolder structure of your input PDF directory in the output directory.

Notes

    Ensure your input PDFs do not contain password protection or encryption, as this script does not handle protected PDFs.
    The script assumes input PDFs are standard and not malformed; unexpected PDF structures may cause errors.

License

This project is licensed under the MIT License - see the LICENSE file for details.
