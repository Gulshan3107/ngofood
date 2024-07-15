from tkinter import *
import mysql.connector as db
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk


win=Tk()
win.title("Hotel Login")
win.geometry("1500x1050")
win.config(bg="#fff")


#-----------------functions--------------------

#-------------------starting of add-event code-------
def add_event():
    print("this add event ")
    f1=Frame(win,width=900,height=600,bg="#fff",borderwidth=10,highlightbackground="black",highlightthickness=5)
    f1.place(x=100,y=0)
    def back():
        f1.destroy()


    def insert():
        print("Insert code running")
        print(location.get())

        con=db.connect(user="root",password="root",host="localhost",database="food_manage")
        x=con.cursor()
        sql="insert into event(typ_event,event_name,date,time,location,people,contact)values('"+type.get()+"','"+name.get()+"','"+date.get()+"','"+time.get()+"','"+location.get()+"','"+people.get()+"','"+contact.get()+"')"
        x.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("Success"," Registered Succesfully....!")
        print("Successfully Inserted.........")
        f1.destroy()

#---------back-button code---------------------
    back_img = Image.open("xmark.jpg")
    resize_image2 = back_img.resize((20, 20))
    filename2 = ImageTk.PhotoImage(resize_image2)
    back_btn = Button(f1,image=filename2,bd=0,bg="#fff",command=back)
    back_btn.image = filename2
    back_btn.place(x=840, y=5)
#---------- starting of event-registration form code-------------------
    lbl_title=Label(f1,text="Event Registration Form",bg="white",font="Montserrat 24 bold ",)
    lbl_title.place(x=200,y=0)

    lbl_event=Label(f1,text="Type of Event",bg="#fff",font=("Sans serif",15),)
    lbl_event.place(x=50,y=100)
    type=StringVar()
    txt_event=Entry(f1, textvariable=type,font=("Sans serif",12),width=40,bd=0,relief=GROOVE,
                    highlightbackground="green",highlightthickness=3)
    txt_event.place(x=50,y=150,height=30)

    lbl_name = Label(f1, text="Name of Event", bg="#fff",font=("Sans serif",15), )
    lbl_name.place(x=500, y=100)
    name = StringVar()
    txt_name = Entry(f1, textvariable=name,font=("Sans serif",12), width=40, bd=2,relief=GROOVE)
    txt_name.place(x=500, y=150, height=30)

    #
    lbl_date=Label(f1,text="Date    year-months-days",bg="#fff",font=("Sans serif",15),)
    lbl_date.place(x=50,y=200)
    date=StringVar()
    txt_date=Entry(f1,textvariable=date, font=("Sans serif",12),width=40,bd=2,relief=GROOVE)
    txt_date.place(x=50,y=250,height=30)

    lbl_time = Label(f1, text="Time  Hours:Mintues AM/PM ", bg="#fff",font=("Sans serif",15), )
    lbl_time.place(x=500, y=200)
    time=StringVar()
    txt_time = Entry(f1, font=("Sans serif",12),width=40, bd=2,textvariable=time,relief=GROOVE)
    txt_time.place(x=500, y=250,height=30)
    #
    lbl_location = Label(f1, text="Venue", bg="#fff",font=("Sans serif",15),)
    lbl_location.place(x=50, y=300)
    location=StringVar()
    txt_location = Entry(f1, font=("Sans serif",12),width=40, bd=2,relief=GROOVE,textvariable=location)
    txt_location.place(x=50, y=350,height=60)
    #
    lbl_people = Label(f1, text="Estimated number of \n people attending", bg="#fff",font=("Sans serif",15), )
    lbl_people.place(x=500, y=300)
    people=StringVar()
    txt_people = Entry(f1, font=("Sans serif",12),width=40, bd=2,textvariable=people,relief=GROOVE)
    txt_people.place(x=500, y=370,height=30)
    #
    lbl_person = Label(f1, text="Contact Person \n & Number", bg="#fff",font=("Sans serif",15), )
    lbl_person.place(x=50, y=450)
    contact=StringVar()
    txt_person = Entry(f1, font=("Sans serif",12),width=40,bd=2,textvariable=contact,relief=GROOVE)
    txt_person.place(x=50, y=500,height=30)

    btn_submit=Button(f1,text="Submit",bg="green",fg="#fff", bd=2,font=("Sans serif",15),width=30,command=insert,)
    btn_submit.place(x=500,y=500)
# --------------------------------------End of function Add event------------------------------------------------------------------------------------------------------------


