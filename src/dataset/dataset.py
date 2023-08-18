from . import pdf
class Dataset:
    """Represents a CDS file"""
    def __init__(self, name: str, year: str):
        self.name = name
        self.year = year
        self.pages = pdf.rasterize_pdf(self.name, self.year)
