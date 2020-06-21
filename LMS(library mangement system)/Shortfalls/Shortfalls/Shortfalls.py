import tkinter as tk
from PIL import Image as img
from PIL import ImageTk as imgtk
import pymysql as mysql
main=tk.Tk()
#img
bg=img.open("bg.jpg")
bg_show=imgtk.PhotoImage(bg)
tk.Label(image=bg_show).pack(expand=True)
tk.Label(text="هذه هي النواقص  والكميه الموجوده فالمخزن",font=33).place(x=500,y=530)
#objects
#listbox
conn=mysql.Connection(host="localhost",user="root",password="",db="sgda")
exe=conn.cursor()
exe.execute("""SELECT name,total FROM main WHERE `total`="0"  """)
results=exe.fetchall()
list=tk.Listbox(font=33, width=100, height=20)
list.place(x=100,y=50)
for row in results:
    list.insert("end",("الاسم والكميه/{}".format(row)))
    
conn.close()
main.mainloop()
