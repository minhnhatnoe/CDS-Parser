import pytesseract
import PIL

# Workaround at https://github.com/madmaze/pytesseract/issues/106#issuecomment-605539554
def parse_page(image: PIL.Image):
    text = pytesseract.image_to_data(image, config=' -c tessedit_create_boxfile=1')
    return text
