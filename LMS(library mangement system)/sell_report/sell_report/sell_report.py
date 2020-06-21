import tkinter as tk
import subprocess
import sys
from PIL import Image as img
from PIL import ImageTk as imgtk
main=tk.Tk()
#img
def find():
    file=open("lms_sell_report.txt", "r")
    read=file.read()
    subprocess.call([sys.executable,("{}\\find\\find\\find.py".format(read))])
    file.close()
def shortfall():
    file=open("lms_sell_report.txt", "r")
    read=file.read()
    subprocess.call([sys.executable,("{}\\Shortfalls\\Shortfalls\\Shortfalls.py".format(read))])
    file.close()
def soldtoday():
    file=open("lms_sell_report.txt", "r")
    read=file.read()
    subprocess.call([sys.executable,("{}\\benefit\\benefit\\benefit.py".format(read))])
    file.close()



#bg
bg= img.open("bg.png")
bg_show=imgtk.PhotoImage(bg)

# btm2
btm_2= img.open("find.png")
btm_2_show=imgtk.PhotoImage(btm_2)
# btm3
btm_3= img.open("shartfall.png")
btm_3_show=imgtk.PhotoImage(btm_3)
# btm4
btm_4= img.open("soldtoday.png")
btm_4_show=imgtk.PhotoImage(btm_4)

##objects
tk.Label(image=bg_show, border=0).pack(expand=True)
tk.Button(image=btm_2_show, border=0, command=find).place(x=0,y=150)
tk.Button(image=btm_3_show, border=0, command=shortfall).place(x=0,y=280)
tk.Button(image=btm_4_show, border=0, command=soldtoday).place(x=0,y=480)



main.mainloop()
