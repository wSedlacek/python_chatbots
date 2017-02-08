from random import randint
from unicodedata import normalize

class Filter:
  def __init__(self, tLimit, tBan, tTopics):
    self.mLimit = tLimit
    self.mBan = tBan
    self.mTopics = tTopics

  def filter(self, tString):
    #tString = self.replaceUnicode(tString)
    tString, tFiltered = self.wordsLimit(tString)
    return tString

  def replaceUnicode(self, tString):
    tString = normalize('NFKD', tString).encode('ascii','ignore')
    return tString
  
  def removeUnicode(self, tString):
    tString = tString.encode('ascii','ignore')
    tString = ''.join([i if ord(i) < 128 else ' ' for i in tString])
    tString = str(tString)
    return tString

  def wordsCensor(self, tString):
    tWords = tString.split()
    tFiltered = False
    for tWord in tWords:
      for tBannedWord in self.mBan:
        if tWord == tBannedWord:
          tFiltered = True
        if tFiltered:
          break
      if tFiltered:
        break
    if tFiltered:
      print "FILTER! " + tString
      tString = self.reTopic()
    return tString, tFiltered

  def wordCensor(self, tWord, tString):
    tFiltered = False
    for tBannedWord in self.mBan:
      if tWord == tBannedWord:
        tFiltered = True
      if tFiltered:
        break
    if tFiltered:
      tString = self.reTopic()
    return tString, tFiltered

  def wordsLimit(self, tString):
    tWords = tString.split()
    tFiltered = False
    for tWordUno in tWords:
      tCount = 0
      for tWordDos in tWords:
        if tWordUno == tWordDos:
          tCount = tCount + 1
          if tCount == self.mLimit:
            tFiltered = True
        tString, tFiltered = self.wordCensor(tWordDos, tString)
        if tFiltered:
          break
      if tFiltered:
        break
    if tFiltered:
      tString = self.reTopic()
    return tString, tFiltered
    
  def reTopic(self):
    tTopic = randint(0, len(self.mTopics) - 1)
    return self.mTopics[tTopic]

  def randomBot(self, tBots, tLastBot):
    tBot = tLastBot
    while tBot == tLastBot: tBot = randint(0, len(tBots) - 1)
    return tBot
