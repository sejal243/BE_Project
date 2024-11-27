from tkinter import *
import tkinter as tk
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
#import requests
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
import webbrowser
def Train():
    """GUI"""
    

    root = tk.Tk()
    image5 = Image.open('P3.jpg')
    image5 = image5.resize((1700,1200))

    background_image = ImageTk.PhotoImage(image5)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=0, y=0)  

    root.geometry("1700x1550")
    root.title("Diagnosis of PCOS")
    root.configure(background="pink")
    FileNo = tk.IntVar()
    Age = tk.IntVar()
    Weight= tk.IntVar()
    Height= tk.IntVar()
    Pulserate= tk.IntVar()
    RR = tk.IntVar()
    Hb= tk.IntVar()
    Cyclelength = tk.IntVar()
    FollicleNo = tk.IntVar()
    Endometrium = tk.IntVar()
    
   
   
    
    #===================================================================================================================
    def back():
        root.destroy()
        from subprocess import call
        call(['python','Main.py'])
    
    
    def window2():
        url = "https://www.swft.nhs.uk/application/files/8015/6586/5352/Dietary_Advice_for_Polycystic_Ovary_Syndrome_A4_2019.pdf"
        webbrowser.open(url)
    
    def Detect():
        
        
        e1=FileNo.get()
        print(e1)
        e2=Age.get()
        print(e2)
        e3= Weight.get()
        print(e3)
        e4= Height.get()
        print(e4)
        e5=Pulserate.get()
        print(e5)
        e6=RR.get()
        print(e6)
        e7=Hb.get()
        print(e7)
        e8=Cyclelength.get()
        print(e8)
        e9=FollicleNo.get()
        print(e9)
        e10=Endometrium.get()
        print(e10)
        
        #########################################################################################
        
        from joblib import dump ,load
        a1=load("DT_PCOS.joblib")
        v= a1.predict([[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]])
        print(v)
        
        # try:
        #     if v[0] == 0:
        #         print("PCOS Not Detected")
        #         yes = tk.Label(root, text="PCOS Not Detected", background="green", foreground="white",
        #                        font=('times', 20, 'bold'), width=20)
        #         yes.place(x=630, y=650)
        #     elif v[0] == 1:
        #         print("PCOS Detected")
        #         no = tk.Label(root, text="PCOS Detected", background="brown", foreground="white",
        #                       font=('times', 20, 'bold'), width=20)
        #         no.place(x=630, y=650)
        # except:
        #     print("Invalid input values")
        #     invalid = tk.Label(root, text="Invalid input values", background="red", foreground="white",
        #                        font=('times', 20, 'bold'), width=20)
        #     invalid.place(x=630, y=650)
    
        
        if v[0]==0:
            print("PCOS Not Detected")
            yes = tk.Label(root,text="PCOS Not Detected",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=630,y=570)
                     
        elif v[0]==1:
            print("PCOS Detected")
            no = tk.Label(root, text="PCOS Detected", background="brown", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=630, y=570)
            
    
            
        # except:
        #     print("Invalid input values")
        #     invalid = tk.Label(root, text="Invalid input values", background="red", foreground="white", font=('times', 20, 'bold'), width=20)
        #     invalid.place(x=630, y=650)    
        
        
        
     #   bg = PhotoImage("P3.jpg") 
        
        # , relwidth=1, relheight=1)
       
            
       
           
    l1=tk.Label(root,text="File No",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l1.place(x=400,y=50)
    FileNo=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=FileNo)
    FileNo.place(x=800,y=50)

    l2=tk.Label(root,text="Age",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l2.place(x=400,y=100)
    Age=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar= Age)
    Age.place(x=800,y=100)
    
    l3=tk.Label(root,text="Weight",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l3.place(x=400,y=150)
    Weight=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=Weight)
    Weight.place(x=800,y=160)
    
    l4=tk.Label(root,text="Height",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l4.place(x=400,y=200)
    Height=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=Height)
    Height.place(x=800,y=200)
    
    l5=tk.Label(root,text="Pulserate",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l5.place(x=400,y=250)
    Pulserate=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=Pulserate)
    Pulserate.place(x=800,y=250)
  
    l6=tk.Label(root,text="RR",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l6.place(x=400,y=300)
    RR=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=RR)
    RR.place(x=800,y=300)
    
    l7=tk.Label(root,text="Hb",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l7.place(x=400,y=350)
    Hb=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=Hb)
    Hb.place(x=800,y=350)
    
    l8=tk.Label(root,text="Cycle length",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l8.place(x=400,y=400)
    Cyclelength=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=Cyclelength)
    Cyclelength.place(x=800,y=400)
    
    l9=tk.Label(root,text="Follicle No",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l9.place(x=400,y=450)
    FollicleNo=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=FollicleNo)
    FollicleNo.place(x=800,y=450)
    
    l10=tk.Label(root,text="Endometrium",bg="snow",font=('Times new roman', 20, 'bold '),width=20)
    l10.place(x=400,y=500)
    Endometrium=tk.Entry(root,bd=2,width=15,font=("Times new roman", 20),textvar=Endometrium)
    Endometrium.place(x=800,y=500)

     
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=660,y=700)
    button = tk.Button(root,text="Back",command=back,font=('times', 20, ' bold '),width=10)
    button.place(x=100,y=700)
    button1 = tk.Button(root,text="Next",command=window2,font=('times', 20, ' bold '),width=10)
    button1.place(x=1300,y=700)
    # button2 = tk.Button(root, text="Tap", command=window2, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
    # button2.place(x=660, y=680)


    root.mainloop()

