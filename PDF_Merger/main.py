from PyPDF2 import PdfWriter
import os
import sys

# Set the working directory to where the script is
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

import time

merger = PdfWriter()

pdfs = []
n = int(input("How many pdfs do you want to merge?\n"))

for i in range(0, n): 
    name = input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    if os.path.exists(pdf):
        print(f"Trying to append: {pdf}")
        merger.append(pdf)
    else:
        print(f"File not found: {pdf}")
        print(f"Checking for: {os.path.abspath(pdf)}")


    time.sleep(1.75)
    

merger.write(f"merged-pdf{n}.pdf")
print(f"Successfully merged {n} PDF's into merged-pdf{n}.pdf ")
merger.close()