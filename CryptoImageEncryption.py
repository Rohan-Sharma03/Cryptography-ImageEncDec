# -*- coding: utf-8 -*-
"""
Submitting as project of Mid-Term I for Cryptograhy Course.

@author: Rohan Sharma
@author: Aditya Shukla 

"""
key=0
iv=0
# Importing required libraries

import base64
import pyaes, pbkdf2, binascii, os, secrets
from tkinter import *
from tkinter import filedialog
import os


# Defining new window as root 

root = Tk(className=" Image Encryptor and Decryptor")
root.geometry("700x700")
root.minsize(700,700)

#  A global variable used to hold file path.

file=""

"""
Utility Funcions

"""

# Defining a function to encode the given image using the password given by user

def displayCredential():
    newWindow1 = Toplevel(root)
    newWindow1.title("key and IV values")
    newWindow1.geometry("600x600")
    
    lab = Label(newWindow1, text='Keep them Safe', width=40, font=("Arial", 15))
    lab.pack(padx =20 ,pady= 10)
    
    keyframe = Frame(newWindow1)
    keyframe.pack()

    Ivframe = Frame(newWindow1)
    Ivframe.pack()    

    label = Message(keyframe, text=bytes(str(key),'utf-8'),width=300, font=("Arial"))
    label.pack(padx =5,pady= 3, side=LEFT)
    
    label = Message(Ivframe, text=iv,width=300, font=("Arial"))
    label.pack(padx =5,pady= 3, side=LEFT)
    
def encodeI(fn,pw):
    global key,iv
    print(fn)
    print(pw)
    
    # open the selected image as string
    with open(fn, "rb") as image2string:
        # transforming the string to base64 encodeing.
        converted_string = base64.b64encode(image2string.read())
    # print(type(converted_string))
    plain_text = converted_string
    
    # Derive a 256-bit AES encryption key from the password given by user
    password = pw
    passwordSalt = os.urandom(128)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(16)
    # print('AES encryption key:', binascii.hexlify(key))
    
    # Defining a iv which ensure the unique encryption everytime a file is encrypted
    iv = secrets.randbits(256)
    
    # Running aes on the base 64 encoded string to encrypte it with the password given.
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plain_text)

    # print(base64.b64encode(ciphertext))
    # ciphertext=base64.b64encode(ciphertext)
    
    print(key,'\n')
    print(iv)
    print(type(key),'\n')
    print(type(iv))
    displayCredential()
    # Saving the encrypted file.
    with open('image_string.bin', "wb") as file:
        file.write(ciphertext)
        
    """
    Note:  The above saved file is encryted using aes.
    """
    
       
def decodeI(key,iv):
    from pathlib import Path
    # Reading the encrypted file
    file = open('image_string.bin', 'rb')
    byte = file.read()
    file.close()
    # Transforming str value of iv to int
    iv=int(iv)
    # Transforming str values of key to bytes to obatin get extra back-slash (\) and converting it again to str
    key = str(bytes(str(key),'utf-8'))
    # Truncating the b and ' ' commans form the key
    key=key[2:-1]
    #  Removing the extra back-slash (\) from byte object
    key=key.encode().decode('unicode_escape').encode("raw_unicode_escape").decode('unicode_escape').encode('raw_unicode_escape')
    
    print(key,'\n')
    print(iv)
    print(type(key),'\n')
    print(type(iv))
    
    # Creating the aes object, which will be used to decrypte the encrpted file.
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    
    decrypted = aes.decrypt(byte)
    
    # # print(decrypted)
    
    # decodeing to orignal image file from the output obtained from the aes decryted object.
    # print(base64.b64decode((decrypted)))
    
    # Saving the image to download section of the file.
    downloads_path = str(Path.home() /"Downloads")
    print(downloads_path)
    save=downloads_path+'\image4.jpeg'
    decodeit = open(r''+save, 'wb')
    decodeit.write(base64.b64decode((decrypted)))
    decodeit.close()


 
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


enc = Button(buttonframe, text='Encrypte', font=("Arial", 10) , width=25 ,command=lambda : encodeI(file,filePassword.get()))
enc.pack(side = LEFT ,padx =20 ,pady= 20)

dec = Button(buttonframe, text='Decrypte', font=("Arial", 10), width=25, command = decryptWindow)
dec.pack(side = RIGHT)

root.mainloop()