Train()




































# from tkinter import *
# import tkinter as tk
# import numpy as np
# import pandas as pd
# #import requests
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import LabelEncoder
# import webbrowser
# def Train():
#     """GUI"""
    

#     root = tk.Tk()

#     root.geometry("1700x1550")
#     root.title("Machine Learning Approaches On Polycystic Ovary Syndrome")
#     root.configure(background="#152238")
#     FileNo = tk.IntVar()
#     Age = tk.IntVar()
#     Weight= tk.IntVar()
#     Height= tk.IntVar()
#     Pulserate= tk.IntVar()
#     RR = tk.IntVar()
#     Hb= tk.IntVar()
#     Cyclelength = tk.IntVar()
#     FollicleNo = tk.IntVar()
#     Endometrium = tk.IntVar()
   
   
   
    
#     #===================================================================================================================
#     def back():
#         root.destroy()
#         from subprocess import call
#         call(['python','Main.py'])
    
    
#     def window2():
#         url = "https://youtu.be/M1Ed9i3jkHo?si=23WQbOIw8hs9hDRn"
#         webbrowser.open(url)
    
#     def Detect():
        
        
#         e1=FileNo.get()
#         print(e1)
#         e2=Age.get()
#         print(e2)
#         e3= Weight.get()
#         print(e3)
#         e4= Height.get()
#         print(e4)
#         e5=Pulserate.get()
#         print(e5)
#         e6=RR.get()
#         print(e6)
#         e7=Hb.get()
#         print(e7)
#         e8=Cyclelength.get()
#         print(e8)
#         e9=FollicleNo.get()
#         print(e9)
#         e10=Endometrium.get()
#         print(e10)
        
#         #########################################################################################
        
#         from joblib import dump ,load
#         a1=load(r'C:/Users/sejal/Desktop/PCOS_code1/SVM_PCOS.joblib')
#         v= a1.predict([[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]])
#         print(v)
        
