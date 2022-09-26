import html
import os
import tempfile

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def get_whole_file_name(file_name):
  cwd = os.getcwd()
  whole_file_name = os.path.join(cwd, file_name)
  return whole_file_name

def convert_txt_to_pdf(txt_file_name):
  pdf_file_name = tempfile.mktemp(".pdf")

  styles = getSampleStyleSheet()
  h1 = styles["h1"]
  normal = styles["Normal"]

  doc = SimpleDocTemplate (pdf_file_name)
  text = html.escape(open(txt_file_name).read()).splitlines()

  #
  # Take the first line of the document as a
  #  header; the rest are treated as body text.
  #
  story = [Paragraph (text[0], h1)]
  for line in text[1:]:
    story.append(Paragraph (line, normal))
    story.append(Spacer (1, 0.2 * inch))

  doc.build (story)
  return pdf_file_name

if __name__ == "__main__":
  test_txt_file = get_whole_file_name("test_files/test.txt")
  pdf = convert_txt_to_pdf(test_txt_file)
