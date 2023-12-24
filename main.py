# Need to install ( pip install pillow )
from PIL import Image

# Need to install ( pip install pytesseract )
# and Need to install the pytesseract application.
import pytesseract

# Need to install ( pip install pytesseract )
from googletrans import Translator

# Standard python library
import pathlib

# Configuring the pytesseract package.
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

translator = Translator()

stars = "\n" + "*" * 50 + "\n\n"


ans = input("Do you want the photos to be translate into persian? (y/n): ")

# Loop for reading files
for path in pathlib.Path("per-pics").iterdir():
    if path.is_file():
        img = path
        per_text = pytesseract.image_to_string(Image.open(img), lang="fas")
        if "y" in ans.lower():
            per_tr_text = translator.translate(per_text, src="fa", dest="en")
            print(f"متن اصلی فایل {img.name}:\n" + per_text)
            print(stars)
            print(f"Translated text of the {img.name} file:\n" + per_tr_text.text)
            with open(fr"D:\Projects\convert-image-to-text\Output-files\{img.name.split(".")[0]}-to-english.txt",
                      "w", encoding="utf-8") as t:
                t.write(per_tr_text.text)
        else:
            print(per_text)
        with open(fr"D:\Projects\convert-image-to-text\Output-files\{img.name.split(".")[0]}.txt",
                  "w", encoding="utf-8") as o:
            o.write(per_text)
        print(stars)


for path in pathlib.Path("eng-pics").iterdir():
    if path.is_file():
        img = path
        en_text = pytesseract.image_to_string(Image.open(img), lang="eng")
        if "y" in ans.lower():
            en_tr_text = translator.translate(en_text, src="en", dest="fa")
            print(f"Original text of the {img.name} file:\n" + en_text)
            print(stars)
            print(f"متن ترجمه شده فایل {img.name}:\n" + en_tr_text.text)
            with open(fr"D:\Projects\convert-image-to-text\Output-files\{img.name.split(".")[0]}-to-persian.txt",
                      "w", encoding="utf-8") as t:
                t.write(en_tr_text.text)
        else:
            print(en_text)
        with open(fr"D:\Projects\convert-image-to-text\Output-files\{img.name.split(".")[0]}.txt",
                  "w", encoding="utf-8") as o:
            o.write(en_text)
        print(stars)
