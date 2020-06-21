import tkinter as tk
import pymysql as mysql
from PIL import Image as img
from PIL import ImageTk as imgtk
import easygui as gui
import datetime as dt


#design
main=tk.Tk()
#function
def add():
    dtime=dt.datetime.today()
    choose=listb.get("anchor")
    unit=units.get()
    fr = fragment.get()
    bill_c=change_bill.get()
    
    _host="localhost"
    _password=""
    _user="root"
    _db="sgda"
    conn=mysql.Connection(host=_host,db=_db,password=_password, user=_user)
    exe=conn.cursor()
    #insert sold
    exe.execute("""SELECT * FROM main WHERE `name`="%s" """%(choose))
    fe=exe.fetchall()
    for row in fe:
        if row[3]==row[2]:
            if unit!="0" and fr=="0":
                unit_1 = int(unit) + int(row[4])
                exe.execute(""" UPDATE `main` SET `numper_unit_sold`="%s" , `numper_unit_fragment_sold`="%s" WHERE `name`="%s" """%(unit_1,unit_1,choose))
            if unit =="0" and fr!="0":
                fr_1 = int(fr) + int(row[4])
                exe.execute(""" UPDATE `main` SET `numper_unit_sold`="%s" , `numper_unit_fragment_sold`="%s" WHERE `name`="%s" """%(fr_1,fr_1,choose))
        if row[3]!=row[2]:
            unit_1 = int(unit) + int(row[4])
            fr_1=int(fr)+int(row[5])
            exe.execute(""" UPDATE `main` SET `numper_unit_sold`="%s" , `numper_unit_fragment_sold`="%s" WHERE `name`="%s" """%(unit_1,fr_1,choose))
    #calculate total
    exe.execute(""" SELECT * FROM main WHERE `name`="%s" """%(choose))
    result=exe.fetchall()
    
    for row in result:
        if row[3]==row[2]:
            if unit==0 or unit=="0" and fr!=0 or fr!="0":
                total_of_units = int(row[2]) - int(row[4])
                total_of_fr = int(row[3]) - int(row[5])
                total_of_resedual = int(total_of_fr)  
                exe.execute(""" `total`="%s" WHERE `name`="%s" """%(total_of_resedual,choose))
            if unit!=0 or unit!="0" and fr==0 or fr=="0":
                    total_of_units = int(row[2]) - int(row[4])
                    total_of_fr = int(row[3]) - int(row[5])
                    total_of_resedual = int(total_of_units)  
                    exe.execute(""" UPDATE `main` SET `total`="%s" WHERE `name`="%s" """%(total_of_resedual,choose))

        if row[3]!=row[2]:
            total_of_units = int(row[2]) - int(row[4])
            total_of_fr = int(row[3]) - int(row[5])
            total_of_resedual = int(total_of_units) + int(total_of_fr)
            exe.execute(""" UPDATE `main` SET  `total`="%s" WHERE `name`="%s" """%(total_of_resedual,choose))
    

        #price-bills and today_insert
        if row[3]!=row[2]:
            if unit==0 or unit=="0" and fr!=0 or fr!="0":
                selled_one_fregment=int(row[1])/int(row[3])
                total_of_fragment= int(selled_one_fregment) * int(row[5])
                selled_units= int(unit) * int(row[1])
                total_price= selled_units+total_of_fragment
                exe.execute("""INSERT INTO sell_today(name,unit,fregment,price,bill_numper,date) VALUES("%s","%s","%s","%s","%s","%s")"""%(choose,unit,fr,total_price,bill_c,dtime))
                gui.msgbox("تم التغيير بنجاح")
                break
            if unit!=0 or unit!="0" and fr==0 or fr=="0":
                fr = 0
                selled_units= int(unit) * int[row[1]]
                total_price= selled_units
                exe.execute("""INSERT INTO sell_today(name,unit,fregment,price,bill_numper,date) VALUES("%s","%s","%s","%s","%s","%s")"""%(choose,unit,fr,total_price,bill_c,dtime))
                gui.msgbox("تم التغيير بنجاح")
                break

            if unit!=0 or unit!="0" and fr!=0 or fr!="0":
                selled_one_fregment=int(row[1])/int(row[3])
                total_of_fragment= int(selled_one_fregment) * int(row[5])
                selled_units= int(unit) * int(row[1])
                total_price= selled_units+total_of_fragment
                exe.execute("""INSERT INTO sell_today(name,unit,fregment,price,bill_numper,date) VALUES("%s","%s","%s","%s","%s","%s","%s")"""%(choose,unit,fr,total_price,bill_c,dtime))
                gui.msgbox("تم التغيير بنجاح")
                break

        if row[3]==row[2]:
            #price of _one frag
            if unit!=0 or unit!="0" and fr==0 or fr=="0":
                total_of_units = int(unit) * int(row[1])
                total_price = total_of_units
                exe.execute("""INSERT INTO sell_today(name,unit,fregment,price,bill_numper,date) VALUES("%s","%s","%s","%s","%s","%s")"""%(choose,unit,unit,total_price,bill_c,dtime))
                gui.msgbox("تم التغيير بنجاح")
                break
            if unit==0 or unit=="0" and fr!=0 or fr!="0":
                total_of_units = int(unit) * int(row[1])
                total_price = total_of_units
                exe.execute("""INSERT INTO sell_today(name,unit,fregment,price,bill_numper,date) VALUES("%s","%s","%s","%s","%s","%s")"""%(choose,fr,fr,total_price,bill_c,dtime))
                gui.msgbox("تم التغيير بنجاح")
                break
    
    ## zero all total (needs)
    _host="localhost"
    _password=""
    _user="root"
    _db="sgda"
    conn2=mysql.Connection(host=_host,db=_db,password=_password, user=_user)
    exe2=conn2.cursor()
    exe2.execute("""UPDATE main SET `numper_i_buy`="0",`numper_of_fragment_in_unit`="0",`numper_unit_sold`="0",`numper_unit_fragment_sold`="0" WHERE `total`="0" """)
    conn2.close()
    ##last order
    ## now_bill
    _host="localhost"
    _password=""
    _user="root"
    _db="sgda"
    conn2=mysql.Connection(host=_host,db=_db,password=_password, user=_user)
    exe2=conn2.cursor()
    exe2.execute("""SELECT `bill_numper` FROM sell_today """)
    result=exe2.fetchall()
    for n in result:
        tk.Label(text="{}".format(max(n)), font=33).place(x=950,y=420)
        
        

    conn2.close()
    
    


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

