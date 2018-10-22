#Kyle Baldwin 4-5
#import time calendar datetime winsound
#def the time
#convert total seconds to min
#convert total min to hours
#time zones
#put the hour min seconds in order
#def alarm
#get input for hours min and seconds and pm or am
#def beep
#print the time
#def quit to close gui
#def show time to show time
#build a gui to show time

import time
import calendar
import datetime
import winsound
from tkinter import*
from tkinter import ttk
from tkinter import font
h=0
m=0
s=0
t="am"

def current_time(h,m,s,t):
       
        total_seconds=calendar.timegm(time.gmtime())
        current_seconds=total_seconds%60
        minutes=total_seconds//60
        current_minutes=minutes%60
        hours=total_seconds//3600
        current_hour=hours%24

        #set time zone
        current_hour=current_hour -6

        if current_hour>=12:
            tag="PM"
        else:
            tag="AM"
        a = str(h)+":"+str(m)+":"+str(s)+t
        timex = str(current_hour)+":"+ str(current_minutes)+":"+str(current_seconds)+tag
        if timex == a:
                beep()
        return timex


def beep():
    winsound.Beep(5600,8000)

def quit(*args):
    root.destroy()

def show_time():
    global h
    global m
    global s
    global t
    time=current_time(h,m,s,t)
    txt.set(time)
    root.after(1000, show_time)

def alarm(*args):
        global h
        h=(input("How many hours"))
        global m
        m=(input("How many minutes"))
        global s
        s=(input("How many seconds"))
        global t
        t=(input('am or pm').upper())

                
                



root=Tk()
root.attributes("-fullscreen",False)
root.configure(background="Black")
root.bind("x",quit)
root.bind("a",alarm)
root.after(1000,show_time)
fnt=font.Font(family='Helvetica', size=60, weight="bold")
txt=StringVar()
lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="White", background='Green')
lbl.place(relx=0.5,rely=0.5, anchor=CENTER)
root.mainloop()

    


