from PyPDF2 import PdfFileReader, PdfFileMerger
pdf_file1 = PdfFileReader("file1.pdf") #read file
pdf_file2 = PdfFileReader("file2.pdf")
pdfoutput = PdfFileMerger()
pdfoutput.append(pdf_file1) #add it to the merger
pdfoutput.append(pdf_file2)

with open("mergedfile.pdf", "wb") as finaloutput:
    pdfoutput.write(finaloutput)

## large file merger
import os
from PyPDF2 import PdfFileMerger
source_dir=os.getcwd() #get current working directory

merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)

merger.write("complete.pdf")
merger.close