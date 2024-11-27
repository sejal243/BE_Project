import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os

window = tk.Tk()
window.geometry("1700x1200")
window.title("REGISTRATION FORM")
window.configure(background="#B0B0E2")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.StringVar()  # Changed to StringVar since phone numbers may contain characters
age = tk.StringVar()  # Changed to StringVar since age may contain characters
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# Function to check password strength
def password_check(passwd): 
    SpecialSym =['$', '@', '#', '%'] 
    val = True
    
    if len(passwd) < 6: 
        print('length should be at least 6') 
        val = False
        
    if len(passwd) > 20: 
        print('length should be not be greater than 8') 
        val = False
        
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
        
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
        
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
        
    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('resistration1.db') as db:
        c = db.cursor()

    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time.isdigit() and (int(time) > 100)) or (time == "")):
        ms.showinfo("Message", "Please Enter valid age")
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('resistration1.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, address, username, Email, Phoneno, age , password) VALUES(?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, time, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            from subprocess import call
            call(["python", "Login.py"])
            window.destroy()
def back():
    window.destroy() 
    from subprocess import call
    call(["python", "GUI_main.py"])
# Labels and entry fields

image2 = Image.open('p3.jpg')
image2 = image2.resize((1700,1200))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

# that is for label1 registration
l1 = tk.Label(window, text="Registration Form", font=("Papyrus", 30, "bold"), bg="LightCoral", fg="Maroon")
l1.place(x=590, y=50)


l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=530, y=150)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=800, y=150)
# that is for label 2 (full name)


l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=530, y=200)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=800, y=200)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=530, y=250)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=800, y=250)
# that is for email address

l6 = tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=530, y=300)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=800, y=300)
# phone number


l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=530, y=350)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=800, y=350)

l4 = tk.Label(window, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l4.place(x=530, y=400)
t3 = tk.Entry(window, textvar=username, width=20, font=('', 15))
t3.place(x=800, y=400)

l9 = tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=530, y=450)
t9 = tk.Entry(window, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=800, y=450)

l10 = tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"), bg="snow")
l10.place(x=530, y=500)

t10 = tk.Entry(window, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=800, y=500)

btn = tk.Button(window, text="Register", bg="#192841",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=1300, y=700)
btn = tk.Button(window, text="Back", bg="#192841",font=("",20),fg="white", width=9, height=1, command=back)
btn.place(x=100, y=700)


# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()
