import tkinter as tk
import subprocess
from PIL import Image as img
from PIL import ImageTk as imgtk
import sys
import os
import easygui as gui
def createlink():
    mainlink=entry_link.get()
    ###lms-others###
    #lms
    lms_main=open(("{}\\LMS\\LMS\\lms.txt".format(mainlink)),"w")
    lms_main.write(mainlink)
    lms_main.close()
    #lms-additem
    lms_additem=open(("{}\\additem\\additem\\lms_additem.txt".format(mainlink)),"w")
    lms_additem.write(mainlink)
    lms_additem.close()
    #lms-buy
    lms_buy=open(("{}\\buy\\buy\\lms_buy.txt".format(mainlink)),"w")
    lms_buy.write(mainlink)
    lms_buy.close()
    #lms_sell
    lms_sell=open(("{}\\sell\\sell\\lms_sell.txt".format(mainlink)),"w")
    lms_sell.write(mainlink)
    lms_sell.close()
    #lms_sell_report\sell_report
    lms_sell_report=open(("{}\\sell_report\\sell_report\\lms_sell_report.txt".format(mainlink)),"w")
    lms_sell_report.write(mainlink)
    lms_sell_report.close()
    ##make this file in main####
    #lms
    lms_main=open(("{}\\LMS\\LMS\\lms.txt".format(mainlink)),"w")
    lms_main.write(mainlink)
    lms_main.close()
    #lms-additem
    lms_additem=open(("{}\\LMS\\LMS\\lms_additem.txt".format(mainlink)),"w")
    lms_additem.write(mainlink)
    lms_additem.close()
    #lms-buy
    lms_buy=open(("{}\\LMS\\LMS\\lms_buy.txt".format(mainlink)),"w")
    lms_buy.write(mainlink)
    lms_buy.close()
    #lms_sell
    lms_sell=open(("{}\\LMS\\LMS\\lms_sell.txt".format(mainlink)),"w")
    lms_sell.write(mainlink)
    lms_sell.close()
    ##sell reports
    #lms_sell_report
    lms_sell_report=open(("{}\\LMS\\LMS\\lms_sell_report.txt".format(mainlink)),"w")
    lms_sell_report.write(mainlink)
    lms_sell_report.close()
    #lms_sell_report-find
    lms_sell_report_find=open(("{}\\find\\find\\lms_sell_report.txt".format(mainlink)),"w")
    lms_sell_report_find.write(mainlink)
    lms_sell_report_find.close()
     #lms_sell_report-Shortfalls
    lms_sell_report_Shortfalls=open(("{}\\Shortfalls\\Shortfalls\\lms_sell_report.txt".format(mainlink)),"w")
    lms_sell_report_Shortfalls.write(mainlink)
    lms_sell_report_Shortfalls.close()
     #lms_sell_report-benefit
    lms_sell_report_benefit=open(("{}\\benefit\\benefit\\lms_sell_report.txt".format(mainlink)),"w")
    lms_sell_report_benefit.write(mainlink)
    lms_sell_report_benefit.close()
    #final msg
    gui.msgbox("sucess.. you can work now")

engine=tk.Tk()
#bg
imgfind=img.open("pg.png")
imgopen=imgtk.PhotoImage(imgfind)
tk.Label( image=imgopen).pack(expand=True)
#btm-add-link
imgfind2=img.open("add.png")
imgopen2=imgtk.PhotoImage(imgfind2)
tk.Button( image=imgopen2, border=0 , command=createlink).place(x=675,y=350)
#textbox
entry_link=tk.Entry(font=33,width=40)
entry_link.bind("<Return>",createlink)
entry_link.place(x=500,y=300)
#lable
tk.Label(text="اكتب مكان الملف باضافه (\\)").place(x=625,y=275)
engine.mainloop()
    
