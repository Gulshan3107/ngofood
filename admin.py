from tkinter import *
import mysql.connector as db
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import webbrowser


win=Tk()
win.title("Admin Dashboard")
win.geometry("1920x1080")
win.config(bg="#fff")

#--------logout--------

def logout():
    win.destroy()
    import main

#------whatsapp------

def whatsapp():
    win.destroy()
    import whatsapp


#------------------------
def view():  #creating frame for view ngo-frame

    frame_view=Frame(win,width=850,height=600,bg="#fff", borderwidth=10, highlightbackground="black",
                     highlightthickness=5,)
    frame_view.place(x=100,y=50)


    def edit():# edit function of btn
        print("this is Edit function")
        selected_item=t1.focus()
        temp=t1.item(selected_item,'values')
        print(temp)


#--------------------update function---------------
        def update():
            n1=name.get()
            e1=email.get()
            m1=mobile.get()
            p1=person_name.get()
            r1=regi_no.get()
            u1=username.get()
            pswd = password.get()
            print("Update function...",n1,e1,m1,p1,r1,u1,pswd)



            con = db.connect(user="root", password="root", host="localhost", database="food_manage")
            x = con.cursor(prepared=True)
            sql="update registration set name=%s,email=%s,mobile=%s,pername=%s,regi_no=%s,username=%s,password=%s Where id="+temp[0]
            tuple1=(n1,e1,m1,p1,r1,u1,pswd)
            x.execute(sql,tuple1)
            con.commit()
            con.close()
            f2.destroy()
            messagebox.showinfo("Success", " Updated Succesfully....!")
            print("Successfully Updated.........")
#--------------------------end of update function----------------
#--------------------------fuction of Navbar---------------------


        #-------------frame for edit-form-------------------------
        f2=Frame(frame_view,width=700,height=550,bg="#fff",highlightthickness=3,highlightbackground="purple")
        f2.place(x=0,y=10)

        # Name
        def on_enter(e):
            txt_name.delete(0, 'end')

        def on_leave(e):
            name = txt_name.get()
            if name == '':
                txt_name.insert(0, 'name')

        name = StringVar()
        txt_name = Entry(f2, width=25, fg='black', bg="#fff", border=0,
                         font=('Microsoft YaHei UI Light', 11), textvariable=name)
        txt_name.place(x=130, y=100)
        txt_name.insert(0, 'name')
        txt_name.bind('<FocusIn>', on_enter)
        txt_name.bind('<FocusOut>', on_leave)
        name.set(temp[1])
        frame_name = Frame(f2, width=295, height=2, bg='#20c997')  # 20c997
        frame_name.place(x=130, y=130)

        # Email
        def on_enter(e):
            user_email.delete(0, 'end')

        def on_leave(e):
            name = user_email.get()
            if name == '':
                user_email.insert(0, 'email')

        email = StringVar()
        user_email = Entry(f2, width=25, fg='black', bg="#fff", border=0,
                           font=('Microsoft YaHei UI Light', 11), textvariable=email)
        user_email.place(x=130, y=150)
        user_email.insert(0, 'email')
        user_email.bind('<FocusIn>', on_enter)
        user_email.bind('<FocusOut>', on_leave)
        email.set(temp[2])
        # code to create txt box back border-------------------------------------------------
        frame_email = Frame(f2, width=295, height=2, bg='#20c997')  # 20c997
        frame_email.place(x=130, y=180)

        # Mobile

        def on_enter(e):
            user_mobile.delete(0, 'end')

        def on_leave(e):
            name = user_mobile.get()
            if name == '':
                user_mobile.insert(0, 'Mobile Number')

        mobile = StringVar()
        user_mobile = Entry(f2, width=25, fg='black', bg="#fff", border=0,
                            font=('Microsoft YaHei UI Light', 11), textvariable=mobile)
        user_mobile.place(x=130, y=200)
        user_mobile.insert(0, 'Mobile Number')
        user_mobile.bind('<FocusIn>', on_enter)
        user_mobile.bind('<FocusOut>', on_leave)
        mobile.set(temp[3])

        # code to create txt box back border-------------------------------------------------
        frame_mobile = Frame(f2, width=295, height=2, bg='#20c997')  # 20c997
        frame_mobile.place(x=130, y=230)

        # Contact Person name

        def on_enter(e):
            user_person.delete(0, 'end')

        def on_leave(e):
            name = user_person.get()
            if name == '':
                user_person.insert(0, 'Contact person Name')

        person_name = StringVar()
        user_person = Entry(f2, width=25, fg='black', bg="#fff", border=0,
                            font=('Microsoft YaHei UI Light', 11), textvariable=person_name)
        user_person.place(x=130, y=250)
        user_person.insert(0, 'Contact person Name')
        user_person.bind('<FocusIn>', on_enter)
        user_person.bind('<FocusOut>', on_leave)
        person_name.set(temp[4])
        # code to create txt box back border-------------------------------------------------
        frame_person = Frame(f2, width=295, height=2, bg='#20c997')  # 20c997
        frame_person.place(x=130, y=280)

        # Registration number

        def on_enter(e):
            user_regino.delete(0, 'end')

        def on_leave(e):
            name = user_regino.get()
            if name == '':
                user_regino.insert(0, 'Registration number')

        regi_no = StringVar()
        user_regino = Entry(f2, width=25, fg='black', bg="#fff", border=0,
                            font=('Microsoft YaHei UI Light', 11), textvariable=regi_no)
        user_regino.place(x=130, y=300)
        user_regino.insert(0, 'Registration number')
        user_regino.bind('<FocusIn>', on_enter)
        user_regino.bind('<FocusOut>', on_leave)
        regi_no.set(temp[5])
        # code to create txt box back border-------------------------------------------------
        frame_regino = Frame(f2, width=295, height=2, bg='#20c997')  # 20c997
        frame_regino.place(x=130, y=330)

        # username

        def on_enter(e):
            user_name.delete(0, 'end')

        def on_leave(e):
            name = user_name.get()
            if name == '':
                user_name.insert(0, 'Username')

        username = StringVar()
        user_name = Entry(f2, width=25, fg='black', bg="#fff", border=0,
                          font=('Microsoft YaHei UI Light', 11), textvariable=username)
        user_name.place(x=130, y=350)
        user_name.insert(0, 'Username')
        user_name.bind('<FocusIn>', on_enter)
        user_name.bind('<FocusOut>', on_leave)
        username.set(temp[6])
        # code to create txt box back border-------------------------------------------------
        frame_n = Frame(f2, width=295, height=2, bg='#20c997')  # 20c997
        frame_n.place(x=130, y=380)

        # password

        def on_enter(e):
            user_password.delete(0, 'end')

        def on_leave(e):
            name = user_password.get()
            if name == '':
                user_password.insert(0, 'Password')

        password = StringVar()
        user_password = Entry(f2, width=25, fg='black', bg="#fff", border=0,
                              font=('Microsoft YaHei UI Light', 11), textvariable=password)
        user_password.place(x=130, y=400)
        user_password.insert(0, 'Password')
        user_password.bind('<FocusIn>', on_enter)
        user_password.bind('<FocusOut>', on_leave)
        password.set(temp[7])
        # code to create txt box back border-------------------------------------------------
        frame_password = Frame(f2, width=295, height=2, bg='#20c997')  # 20c997
        frame_password.place(x=130, y=430)

        btn_submit = Button(f2, text="Update", bg="green",fg="#fff", bd=2,
                            font=("Sans serif", 15,'italic'), width=15,command=update )
        btn_submit.place(x=100, y=500)
        btn_submit = Button(f2, text="Back", bg="#24a0ed", fg="#fff", bd=2,
                            font=("Sans serif", 15, 'italic'), width=15,
                            command=back)
        btn_submit.place(x=360, y=500)
