from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog
import os

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# image_path = r"C:\Users\desti\OneDrive - Stratford University\Aditya\DataScience\Python\text_image2.png"
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

# Opening the image & storing it in an image object
img = Image.open(file_path)
print('File Path>>>>>>>>>>', file_path)
filename = os.path.basename(file_path)
pathname, extension = os.path.splitext(file_path)
filename = pathname.split('/')
final_filename = filename[-1]
print('File Name Without Extension>>>>>>>>>>>>>>>>>>', final_filename)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)

print('Text?????????????????', text)

# location to save created text file temporaily
text_file_path = r"C:\Users\desti\OneDrive - Stratford University\Aditya\DataScience\Python\generated_files"
suffix = '.txt'
final_file_path = os.path.join(text_file_path, final_filename + suffix)
print('final_file_path>>>>>>>>>>>>>', final_file_path)

if not os.path.exists(text_file_path):
    os.makedirs(text_file_path)
f = open(final_file_path, "w")
text_file_with_content = f.write(text[:-1])

# Displaying the extracted text
print('text_file_with_content>>>>>>>>>>>>>>>>>', text_file_with_content)
