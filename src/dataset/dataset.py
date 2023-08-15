import pathlib
import json
import requests
import pdf2image
import PIL
import pytesseract

class Dataset:
    """Represents a CDS file"""
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year

def get_urls() -> dict:
    cds_url_path = pathlib.Path.cwd() / 'assets' / 'cds.json'
    with open(cds_url_path, 'r') as f:
        return json.load(f)

dataset_urls = get_urls()

def rasterize_pdf(dataset: Dataset) -> list[PIL.Image]:
    """Fetches the PDF from the CDS and converts it to a list of PIL images"""
    response = requests.get(dataset_urls[dataset.name][dataset.year]["url"])
    response.raise_for_status()

    pages = pdf2image.convert_from_bytes(response.content)
    return pages
