# Encryptyion-AES
Using AES to encrypt and decrypt . It is the most advanced encryption system. It need a key (given by user.)

# Prerequisites
   # On Linux
    pip3
    python3
    pip3 install hashlib 
    pip3 install pycrypto 
    
   # On windows
    pip or pip
    python3 or python
    pip install hashlib 
    pip install pycrypto
    
# How to Use
  # you can access the code by importing the Crypt Module
    from bitencryption16 import Crypt
  # To Encrypt 
    h = Crypt().encrypt(input("Enter the text : "))
  # To Decrypt 
    n = Crypt().decrypt(h).decode().replace("@","")
  # print the Encrypted text
    print("Encrypted text : ",h)
  # As well As you can print the decrypted text
    print("Decrypted text : ",n)


Contact Me 
Instagram :  https://instagram.com/nothing__2017
