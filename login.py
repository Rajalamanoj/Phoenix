from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as MessageBox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Sytem")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        # ===Bg Image===
        self.bg = ImageTk.PhotoImage(file="images/2.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ====login frame===
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=650, y=150, height=300, width=500)
        #=====labels===
        title = Label(root, text="LOGIN FORM", fg="blue", bg="white", font=("bold", 30))
        title.place(x=775, y=170)
        uname = Label(root, text="USER NAME", fg="black", bg="white", font=("bold", 15))
        uname.place(x=700, y=250)
        password = Label(root, text="PASSWORD", fg="black", bg="white", font=("bold", 15))
        password.place(x=700, y=300)
        #====fields===
        t_uname = Entry(font=("times new roman", 15), bg="lightgray")
        t_uname.place(x=850, y=250)
        t_password = Entry(font=("times new roman", 15), bg="lightgray")
        t_password.place(x=850, y=300)
        t_password.config(show='*')
        #=====buttons====
        submit = Button(root, text="LOGIN", font=("times new roman", 15, "bold"), bg="blue",fg="white")
        submit.place(x=875, y=350)
        register = Button(root, text="Register", font=("times new roman", 15, "bold"), bg="blue",fg="white")
        register.place(x=750, y=350)
        admin = Button(root, text="Admin", font=("times new roman", 15, "bold"), bg="blue",fg="white")
        admin.place(x=1000, y=350)


root = Tk()
obj = Login(root)
root.mainloop()
