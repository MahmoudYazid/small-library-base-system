import tkinter as tk
import subprocess
import sys
import os
from tkinter.messagebox import *
from PIL import Image, ImageTk
import easygui as msg
engine = tk.Tk()


def connect():
    msg.msgbox("connected")



def buy_btm():
    file = open("lms.txt", "r")
    file_read = file.read()
    subprocess.call([sys.executable, ("{}\\buy\\buy\\buy.py".format(file_read))])
    file.close()


def sell_btm():
    file = open("lms.txt", "r")
    file_read = file.read()
    subprocess.call([sys.executable, ("{}\\sell\\sell\\sell.py".format(file_read))])
    file.close()


def additem_btm():
    file = open("lms.txt", "r")
    file_read = file.read()
    subprocess.call([sys.executable, ("{}\\additem\\additem\\additem.py".format(file_read))])
    file.close()


def sellreports_btm():
    file = open("lms.txt", "r")
    file_read = file.read()
    subprocess.call([sys.executable, ("{}\\sell_report\\sell_report\\sell_report.py".format(file_read))])
    file.close()


def option_btm():
    file = open("lms.txt", "r")
    file_read = file.read()
    subprocess.call([sys.executable, ("{}\\option\\option\\option.py".format(file_read))])
    file.close()


##import imgs
# bg
file = open("lms.txt", "r")
file_read = file.read()
img1 = Image.open(("{}\\LMS\\LMS\\bg.png".format(file_read)))
imgshow1 = ImageTk.PhotoImage(img1)
tk.Label(image=imgshow1).pack(expand=True, )
file.close()
# buy
img2 = Image.open("buy.png")
imgshow2 = ImageTk.PhotoImage(img2)
tk.Button(image=imgshow2, height=60, border=0, command=buy_btm).place(x=0, y=100)
# sell
img3 = Image.open("sell.png")
imgshow3 = ImageTk.PhotoImage(img3)
tk.Button(image=imgshow3, height=60, border=0, command=sell_btm).place(x=0, y=164)
# addd new item
img4 = Image.open("new_item.png")
imgshow4 = ImageTk.PhotoImage(img4)
tk.Button(image=imgshow4, height=60, border=0, command=additem_btm).place(x=0, y=228)
# sell reports
img5 = Image.open("sellreports.png")
imgshow5 = ImageTk.PhotoImage(img5)
tk.Button(image=imgshow5, height=200, border=0, command=sellreports_btm).place(x=0, y=292)
# option page
img6 = Image.open("option_page.png")
imgshow6 = ImageTk.PhotoImage(img6)
tk.Button(image=imgshow6, height=200, border=0, command=option_btm).place(x=0, y=480)
# patch
img8 = Image.open("patch.png")
imgshow8 = ImageTk.PhotoImage(img8)
tk.Button(image=imgshow8, border=0, bg="white", command=connect).place(x=1250, y=250)
engine.mainloop()
