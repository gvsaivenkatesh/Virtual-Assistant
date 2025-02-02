import pyttsx3
import speech_recognition as sr
import webbrowser
def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening.....")
    r.pause_threshold = 1
    audio = r.listen(source)
    try:
      print("Recognizing.....")
      query = r.recognize_google(audio,language='en-in')
      print("Recognized Data: ",query)
    except Exception as e:
      print(e)
      print("Say that again.....")
      return "None"
    query = query.lower()
    return query 
def speak(audio):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice',voices[0].id)
  engine.say(audio)
  engine.runAndWait()
def hello():
  speak("Hello, I am your Virtual assistant. How are you doing.")
def take_user_input():
  hello()
  while True:
    query = takecommand() 
    if "how are you" in query:
      speak("I am doing Good. How about you ?")
    elif "what is your name" in query:
      speak("I am Virtual Assistant")
    elif "open page" in query:
      speak("Opening your web page")
      webbrowser.open("www.codegnan.com")
    elif "Tata" in query:
      speak("Bye Bye, Take Care !")
      exit()
    else:
      speak("I can not get you, speek again !")
take_user_input()
    
