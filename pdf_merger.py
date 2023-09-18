import PyPDF2

pdfiles = ["Exp3.pdf", "Tutorial-1.pdf", "Tutorial2.pdf" ]  #pdf files to be mereged

merger = PyPDF2.PdfMerger()
for filename in pdfiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)

pdfFile.close()
merger.write('merged.pdf')
