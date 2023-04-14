# import time
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import speech_recognition as sr

win = Tk()
win.geometry("500x500")
win.title("Inversor")
frame1 = Frame(win)
frame1.pack(ipadx=50, ipady=50, expand=True, fill='both')

bg = ImageTk.PhotoImage(file='bg6.png')

canvas = Canvas(frame1, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')


def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("bg6.png")
    # resize the image with width and height of window
    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')

    canvas.create_text(760, 340, text="Name", font=('Helvetica 28 bold'), fill='red')
    canvas.pack()
    # canvas.create_text(600, 460, text="text ▶ Voice", font=('Helvetica 28 bold'), fill='red')
    # canvas.pack()

win.bind("<Configure>", resize_image)


def tts_fn():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(f'Hai {name_e.get()}, how are you doing?')
    engine.runAndWait()

    def speak_fn():
        # global photo
        text = txt_en.get(1.0, "end-1c")
        print(text)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    frame1.destroy()
    # frame4 = Frame(win, bg='red')
    # frame4.pack(expand=True)

    frame2 = Frame(win, bg='black')
    frame2.pack(ipadx=50, ipady=50, expand=True, fill='both')

    # title image
    # label = Label(image=photo, bg='black')
    # label.img = photo  # keep a reference!
    # label.place(x=450,y=10)
    # Label---Frame2---
    txt_l = Label(frame2, text="Enter your text", font='Helvetica 20 bold', fg='red', bg='black')
    txt_l.place(x=670, y=320)

    photo = Image.open('bg_crop_2.png')
    img2 = ImageTk.PhotoImage(photo)
    # def ing():
    #     global photo, img_l
    #     photo = Image.open('bg_crop_2.png')
    #     height = img_l.winfo_height()
    #     width = img_l.winfo_width()
    #     img = photo.resize((width, height), Image.ANTIALIAS)
    #     img1 = ImageTk.PhotoImage(img)
    #     img_l.configure(image=img1)
    #     img_l.image = img1

    img_l = Label(frame2, image=img2, bg='black', width=498, height=165)
    img_l.image = img2
    # btn = Button(frame2, text='check', command=ing)
    # btn.place(x=300, y=670)
    img_l.pack(ipady=5,pady=10)
    # img_l.place(x=520, y=15)
    # img_l.bind('<Configure>', ing)

    # -------Images

    # Entry
    sb_ver_f2 = Scrollbar(frame2,orient=VERTICAL)
    txt_en = Text(frame2, width=40, height=4,font='12',yscrollcommand=sb_ver_f2.set)
    txt_en.place(x=540, y=400)
    sb_ver_f2.place(x=980, y=400, height=96)
    sb_ver_f2.config(command=txt_en.yview())


    speak_btn = Button(frame2, text="Speak", font='Helvetica 16 bold', borderwidth=5, command=speak_fn)
    speak_btn.place(x=730, y=520)

    rf_btn = Button(frame2, text='🔁', font=24)
    rf_btn.place(x=953, y=359)

    # back_btn=Button(frame2,text='⬅',font=24,bg='black',fg='red',borderwidth=5,command=back_fn)
    # back_btn.place(x=2,y=2)

    # ing()
def stt_fn():
    def refresh_fn():
        text_area.delete('1.0', END)

    def listen_fn():
        # ------listening
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say("i am listening")
        engine.runAndWait()
        # -------------
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("say something...")
            audio = r.listen(source)

        try:
            output = r.recognize_google(audio)
            print(output)
            text_area.insert(END, output)

        except Exception as e:
            print(str(e))
            if '[Errno 11001]' in str(e):
                print('please connect to the network')
                engine.say('please connect to the network')
                engine.runAndWait()

    frame1.destroy()
    frame3 = Frame(win, bg='black')
    frame3.pack(ipadx=50, ipady=50, expand=True, fill='both')


    f3_l1 = Label(frame3, text="I'm listening...", font='Helvetica 20 bold', fg='red', bg='black')
    f3_l1.place(x=680, y=290)
    sb_ver = Scrollbar(frame3,orient=VERTICAL)
    text_area = Text(frame3, width=30, height=4,font='12',yscrollcommand=sb_ver.set)
    text_area.place(x=610, y=400)
    sb_ver.place(x=940,y=400,height=96)
    sb_ver.config(command=text_area.yview)

    listen_btn = Button(frame3, text='Start', font='Helvetica 16 bold', borderwidth=5, command=listen_fn)
    listen_btn.place(x=740, y=500)

    refresh_btn = Button(frame3, text='Refresh', font='Helvetica 16 bold', borderwidth=5, command=refresh_fn)
    refresh_btn.place(x=723, y=550)

    photo_f3 = Image.open('bg_crop_2.png')
    img2_f3 = ImageTk.PhotoImage(photo_f3)
    img_l_f3 = Label(frame3, image=img2_f3, bg='black', width=498, height=165)
    img_l_f3.image = img2_f3
    img_l_f3.pack(ipady=5, pady=10)


# Frame1------Labels
name_en = StringVar()
name_e = Entry(frame1, width=30, textvariable=name_en)
name_e.place(x=670, y=370)

# Buttons----
tts_btn = Button(frame1, text='Text ► Voice', font='Helvetica 16 bold', borderwidth=5, command=tts_fn)
tts_btn.place(x=685, y=450)

stt_btn = Button(frame1, text='Voice ► Text', font='Helvetica 16 bold', borderwidth=5, command=stt_fn)
stt_btn.place(x=685, y=520)

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
