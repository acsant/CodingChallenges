from sets import Set
class Library:
    def __init__(self, LIBRARY_DATA):
        self.word_dict = {}
        self.processData(LIBRARY_DATA)

    def processData(self, LIBRARY_DATA):
        for line in LIBRARY_DATA:
            currLine = line.split(': ')
            if currLine[0] == 'TITLE':
                currName = currLine[1].rstrip()
            elif currLine[0] == 'AUTHOR' or currLine[0] == 'DESCRIPTION':
                keyList = Set(currLine[1].split(" "))
                for key in keyList:
                    oneKey = key.rstrip().lower()
                    oneKey = oneKey.replace(',','')
                    if oneKey in self.word_dict:
                        self.word_dict[oneKey].update([currName])
                    else:
                        self.word_dict[oneKey] = Set([currName])

    def search(self, word):
        if word.lower() in self.word_dict:
            results = self.word_dict[word.lower()]
            toRet = []
            for res in results:
                toRet.append(Book(res))
            return toRet
        return []

class Book:
    def __init__(self, title):
        self.title = title
