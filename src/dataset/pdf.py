import pathlib
import json
import logging
import requests
import PIL
import pdf2image

__all__ = ["rasterize_pdf"]

def get_urls() -> dict:
    cds_url_path = pathlib.Path.cwd() / 'assets' / 'cds.json'
    with open(cds_url_path, 'r') as f:
        return json.load(f)


dataset_urls = get_urls()


def rasterize_pdf(name: str, year: str) -> list[PIL.Image]:
    """Fetches the PDF from the CDS and converts it to a list of PIL images"""
    pdf_info = dataset_urls[name][year]

    logging.info(f"Fetching {name} {year} CDS")
    response = requests.get(pdf_info["url"])
    response.raise_for_status()

    logging.info(f"Rasterizing {name} {year} CDS")
    start_page = pdf_info["start_page"]
    pages = pdf2image.convert_from_bytes(response.content, first_page=start_page,
                                         grayscale=True, dpi=300)

    logging.info(f"Preprocessing {name} {year} CDS")
    header, footer = pdf_info["header"], pdf_info["footer"]

    def cropped_page_bbox(size: tuple[int, int]) -> tuple[int, int, int, int]:
        return 0, int(size[1] * header), size[0], int(size[1] * (1 - footer))
    pages = [page.crop(cropped_page_bbox(page.size)) for page in pages]

    return pages
