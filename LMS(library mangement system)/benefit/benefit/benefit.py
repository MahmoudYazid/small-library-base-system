import tkinter as tk
from PIL import Image as img
from PIL import ImageTk as imgtk
import pymysql as mysql
import pyexcel as exel

       
main=tk.Tk()


   

       
       
    
#img
bg=img.open("bg.jpg")
bg_show=imgtk.PhotoImage(bg)
tk.Label(image=bg_show).pack(expand=True)
tk.Label(text="هذه هي مبيعاتك اليوم",font=33).place(x=500,y=530)
#objects
#listbox
conn=mysql.Connection(host="localhost",user="root",password="",db="sgda")
exe=conn.cursor()
exe.execute("""SELECT * FROM sell_today """)
results=exe.fetchall()
list=tk.Listbox(font=33, width=110, height=20)
list.place(x=100,y=50)
for row in results:
    list.insert("end",("الاسم\{}".format(row[0])))
    list.insert("end",("كم قطعه\{}".format(row[1])))
    list.insert("end",("كم وحده\{}".format(row[2])))
    list.insert("end",("السعر\{}".format(row[3])))
    list.insert("end",("وقت الصرف\{}".format(row[4])))
    list.insert("end",("رقم الفاتوره\{}".format(row[6])))
    list.insert("end",("---------------------------"))
tk.Label(text="المبلغ الكلي للبيع",font=50).place(x=180,y=600)
exe.execute("""SELECT `price` FROM sell_today """)
result=exe.fetchall()
sum=0
for p in result:
    sum = sum + int(p[0])
    tk.Label(text="{}".format(sum), font=50).place(x=180,y=650)

   
conn.close()
main.mainloop()

                                              