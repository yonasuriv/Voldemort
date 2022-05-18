# Voldemort Ransomware

### Disclaimer
This is for educational purposes only. Sure. Learn it, play with it. Go crazy with it, but never, use it for malicious purposes.
Use it at your own risk, altought there will be no risk using it on the default download folder.

## How it works
Voldemort will encrypt ALL files in the same directory where it is. This will exclude folders and it contents, making files it targets only, this can be changed further, altought it's not recomended because it would be more lethal. 

## Encryption and decryption of files
voldemort.py for encryption and potter.py for decryption

Password for decrypting: `yonasuriv`

## FAQ

### Can I protect my code from being read by users?
You must use the right tool to do the right thing, and Python was not designed to be obfuscated. 
It's the contrary; everything is open or easy to reveal or modify in Python because that's the language's philosophy.

If you want something you can't see through, look for another tool or programming language. 
This is not a bad thing, it is important that several different tools exist for different usages.

I made this just to show people how a basic ransomware would look like, that's why I chose python.

Python, being a byte-code-compiled interpreted language, is very difficult to lock down. 
Even if you use a exe-packager like py2exe, the layout of the executable is well-known, and the Python byte-codes are well understood.


And also, if you chose another language... nothing can be protected against reverse engineering. 
Even the firmware on DVD machines has been reverse engineered and the AACS Encryption key exposed. And that's in spite of the DMCA making that a criminal offense.

#### Fun Fact
The method used to encrypt files for ransomware is the same method used by laptop OEM’s among many others to encrypt your entire hard drive and and protect the data in case of theft.
