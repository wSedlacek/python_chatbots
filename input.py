import sys, select, time

class Input:
  def __init__(self, tTimer):
    self.mTimer = tTimer

  def timed_input(self):
    i, o, e = select.select( [sys.stdin], [], [], self.mTimer )

    if (i):
      return sys.stdin.readline().strip()
    else:
      return ""

  def Interupt(self, tString, tFilter):
    tInput = self.timed_input()
    if tInput == "p":
      time.sleep(30)
    elif tInput == "t":
      tString = tFilter.reTopic()
    elif tInput == "s":
      raw_input()
    elif tInput == "e":
      exit()
    return tString
  
