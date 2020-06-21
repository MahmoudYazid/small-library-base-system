import tkinter as tk
import pymysql as mysql
from PIL import Image as img
from PIL import ImageTk as imgtk
import easygui as gui

#design
main=tk.Tk()
#function
def add():
    choose=listb.get(listb.curselection())
    money=price.get()
    unit=units.get()
    frag=fragments.get()
    _host="localhost"
    _password=""
    _user="root"
    _db="sgda"
    conn=mysql.Connection(host=_host,db=_db,password=_password, user=_user)
    exe=conn.cursor()
    exe.execute("""SELECT * FROM main where `name`="%s" """%(choose))
    results=exe.fetchall()
    
    for row in results:
        if frag==0 or frag=="0":
            if row[2]==0  and row[3]==0 and unit==0 and frag==0  :
                unit_1=int(row[2]) + int(unit)
                exe.execute(""" UPDATE `main` SET `price`="%s" , `numper_i_buy`="%s",`numper_of_fragment_in_unit`="%s"  WHERE `name`="%s" """%(money,unit_1,unit_1,choose))
                gui.msgbox("تم التغيير بنجاح")
                break
            if row[2]==0  and row[3]==0 and unit!=0 :
                unit_1=int(row[2]) + int(unit)
                exe.execute(""" UPDATE `main` SET `price`="%s" , `numper_i_buy`="%s",`numper_of_fragment_in_unit`="%s"  WHERE `name`="%s" """%(money,unit_1,unit_1,choose))
                gui.msgbox("تم التغيير بنجاح")
                break
            if row[2]==0  and row[3]==0 and unit==0 :
                unit_2=int(row[2]) + int(frag)
                exe.execute(""" UPDATE `main` SET `price`="%s" , `numper_i_buy`="%s",`numper_of_fragment_in_unit`="%s"  WHERE `name`="%s" """%(money,unit_2,unit_2,choose))
                gui.msgbox("تم التغيير بنجاح")
                break
            if row[2]!= 0  and row[3]==0 :
                unit_1=int(row[2]) + int(unit)
                exe.execute(""" UPDATE `main` SET `price`="%s" , `numper_i_buy`="%s"  WHERE `name`="%s" """%(money,unit_1,choose))
                exe.execute(""" UPDATE `main` SET `numper_of_fragment_in_unit`="%s"  WHERE `name`="%s" """%(row[2],choose))
                gui.msgbox("تم التغيير بنجاح")
                break
            if row[2]== 0 and row[3]!=0 :
                unit_1=int(row[3]) + int(unit)
                unit_2=int(row[3]) + int(unit)
                exe.execute(""" UPDATE `main` SET `price`="%s" , `numper_i_buy`="%s",`numper_of_fragment_in_unit`="%s"  WHERE `name`="%s" """%(money,unit_1,unit_2,choose))
                gui.msgbox("تم التغيير بنجاح")  
                break
            if row[2]!=0 and row[3]!=0 :
                unit_1=int(row[2]) + int(unit)
                unit_2=int(row[2]) + int(unit)
                exe.execute(""" UPDATE `main` SET `price`="%s" , `numper_i_buy`="%s",`numper_of_fragment_in_unit`="%s"  WHERE `name`="%s" """%(money,unit_1,unit_2,choose))
                gui.msgbox("تم التغيير بنجاح")
                break

                    
        if frag!=0 or frag!="0":
            unit_1=int(row[2]) + int(unit)
            frag_1=int(row[3]) + int(frag)
            exe.execute(""" UPDATE `main` SET `price`="%s" , `numper_i_buy`="%s",`numper_of_fragment_in_unit`="%s"  WHERE `name`="%s" """%(money,unit_1,frag_1,choose))
            gui.msgbox("تم التغيير بنجاح")

        
    
#bg
bg=img.open("bg.png")
bg_show=imgtk.PhotoImage(bg)
tk.Label(image=bg_show).pack(expand=True)
#btm
bg2=img.open("add.png")
bg_show2=imgtk.PhotoImage(bg2)
tk.Button(image=bg_show2, border=0, command=add).place(x=100,y=500)
###
#name(list)

_host="localhost"
_password=""
_user="root"
_db="sgda"
conn=mysql.Connection(host=_host,db=_db,password=_password, user=_user)
exe=conn.cursor()
exe.execute("""SELECT name FROM main  """)
result=exe.fetchall()
listb=tk.Listbox(border=1,width=100, font=33)
listb.bind("<Return>",add)
listb.place(x=40,y=90)
for row in result:
    listb.insert("end",row[0])
    


#unit
tk.Label(text="كم قطعه اشتريت؟",border=0, font=33).place(x=500,y=360)
units=tk.Entry(font=30)
units.bind("<Return>",add)
units.place(x=500,y=400)
#framents
tk.Label(text="كم وحده فالقطعه؟",border=0, font=33).place(x=1000,y=360)
fragments=tk.Entry(font=30)
fragments.bind("<Return>",add)
fragments.place(x=1000,y=400)
#price
tk.Label(text="?سعر القطعه الواحده",border=0, font=33).place(x=100,y=360)
price=tk.Entry(font=30)
price.bind("<Return>",add)
price.place(x=100,y=400)
main.mainloop()


