import PyPDF2
def FileReader(filePathIn, fileOutput):
    pdfFileObj = open(filePathIn,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numbers = pdfReader.numPages
    text_file = open(fileOutput,'w')
    pageObj = pdfReader.getPage(0)
    outs = pageObj.extractText()
    #print outs
    text_file.write(outs.encode('utf-16'))
    #print outs
    return outs