#--------------end of edit form frame---------------------------


#-------------------------back function------------
    def back():
        frame_view.destroy()

    back_img = Image.open("xmark.jpg")
    resize_image2 = back_img.resize((20, 20))
    filename2 = ImageTk.PhotoImage(resize_image2)
    back_btn = Button(frame_view, image=filename2, bd=0, bg="#fff", command=back)
    back_btn.image = filename2
    back_btn.place(x=800, y=5)


# -------------- starting of Delete functions code--------------------------------------
    def delete():
        print("Delete function.............")
        selected_item = t1.focus()
        temp = t1.item(selected_item, 'values')
        id= temp[0]
        print(id)
        con = db.connect(user="root", password="root", host="localhost", database="food_manage")
        x = con.cursor()
        x.execute("delete from registration where id = "+temp[0])
        con.commit()
        con.close()
        t1.delete(selected_item)
        print("succesfully deleted................")
        # ---------------End of delete function code----------------------

#--------------------------show data in Table NGO----------
    con = db.connect(user="root", password="root", host="localhost", database="food_manage")
    x = con.cursor()
    query = ("select * from registration where user_type like 'ngo' ")
    x.execute(query)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=3, backgroundcolor="red", font=('Helvetica', 10))
    style.configure("mystyle.Treeview.Heading", font=('Helvetica', 11, 'bold'))
    col = ('id','name','email', 'mobile', 'pername', 'regi_no', 'username', 'password',)

    t1=ttk.Treeview(frame_view,height=15,show="headings",columns=col)
    # Adding column in treeview
    t1.column("id",width=50,anchor=CENTER)
    t1.column("name",width=100,anchor=CENTER)
    t1.column("email",width=100,anchor=CENTER)
    t1.column("mobile",width=100,anchor=CENTER)
    t1.column("pername",width=100,anchor=CENTER)
    t1.column("regi_no",width=100,anchor=CENTER)
    t1.column("username",width=100,anchor=CENTER)
    t1.column("password",width=100,anchor=CENTER)

    #Adding heading to the column..
    t1.heading("id",text="ID")
    t1.heading("name",text="Name")
    t1.heading("email",text="Email")
    t1.heading("mobile",text="Mobile")
    t1.heading("pername",text="Person name")
    t1.heading("regi_no",text="Registration Number")
    t1.heading("username",text="Username")
    t1.heading("password",text="Password")

    i = 0
    for ro in x:
        t1.insert('', i, text="", values=(ro[0],ro[2], ro[3], ro[4], ro[5], ro[6], ro[7],ro[8]))
        i = i + 1

    t1.place(x=20, y=20)

    btn_open = Button(frame_view, text="Edit", width=10, bg="#24a0ed", fg="#fff", font=("Sans serif", 15),command=edit )
    btn_open.place(x=200, y=500)

    btn_open = Button(frame_view, text="Delete", width=10, bg="red", fg="#fff", font=("Sans serif", 15),command=delete)
    btn_open.place(x=350, y=500)
