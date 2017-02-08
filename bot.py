from colors import Colors
from cleverbot import Cleverbot
import pyttsx
from filter import Filter

class Bot:
  def __init__(self, tName, tColor, tVoice, tVoiceRate, tFilter):
    self.mCb = Cleverbot(tName)
    self.mName = tName
    self.mColor = tColor
    self.mVoice = tVoice
    self.mVoiceRate = tVoiceRate
    self.mFilter = tFilter
    
  def ask(self, tQuestion):
    #tQuestion = self.mFilter.removeUnicode(tQuestion)
    tReply = self.mCb.ask(tQuestion)
    tReply = self.mFilter.filter(tReply)
    self.type(tReply)
    self.say(tReply)
    return tReply
    
  def type(self, tText):
    print Colors.BOLD + self.mColor + self.mName + ": " + Colors.ENDC + self.mColor + tText + Colors.ENDC

  def say(self, tText):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + self.mVoiceRate)
    voices= engine.getProperty('voices')
    engine.setProperty('voice', self.mVoice)
    engine.say(tText)
    a = engine.runAndWait()
