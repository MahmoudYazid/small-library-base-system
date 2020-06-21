import tkinter as tk
from PIL import Image as img
from PIL import ImageTk as imgtk
import pymysql as mysql
main=tk.Tk()
def find():
    choose=list.get(list.curselection())
    #mysql
    conn=mysql.Connection(host="localhost",db="sgda",password="",user="root")
    exe=conn.cursor()
    exe.execute("""SELECT * FROM main WHERE `name`="%s" """%(choose))
    results=exe.fetchall()
    tk.Frame(bg="black", height=500, width=500).place(y=50,x=1000)
    for n in results:
        tk.Label(text=("اسم البضاعه:-"+"  "+n[0]), border=0, font=33).place(y=50,x=1200)
        tk.Label(text=("سعر القطعه الواحده :-" + "  " + str(n[1])), border=0, font=33).place(y=100,x=1200)
        tk.Label(text=("كم وحده فالقطعه الواحده :-" + "  " + str(n[2])), border=0, font=33).place(y=150,x=1200)
        tk.Label(text=("باقي معك في المخزن :-" + "  " + str(n[6])), border=0, font=33).place(y=200,x=1200)
        
       
       


    conn.close()

#img
bg=img.open("bg.png")
bg_show=imgtk.PhotoImage(bg)
#img_btm
btm=img.open("btm_find.png")
btm_show=imgtk.PhotoImage(btm)
# objects
tk.Label(image=bg_show).pack(expand=True)
tk.Button(image=btm_show, border=0, command=find).place(x=200,y=550)
#listbox
conn=mysql.Connection(host="localhost",db="sgda",password="",user="root")
exe=conn.cursor()
exe.execute("""SELECT name FROM main """)
items=exe.fetchall()
list=tk.Listbox(width=50, font=33)
list.bind("<Return>",find)
list.place(x=50,y=50)
for n in items:
    list.insert("end",n)

conn.close()
main.mainloop()