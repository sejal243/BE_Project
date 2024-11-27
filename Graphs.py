def Graphs():
    import tkinter as tk

    import pandas as pd
    from PIL import Image,ImageTk
    from tkinter import ttk


    root= tk.Tk()
    '''root = tk.Toplevel()'''
    root.title("PCOS")

    w,h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
     
    image4 =Image.open('D1.jpg')
    image4 =image4.resize((w,h), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image4)
    background_label = tk.Label(root, image=background_image)
    background_label.image=background_image
    background_label.place(x=0, y=0) 

    image4 =Image.open('ACCURACY.png')
    image4 =image4.resize((360,260), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image4)
    background_label = tk.Label(root, image=background_image)
    background_label.image=background_image
    background_label.place(x=50, y=50) 
    #############################################
    
    image4 =Image.open('Histogram.png')
    image4 =image4.resize((360,260), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image4)
    background_label = tk.Label(root, image=background_image)
    background_label.image=background_image
    background_label.place(x=50, y=400) 
    
    image4 =Image.open('ScatterPlot.png')
    image4 =image4.resize((360,260), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image4)
    background_label = tk.Label(root, image=background_image)
    background_label.image=background_image
    background_label.place(x=900, y=50) 
    
    
    image4 =Image.open('Correlation.png')
    image4 =image4.resize((360,260), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image4)
    background_label = tk.Label(root, image=background_image)
    background_label.image=background_image
    background_label.place(x=450, y=50)
 
    ######################################################
    image4 =Image.open('Confusion Matrix.png')
    image4 =image4.resize((360,260), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image4)
    background_label = tk.Label(root, image=background_image)
    background_label.image=background_image
    background_label.place(x=450, y=400)

    ######################################################
    image4 =Image.open('HistogramCyclelength.png')
    image4 =image4.resize((360,260), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image4)
    background_label = tk.Label(root, image=background_image)
    background_label.image=background_image
    background_label.place(x=900, y=400)

    
    # image4 =Image.open('grades.png')
    # image4 =image4.resize((360,260), Image.ANTIALIAS)

    # background_image=ImageTk.PhotoImage(image4)
    # background_label = tk.Label(root, image=background_image)
    # background_label.image=background_image
    # background_label.place(x=450, y=600)

    # ######################################################
    # image4 =Image.open('grades2.png')
    # image4 =image4.resize((360,260), Image.ANTIALIAS)

    # background_image=ImageTk.PhotoImage(image4)
    # background_label = tk.Label(root, image=background_image)
    # background_label.image=background_image
    # background_label.place(x=0, y=600)
    
    # image4 =Image.open('grades3.png')
    # image4 =image4.resize((360,260), Image.ANTIALIAS)

    # background_image=ImageTk.PhotoImage(image4)
    # background_label = tk.Label(root, image=background_image)
    # background_label.image=background_image
    # background_label.place(x=900, y=600)

    def window():
       root.destroy()
       
    '''button4=tk.Button(root,foreground="white",background="black",font=("Tempus Sans ITC",14,"bold"),text="Graphs",command=Graphs,width=20,height=2)
    button4.place(x=45,y=530)'''
     
    root.mainloop()          


Graphs()
  