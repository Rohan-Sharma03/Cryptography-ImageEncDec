# -*- coding: utf-8 -*-
"""
Submitting as a project of Cryptograhy Course.

@author: Rohan Sharma
@author: Aditya Shukla 

"""

# Importing required libraries

from pro.utility1 import *
from tkinter import *
from tkinter import filedialog
import os


# Defining new window as root 

root = Tk(className=" Image Encryptor and Decryptor")
root.geometry("700x700")
root.minsize(700,700)

#  A global variable used to hold values.

file=""

"""
Utility Funcions

"""
 
# A function defined to decrypt a file.
def decryptWindow():

    newWindow = Toplevel(root)
    newWindow.title("Decrypt File ")
    newWindow.geometry("600x600")
    
    lab = Label(newWindow, text='Get Key and Iv to Decrypt Your Image !', width=40, font=("Arial", 15))
    lab.pack(padx =20 ,pady= 10)
    
    keyframe = Frame(newWindow)
    keyframe.pack()

    Ivframe = Frame(newWindow)
    Ivframe.pack()    

    label = Message(keyframe, text='Key:',width=300, font=("Arial"))
    label.pack(padx =5,pady= 3, side=LEFT)

    fileKey= Entry(keyframe,width=200, font=("Arial" ))
    fileKey.pack(padx =5,pady= 3,side=RIGHT)
    
    label = Message(Ivframe, text='Iv:',width=300, font=("Arial"))
    label.pack(padx =5,pady= 3, side=LEFT)
    
    fileIv= Entry(Ivframe,width=200, font=("Arial" ))
    fileIv.pack(padx =5,pady= 3,side=RIGHT)
    
    go = Button(newWindow, text='Get Image', font=("Arial", 10), width=25, command = lambda: decodeI(fileKey.get(),fileIv.get()))
    go.pack()


# A function defined to select a file from file manager.
def browseFiles():
    global file
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("png",
                                                        "*.png*"),
                                                       ("jpg",
                                                        "*.jpg")))
    if filename:
        filePath= os.path.abspath(filename)
        Label(frame, text=str(filePath), width=400, font=("Arial", 15)).pack()
        file=str(filePath)


frame= Frame(root)
frame.pack()

lab = Label(frame, text='SECURE YOUR IMAGE !', width=40, font=("Arial", 15))
lab.pack(padx =20 ,pady= 10)

guide = Label(frame, text='Select image from files you want to secure !', width=40, font=("Arial", 15))
guide.pack(padx =20 ,pady= 10)

buttonframe = Frame(root)
buttonframe.pack(side = BOTTOM)

fileExp= Button(frame, text='Open File manager', font=("Times New Roman", 10) , width=25, command=browseFiles)
fileExp.pack(side = TOP ,padx =20 ,pady= 20)

label = Message(frame, text='Password :',width=300, font=("Arial"))
label.pack(padx =5,pady= 10, side=LEFT)

filePassword = Entry(frame,width=200, font=("Arial" ))
filePassword.pack(padx =10,pady= 10)

# label = Message(frame, text='Change',width=300, font=("Arial"))
# label.pack(padx =5,pady= 10,)

enc = Button(buttonframe, text='Encrypte', font=("Arial", 10) , width=25 ,command=lambda : encodeI(file,filePassword.get()))
enc.pack(side = LEFT ,padx =20 ,pady= 20)

dec = Button(buttonframe, text='Decrypte', font=("Arial", 10), width=25, command = decryptWindow)
dec.pack(side = RIGHT)

root.mainloop()

