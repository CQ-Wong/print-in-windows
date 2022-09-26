import win32api

from utils.process_file import convert_txt_to_pdf, get_whole_file_name


def print_txt_as_pdf(txt_file_name):
  pdf_file_name = convert_txt_to_pdf(txt_file_name=txt_file_name)
  win32api.ShellExecute(0, "print", pdf_file_name, None, ".", 0)


def print_pdf(pdf_file_name):
  win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)


if __name__ == "__main__":
  test_txt_file = get_whole_file_name("test_files/test.txt")
  print_txt_as_pdf(test_txt_file)

  test_pdf_file = get_whole_file_name("test_files/test.pdf")
  print_pdf(pdf_file_name=test_pdf_file)