#---------------------------------Starting of show All Event code---------------------------------------------------------------------------------------------------------
def getAllEvent():
    print("All event")
    f1 = Frame(win, width=900, height=700, bg="#fff", borderwidth=10,
               highlightbackground="black", highlightthickness=5)
    f1.place(x=100, y=50)
    lbl_evnt = Label(f1, text="Show All  Event", bg="#fff", font=("Sans serif", 18, 'bold'))
    lbl_evnt.place(x=400, y=20)
    def edit():
        #----------------- starting of update-function  code-------------------
        def update():
            t1=type.get()
            n1=name.get()
            d1=date.get()
            time1=time.get()
            l1=location.get()
            p1=people.get()
            c1=contact.get()
            print(t1,n1,d1,time1,l1,p1,c1)

            print("Update function is running..............")
            con = db.connect(user="root", password="root", host="localhost", database="food_manage")
            x = con.cursor(prepared=True)
            sql = "update event set typ_event=%s,event_name=%s,date=%s,time=%s,location=%s,people=%s," \
                  "contact=%s Where srno="+temp[0]
            tuple1=(t1,n1,d1,time1,l1,p1,c1)
            x.execute(sql,tuple1)
            con.commit()
            con.close()
            f2.destroy()
            messagebox.showinfo("Success", " Updated Succesfully....!")
            print("Successfully Updated.........")
       #-----------End of update function code----------------


    #-------------------Starting of Edit-frame-code------------------------------------------
        print("this is Edit function")
        selected_item=treeview.focus()
        temp=treeview.item(selected_item,'values')
        print(temp[0])
        con = db.connect(user="root", password="root", host="localhost", database="food_manage")
        x = con.cursor()
        x.execute("select * from event where srno = "+temp[0])
        result_list=x.fetchone()
        print(result_list)

        f2=Frame(f1,width=700,height=650,bg="#fff",highlightthickness=3,highlightbackground="purple")
        f2.place(x=100,y=10)

        lbl_title = Label(f2, text="Event Details", bg="#fff", font=("Sans serif", 15, 'bold'), )
        lbl_title.place(x=260, y=20)

        lbl_type=Label(f2,text="Type of Event",bg="#fff",font=("Sans serif",10,'bold'),)
        lbl_type.place(x=200,y=80,)
        type=StringVar()
        txt_type=Entry(f2,width=30,textvariable=type,bg="#fff",font=("Sans serif",10,))
        txt_type.place(x=350,y=80,height=30)
        type.set(temp[1])

        lbl_name = Label(f2, text="Name of Event", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_name.place(x=200, y=120)
        name = StringVar()
        txt_name = Entry(f2, textvariable=name, width=30, bd=2, bg="#fff", font=("Sans serif", 10,),relief=GROOVE)
        txt_name.place(x=350, y=120, height=30)
        name.set(temp[2])
        #
        # #
        lbl_date = Label(f2, text="Date", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_date.place(x=200, y=160)
        date = StringVar()
        txt_date = Entry(f2, textvariable=date, width=30, bd=2,bg="#fff", font=("Sans serif", 10,'bold'), relief=GROOVE)
        txt_date.place(x=350, y=160, height=30)
        date.set(temp[3])

        lbl_time = Label(f2, text="Time ", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_time.place(x=200, y=200)
        time = StringVar()
        txt_time = Entry(f2, width=30, bd=2, textvariable=time,bg="#fff", font=("Sans serif", 10,), relief=GROOVE)
        txt_time.place(x=350, y=200, height=30)
        time.set(temp[4])

        lbl_location = Label(f2, text="Venue", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_location.place(x=200, y=240)
        location = StringVar()
        txt_location = Entry(f2, width=30, bd=2,textvariable=location ,bg="#fff", font=("Sans serif", 10,),relief=GROOVE)
        txt_location.place(x=350, y=240, height=50)
        location.set(temp[5])
        # #
        lbl_people = Label(f2, text="Estimated people", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_people.place(x=200, y=300)
        people = StringVar()
        txt_people = Entry(f2, width=30, bd=2, textvariable=people,bg="#fff", font=("Sans serif", 10,), relief=GROOVE)
        txt_people.place(x=350, y=300, height=30)
        people.set(temp[6])
        # #
        lbl_person = Label(f2, text="Contact Person \n & Number", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_person.place(x=200, y=340)
        contact = StringVar()
        txt_person = Entry(f2, width=30, bd=2, textvariable=contact, bg="#fff", font=("Sans serif", 10),relief=GROOVE)
        txt_person.place(x=350, y=340, height=30)
        contact.set(temp[7])

        btn_submit = Button(f2, text="Update", bg="green",fg="#fff", bd=2, font=("Sans serif", 15,'italic'), width=15, command=update )
        btn_submit.place(x=100, y=400)
        btn_submit = Button(f2, text="Back", bg="#24a0ed", fg="#fff", bd=2, font=("Sans serif", 15, 'italic'), width=15,
                            command=back)
        btn_submit.place(x=360, y=400)
        con.close()
        print("succesfully edited.........")
    #   -------------End of Edit frame----------------------------------------------



     #-------------- starting of Delete functions code--------------------------------------
    def delete():
        print("Delete function.............")
        selected_item = treeview.focus()
        temp=treeview.item(selected_item,'values')
        sr_no=temp[0]
        print(sr_no)

        con = db.connect(user="root", password="root", host="localhost", database="food_manage")
        x = con.cursor()
        x.execute("delete from event where srno ="+temp[0])
        con.commit()
        con.close()
        treeview.delete(selected_item)
        print("succesfully deleted................")
   #---------------End of delete function code----------------------




    #--------------- show data in Table code------------
    con = db.connect(user="root", password="root", host="localhost", database="food_manage")
    x = con.cursor()
    query = "select * from event"
    x.execute(query)

    style=ttk.Style()
    style.configure("mystyle.Treeview",highlightthickness=1,bd=2,backgroundcolor="red",font=('Helvetica',10))
    style.configure("mystyle.Treeview.Heading",font=('Helvetica',11,'bold'))
    col = ('srno','etype', 'ename', 'date', 'time', 'venue', 'people', 'cnt_person')

    treeview = ttk.Treeview(f1, style="mystyle.Treeview", show='headings', columns=col)

    # adding columns....
    treeview.column('srno',width=100,anchor=CENTER)
    treeview.column('etype', width=100, anchor=CENTER)
    treeview.column('ename', width=100, anchor=CENTER)
    treeview.column('date', width=100, anchor=CENTER)
    treeview.column('time', width=100, anchor=CENTER)
    treeview.column('venue', width=100, anchor=CENTER)
    treeview.column('people', width=100, anchor=CENTER)
    treeview.column('cnt_person', width=100, anchor=CENTER)


    # addings heading
    treeview.heading('srno',text="Sr No")
    treeview.heading('etype', text='Type of Event')
    treeview.heading('ename', text='Name of Event')
    treeview.heading('date', text='Date')
    treeview.heading('time', text='Time')
    treeview.heading('venue', text='Venue')
    treeview.heading('people', text='Estimate Number Of People')
    treeview.heading('cnt_person', text='Contact')
    i=0
    for ro in x:
        treeview.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]))
        i= i + 1

    treeview.place(x=50,y=100)

    btn_open = Button(f1, text="Edit", width=10, bg="#24a0ed",fg="#fff", font=("Sans serif", 15),command=edit)
    btn_open.place(x=300,y=400)

    btn_open = Button(f1, text="Delete", width=10,bg="red" ,fg="#fff",font=("Sans serif", 15), command=delete)
    btn_open.place(x=500, y=400)
  #-----------starting of back-button-code and back-function code----------------
    def back():
        f1.destroy()

    back_img = Image.open("xmark.jpg")
    resize_image2 = back_img.resize((20, 20))
    filename2 = ImageTk.PhotoImage(resize_image2)
    back_btn = Button(f1, image=filename2, bd=0, bg="#fff", command=back)
    back_btn.image = filename2
    back_btn.place(x=840, y=5)
      #-----------End of back-button-code and back-function code----------------

#---------------------------------End of show all event -------------------------------------------------------------------------------------------------------





#--------------------------------Starting of Assign Event-------------------------------------------------------------------------------------------------------------
def ass_event():

    print("assign event running......")
    f1 = Frame(win, width=900, height=700, bg="#fff", borderwidth=10, highlightbackground="black", highlightthickness=5)
    f1.place(x=100, y=50)

    lbl_evnt=Label(f1,text="Assign Event",bg="#fff",font=("Sans serif", 18,'bold'))
    lbl_evnt.place(x=400,y=20)
    def assign():
        print("This assign function............")
        selected_item = treeview.focus()
        temp = treeview.item(selected_item, 'values')
        print(temp[0])
        con = db.connect(user="root", password="root", host="localhost", database="food_manage")
        x = con.cursor()
        x.execute("update event set status='Assign' where srno="+temp[0])
        con.commit()
        con.close()
        messagebox.showinfo("Success", " Assign Succesfully....!")
        print("successfully Updated assign")


    # txt_search = Entry(f1, width=30, borderwidth=2, relief="groove", font="cooper 10", justify="left", )
    # txt_search.place(x=50, y=80, height=30)
    # # Button for search
    # search_delete_btn = Button(f1, text="Search", width=10, font="cooper 10 bold", bg="#00c853", fg="white",
    #                            borderwidth=1, height=1,)
    # search_delete_btn.place(x=280, y=80)

    con = db.connect(user="root", password="root", host="localhost", database="food_manage")
    x = con.cursor()
    query = "select * from event"
    x.execute(query)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=2, backgroundcolor="red", font=('Helvetica', 10))
    style.configure("mystyle.Treeview.Heading", font=('Helvetica', 11, 'bold'))
    col = ('srno', 'etype', 'ename', 'date', 'time', 'venue', 'people', 'cnt_person')
    treeview = ttk.Treeview(f1, style="mystyle.Treeview", show='headings', columns=col)

    # adding columns....
    treeview.column('srno', width=100
                    , anchor=CENTER)
    treeview.column('etype', width=100, anchor=CENTER)
    treeview.column('ename', width=100, anchor=CENTER)
    treeview.column('date', width=100, anchor=CENTER)
    treeview.column('time', width=100, anchor=CENTER)
    treeview.column('venue', width=100, anchor=CENTER)
    treeview.column('people', width=100, anchor=CENTER)
    treeview.column('cnt_person', width=100, anchor=CENTER)

    # addings heading
    treeview.heading('srno', text="Sr No")
    treeview.heading('etype', text='Type of Event')
    treeview.heading('ename', text='Name of Event')
    treeview.heading('date', text='Date')
    treeview.heading('time', text='Time')
    treeview.heading('venue', text='Venue')
    treeview.heading('people', text='Estimate Number Of People')
    treeview.heading('cnt_person', text='Contact')
    i = 0
    for ro in x:
        treeview.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
        i = i + 1

    treeview.place(x=50, y=150)

    btn_open = Button(f1, text="Assign", width=10, bg="Green", fg="#fff", font=("Sans serif", 15),command=assign )
    btn_open.place(x=400, y=400)



    # -----------starting of back-button-code and back-function code----------------
    def back():
        f1.destroy()

    back_img = Image.open("xmark.jpg")
    resize_image2 = back_img.resize((20, 20))
    filename2 = ImageTk.PhotoImage(resize_image2)
    back_btn = Button(f1, image=filename2, bd=0, bg="#fff", command=back)
    back_btn.image = filename2
    back_btn.place(x=840, y=5)
#--------------End of Assign Event -------------------------------------------------------------------------------------------------------------------------


def logout():
    win.destroy()
    import main



# ------------------starting of navbar------
lbl_navbar = Label(win, bg="#20c997", width=120,)
lbl_navbar.place(x=0, y=0,height=42)

btn_advs = Button(win, text="Add Event",
                  font=" Montserrat 12  bold italic", bd=0,
                  bg="#20c997",fg="#000",command=add_event)
btn_advs.place(x=1, y=5)


btn_update = Button(win, text="Show All Event", font=" Montserrat 12 bold italic", bd=0, bg="#20c997",
                                 fg="#000",command=getAllEvent)
btn_update.place(x=100, y=5)



btn_exit = Button(win, text="Assign Event ", font=" Montserrat 12 bold italic", bd=0, bg="#20c997",
                               fg="#000",command=ass_event)
btn_exit.place(x=250, y=5)


btn_lgout = Button(win, text="Log-out", font=" Montserrat 12 bold italic", bd=0, bg="#20c997",
                               fg="#000",command=logout )
btn_lgout.place(x=380, y=5)


txt_srch=Entry(win,width=30,font=" Montserrat 12 bold italic", bd=2,)
txt_srch.place(x=480,y=4,height=35)

btn_txt=Button(win,text="Search",font="Montserrat 12 bold",command="search")
btn_txt.place(x=770,y=5,height=30)


# -------------------End of navbar------

#---------text-------------------------
lbl_title1 = Menubutton(win, text="FOOD FOR NEEDY", fg="black",bg="orange",font="Montserrat 28 bold italic")
lbl_title1.place(x=480, y=100)
lbl_title2 = Label(win, text="Is one of the most extensive vegetarian food donation programs  glovally,"
                             "serving millions of meals every Day",
                                fg="black", bg="#fff", font="Montserrat 18 bold italic underline")
lbl_title2.place(x=10, y=200, )
#----------end of text code---------------------

#-----------donate button-code--------
donate_img=Image.open("donate_btn.png")
resize_image1=donate_img.resize((250,150))
filename1=ImageTk.PhotoImage(resize_image1)
donate_btn=Button(image=filename1,bd=0,bg="#fff")
donate_btn.image=filename1
donate_btn.place(x=1050,y=30)
#-------------------------End of donate-button code---------------

#------------------background image code----------
image=Image.open("donate1.jpg")
resize_image=image.resize((1250,400))

filename=ImageTk.PhotoImage(resize_image)
background_image = Label(image=filename)
background_image.image=filename
background_image.place(x=10,y=240)

win.mainloop()