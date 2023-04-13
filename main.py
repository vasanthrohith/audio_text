from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.geometry("500x500")
win.title("Inversor")
frame1 = Frame(win)
frame1.pack(ipadx=50, ipady=50, expand=True, fill='both')

bg = ImageTk.PhotoImage(file='text_aud_bg.png')

canvas = Canvas(frame1)
canvas.pack(fill=BOTH, expand=True)

canvas.create_image(0, 0, image=bg, anchor='nw')


def resize_image(e):
    # global image, resized, image2
    # open image to resize it
    image = Image.open("text_aud_bg.png")
    # resize the image with width and height of window
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')


# #    Labels
#    canvas.create_text(750, 80, text="Domain-Username Separator", font=('Helvetica 32 bold'), fill='orange')
#    canvas.pack()
#
#    canvas.create_text(290,360,text='Mail id',font='Helvetica 20 bold',fill='orange')
#    canvas.pack()
#
#    canvas.create_text(965,280,text='Username',font='Helvetica 20 bold',fill='orange')
#    canvas.pack()
#
#    canvas.create_text(990, 400, text='Domain name', font='Helvetica 20 bold', fill='orange')
#    canvas.pack()


win.bind("<Configure>", resize_image)

win.mainloop()

# Text to speech---------
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
#
#
# # Speech to text-----
#
# r=sr.Recognizer()
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source)
#
#     print("say something...")
#     audio=r.listen(source)
#
# try:
#     print(r.recognize_google(audio))
# except Exception as e:
#     print(str(e))
