import tkinter as tk
from tkinter import filedialog as dg
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import pyexcel as exel
import pymysql as mysql

main=tk.Tk()
def delete():
    #mysql
    _host="localhost"
    _passoword=""
    _user="root"
    _db="sgda"
    conn=mysql.Connection(host=_host,db=_db,password=_passoword,user=_user)
    exe=conn.cursor()
    exe.execute(""" DROP TABLE main """)
    exe.execute(""" DROP TABLE sell_today """)
    conn.commit()
    conn.commit()
    print("table has been droped")

def choose():
    #open xls
    link_file=dg.askopenfilename(type="xls")
    sheet=exel.load("{}".format(link_file))
    #mysql
    _host="localhost"
    _passoword=""
    _user="root"
    _db="sgda"
    conn=mysql.Connection(host=_host,db=_db,password=_passoword,user=_user)
    exe=conn.cursor()

    exe.execute("""CREATE TABLE main(%s VARCHAR(32) DEFAULT '' not null,%s INT DEFAULT '0' ,%s INT DEFAULT '0' ,%s INT DEFAULT '0' ,%s INT DEFAULT '0' ,%s INT DEFAULT '0',%s INT DEFAULT '0') """%("name","price","numper_i_buy","numper_of_fragment_in_unit","numper_unit_sold","numper_unit_fragment_sold","total"))
    conn.commit()
    print("the table created")
    for n in sheet.row_range() :
        exe.execute(""" INSERT INTO main(name) VALUES("%s")"""%(sheet[n,0]))
        conn.commit() 
    for n in sheet.row_range() :
        exe.execute(""" UPDATE `main` SET `price`="%s" WHERE `name`="%s"  """%(sheet[n,1],sheet[n,0]))
        conn.commit() 

    exe.execute("""CREATE TABLE sell_today(%s VARCHAR(32) DEFAULT '' not null,%s INT DEFAULT '0' ,%s INT DEFAULT '0' ,%s INT DEFAULT '0',%s VARCHAR(32) DEFAULT '' not null,%s VARCHAR(32) DEFAULT '' not null,%s INT DEFAULT '0') """%("name","unit","fregment","price","date","bill_link","bill_numper"))
    conn.commit()
    conn.close()
    


tk.Button(text="choose" , command=choose).pack()
tk.Button(text="delete db" , command=delete).pack()

main.mainloop()


