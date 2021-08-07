def encrypt(file_name,password):
    out = PdfFileWriter()
    file = PdfFileReader("Simple files/"+file_name)
    num = file.numPages
    for idx in range(num):
        page = file.getPage(idx)
        out.addPage(page)
        out.encrypt(password)
        with open("Encrypted/"+file_name, "wb") as f:
            out.write(f)


import os
from PyPDF2 import PdfFileWriter, PdfFileReader
arr = os.listdir('Simple files')
password="password"
for i in arr:
    encrypt(i,password)

