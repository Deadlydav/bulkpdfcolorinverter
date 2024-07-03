# BULK PDF Color Inverter

This Python script automates the process of inverting colors in PDF documents, tailored for text-heavy or image-heavy pages giving a Dark Mode feeling

## Features

- **Color Inversion**: Efficiently inverts colors of PDF pages.
- **Text and Image Detection**: Differentiates between text-heavy and image-heavy pages for optimal processing.
- **Multi-threaded Processing**: Uses concurrent threads for faster processing of multiple PDF files.
- **Automatic PDF Conversion**: Converts processed pages back into PDF format without converting everything into images first, saving space.

## Requirements

- Python 3.6+
- PyMuPDF (`fitz`) library
- Pillow (`PIL`) library
- PyPDF2 library

## Installation

1. Clone the repository:
```

git clone https://github.com/Deadlydav/bulkpdfcolorinverter.git

```

3. Install the required libraries:
```

pip install PyMuPDF pillow PyPDF2

```

## Usage

1. Modify the input_folder and output_folder variables at the end of the invert_pdf_colors.py to specify your input PDF directory and desired output directory.
```
    # Define input and output directories
    input_folder = '/path/to/your/input/folder'
    output_folder = '/path/to/your/output/folder'
```

3. Run the script:
```

python3 invert_pdf_colors.py

```


3. Inverted PDFs will be saved in the `output` folder structure.

## Configuration

Adjust the following parameters in `invert_pdf_colors.py` as needed:

- `dpi`: DPI resolution for image conversion.
- `contrast_factor`: Adjusts contrast enhancement for image-heavy pages.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyMuPDF](https://pypi.org/project/PyMuPDF/)
- [Pillow](https://pypi.org/project/Pillow/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Contributing

Pull requests are welcome.
