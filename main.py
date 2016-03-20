import pdfread
import glob
import textProcessor
listo = []

#globsys = 'home/*/*/*/*/*/*PZO*.pdf'
#def filefinder(globsys):
#    for name in glob.glob(globsys):
#        list.append(name)
#    for uses in listo:
#        print(uses)

pdfread.FileReader()
textProcessor.sanitizeText()
textProcessor.wordIntoSortList()
textProcessor.wordCount()
