# Requires: Pillow
import sys, glob
from PIL import Image, ImageOps

def convert(filepaths):
  images = [(filepath, ImageOps.exif_transpose(Image.open(filepath))) for filepath in filepaths]

  for (filepath, image) in images:
    dot = filepath.rfind(".")
    pdf_path = filepath[:dot] + ".pdf"
    image.save(pdf_path, "PDF", resolution=600.0, save_all=True)  

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("usage: <input_dir>")
  raw_filepaths = sys.argv[1:]

  filepaths = []
  for rfp in raw_filepaths:
    for g in glob.glob(rfp):
      filepaths.append(g)

  if not filepaths:
    raise Exception("no files")

  convert(filepaths=filepaths)
