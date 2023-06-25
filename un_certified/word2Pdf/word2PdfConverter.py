# Python3 program to convert docx to pdf
# using docx2pdf module
 
# Import the convert method from the
# docx2pdf module
import os
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from docx2pdf import convert
 
# Converting docx present in the same folder
# as the python file
#convert("GFG.docx")

pdf_file = r"C:\Users\desti\OneDrive - Stratford University\Aditya\DataScience\Python\generated_files\word_2_pdf_generated_files"
root = tk.Tk()
root.withdraw()
docx_file_path = filedialog.askopenfilename()
print('pdf_file>>>>>>>>>>>>>>', pdf_file)
filname_Without_ext = Path(docx_file_path).stem
print('File Name Without Extension>>>>>>>>>>>>>>>>>>', filname_Without_ext)
suffix = '.pdf'
pdf_file_path = os.path.join(pdf_file, filname_Without_ext + suffix)
print('final_file_path>>>>>>>>>>>>>', pdf_file_path)
 
# Converting docx specifying both the input
# and output paths
converted_pdf_file = convert(docx_file_path, pdf_file_path)
print('converted_pdf_file>>>>>>>>>>>>>', converted_pdf_file)
 
# Notice that the output filename need not be
# the same as the docx
 
# Bulk Conversion
# convert("GeeksForGeeks\")