exe.close()
#unit
tk.Label(text="كم قطعه ؟",border=0, font=33).place(x=500,y=360)
units=tk.Entry(font=30)
units.bind("<Return>",add)
units.place(x=500,y=400)
#fragment
tk.Label(text="?كم وحده",border=0, font=33).place(x=100,y=360)
fragment=tk.Entry(font=30)
fragment.bind("<Return>",add)
fragment.place(x=100,y=400)
# bill
## now_bill
_host="localhost"
_password=""
_user="root"
_db="sgda"
conn2=mysql.Connection(host=_host,db=_db,password=_password, user=_user)
exe2=conn2.cursor()
exe2.execute("""SELECT `bill_numper` FROM sell_today """)
result=exe2.fetchall()
tk.Label(text=":رقم الفاتوره الحالي").place(x=950,y=380)
tk.Label(text="تغيير رقم الفاتوره").place(x=950,y=460)
change_bill=tk.Entry(font=22)
change_bill.bind("<Return>",add)
change_bill.place(x=950,y=500)
    
for n in result:
    
    numper_bill_show=tk.Label(text="{}".format(max(n)), font=33)
    numper_bill_show.bind("<Return>",add)
    numper_bill_show.place(x=950,y=420)
    
    
conn2.close()
#choose bill
tk.Entry().place()
tk.Label().place()
## zero all total (needs)
_host="localhost"
_password=""
_user="root"
_db="sgda"
conn2=mysql.Connection(host=_host,db=_db,password=_password, user=_user)
exe2=conn2.cursor()
exe2.execute("""UPDATE main SET `numper_i_buy`="0",`numper_of_fragment_in_unit`="0",`numper_unit_sold`="0",`numper_unit_fragment_sold`="0" WHERE `total`="0" """)
conn2.close()
main.mainloop()



