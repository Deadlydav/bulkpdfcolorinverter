import os
import fitz  # PyMuPDF
from PIL import Image, ImageOps, ImageEnhance
from PyPDF2 import PdfWriter, PdfReader
import tempfile
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm  # Import tqdm for progress bar

# Function to convert an image to a PDF page
def image_to_pdf(image_path, output_pdf_path, dpi=300):
    image = Image.open(image_path)
    pdf_page = Image.new('RGB', image.size)
    pdf_page.paste(image)
    pdf_page.save(output_pdf_path, dpi=(dpi, dpi))

# Function to analyze page content
def analyze_page_content(page):
    text_instances = page.search_for("")
    image_instances = page.get_images(full=True)
    is_text_heavy = (text_instances is not None and len(text_instances) > len(image_instances))
    return is_text_heavy

# Function to invert colors of a PDF page
def invert_colors(page, temp_image_path, dpi=300, contrast_factor=1.5):
    try:
        if analyze_page_content(page):
            for inst in page.search_for(""):
                text = page.get_textbox(inst)
                if text:
                    page.insert_textbox(inst, text, color=(1, 1, 1), fill=(0, 0, 0))
            page.save(temp_image_path)
        else:
            pix = page.get_pixmap(dpi=dpi)
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            enhancer = ImageEnhance.Contrast(image)
            enhanced_image = enhancer.enhance(contrast_factor)
            inverted_image = ImageOps.invert(enhanced_image)
            
            inverted_image.save(temp_image_path)
    
    except Exception as e:
        print(f"Error processing page: {e}")

# Function to process a PDF file
def process_pdf(input_file, output_folder, dpi=300, contrast_factor=1.5):
    try:
        pdf_input = fitz.open(input_file)
        
        # Create subfolder structure in output directory
        relative_path = os.path.relpath(input_file, start=input_folder)
        output_subfolder = os.path.join(output_folder, os.path.dirname(relative_path))
        if not os.path.exists(output_subfolder):
            os.makedirs(output_subfolder)
        
        # Create a temporary folder for storing individual page images
        temp_folder = tempfile.mkdtemp()
        
        temp_files = []
        for page_num in range(len(pdf_input)):
            page = pdf_input.load_page(page_num)
            temp_image_path = os.path.join(temp_folder, f"temp_page_{page_num}.png")
            invert_colors(page, temp_image_path, dpi=dpi, contrast_factor=contrast_factor)
            temp_files.append(temp_image_path)
        
        # Convert each page image back to PDF and merge into a single PDF
        with PdfWriter() as pdf_writer:
            for temp_file in temp_files:
                temp_pdf_path = temp_file.replace('.png', '.pdf')
                image_to_pdf(temp_file, temp_pdf_path, dpi=dpi)
                with open(temp_pdf_path, 'rb') as temp_pdf_file:
                    pdf_reader = PdfReader(temp_pdf_file)
                    for page in pdf_reader.pages:
                        pdf_writer.add_page(page)
                os.remove(temp_file)
                os.remove(temp_pdf_path)
            
            # Save the merged PDF to the output subfolder
            output_file = os.path.join(output_subfolder, os.path.basename(input_file))
            with open(output_file, 'wb') as output_pdf_file:
                pdf_writer.write(output_pdf_file)
        
        # Clean up temporary folder
        os.rmdir(temp_folder)
        
        print(f"Processed: {os.path.basename(input_file)}")
    
    except Exception as e:
        print(f"Error processing {os.path.basename(input_file)}: {e}")

# Function to process all PDFs in a directory
def process_pdfs_in_directory(input_folder, output_folder, dpi=300, contrast_factor=1.5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    files = []
    for root, _, filenames in os.walk(input_folder):
        for filename in filenames:
            if filename.endswith('.pdf'):
                input_file = os.path.join(root, filename)
                files.append((input_file, output_folder, dpi, contrast_factor))
    
    total_files = len(files)
    
    # Use tqdm for progress bar
    with tqdm(total=total_files, desc="Processing PDFs") as pbar:
        def update_progress(*_):
            pbar.update()
        
        with ThreadPoolExecutor() as executor:
            for file_info in files:
                executor.submit(process_pdf, *file_info).add_done_callback(update_progress)

if __name__ == "__main__":
    # Define input and output directories
    input_folder = '/path/to/your/input/folder'
    output_folder = '/path/to/your/output/folder'
    
    # Invert colors of PDFs from input folder and save to output folder
    process_pdfs_in_directory(input_folder, output_folder, dpi=300, contrast_factor=1.5)

