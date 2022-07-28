import speech_recognition as spr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes


listener = spr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    print(text)
    alexa.say(text)
    alexa.runAndWait()


def takeCommand():
    try:
        with spr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print('Me : ' + command)
            modCommand = command.lower()
            if 'asma' in modCommand:
                command = modCommand.replace('asma', '')
    except:
        pass

    return command


def runAlexa():
    command = takeCommand()
    modCommand = command.lower()
    if 'time' in modCommand:
        time = datetime.datetime.now().strftime('%I: %M: %S %p')
        print(f'Current time is : {time}')
        talk('Current time is ' + time)

    elif 'play' in modCommand:
        song = modCommand.replace('play', '')
        talk('Playing '+song)
        pywhatkit.playonyt(song)

    elif 'about' in modCommand:
        info = wikipedia.summary(modCommand, 1)
        talk(info)

    elif 'joke' in modCommand:
        talk(pyjokes.get_joke())

    elif 'change your name' in modCommand:
        talk('Thank you, I love this name')

    elif 'your name' in modCommand:
        talk('You said, I am Asmaa Begum')

    elif 'boyfriend' in modCommand:
        talk('I have doubt about it')


runAlexa()
