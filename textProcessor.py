import re

def sanitizeText(txtSource):
    print txtSource
    regex = re.compile('[^a-zA-Z\'., \n]')
    sample = regex.sub('', txtSource)
    print sample
    return txtSource

def wordIntoSortList(wordString):
    #regex = re.compile()
    wordList = re.split('\w', wordString)
    wordList.sort()
    print wordList
    return wordList

def wordCount(wordList):
    print wordList
    dictionary = dict()
    for word in wordList:
        if not dictionary.has_key(word):
            print word
            dictionary[word] = wordList.count(word)
    return dictionary
