import os
import exifread
import PyPDF2
import sys
from PIL import Image


def extract_metadata(filepath):
    # Get file extension
    ext = os.path.splitext(filepath)[1].lower()

    # Initialize metadata dictionary
    metadata = {}

    # Extract metadata based on file type
    if ext == ".jpg" or ext == ".jpeg" or ext == ".png" or ext == ".gif":
        with open(filepath, "rb") as f:
            tags = exifread.process_file(f)
            for tag in tags.keys():
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    metadata[tag] = str(tags[tag])
    elif ext == ".pdf":
        with open(filepath, "rb") as f:
            pdf = PyPDF2.PdfFileReader(f)
            info = pdf.getDocumentInfo()
            for key, value in info.items():
                metadata[key] = value
    else:
        # Handle unsupported file types
        print("Unsupported file type:", ext)
    return metadata

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python metadata_scraper.py <filename>")
        sys.exit(1)
    filename_path = sys.argv[1]
    metadata = extract_metadata(filename_path)
    print(metadata)   

