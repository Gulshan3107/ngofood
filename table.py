# Python program to create a table

from tkinter import *
from tkinter import ttk
win=Tk()
win.title("Dynamic coding treeview")
win.geometry("600x600")
win.config(bg="#fff")

col=('etype','ename','date','time','venue','people','cnt_person','open')
treeview=ttk.Treeview(win,height=5,show='headings',columns=col)

# adding columns....
treeview.column('etype',width=100,anchor=CENTER)
treeview.column('ename',width=100,anchor=CENTER)
treeview.column('date',width=100,anchor=CENTER)
treeview.column('time',width=100,anchor=CENTER)
treeview.column('venue',width=100,anchor=CENTER)
treeview.column('people',width=100,anchor=CENTER)
treeview.column('cnt_person',width=100,anchor=CENTER)
treeview.column('open',width=100,anchor=CENTER)

#addings heading

treeview.heading('etype',text='Type of Event')
treeview.heading('ename',text='Name of Event')
treeview.heading('date',text='Date')
treeview.heading('time',text='Time')
treeview.heading('venue',text='Venue')
treeview.heading('people',text='Estimate Number Of People')
treeview.heading('cnt_person',text='Contact')
treeview.heading('open',text="Open")

treeview.place(x=100,y=200)



win.mainloop()