from tkinter import *
from tkinter import messagebox
import mysql.connector as db
from tkinter import ttk

win=Tk()
win.title("My Software")
win.geometry("1366x700")

#functions......

def login(): #login code
    user_name=username.get()
    user_password=password.get()
    if(type.get()=="ngo"):
        con = db.connect(user="root", password="root", host="localhost", database="food_manage")
        x = con.cursor()
        x.execute("select * from registration where username ='" + user_name + "' and password='" + user_password + "'")
        result_list = x.fetchone()
        con.commit()
        con.close()
        print(result_list, "Login successfully..........")
        win.destroy()
        import ngo

    if (type.get() == "hotel"):
        con = db.connect(user="root", password="root", host="localhost", database="food_manage")
        x = con.cursor()
        x.execute("select * from registration where username ='" + user_name + "' and password='" + user_password + "' like ")
        result_list = x.fetchone()
        con.commit()
        con.close()
        print(result_list, "Login successfully..........")

        if(type.get.equal("hotel")):
            win.destroy()
            import profile



# Registration function

def registration():
    frame_regi = Frame(win, width=665,bg="#20c997")
    frame_regi.place(x=700, y=0, height=700)

    def back():
        frame_regi.destroy()

    def insert():
        print("Insert code running")


        con = db.connect(user="root", password="root", host="localhost", database="food_manage")
        x = con.cursor()
        sql = "insert into registration(user_type,name,email,mobile,pername,regi_no,username,password)values('" + type.get() + "','" + name.get() + "','" + email.get() + "','" + mobile.get() + "','" + person_name.get() + "','" + regi_no.get() + "','" + username.get() + "','" +password.get()+ "')"
        x.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo("Success", " User Register Succesfully....!")
        print(" User Successfully Register.........")
        frame_regi.destroy()



    # registration form code
    lbl_title=Label(frame_regi,text="Registration....", font="Montserrat 22 bold",fg="#fff",bg="#20c997")
    lbl_title.place(x=200,y=50)

    lbl_type=Label(frame_regi,text="Type",font=('Microsoft YaHei UI Light', 11),fg="#000",bg="#20c997")
    lbl_type.place(x=130,y=150)

    type= StringVar()
    drp_type=ttk.Combobox(frame_regi,font=('Microsoft YaHei UI Light', 11),textvariable=type)
    drp_type["values"]=("Hotel","NGO")
    drp_type.place(x=200,y=150)

# Name
    def on_enter(e):
        txt_name.delete(0, 'end')

    def on_leave(e):
        name = txt_name.get()
        if name == '':
            txt_name.insert(0, 'name')

    name=StringVar()
    txt_name=Entry(frame_regi,width=25, fg='black', bg="#20c997", border=0,
                   font=('Microsoft YaHei UI Light', 11),textvariable=name)
    txt_name.place(x=130,y=200)
    txt_name.insert(0, 'name')
    txt_name.bind('<FocusIn>', on_enter)
    txt_name.bind('<FocusOut>', on_leave)

    frame_name = Frame(frame_regi, width=295, height=2, bg='#000')  # 20c997
    frame_name.place(x=130, y=230)
#Email
    def on_enter(e):
        user_email.delete(0, 'end')

    def on_leave(e):
        name = user_email.get()
        if name == '':
            user_email.insert(0, 'email')

    email=StringVar()
    user_email = Entry(frame_regi, width=25, fg='black', bg="#20c997", border=0,
                          font=('Microsoft YaHei UI Light', 11),textvariable=email)
    user_email.place(x=130, y=250)
    user_email.insert(0, 'email')
    user_email.bind('<FocusIn>', on_enter)
    user_email.bind('<FocusOut>', on_leave)
    # code to create txt box back border------
    frame_email = Frame(frame_regi, width=295, height=2, bg='#000')  # 20c997
    frame_email.place(x=130, y=280)

#Mobile

    def on_enter(e):
        user_mobile.delete(0, 'end')

    def on_leave(e):
        name = user_mobile.get()
        if name == '':
            user_mobile.insert(0, 'Mobile Number')

    mobile=StringVar()
    user_mobile = Entry(frame_regi, width=25, fg='black', bg="#20c997", border=0,
                          font=('Microsoft YaHei UI Light', 11),textvariable=mobile)
    user_mobile.place(x=130, y=300)
    user_mobile.insert(0, 'Mobile Number')
    user_mobile.bind('<FocusIn>', on_enter)
    user_mobile.bind('<FocusOut>', on_leave)

    # code to create txt box back border--------------------
    frame_mobile = Frame(frame_regi, width=295, height=2, bg='#000')  # 20c997
    frame_mobile.place(x=130, y=330)
#Contact Person name

    def on_enter(e):
        user_person.delete(0, 'end')

    def on_leave(e):
        name = user_person.get()
        if name == '':
            user_person.insert(0, 'Contact person Name')

    person_name=StringVar()
    user_person = Entry(frame_regi, width=25, fg='black', bg="#20c997", border=0,
                        font=('Microsoft YaHei UI Light', 11),textvariable=person_name)
    user_person.place(x=130, y=350)
    user_person.insert(0, 'Contact person Name')
    user_person.bind('<FocusIn>', on_enter)
    user_person.bind('<FocusOut>', on_leave)



    # code to create txt box back border-------------------------------------------------
    frame_person = Frame(frame_regi, width=295, height=2, bg='#000')#20c997
    frame_person.place(x=130, y=380)
