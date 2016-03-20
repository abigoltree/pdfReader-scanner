import re
march = re.compile('\W', re.IGNORECASE)
with open('/home/pc-linux/programming/txtout.txt', 'rw') as textStream:
    totalStr = textStream.read()
#print totalStr
def WordCounter():
    for line in totalStr:
        for word in line.split():
            print read()
            wordList = march.findAll(word)
            print wordList.length
