# -*- coding: utf-8 -*-
"""

@author: Rohan Sharma
@author: Aditya Shukla

"""
# Importing required libraries
import base64
import pyaes, pbkdf2, binascii, os, secrets

"""
Utility Funcions

"""
# key=0
# iv=0

# Defining a function to encode the given image using the password given by user
def encodeI(fn,pw):
    # global iv,key
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
    print(key)
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
    # print('Encrypted:',(ciphertext))
      
    # Saving the encrypted file.
    with open('image_string.bin', "wb") as file:
        file.write(ciphertext)
        
    """
    Note:  The above saved file is encryted using aes.
    """

    
    
def decodeI(key,iv):
    # global iv,key
    from pathlib import Path
    
    # Reading the encrypted file
    file = open('image_string.bin', 'rb')
    byte = file.read()
    file.close()
    iv = int(iv)
    key=key.encode("raw_unicode_escape")
    # keyM=b''
    # for b in key.split(b'\\'):
    #     keyM=keyM+b+b'\\'
    # print(fr'{keyM}')
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