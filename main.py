import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
import pyttsx3

engine = pyttsx3.init()

def getInputBoxValue():
    global userInput
    userInput = tInput.get()
    return userInput

def btnClickFunction():
    getInputBoxValue()
    engine.say(userInput)
    engine.runAndWait()

def upr():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    F = open(filename,"r") 
    engine.say(F.read())
    engine.runAndWait()

def stop():
    engine.stop()
    mb.showwarning(title="Text Reader", message="Text Reader stopped")

def male():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    mb.showinfo(title="Text Reader", message="Text Reader set on Male")

def female():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    mb.showinfo(title="Text Reader", message="Text Reader set on Female")

root = Tk()

root.geometry('600x300')
root.configure(background='#F0F8FF')
root.title('Python Voice Talk')

Label(root, text='Python synthetic voice reader', bg='#F0F8FF', font=('arial', 24, 'normal')).place(x=111, y=9)

tInput=Entry(root)
tInput.place(x=244, y=87)

Button(root, text='Read', bg='#FF4040', font=('arial', 14, 'normal'), command=btnClickFunction).place(x=272, y=115)

Button(root, text='Male Reader', bg='#F0F8FF', font=('arial', 12, 'normal'), command=male).place(x=400, y=78)

Button(root, text='Female Reader', bg='#F0F8FF', font=('arial', 12, 'normal'), command=female).place(x=400, y=129)

Label(root, text='OR', bg='#F0F8FF', font=('helvetica', 14, 'normal')).place(x=294, y=167)

Button(root, text='Upload and read', bg='#0000FF', font=('helvetica', 14, 'normal'), command=upr).place(x=230, y=212)


root.mainloop()
