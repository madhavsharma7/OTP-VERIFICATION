from tkinter import *
from tkinter import messagebox
import smtplib
import random

value = random.randint(101, 990)
win = Tk()
win.title("OTP Generator")
win.resizable(False, False)
win.geometry("400x400")

l1 = Label(win, text="Enter your Email id") #receiveremailid
l1.place(x=50, y=100)

receive=StringVar()
l2 = Entry(win, textvariable=receive, font=5)
l2.place(x=170, y=100)

veri = StringVar()
l = Label(win, text="Enter your OTP")
l.place(x=50, y=150)
l3 = Entry(win, textvariable=veri, font=5)
l3.place(x=170, y=150)


def ooo():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    password = '' #inapppassword
    server.login('', password) #senderemailid
    try:
        global otp
        otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
        msg = 'Hello!! PYTHON SENt YOU AN OTP YOUR OTP IS ' + str(otp)
        sender = '' #senderemailid
        receiver = receive.get()
        server.sendmail(sender, receiver, msg)
        print(msg)
    except Exception as a:
        print(a)


def check():
    if otp==veri.get():
        print("ok")
    else:
        print("check otp")

bu = Button(win, text="Send OTP", font=10, command=ooo, relief="raised")
bu.place(x=175, y=250)


bu=Button(win,text="Verify",font=10,command=check)
bu.place(x=175,y=300)


win.mainloop()
