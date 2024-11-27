
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
from tkinter import LEFT

root = tk.Tk()
root.configure(background="#152238")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("1700x1650")
root.title("login Form")

username = tk.StringVar()
password = tk.StringVar()

image2 = Image.open('p3.jpg')
image2 = image2.resize((w,h))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()
    
    # Remove this function as it's not needed anymore
    #pass

def login():
    with sqlite3.connect('resistration1.db') as db:
        c = db.cursor()

        # Find user If there is any take proper action
        db = sqlite3.connect('resistration1.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                        "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,age TEXT , password TEXT)")
        db.commit()
        find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
        c.execute(find_entry, [(username.get()), (password.get())])
        result = c.fetchall()

        if result:
            ms.showinfo("messege", "LogIn sucessfully")
            root.destroy()
            from subprocess import call
            call(['python','Main.py'])
        else:
            ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

# bg_icon=ImageTk.PhotoImage(file="C:/Users/sejal/Desktop/PCOS_code1/f.jpg")
# user_icon=ImageTk.PhotoImage(file="C:/Users/sejal/Desktop/PCOS_code1/l1.png")
# pass_icon=ImageTk.PhotoImage(file="C:/Users/sejal/Desktop/PCOS_code1/p1.jpg")
        


bg_icon=ImageTk.PhotoImage(file="f.jpg")
user_icon=ImageTk.PhotoImage(file="l1.png")
pass_icon=ImageTk.PhotoImage(file="p1.jpg")


title=tk.Label(root, text="Login Here", font=("Papyrus", 30, "bold","italic"),bd=5,bg="LightCoral",fg="Maroon")
title.place(x=650,y=100,width=250)
        
Login_frame=tk.Frame(root,bg="white")
Login_frame.place(x=510,y=220)
        
logolbl=tk.Label(Login_frame,image=bg_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username",image=user_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",image=pass_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="#75FA8D",fg="black")
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="#FF3727",fg="black")
btn_reg.grid(row=3,column=0,pady=10)
        
        

        
# title=tk.Label(root, text="Login Here", font=("Algerian", 30, "bold","italic"),bd=5,bg="black",fg="white")
# title.place(x=620,y=100,width=250)
        
# Login_frame=tk.Frame(root,bg="white")
# Login_frame.place(x=510,y=220)
        
# logolbl=tk.Label(Login_frame,image=bg_icon,bd=0).grid(row=0,columnspan=2,pady=20)
        
# lbluser=tk.Label(Login_frame,text="Username",image=user_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
# txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
# txtuser.grid(row=1,column=1,padx=20)
        
# lblpass=tk.Label(Login_frame,text="Password",image=pass_icon,compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
# txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
# txtpass.grid(row=2,column=1,padx=20)
        
# btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="Green",fg="black")
# btn_log.grid(row=3,column=1,pady=10)

def window():
    root.destroy()

root.mainloop()
