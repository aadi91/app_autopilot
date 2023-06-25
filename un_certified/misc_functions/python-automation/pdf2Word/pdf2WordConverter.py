
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from pdf2docx import parse


docx_file_path = r"C:\Users\desti\OneDrive - Stratford University\Aditya\DataScience\Python\generated_files\pdf_2_word_generated_files"
root = tk.Tk()
root.withdraw()
pdf_file = filedialog.askopenfilename()
print('pdf_file>>>>>>>>>>>>>>', pdf_file)
filname_Without_ext = Path(pdf_file).stem
print('File Name Without Extension>>>>>>>>>>>>>>>>>>', filname_Without_ext)
suffix = '.docx'
word_file_path = os.path.join(docx_file_path, filname_Without_ext + suffix)
print('final_file_path>>>>>>>>>>>>>', word_file_path)

# convert pdf to docx
converted_docx_file = parse(pdf_file, word_file_path, start=0, end=None)
print('converted_docx_file>>>>>>>>>>>>>>', converted_docx_file)
