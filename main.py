import urllib.request
import fitz
import datetime
import os
from PyPDF2 import PdfFileWriter, PdfFileReader


now = datetime.datetime.now()
pdf =urllib.request.urlretrieve("https://cloud.nntc.nnov.ru/index.php/s/fYpXD39YccFB5gM/download", "сайт zameny2021dist.pdf") 
os.rename("сайт zameny2021dist.pdf","list.pdf")
pages_to_keep = [0, 1, 2] # page numbering starts from 0
infile = PdfFileReader('list.pdf', 'rb')
output = PdfFileWriter()

for i in pages_to_keep:
    p = infile.pages[i] 
    output.addPage(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)
fname = "newfile.pdf"  # get filename from command line
doc = fitz.open(fname)  # open document
for page in doc:  # iterate through the pages
    pix = page.get_pixmap()  # render page to an image
    pix.save("page-%i.png" % page.number)  # store image as a PNG

