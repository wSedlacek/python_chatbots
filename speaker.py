import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 70)

voices = engine.getProperty('voices')
for voice in voices:
    print voice.id  
    engine.setProperty('voice', voice.id)
    engine.say("Hi there, how's you ?")