#-----end of view function----------------

#-----------show hotel------------


    con = db.connect(user="root", password="root", host="localhost", database="food_manage")
    x = con.cursor()
    query = ("select * from registration where user_type like 'ngo' ")
    x.execute(query)

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=1, bd=3, backgroundcolor="red", font=('Helvetica', 10))
    style.configure("mystyle.Treeview.Heading", font=('Helvetica', 11, 'bold'))
    col = ('id','name','email', 'mobile', 'pername', 'regi_no', 'username', 'password',)

    t1=ttk.Treeview(frame_view,height=15,show="headings",columns=col)
    # Adding column in treeview
    t1.column("id",width=50,anchor=CENTER)
    t1.column("name",width=100,anchor=CENTER)
    t1.column("email",width=100,anchor=CENTER)
    t1.column("mobile",width=100,anchor=CENTER)
    t1.column("pername",width=100,anchor=CENTER)
    t1.column("regi_no",width=100,anchor=CENTER)
    t1.column("username",width=100,anchor=CENTER)
    t1.column("password",width=100,anchor=CENTER)

    #Adding heading to the column..
    t1.heading("id",text="ID")
    t1.heading("name",text="Name")
    t1.heading("email",text="Email")
    t1.heading("mobile",text="Mobile")
    t1.heading("pername",text="Person name")
    t1.heading("regi_no",text="Registration Number")
    t1.heading("username",text="Username")
    t1.heading("password",text="Password")

    i = 0
    for ro in x:
        t1.insert('', i, text="", values=(ro[0],ro[2], ro[3], ro[4], ro[5], ro[6], ro[7],ro[8]))
        i = i + 1

    t1.place(x=20, y=20)

    btn_open = Button(frame_view, text="Edit", width=10, bg="#24a0ed", fg="#fff", font=("Sans serif", 15),command=edit )
    btn_open.place(x=200, y=500)

    btn_open = Button(frame_view, text="Delete", width=10, bg="red", fg="#fff", font=("Sans serif", 15),command=delete)
    btn_open.place(x=350, y=500)
#-----end of view function----------------
# ------------------starting of navbar-----------------------------------------------
lbl_navbar = Label(win, bg="blue", width=120,)
lbl_navbar.place(x=0, y=0,height=42)

btn_advs = Button(win, text="View Ngo",font=" Montserrat 12  bold italic",
                  bd=0, bg="white",fg="#000", command=view)
btn_advs.place(x=1, y=5)


btn_update = Button(win, text="View Hotel", font=" Montserrat 12 bold italic", bd=0, bg="white", fg="#000",)
btn_update.place(x=100, y=5)



btn_exit = Button(win, text="Whatsapp ", font=" Montserrat 12 bold italic", bd=0, bg="white",fg="#000",command=whatsapp)
btn_exit.place(x=200, y=5)


btn_lgout = Button(win, text="Log-out", font=" Montserrat 12 bold italic", bd=0, bg="white",fg="#000",command=logout )
btn_lgout.place(x=380, y=5)


txt_srch=Entry(win,width=30,font=" Montserrat 12 bold italic", bd=2,)
txt_srch.place(x=480,y=4,height=35)

btn_txt=Button(win,text="Search",font="Montserrat 12 bold",command="search")
btn_txt.place(x=770,y=5,height=30)
#---------------------------------Background Image Of Admin-------------------------------------------------------------

image=Image.open("admin.jpg")
resize_image=image.resize((1280,600))

filename=ImageTk.PhotoImage(resize_image)
background_image = Label(image=filename)
background_image.image=filename
background_image.place(x=0,y=40)


win.mainloop()