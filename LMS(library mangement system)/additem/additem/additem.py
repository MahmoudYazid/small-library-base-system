import tkinter as tk
import pymysql as mysql
from PIL import Image as img
from PIL import ImageTk as imgtk
import easygui as gui

#design
main=tk.Tk()
#function
def add():
    names = name.get()
    unit = units.get()
    fragment=fragments_in_unit.get()
    money=price.get()

    _host="localhost"
    _password=""
    _user="root"
    _db="sgda"
    conn=mysql.Connection(host=_host,db=_db,password=_password, user=_user)
    exe=conn.cursor()
    exe.execute(""" INSERT INTO main(name,numper_i_buy,numper_of_fragment_in_unit,price) VALUES("%s","%s","%s","%s")"""%(names,unit,fragment,money))
    gui.msgbox("قد تم ايداع هذه السلعه الجديده ضمن قائمه عروضك")
    conn.close()
#bg
bg=img.open("bg.png")
bg_show=imgtk.PhotoImage(bg)
tk.Label(image=bg_show).pack(expand=True)
#btm
bg2=img.open("add.png")
bg_show2=imgtk.PhotoImage(bg2)
tk.Button(image=bg_show2, border=0, command=add).place(x=100,y=500)
###
#name
tk.Label(text="?اسم المنتج الجديد", border=0, font=33).place(x=100,y=120)
name=tk.Entry(font=30)
name.bind("<Return>",add)
name.place(x=100,y=160)

#unit
tk.Label(text="كم قطعه تمتلك؟",border=0, font=33).place(x=100,y=200)
units=tk.Entry(font=30)
units.bind("<Return>",add)
units.place(x=100,y=240)
#how many fragment in unit
tk.Label(text="?القطعه بها كم وحده",border=0, font=33).place(x=100,y=280)
fragments_in_unit=tk.Entry(font=30)
fragments_in_unit.bind("<Return>",add)
fragments_in_unit.place(x=100,y=320)
#price
tk.Label(text="?سعر القطعه الواحده",border=0, font=33).place(x=100,y=360)
price=tk.Entry(font=30)
price.bind("<Return>",add)
price.place(x=100,y=400)
main.mainloop()

