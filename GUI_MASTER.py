from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import warnings
import joblib
from joblib import dump
import pickle
warnings.filterwarnings("ignore", category=DeprecationWarning) 
root = tk.Tk()
root.title("Diagnosis of PCOS")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


image = Image.open('B1.jpg')

image = image.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

image = Image.open('p1.png')

image = image.resize((1400,700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image)

background_image=ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=100, y=30)


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
# function to change to next image
'''def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img3)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()'''




  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Textual Data Input", font=('times', 35,' bold '), height=1, width=62,bg="brown",fg="white")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Model_Training():
    data = pd.read_csv("C:/Users/sejal/Desktop/PCOS_code1/PCOS.csv")
    data.head()

    data = data.dropna()
    

    """Feature Selection => Manual"""
    x = data.drop(['PCOS (Y/N)'], axis=1)
    data = data.dropna()
    

    

    print(type(x))
    y = data['PCOS (Y/N)']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=12,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=510,y=150)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as SVM_PCOS.joblib",width=45,height=2,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=510,y=370)
    X = data.drop('PCOS (Y/N)', axis=1)  # Adjust the column name according to your dataset
    y = data['PCOS (Y/N)']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the SVM model
    svm_model = SVC()
    svm_model.fit(X_train_scaled, y_train)
    from joblib import dump
    dump (svcclassifier,"SVM_PCOS.joblib")
    print("Model saved as SVM_PCOS.joblib")
    svm_model = joblib.load("SVM_PCOS.joblib")
    # Save the SVM model to a pickle file
    with open("SVM_PCOS.pkl", "wb") as file:
        pickle.dump(svm_model, file)
    with open("scaler.pkl", "wb") as file:
        pickle.dump(scaler, file)




def DT():
    data = pd.read_csv("C:/Users/sejal/Desktop/PCOS_code1/PCOS.csv")
    data.head()

    data = data.dropna()
    

    """Feature Selection => Manual"""
    x = data.drop(['PCOS (Y/N)'], axis=1)
    data = data.dropna()
    

    

    print(type(x))
    y = data['PCOS (Y/N)']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=2)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier(criterion='entropy', random_state=0)  
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()


 
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=510,y=150)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as DT_PCOS.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=510,y=370)
    from joblib import dump
    dump (svcclassifier,"DT_PCOS.joblib")
    print("Model saved as DT_PCOS.joblib")

def RF():
    data = pd.read_csv("C:/Users/sejal/Desktop/PCOS_code1/PCOS.csv")
    data.head()

    data = data.dropna()
    

    """Feature Selection => Manual"""
    x = data.drop(['PCOS (Y/N)'], axis=1)
    data = data.dropna()
    

    

    print(type(x))
    y = data['PCOS (Y/N)']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=12)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=2)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    
    from sklearn.ensemble import RandomForestClassifier  
    svcclassifier =RandomForestClassifier(n_estimators= 10, criterion="entropy") 
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
     
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=510,y=150)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as RF_PCOS.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=510,y=370)
    from joblib import dump
    dump (svcclassifier,"RF_PCOS.joblib")
    print("Model saved as RF_PCOS.joblib")
    
   


def NB():
    data = pd.read_csv("C:/Users/sejal/Desktop/PCOS_code1/PCOS.csv")
    data.head()

    data = data.dropna()
    

    """Feature Selection => Manual"""
    x = data.drop(['PCOS (Y/N)'], axis=1)
    data = data.dropna()
    

    

    print(type(x))
    y = data['PCOS (Y/N)']
    print(type(y))
    x.shape


 
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

    from sklearn.naive_bayes import GaussianNB
    naive_bayes_classifier = GaussianNB()
    naive_bayes_classifier.fit(x_train, y_train)

    y_pred = naive_bayes_classifier.predict(x_test)
    print(y_pred)

    print("Confusion Matrix :")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.savefig('Confusion Matrix.png', bbox_inches='tight')
    plt.show()
    

    print("=" * 40)
    print("==========")
    print("Classification Report : ", (classification_report(y_test, y_pred)))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))

    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label4.place(x=510,y=150)
    
    label5 = tk.Label(root,text ="Accuracy : "+str(ACC)+"%\nModel saved as NB_PCOS.joblib",width=45,height=3,bg='#152238',fg='white',font=("Tempus Sanc ITC",14))
    label5.place(x=510,y=370)
    from joblib import dump
    dump (naive_bayes_classifier,"NB_PCOS.joblib")
    print("Model saved as NB_PCOS.joblib")
    
def call_file():
    from subprocess import call
    call(['python','Check.py'])
    #import Check.py
    #Check.py()


def window1():
    from subprocess import call
    call(['python','Graphs.py'])
    

def window():
    root.destroy()
    from subprocess import call
    call(['python','Main.py'])

framed = tk.LabelFrame(root, text=" --Result-- ", width=830, height=100, bd=5, font=('times', 14, ' bold '),bg="black",fg="white")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=370, y=600)

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="SVM", command=Model_Training, width=15, height=2)
button3.place(x=400, y=530)

button4 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="DT", command=DT, width=15, height=2)
button4.place(x=600, y=530)

button5 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="RF", command=RF, width=15, height=2)
button5.place(x=800, y=530)
exit = tk.Button(root, text="NB", command=NB, width=15, height=2, font=('times', 15, ' bold '),bg="#560319",fg="white")
exit.place(x=1000, y=530)

exit1 = tk.Button(root, text="Prediction", command=call_file, width=15, height=2, font=('times', 15, ' bold '),bg="brown",fg="white")
exit1.place(x=500, y=630)

exit2 = tk.Button(root, text="Visualization", command=window1, width=15, height=2, font=('times', 15, ' bold '),bg="brown",fg="white")
exit2.place(x=700, y=630)

exit2 = tk.Button(root, text="Back", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit2.place(x=900, y=630)


root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''