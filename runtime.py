from bot import Bot
from filter import Filter
from input import Input

import settings
from settings import BotSettings

Censor = Filter(settings.limit, settings.ban, settings.topics)
Starter = Censor.reTopic()
Reader = Input(settings.timer)


Bots = []
for i in range(settings.NumBots):
  Bots.append(Bot(BotSettings.name[i], BotSettings.color[i], BotSettings.voice[i], BotSettings.voice_rate[i], Censor))

tRandomBot = -1

while True:
  if 'tReply' not in locals():
    tReply = Starter
  tRandomBot = Censor.randomBot(Bots, tRandomBot)
  tReply = Bots[tRandomBot].ask(tReply)
  tReply = Reader.Interupt(tReply, Censor)
