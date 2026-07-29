import PyPDF2
import os
import sys

def merge_pdfs(output_filename):
    merger=PyPDF2.PdfMerger()
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
    merger.write(output_filename)
    merger.close()

output_filename = input("Enter the name of the output merged PDF file (with .pdf extension): ")
merge_pdfs(output_filename)

