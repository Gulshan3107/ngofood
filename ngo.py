from tkinter import *
from PIL import ImageTk,Image
import  mysql.connector as db
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.title("NGO-Profile")
win.geometry("1920x1080")
win.config(bg="#fff")

def getAllEvent():
    print("All event")
    f1 = Frame(win, width=900, height=700, bg="#fff", borderwidth=10,
               highlightbackground="black", highlightthickness=5)
    f1.place(x=100, y=50)

    def edit():
        def back():
            f2.destroy()
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

        f2=Frame(f1,width=700,height=650,bg="#fff",highlightthickness=3,highlightbackground="red")
        f2.place(x=100,y=0)

        lbl_title = Label(f2, text="Event Details",bg="#fff", font=("Sans serif", 15,'bold'), )
        lbl_title.place(x=260, y=20)

        lbl_type=Label(f2,text="Type of Event:",bg="#fff",font=("Sans serif",10,'bold'),)
        lbl_type.place(x=200,y=80)
        type=StringVar()
        txt_type=Label(f2,bg="#fff",textvariable=type,font=("Sans serif",10,))
        txt_type.place(x=350,y=80)
        type.set(temp[1])

        lbl_name = Label(f2, text="Name of Event", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_name.place(x=200, y=120)
        name = StringVar()
        txt_name = Label(f2, textvariable=name,bg="#fff",font=("Sans serif", 10,) )
        txt_name.place(x=350, y=120,)
        name.set(temp[2])

        # #
        lbl_date = Label(f2, text="Date", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_date.place(x=200, y=160)
        date = StringVar()
        txt_date = Label(f2, textvariable=date, bg="#fff", font=("Sans serif", 10), )
        txt_date.place(x=350, y=160, )
        date.set(temp[3])
        #
        lbl_time = Label(f2, text="Time ", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_time.place(x=200, y=200)
        time = StringVar()
        txt_time = Label(f2,  textvariable=time,bg="#fff", font=("Sans serif", 10,'bold'), )
        txt_time.place(x=350, y=200, )
        time.set(temp[4])
        #
        lbl_location = Label(f2, text="Venue", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_location.place(x=200, y=240)
        location = StringVar()
        txt_location = Label(f2, textvariable=location , font=("Sans serif", 10,'bold'))
        txt_location.place(x=350, y=240, )
        location.set(temp[5])

        lbl_people = Label(f2, text="Estimated people", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_people.place(x=200, y=280)
        people = StringVar()
        txt_people = Label(f2,textvariable=people,bg="#fff", font=("Sans serif",10) )
        txt_people.place(x=350, y=280,)
        people.set(temp[6])
        #
        # lbl_cntdetails = Label(f2, text="Contact Details", bg="#fff", font=("Sans serif", 15, 'bold'), )
        # lbl_cntdetails.place(x=260, y=350)

        # #
        lbl_person = Label(f2, text="Contact person \n & Number", bg="#fff", font=("Sans serif", 10,'bold'), )
        lbl_person.place(x=200, y=320)
        contact = StringVar()
        txt_person = Label(f2,  textvariable=contact,bg="#fff", font=("Sans serif", 10,'bold'))
        txt_person.place(x=350, y=320)
        contact.set(temp[7])

        btn_submit = Button(f2, text="Back", bg="#24a0ed",fg="#fff", bd=2,
                            font=("Sans serif", 15,'italic'), width=15, command=back )
        btn_submit.place(x=260, y=380)
        con.close()
        print("succesfully edited.........")
      #-------------End of Edit frame------



    #--------------- show data in Table code------------
    con = db.connect(user="root", password="root", host="localhost", database="food_manage")
    x = con.cursor()
    query = "select * from event"
    x.execute(query)

    style=ttk.Style()
    style.configure("mystyle.Treeview",highlightthickness=1,bd=0,backgroundcolor="red",font=('Helvetica',10))
    style.configure("mystyle.Treeview.Heading",font=('Helvetica',11,'bold'))
    col = ('srno','etype', 'ename', 'date', 'time', 'venue', 'people', 'cnt_person')
    treeview = ttk.Treeview(f1, style="mystyle.Treeview", show='headings', columns=col)

    # adding columns....
    treeview.column('srno',width=100
                    ,anchor=CENTER)
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
    i = 0
    for ro in x:
        treeview.insert('',i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
        i = i + 1

    treeview.place(x=50,y=100)

    btn_open = Button(f1, text="Open", width=10, bg="#24a0ed",fg="#fff",
                      font=("Sans serif", 15),command=edit)
    btn_open.place(x=300,y=400)


  #-starting of back-button-code and back-function code-
    def back():
        f1.destroy()

    back_img = Image.open("xmark.jpg")
    resize_image2 = back_img.resize((20, 20))
    filename2 = ImageTk.PhotoImage(resize_image2)
    back_btn = Button(f1, image=filename2, bd=0, bg="#fff", command=back)
    back_btn.image = filename2
    back_btn.place(x=840, y=5)
    print("hello beta ji")

#--End-of show all event---------


#----Starting of Assign Function-------
def assign():
    def back():
        f1.destroy()


    f1 = Frame(win, width=1000, height=700, bg="#fff", borderwidth=10,
               highlightbackground="black", highlightthickness=5)
    f1.place(x=100, y=50)
    con = db.connect(user="root", password="root", host="localhost", database="food_manage")
    x = con.cursor()
    x.execute("select * from event where status ='Assign'" )


    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=0, backgroundcolor="red", font=('Helvetica', 10))
    style.configure("mystyle.Treeview.Heading", font=('Helvetica', 11, 'bold'))
    col = ('srno', 'etype', 'ename', 'date', 'time', 'venue', 'people', 'cnt_person','status')
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
    treeview.column('status', width=100, anchor=CENTER)

    # addings heading
    treeview.heading('srno', text="Sr No")
    treeview.heading('etype', text='Type of Event')
    treeview.heading('ename', text='Name of Event')
    treeview.heading('date', text='Date')
    treeview.heading('time', text='Time')
    treeview.heading('venue', text='Venue')
    treeview.heading('people', text='Estimate Number Of People')
    treeview.heading('cnt_person', text='Contact')
    treeview.heading('status', text='Status')
    i = 0
    for ro in x:
        treeview.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7],ro[8]))
        i = i + 1

    treeview.place(x=50, y=100)

    back_img = Image.open("xmark.jpg")
    resize_image2 = back_img.resize((20, 20))
    filename2 = ImageTk.PhotoImage(resize_image2)
    back_btn = Button(f1, image=filename2, bd=0, bg="#fff", command=back)
    back_btn.image = filename2
    back_btn.place(x=940, y=5)

def logout():
    win.destroy()
    import main


#------------------starting of navbar----
lbl_navbar=Label(win,bg="#20c997",width=70,height=2)
lbl_navbar.place(x=0,y=0)
btn_advs = Button(win, text="Show Event", font=" Montserrat 12  bold italic",bd=0,
                  bg="#20c997",fg="#000",command=getAllEvent)
btn_advs.place(x=1, y=5)
                #
btn_update = Button(win, text="Show Assigned Event",
                    font=" Montserrat 12 bold italic",bd=0, bg="#20c997",
                    fg="#000",command=assign  )
btn_update.place(x=130, y=5)
                #
btn_delete = Button(win, text="Report", font=" Montserrat 12 bold italic",bd=0, bg="#20c997",fg="#000" )
btn_delete.place(x=320, y=5)

# btn_exit = Button(frame_ngo, text="Assign Event ",font=" Montserrat 12 bold italic",bd=0, bg="#20c997",fg="#000" )
# btn_exit.place(x=250, y=5)


btn_lgout = Button(win, text="Log-out",
                   font=" Montserrat 12 bold italic",bd=0, bg="#20c997",fg="#000",command=logout)
btn_lgout.place(x=420, y=5)
# -------------------End of navbar-------
lbl_title2=Menubutton(win,text="FOOD DONATION",fg="black",bg="pink",font="Montserrat 28 bold")
lbl_title2.place(x=480,y=100)
lbl_title2 = Label(win, text="HELP US TO ERADICATE HUNGER JOIN FOOD FOR LIFE CAMPAIGN", fg="black", bg="#fff",
                   font="Montserrat 18 bold italic underline")
lbl_title2.place(x=220, y=200,)
#---------------donate-btn code---------
donate_img=Image.open("donate_btn.png")
resize_image1=donate_img.resize((250,150))
filename1=ImageTk.PhotoImage(resize_image1)
donate_btn=Button(image=filename1,bd=0,bg="#fff")
donate_btn.image=filename1
donate_btn.place(x=1020,y=30)


#------------------background image code-----
image=Image.open("image25.jpg")
resize_image=image.resize((1250,400))

filename=ImageTk.PhotoImage(resize_image)
background_image = Label(image=filename)
background_image.image=filename
background_image.place(x=10,y=240)

win.mainloop()