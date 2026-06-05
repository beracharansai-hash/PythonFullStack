import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
name=in

engine=pyttsx3.init()


def speak():
    engine.say("Sampath rama krishna good afternoon")
    engine.runAndWait()
    
speak()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
    try:
        print("Recognizing...")
        command=recognizer.recognizer_google(audio)
        print("You Said:",command)
        return command.lower()
    except Exception:
        print("Sorry, Please say that again.")
        return""
def wish_user():
    hour=datetime.datetime.now().hour
    if hour<12:
        speak("Good Morning")
    elif hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
speak("Iam your Virtual assistance")
wish_user()
while True:
    command=take_command()
    if "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %P")
        speak(f"The time is {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.google.com")
    elif "who is" in command:
        person=command.replace("who is","")
        info=wikipedia.summary(person,2)
        print(info)
        speak()
    elif "exit" in command:
        speak("Goodbye")
        break
