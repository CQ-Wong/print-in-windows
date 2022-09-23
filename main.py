import html
import os
import tempfile

import win32api
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def print_txt_as_pdf():
  cwd = os.getcwd()
  source_file_name = f"{cwd}\\test_files\\test.txt"
  pdf_file_name = tempfile.mktemp(".pdf")

  styles = getSampleStyleSheet()
  h1 = styles["h1"]
  normal = styles["Normal"]

  doc = SimpleDocTemplate (pdf_file_name)
  #
  # reportlab expects to see XML-compliant
  #  data; need to escape ampersands &c.
  #
  text = html.escape(open(source_file_name).read()).splitlines()

  #
  # Take the first line of the document as a
  #  header; the rest are treated as body text.
  #
  story = [Paragraph (text[0], h1)]
  for line in text[1:]:
    story.append(Paragraph (line, normal))
    story.append(Spacer (1, 0.2 * inch))

  doc.build (story)
  win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)

def print_pdf():
  cwd = os.getcwd()
  pdf_file_name = f"{cwd}\\test_files\\test.pdf"
  win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

if __name__ == "__main__":
  # print_pdf()
  print_txt_as_pdf()

