import pyttsx3
import PyPDF3
import speech_recognition as sr
import pyaudio


# speaker=pyttsx3.init()
# pdf=open('Speak to Win1.pdf','rb')
# # inp = input("Enter your words : ")
# pdf1=PyPDF3.PdfFileReader(pdf)
# pages=pdf1.numPages
# print(pages)
#
# for i in range(7,209):
#     pdf2 = pdf1.getPage(i)
#     words = pdf2.extractText()
#     speaker.say(words)
#     speaker.runAndWait()

r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    print("say something...")
    audio=r.listen(source)

try:
    print(r.recognize_google(audio))
except Exception as e:
    print(str(e))



