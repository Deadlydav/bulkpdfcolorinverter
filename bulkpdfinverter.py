import os
import fitz  # PyMuPDF
from PIL import Image, ImageOps
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def image_to_pdf(image_path, output_path, dpi):
    """Convert an image file to a PDF using reportlab and save to output_path."""
    image = Image.open(image_path)
    width, height = image.size
    c = canvas.Canvas(output_path, pagesize=(width, height))
    c.drawImage(image_path, 0, 0, width=width, height=height)
    c.save()

def invert_pdf_colors(input_folder, output_folder, dpi=300):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through all folders and files in the input directory
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith('.pdf'):
                input_file = os.path.join(root, filename)
                relative_path = os.path.relpath(input_file, input_folder)
                output_subfolder = os.path.dirname(os.path.join(output_folder, relative_path))
                output_file = os.path.join(output_subfolder, filename)
                
                try:
                    # Open the input PDF file
                    pdf_input = fitz.open(input_file)
                    pdf_output = PdfWriter()
                    
                    # Loop through each page in the PDF document
                    for page_num in range(len(pdf_input)):
                        page = pdf_input.load_page(page_num)
                        
                        # Convert page to image with high resolution
                        pix = page.get_pixmap(dpi=dpi)
                        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                        
                        # Invert colors of the image
                        inverted_image = ImageOps.invert(image)
                        
                        # Save the inverted image as a temporary file
                        temp_image_path = f'temp_page_{page_num}.png'
                        inverted_image.save(temp_image_path)
                        
                        # Convert the inverted image to a temporary PDF
                        temp_pdf_path = f'temp_page_{page_num}.pdf'
                        image_to_pdf(temp_image_path, temp_pdf_path, dpi)
                        
                        # Add the temporary PDF page to the output PDF
                        temp_pdf = PdfReader(temp_pdf_path)
                        pdf_output.add_page(temp_pdf.pages[0])
                        
                        # Clean up temporary files
                        os.remove(temp_image_path)
                        os.remove(temp_pdf_path)
                    
                    # Ensure output subfolder exists
                    if not os.path.exists(output_subfolder):
                        os.makedirs(output_subfolder)
                    
                    # Write output PDF to file
                    with open(output_file, 'wb') as f:
                        pdf_output.write(f)
                    
                    print(f"Processed: {input_file}")
                
                except Exception as e:
                    print(f"Error processing {input_file}: {e}")

if __name__ == "__main__":
    # Define input and output directories
    input_folder = '/input/folder/location'
    output_folder = '/output/folder/location'
    
    # Invert colors of PDFs from input folder and save to output folder with a DPI suitable for a Kindle
    invert_pdf_colors(input_folder, output_folder, dpi=300)  # Use 167 if targeting older models

