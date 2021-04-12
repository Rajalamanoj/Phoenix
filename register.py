from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as MessageBox


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        # ===Bg Image===
        self.bg = ImageTk.PhotoImage(file="images/2.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ====register frame===
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=650, y=150, height=450, width=500)
        #===labels===
        title = Label(root, text="Create Account", fg="purple", bg="white", font=("bold", 30))
        title.place(x=800, y=170)
        uname = Label(root, text="USER NAME", fg="blue", bg="white", font=("bold", 15))
        uname.place(x=700, y=250)
        password = Label(root, text="PASSWORD", fg="blue", bg="white", font=("bold", 15))
        password.place(x=700, y=450)
        cn_password = Label(root, text="CONFIRM PASSWORD", fg="blue", bg="white", font=("bold", 13))
        cn_password.place(x=700, y=500)
        email=Label(root, text="Email", fg="blue", bg="white", font=("bold", 15))
        email.place(x=700, y=300)
        phonenumber=Label(root, text="PHONE NUMBER", fg="blue", bg="white", font=("bold", 15))
        phonenumber.place(x=700, y=350)
        dofb = Label(root, text="DATE OF BIRTH", fg="blue", bg="white", font=("bold", 15))
        dofb.place(x=700, y=400)
        #====textfields=====
        t_uname = Entry(font=("times new roman", 15), bg="lightgray")
        t_uname.place(x=900, y=250)
        t_password = Entry(font=("times new roman", 15), bg="lightgray")
        t_password.place(x=900, y=450)
        t_password.config(show='*')
        cn_password1 = Entry(font=("times new roman", 15), bg="lightgray")
        cn_password1.place(x=900, y=500)
        cn_password1.config(show='*')
        email1=Entry(font=("times new roman", 15), bg="lightgray")
        email1.place(x=900, y=300)
        phonenumber = Entry(font=("times new roman", 15), bg="lightgray")
        phonenumber.place(x=900, y=350)
        dofb1=Entry(font=("times new roman", 15), bg="lightgray")
        dofb1.place(x=900, y=400)
        #====buttons===
        create = Button(root, text="Create", font=("times new roman", 15, "bold"), bg="blue",fg="white")
        create.place(x=900, y=550)


root = Tk()
obj = register(root)
root.mainloop()