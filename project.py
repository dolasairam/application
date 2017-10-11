from Tkinter import *
from sqlite3 import *
import tkMessageBox
import sqlite3
top = Tk()
def order_pizza():
    order_pizza = Tk()
    Name = Label(order_pizza, text="Name").grid(row=0)
    entryname = Entry(order_pizza, bd=5)
    doorno = Label(order_pizza, text="door no").grid(row=1)
    door_no_en=Entry(order_pizza,bd=5)
    streetl = Label(order_pizza, text="street").grid(row=2)
    street_en=Entry(order_pizza,bd=5)
    area = Label(order_pizza, text="area name").grid(row=3)
    area_en=Entry(order_pizza,bd=5)
    pizzatype = Label(order_pizza,text= "pizzatype")
    ph = Label(order_pizza, text="Phone No")
    PhE =Entry(order_pizza, bd=5)
    L1 = Label(order_pizza, text= "No of small pizzas")
    L1E = Entry(order_pizza, bd=5)
    L2 = Label(order_pizza, text= "No of medium pizzas")
    L2E = Entry(order_pizza, bd=5)
    L3 = Label(order_pizza, text= "No of large pizzas")
    L3E = Entry(order_pizza, bd=5)
    mb=  Menubutton(order_pizza, text="Select pizza", relief=RAISED,\
                    activebackground="Red", bg="Blue")
    mb.menu  =  Menu ( mb, tearoff = 0 )
    mb["menu"]  =  mb.menu
    neoVar  = IntVar()
    dou = IntVar()
    Mar = IntVar()
    moz = IntVar()
    tom = IntVar()
    Mus = IntVar()
    art = IntVar()
    Ham = IntVar()
    mb.menu.add_checkbutton ( label="Neapolitan Pizza",\
                          variable=neoVar )
    mb.menu.add_checkbutton ( label="Double Cheese Pizza",\
                          variable=dou )
    mb.menu.add_checkbutton ( label="Margherita Pizza",\
                          variable=Mar )
    mb.menu.add_checkbutton ( label="Mozzarella Pizza",\
                          variable=moz )
    mb.menu.add_checkbutton ( label="Tomato Pizza",\
                          variable=Mar )
    mb.menu.add_checkbutton ( label="Mushrooms Pizza",\
                          variable=Mar )
    mb.menu.add_checkbutton ( label="Artichokes Pizza",\
                          variable=art )
    mb.menu.add_checkbutton ( label="Cooked Ham Pizza",\
                          variable=Ham )
    name=entryname.get()
    door_no=door_no_en.get()
    street=street_en.get()
    area=area_en.get()
    Phone_no=PhE.get()
    no_of_small=L1E.get()
    no_of_medium=L2E.get()
    no_of_large=L3E.get()
    total=(no_of_small*75)+(no_of_medium*100)+(no_of_large*150)
    def dbms(Name, door_no, street, area, Phone_no, no_of_small, no_of_medium, no_of_large, total):
       plist=[Name, door_no, street, area, Phone_no, no_of_small, no_of_medium, no_of_large, total]
       sqlite_file = 'my_first_db.sqlite'
       conn = sqlite3.connect(sqlite_file)
       c = conn.cursor()
       #c.execute('create sequence sname increment by 1 start with 1 maxvalue 1000 nocycle nocache')
       #c.execute('create table pizza_data(name text(10), dr_no int(10), street text(10),area text(10),Ph_no int(10), small int(10), medium int(10), large int(10), total int(10))')
       #c.execute('select * from pizza_data')
       c.execute('insert into pizza_data values(?,?,?,?,?,?,?,?,?)',plist)
       #print c.fetchall()
       #c.execute('drop table pizza_data')
       conn.commit()
       conn.close()
    submit=Button( order_pizza, text="SUBMIT", relief=RAISED, activebackground="Red",\
                   bg="Blue", command=dbms(name, door_no, street, area, Phone_no, no_of_small,no_of_medium,no_of_large,total))
    quit1 = Button(order_pizza, text='QUIT', relief=RAISED, activebackground="Orange",\
                   bg="Green",command=quit)
    entryname.grid(row=0,column=2)
    door_no_en.grid(row=1, column=2)
    street_en.grid(row=2, column=2)
    area_en.grid(row=3, column=2)
    pizzatype.grid(row=4)
    L1.grid(row=5)
    L1E.grid(row=5, column=2)
    L2.grid(row=6)
    L2E.grid(row=6, column=2)
    L3.grid(row=7)
    L3E.grid(row=7, column=2)
    mb.grid(row=8, column=2)
    submit.grid(row=9, column=2)
    quit1.grid(row=10, column=2)
    order_pizza.mainloop()
def can():
   L1=[p]
   sqlite_file = 'my_first_db.sqlite'
   conn = sqlite3.connect(sqlite_file)
   c = conn.cursor()
   #c.execute('alter table pizza_data delete column(ph=?)',L1)
   conn.commit()
   conn.close()
   tkMessageBox.showinfo("quit","Thank you")
def cancel():
   cancel=Tk()
   name=Label(cancel, text="name").grid(row=0)
   name_en=Entry(cancel, bd=5).grid(row=0, column=1)
   ph=Label(cancel, text="Phone number").grid(row=1)
   ph_en=Entry(cancel, bd=5).grid(row=1, column=1)
   #p=ph_en.get()
   submit=Button(cancel, text="cancel",relief=RAISED, activebackground="Orange",\
                  bg="Green", command=can).grid(row=2, column=2)
   cancel.mainloop()
def track():
   sqlite_file = 'my_first_db.sqlite'
   conn = sqlite3.connect(sqlite_file)
   c = conn.cursor()
   #l=[p]
   c.execute('select * from pizza_data where Ph_no=?',l)
   print "soon you will get it"
   conn.commit()
   conn.close()
def track_order():
   track_order=Tk()
   ph_l=Label(track_order, text="Phone Number")
   ph_en=Entry(track_order, bd=5)
   #p1=ph_en.get()
   ph_l.grid(row=0)
   ph_en.grid(row=0, column=1)
   submit=Button(track_order, text='submit', relief=RAISED, activebackground="Orange",\
                   bg="Green", command= track)
   submit.grid(row=1)
   track_order.mainloop()
def vender():
   vender=Tk()
   new_pizza_order = Button(vender, text="new pizza order", relief=RAISED, activebackground="Red",\
                            bg="Green", command=order_pizza)
   cancel_pizza_order=Button(vender, text="cancel_order", relief=RAISED, activebackground="Red",\
                             bg="Green", command=cancel)
   servered_order=Button(vender, text="server order", relief=RAISED, activebackground="Red",\
                       bg="Green")
   pending_order=Button(vender, text="Pending Order", relief=RAISED, activebackground="Red",\
                        bg="Green")
   new_pizza_order.grid(row=0)
   cancel_pizza_order.grid(row=0,column=3)
   servered_order.grid(row=2)
   pending_order.grid(row=2, column=3)
   vender.mainloop()
f1=Frame(top,height=1200,width=1400,bg="lightgreen");
op = Button(top, text ="order pizza", command=order_pizza, activebackground="Red")
co = Button(top,text ="cancel order", activebackground="Red", command=cancel)
to = Button(top,text ="Track order", activebackground="Red", command=track_order)
ve = Button(top,text="Vender", activebackground="Red", command= vender)
op.grid(row=0, sticky=W, pady=4)
co.grid(row=2, sticky=W, pady=4)
to.grid(row=4, sticky=W, pady=4)
ve.grid(row=6, sticky=W, pady=4)
top.mainloop()
