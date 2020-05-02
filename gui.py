from tkinter import *
import os
import pandas as pd
import tkinter.scrolledtext as tkst
main = Tk()
main.geometry('{}x{}'.format(640, 420))
main.wm_title("Face recognition ")

svalue = StringVar() # defines the widget state as string
svalue1 = StringVar()
#imagePath = PhotoImage(file="facerec.png")
#widgetf = Label(main, image=imagePath).pack(side="bottom")
#imagePath1 = PhotoImage(file="efylogo.png")
#widgetf = Label(main, image=imagePath1).pack(side="top")
df=pd.read_json('data.json')
comments = """Welcome to Face Recognition Based Attendence System 


"""

widgets = Label(main, 
           justify=CENTER,
           padx = 10,

           text=comments).pack(side="top")

comments1=""" Developed and Design by Aseem Kanungo"""
widgets1 = Label(main,
           justify=CENTER,
           padx = 10,

           text=comments1).pack(side="bottom")




Label(main,text='Name',justify=CENTER).place(relx=0.30,y=100)

w = Entry(main,textvariable=svalue,justify=CENTER) # adds a textarea widget
w.pack()
w.place(relx=0.4,y=100)
Label(main,text='ScholarID',justify=CENTER).place(relx=0.54,y=100)
q= Entry(main,textvariable=svalue1,justify=CENTER) # adds a textarea widget
q.pack()
q.place(relx=0.64,y=100)
def fisher_database_button_fn():
     name = svalue.get()
     scholarid= svalue1.get()
     os.system('python database.py {0} {1}'.format(name,scholarid))



def fisher_dataset_button_fn():

    os.system('python gui1.py ')

def fisher_recog_button_fn():
    os.system('python 03_face_recognition.py')

def fisher_atendence_button_fn():
    os.system('python 03_face_recognition1.py')



train_database_button = Button(main,text="Enter new data ", command=fisher_database_button_fn,justify=CENTER)
train_database_button.pack()
train_database_button.place(relx=0.74,y=95)

recog_fisher_button = Button(main,text="Recognize", command=fisher_recog_button_fn,justify=CENTER)
recog_fisher_button.pack()
recog_fisher_button.place(x=250,y=200)

recog_fisher_button = Button(main,text="Add to dataset ", command=fisher_dataset_button_fn,justify=CENTER)
recog_fisher_button.pack()
recog_fisher_button.place(x=250,y=225)

recog_train_button = Button(main,text="Take Attendence", command=fisher_atendence_button_fn,justify=CENTER)
recog_train_button.pack()
recog_train_button.place(x=250,y=280)

main.mainloop()
