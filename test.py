# tests functions and process for these scripts starting from main
# (main needs to be renamed)

import main
import pdfread
import textProcessor

main.filefinder()
sampleFile = main.filefinder('/home/*/*/*/*/*/*PZO*.pdf')
textProcessor.sanitizeText()
textProcessor.sanitizeText('hey dawg !!!ggg...\nhey hey hey')
textProcessor.sanitizeText(sampleFile)
textProcessor.wordIntoSortList()
textProcessor.wordIntoSortList()