#Registration number

    def on_enter(e):
        user_regino.delete(0, 'end')

    def on_leave(e):
        name = user_regino.get()
        if name == '':
            user_regino.insert(0, 'Registration number')
    regi_no=StringVar()
    user_regino = Entry(frame_regi, width=25, fg='black', bg="#20c997", border=0,
                        font=('Microsoft YaHei UI Light', 11),textvariable=regi_no)
    user_regino.place(x=130, y=400)
    user_regino.insert(0, 'Registration number')
    user_regino.bind('<FocusIn>', on_enter)
    user_regino.bind('<FocusOut>', on_leave)

    # code to create txt box back border-------------------------------------------------
    frame_regino = Frame(frame_regi, width=295, height=2, bg='#000')  # 20c997
    frame_regino.place(x=130, y=430)
    #username

    def on_enter(e):
        user_name.delete(0, 'end')

    def on_leave(e):
        name = user_name.get()
        if name == '':
            user_name.insert(0, 'Username')
    username=StringVar()
    user_name = Entry(frame_regi, width=25, fg='black', bg="#20c997", border=0,
                      font=('Microsoft YaHei UI Light', 11),textvariable=username)
    user_name.place(x=130, y=450)
    user_name.insert(0, 'Username')
    user_name.bind('<FocusIn>', on_enter)
    user_name.bind('<FocusOut>', on_leave)

    # code to create txt box back border--
    frame_n = Frame(frame_regi, width=295, height=2, bg='#000')  # 20c997
    frame_n.place(x=130, y=480)

    #password


    def on_enter(e):
        user_password.delete(0, 'end')

    def on_leave(e):
        name = user_password.get()
        if name == '':
            user_password.insert(0, 'Password')
    password=StringVar()
    user_password = Entry(frame_regi, width=25, fg='black', bg="#20c997", border=0,
                          font=('Microsoft YaHei UI Light', 11),textvariable=password)
    user_password.place(x=130, y=500)
    user_password.insert(0, 'Password')
    user_password.bind('<FocusIn>', on_enter)
    user_password.bind('<FocusOut>', on_leave)



    # code to create txt box back border-------------------------------------------------
    frame_password = Frame(frame_regi, width=295, height=2, bg='#000')#20c997
    frame_password.place(x=130, y=530)

#register btn...
    btn_singup=Button(frame_regi,text="Register",font=('Microsoft YaHei UI Light', 11),fg="black",bg="#fff",command=insert)
    btn_singup.place(x=150,y=580,width=200)


#----------------------- left frame start---------------------------------------------
lbl_left=Frame(win,width=700,bg="#fff")
lbl_left.place(x=0,y=0,height=700)
lbl_singup=Label(lbl_left,text="Login to your Account",font="Montserrat 28 bold",fg="black",bg="white")
lbl_singup.place(x=200,y=50)

type=StringVar()
rd_admin=Radiobutton(lbl_left, text="NGO", variable=type,value="ngo",font="Montserrat 16 bold",fg="Black",bg="#fff")
rd_admin.place(x=200,y=200)

rd_admin=Radiobutton(lbl_left, text="Hotel",variable=type,value="hotel",font="Montserrat 16 bold",bg="#fff")
rd_admin.place(x=380,y=200)

lbl_username=Label(lbl_left,text="Username",font="Montserrat 16 bold",bg="#fff")
lbl_username.place(x=200,y=280)
username=StringVar()
txt_username=Entry(lbl_left,width=30,font="poppins 12 bold",border=3,textvariable=username)
txt_username.place(x=320,y=280)

lbl_username=Label(lbl_left,text="Password",font="Montserrat 16 bold",bg="#fff")
lbl_username.place(x=200,y=380)
password=StringVar()
txt_password=Entry(lbl_left,width=30,font="poppins 12 bold",border=3,text="",textvariable=password,show="*")
txt_password.place(x=320,y=380)

btn_login=Button(lbl_left,text="Login",font="Montserrat 16 bold",bg="#20c997",fg="#fff",command=login)
btn_login.place(x=350,y=470,width=200)

#-----------------------        right-frame start---------------------------------------------

frame_right=Frame(win,width=665,bg="#20c997",bd=7)
frame_right.place(x=700,y=0,height=700)

lbl_t1=Label(frame_right,text="New Here?",font="Montserrat 32 bold",fg="#fff",bg="#20c997")
lbl_t1.place(x=250,y=230)
txt=Label(frame_right,text="Sing Up and discover a great \n "
     " amount of new opporturties!",font="Montserrat 12 bold",fg="#fff",bg="#20c997")
txt.place(x=250,y=300)

btn_singup=Button(frame_right,text="Registration",font=('Microsoft YaHei UI Light', 11),fg="black",bg="#fff",
                  command=registration)
btn_singup.place(x=275,y=400,width=200)

win.mainloop()

