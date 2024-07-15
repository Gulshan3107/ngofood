import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Send Messages To Ngo Or Hotel")
window.geometry("600x400")
#window.configure(background='grey')

path = "whtas.png"
img = ImageTk.PhotoImage(Image.open(path),width=1250)
panel = tk.Label(window, image = img)

txtVar = tk.StringVar(None)
usrIn = tk.Entry(window, textvariable = txtVar, width = 30)
usrIn.grid(row = 10, column = 10)

usrIn.place(x=100,y=60)
panel.pack(x=0,y=30)
window.mainloop()