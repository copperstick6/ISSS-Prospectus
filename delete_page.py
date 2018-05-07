from PyPDF2 import PdfFileWriter, PdfFileReader
pages_to_keep = [0, 1] # page numbering starts from 0
infile = PdfFileReader('isss_prospectus.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i in pages_to_keep:
        p = infile.getPage(i)
        output.addPage(p)

with open('isss_short_prospectus.pdf', 'wb') as f:
    output.write(f)
