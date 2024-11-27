import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
import sqlite3
import webbrowser
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Machine Learning Approaches On Polycystic Ovary Syndrome")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('D1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

#img=ImageTk.PhotoImage(Image.open("B4.png"))

#img2=ImageTk.PhotoImage(Image.open("B5.jpg"))

#img3=ImageTk.PhotoImage(Image.open("B7.jpg"))


#
lbl = tk.Label(root, text="Machine Learning Approaches On Polycystic Ovary Syndrome", font=('times', 35,' bold '), height=1, width=60,bg="maroon",fg="white")
lbl.place(x=0, y=3)


frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=400, bd=5, font=('times', 14, ' bold '),bg="#152238")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=90)


frame_alpr1 = tk.LabelFrame(root, width=220, height=90, bd=5, font=('times', 14, ' bold '),bg="#152238")
frame_alpr1.grid(row=0, column=0, sticky='nw')
frame_alpr1.place(x=1300, y=680)

frame_alpr2 = tk.LabelFrame(root, width=220, height=75, bd=5, font=('times', 14, ' bold '),bg="#152238")
frame_alpr2.grid(row=0, column=0, sticky='nw')
frame_alpr2.place(x=10, y=675)
    
    
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModel.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    print(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from tensorflow.keras.models import load_model
    #from keras.optimizers import Adam

#    global fn
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('PCOSCNN.h5')
            
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        plant=np.argmax(prediction)
        print(plant)
        
        
        
        
    
    
        if plant == 0:
            Cd="Polycystic Ovary Syndrome Detected \n Focus on a balanced diet that includes a variety of whole foods,\n such as fruits, vegetables, lean proteins, and whole grains.\n Schedule regular check-ups with your healthcare \n provider to monitor your condition \n and address any concerns."
            # PD = tk.Button(root, text="Tap", command=window,background="black",font=('times', 20, ' bold '), width=10, fg="white")
            # PD.place(x=300, y=650)
            
            
             
        elif plant == 1:
            Cd="Polycystic Ovary Syndrome Not Detected"
        
        
        A=Cd
        return A
    
    
    
    
    
    
    

        
    
           
def window2():
    url = "https://youtu.be/M1Ed9i3jkHo?si=23WQbOIw8hs9hDRn"
    webbrowser.open(url)
############################################################
def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=450)

###############################################################################


def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        #X1="Selected Image is {0}".format(X)
        x2=format(X)+""
        
        end = time.time()
            
        ET="\n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ x2 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
#############################################################################
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='C:/Users/Kadam/Desktop/project/New folder/PCOS 100% Code/test_set',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])



    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=100)
  
#############################################################################    

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)


#################################################################################################################
def window():
    root.destroy()

def window1():
    root.destroy()
    from subprocess import call
    call(['python','Main.py'])



button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=40)

button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button2.place(x=10, y=100)

button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button3.place(x=10, y=320)
# #
button4 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=160)


button4 = tk.Button(frame_alpr2, text="Back",command=window1,width=15,height=1, bg="white", fg="black",font=('times', 15, 'bold'))
button4.place(x=10, y=10)

# button4 = tk.Button(frame_alpr2, text="Back", command=window1,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
# button4.place(x=10, y=310)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)
# button2 = tk.Button(frame_alpr1, text="Next", command=window2, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button2.place(x=1250, y=650)

button2 = tk.Button(frame_alpr1,text="Next", command=window2,width=15,height=1, font=('times', 15, 'bold'), bg="white",fg="black")
button2.grid(row=0, column=0, padx=10, pady=10)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=220)
#(x=1250, y=650)


root.mainloop()


















# import tkinter as tk
# from tkinter import ttk, LEFT, END
# from PIL import Image , ImageTk 
# from tkinter.filedialog import askopenfilename
# import cv2
# import numpy as np
# import time
# import CNNModel 
# import sqlite3
# import webbrowser
# #import tfModel_test as tf_test
# global fn
# fn=""
# ##############################################+=============================================================
# root = tk.Tk()
# root.configure(background="seashell2")
# #root.geometry("1300x700")


# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))
# root.title("Machine Learning Approaches On Polycystic Ovary Syndrome")


# #430
# #++++++++++++++++++++++++++++++++++++++++++++
# #####For background Image
# image2 =Image.open('D1.jpg')
# image2 =image2.resize((w,h), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

# #img=ImageTk.PhotoImage(Image.open("B4.png"))

# #img2=ImageTk.PhotoImage(Image.open("B5.jpg"))

# #img3=ImageTk.PhotoImage(Image.open("B7.jpg"))


# #
# lbl = tk.Label(root, text="Machine Learning Approaches On Polycystic Ovary Syndrome", font=('times', 35,' bold '), height=1, width=60,bg="maroon",fg="white")
# lbl.place(x=0, y=3)


# frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=490, bd=5, font=('times', 14, ' bold '),bg="#152238")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=10, y=90)

    
    
# ###########################################################################
# def train_model():
 
#     update_label("Model Training Start...............")
    
#     start = time.time()

