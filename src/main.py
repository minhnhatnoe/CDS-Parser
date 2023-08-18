import logging
from dataset.dataset import Dataset
from dataset import ocr

logging.basicConfig(level=logging.INFO)

a = Dataset("stanford", "2022-2023")
print(ocr.parse_page(a.pages[3]))
