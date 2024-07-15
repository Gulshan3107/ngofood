from tkinter import *
from PIL import Image,ImageTk
import webbrowser
from tkinter import ttk
win=Tk()
win.title("Send Messages To Ngo Or Hotel")
win.geometry("700x700")


#-----------send msg------

def Go():
    webbrowser.open_new("https://web.whatsapp.com/send?phone=918329825206&text=Hi")

    if(m.get()=="value=1"):
        print("Your Selected Ngo ")
    else:
       print ("Please Select Write Option")

#---------frame-----------------

F1=Frame(win,width=490,height=630,bg="#50C878")
F1.place(x=800,y=30)

lbl_main=Menubutton(win,text="👉  Directly Send Messages To Ngo Or Hotel   💻",
                    font="Arial 14 bold italic underline",bg="black",fg="white",activebackground="green")
lbl_main.pack(fill="x")

lbl_name=Label(win,text="Enter The Number :",font="BellMT 16 bold italic ",bg="#50C878",fg="black")
lbl_name.place(x=820,y=100)

E1=Entry(win,width=30)
E1.place(x=1050,y=103)


m=StringVar()
rd_ngo=Radiobutton(win,text="NGO",font="Arial 12 bold",bg="#50C878",value=1,variable=m)
rd_ngo.place(x=900,y=200)

rd_hotel=Radiobutton(win,text="Hotel",font="Arial 12 bold",bg="#50C878",value=2,variable=m)
rd_hotel.place(x=1070,y=200)


#drp_list=ttk.Combobox(win,font=('Microsoft YaHei UI Light', 11))
#drp_list["values"]=["HOTEL","NGO"]
#drp_list.place(x=1000,y=300)



btn_send=Button(win,text="SEND",font="Arial 16 bold italic",fg="white",bg="#50C878",command=Go)
btn_send.place(x=980,y=300)
#-------------Add img----------------
image=Image.open("whtas.png")
resize_image=image.resize((800,615))

filename=ImageTk.PhotoImage(resize_image)
background_image = Label(image=filename)
background_image.image=filename
background_image.place(x=0,y=30)


win.mainloop()