#     X= CNNModel.main()
    
#     end = time.time()
        
#     ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
#     msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

#     print(msg)

# import functools
# import operator


# def convert_str_to_tuple(tup):
#     s = functools.reduce(operator.add, (tup))
#     return s

# def test_model_proc(fn):
#     from tensorflow.keras.models import load_model
#     #from keras.optimizers import Adam

# #    global fn
    
#     IMAGE_SIZE = 64
#     LEARN_RATE = 1.0e-4
#     CH=3
#     print(fn)
#     if fn!="":
#         # Model Architecture and Compilation
       
#         model = load_model('PCOSCNN.h5')
            
#         img = Image.open(fn)
#         img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
#         img = np.array(img)
        
#         img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
#         img = img.astype('float32')
#         img = img / 255.0
#         print('img shape:',img)
#         prediction = model.predict(img)
#         print(np.argmax(prediction))
#         plant=np.argmax(prediction)
#         print(plant)
        
        
        
        
    
    
#         if plant == 0:
#             Cd="Polycystic Ovary Syndrome Detected \n Focus on a balanced diet that includes a variety of whole foods,\n such as fruits, vegetables, lean proteins, and whole grains.\n Schedule regular check-ups with your healthcare \n provider to monitor your condition \n and address any concerns."
#             # PD = tk.Button(root, text="Tap", command=window,background="black",font=('times', 20, ' bold '), width=10, fg="white")
#             # PD.place(x=300, y=650)
            
            
             
#         elif plant == 1:
#             Cd="Polycystic Ovary Syndrome Not Detected"
        
        
#         A=Cd
#         return A
    
    
    
    
    
    
    

        
    
           
# def window2():
#     url = "https://youtu.be/M1Ed9i3jkHo?si=23WQbOIw8hs9hDRn"
#     webbrowser.open(url)
# ############################################################
# def update_label(str_T):
#     #clear_img()
#     result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25), bg='bisque2', fg='black')
#     result_label.place(x=300, y=450)

# ###############################################################################


# def test_model():
#     global fn
#     if fn!="":
#         update_label("Model Testing Start...............")
        
#         start = time.time()
    
#         X=test_model_proc(fn)
        
#         #X1="Selected Image is {0}".format(X)
#         x2=format(X)+""
        
#         end = time.time()
            
#         ET="\n".format(end-start)
        
#         msg="Image Testing Completed.."+'\n'+ x2 + '\n'+ ET
#         fn=""
#     else:
#         msg="Please Select Image For Prediction...."
        
#     update_label(msg)
    
# #############################################################################
    
# def openimage():
   
#     global fn
#     fileName = askopenfilename(initialdir='C:/Users/Kadam/Desktop/project/New folder/PCOS 100% Code/test_set',
#                                filetypes=[("all files", "*.*")])
#     IMAGE_SIZE=200
#     imgpath = fileName
#     fn = fileName


# #        img = Image.open(imgpath).convert("L")
#     img = Image.open(imgpath)
    
#     img = img.resize((IMAGE_SIZE,200))
#     img = np.array(img)
# #        img = img / 255.0
# #        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


#     x1 = int(img.shape[0])
#     y1 = int(img.shape[1])



#     im = Image.fromarray(img)
#     imgtk = ImageTk.PhotoImage(im)
#     img = tk.Label(root, image=imgtk, height=250, width=250)
#     img.image = imgtk
#     img.place(x=300, y=100)
  
# #############################################################################    

# def convert_grey():
#     global fn    
#     IMAGE_SIZE=200
    
#     img = Image.open(fn)
#     img = img.resize((IMAGE_SIZE,200))
#     img = np.array(img)
    
#     x1 = int(img.shape[0])
#     y1 = int(img.shape[1])

#     gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

#     gs = cv2.resize(gs, (x1, y1))

#     retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#     print(threshold)

#     im = Image.fromarray(gs)
#     imgtk = ImageTk.PhotoImage(image=im)
    
#     #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
#     #result_label1.place(x=300, y=400)
#     img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
#     img2.image = imgtk
#     img2.place(x=580, y=100)

#     im = Image.fromarray(threshold)
#     imgtk = ImageTk.PhotoImage(image=im)

#     img3 = tk.Label(root, image=imgtk, height=250, width=250)
#     img3.image = imgtk
#     img3.place(x=880, y=100)
#     #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
#     #result_label1.place(x=300, y=400)


# #################################################################################################################
# def window():
#     root.destroy()

# def window1():
#     root.destroy()
#     from subprocess import call
#     call(['python','Main.py'])



# button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button1.place(x=10, y=40)

# button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button2.place(x=10, y=100)

# button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=270)
# # #
# button4 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
# button4.place(x=10, y=160)


# button4 = tk.Button(frame_alpr, text="Back", command=window1,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
# button4.place(x=10, y=310)
# #
# #
# #button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
# #button5.place(x=450, y=20)
# button2 = tk.Button(frame_alpr, text="Tap", command=window2, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button2.place(x=10, y=410)


# exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
# exit.place(x=10, y=220)



# root.mainloop()