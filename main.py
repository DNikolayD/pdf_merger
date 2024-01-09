from os import listdir, curdir
from PyPDF2 import PdfMerger

merger = PdfMerger()

for file in listdir(curdir):
    if file.endswith('.pdf'):
        merger.append(file)
    merger.write('merged_pdfs_rename.pdf')
