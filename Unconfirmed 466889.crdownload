from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as MessageBox


class enquiry:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        # ===Bg Image===
        self.bg = ImageTk.PhotoImage(file="images/2.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ====register frame===
        Frame_enquiry = Frame(self.root, bg="white")
        Frame_enquiry.place(x=650, y=150, height=350, width=500)
        # ===labels===
        title = Label(root, text="ENQUIRY PAGE", fg="purple", bg="white", font=("bold", 30))
        title.place(x=700, y=170)
        source = Label(root, text="SOURCE", fg="blue", bg="white", font=("bold", 15))
        source.place(x=700, y=250)
        destination = Label(root, text="DESTINATION", fg="blue", bg="white", font=("bold", 15))
        destination.place(x=700, y=300)
        date = Label(root, text="DATE", fg="blue", bg="white", font=("bold", 15))
        date.place(x=700, y=350)
        # ====textfields=====
        t_source = Entry(font=("times new roman", 15), bg="lightgray")
        t_source.place(x=900, y=250)
        t_destination = Entry(font=("times new roman", 15), bg="lightgray")
        t_destination.place(x=900, y=300)
        date1 = Entry(font=("time new roman", 15), bg="lightgray")
        date1.place(x=900, y=350)
        # ====buttons===
        create = Button(root, text="SEARCH", font=("times new roman", 15, "bold"), bg="blue", fg="white")
        create.place(x=900, y=400)


root = Tk()
obj = enquiry(root)
root.mainloop()