#         # try:
#         #     if v[0] == 0:
#         #         print("PCOS Not Detected")
#         #         yes = tk.Label(root, text="PCOS Not Detected", background="green", foreground="white",
#         #                        font=('times', 20, 'bold'), width=20)
#         #         yes.place(x=630, y=650)
#         #     elif v[0] == 1:
#         #         print("PCOS Detected")
#         #         no = tk.Label(root, text="PCOS Detected", background="brown", foreground="white",
#         #                       font=('times', 20, 'bold'), width=20)
#         #         no.place(x=630, y=650)
#         # except:
#         #     print("Invalid input values")
#         #     invalid = tk.Label(root, text="Invalid input values", background="red", foreground="white",
#         #                        font=('times', 20, 'bold'), width=20)
#         #     invalid.place(x=630, y=650)
    
        
#         if v[0]==0:
#             print("PCOS Not Detected")
#             yes = tk.Label(root,text="PCOS Not Detected",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
#             yes.place(x=630,y=650)
                     
#         elif v[0]==1:
#             print("PCOS Detected")
#             no = tk.Label(root, text="PCOS Detected", background="brown", foreground="white",font=('times', 20, ' bold '),width=20)
#             no.place(x=630, y=650)
            
    
            
#         # except:
#         #     print("Invalid input values")
#         #     invalid = tk.Label(root, text="Invalid input values", background="red", foreground="white", font=('times', 20, 'bold'), width=20)
#         #     invalid.place(x=630, y=650)    
              
    
       
            
        
            
           
#     l1=tk.Label(root,text="FileNo",background="olive",font=('times', 20, ' bold '),width=20)
#     l1.place(x=400,y=50)
#     FileNo=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=FileNo)
#     FileNo.place(x=800,y=50)

#     l2=tk.Label(root,text="Age",background="olive",font=('times', 20, ' bold '),width=20)
#     l2.place(x=400,y=100)
#     Age=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar= Age)
#     Age.place(x=800,y=100)
    
#     l3=tk.Label(root,text="Weight",background="olive",font=('times', 20, ' bold '),width=20)
#     l3.place(x=400,y=150)
#     Weight=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Weight)
#     Weight.place(x=800,y=160)
    
#     l4=tk.Label(root,text="Height",background="olive",font=('times', 20, ' bold '),width=20)
#     l4.place(x=400,y=200)
#     Height=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Height)
#     Height.place(x=800,y=200)
    
#     l5=tk.Label(root,text="Pulserate",background="olive",font=('times', 20, ' bold '),width=20)
#     l5.place(x=400,y=250)
#     Pulserate=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Pulserate)
#     Pulserate.place(x=800,y=250)
  
#     l6=tk.Label(root,text="RR",background="olive",font=('times', 20, ' bold '),width=20)
#     l6.place(x=400,y=300)
#     RR=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=RR)
#     RR.place(x=800,y=300)
    
#     l7=tk.Label(root,text="Hb",background="olive",font=('times', 20, ' bold '),width=20)
#     l7.place(x=400,y=350)
#     Hb=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Hb)
#     Hb.place(x=800,y=350)
    
#     l8=tk.Label(root,text="Cyclelength",background="olive",font=('times', 20, ' bold '),width=20)
#     l8.place(x=400,y=400)
#     Cyclelength=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Cyclelength)
#     Cyclelength.place(x=800,y=400)
    
#     l9=tk.Label(root,text="FollicleNo",background="olive",font=('times', 20, ' bold '),width=20)
#     l9.place(x=400,y=450)
#     FollicleNo=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=FollicleNo)
#     FollicleNo.place(x=800,y=450)
    
#     l10=tk.Label(root,text="Endometrium",background="olive",font=('times', 20, ' bold '),width=20)
#     l10.place(x=400,y=500)
#     Endometrium=tk.Entry(root,bd=2,width=15,font=("TkDefaultFont", 20),textvar=Endometrium)
#     Endometrium.place(x=800,y=500)

     
    
#     button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
#     button1.place(x=660,y=580)
#     button = tk.Button(root,text="Back",command=back,font=('times', 20, ' bold '),width=10)
#     button.place(x=860,y=580)
#     button1 = tk.Button(root,text="Tap",command=window2,font=('times', 20, ' bold '),width=10)
#     button1.place(x=660,y=640)
#     # button2 = tk.Button(root, text="Tap", command=window2, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
#     # button2.place(x=660, y=680)


#     root.mainloop()

# Train()