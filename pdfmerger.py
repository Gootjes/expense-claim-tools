# requires pypdf, reportlab
# https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python
import pypdf, glob
import io
import sys
from reportlab.pdfgen import canvas

from reportlab.lib import colors
import re
import pathlib

def merge(files, output_file):
  merger = pypdf.PdfWriter()
  for pdf in files:
    merger.append(pdf)
  merger.write(output_file)
  merger.close()

if __name__ == "__main__":
  input_dir = sys.argv[1]
  if not input_dir:
    raise Exception("no input directory specified: usage <input_dir> [<output_dir>]")
  output_file = input_dir + "/merged.pdf"
  filepaths = []
  for g in glob.glob(input_dir + "/*.pdf"):
    filepaths.append(g)
  merge(filepaths, output_file)

