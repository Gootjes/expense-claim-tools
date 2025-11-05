# requires pypdf, reportlab
# https://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python
import pypdf
import io
import sys
from reportlab.pdfgen import canvas

from reportlab.lib import colors
import re
import pathlib

def generate_packet(number):
  packet = io.BytesIO()
  can = canvas.Canvas(packet)
  can.setStrokeColor(colors.black) # white
  can.setFillColor(colors.black) # black
  can.rect(0, 0, 100, 30, stroke=1, fill=1) 

  can.setFillColor(colors.white) # black
  can.drawString(10, 10, f"{number}")

  can.save()

  packet.seek(0)
  return packet

def add_text(input_dir, output_dir):
  files = list(pathlib.Path(input_dir).glob("*.pdf"))
  for file in files:
    reader = pypdf.PdfReader(str(file))
    writer = pypdf.PdfWriter()
    m = re.match("^([0-9]{3}-)+", file.name)
    if m:
      number = m.group(0)[:-1]
      packetPDF = pypdf.PdfReader(generate_packet(number))
      for page in reader.pages:
        page.merge_page(packetPDF.pages[0])  
        added_page = writer.add_page(page)
      writer.write(f"{output_dir}/{file.name}")
    reader.close()
    writer.close()

if __name__ == "__main__":
  input_dir = sys.argv[1]
  if not input_dir:
    raise Exception("no input directory specified: usage <input_dir> [<output_dir>]")
  output_dir = input_dir + "/Stamped"
  if len(sys.argv) > 2:
    output_dir = sys.argv[2]
  if not pathlib.Path(output_dir).exists:
   raise Exception("output directory does not exist")
  add_text(input_dir=input_dir, output_dir=output_dir)

