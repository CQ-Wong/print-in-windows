import os

import win32api


def print_pdf():
  cwd = os.getcwd()
  pdf_file_name = f"{cwd}\\test_files\\test.pdf"
  win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

if __name__ == "__main__":
  print_pdf()

