from Crypto.Cipher import AES
import hashlib
class Crypt:
    def __init__(self): 
        self.pwd = "As you wish" 
        self.password = self.pwd.encode()      
        self.key = hashlib.sha256(self.password).digest()
        self.mode = AES.MODE_CBC
        self.IV = "This is an IV456" 
        self.cipher = AES.new(self.key,self.mode,self.IV)

    def encrypt(self,message):
        padded_message = self.padding(message=message)
        encrypted_msg = self.cipher.encrypt(padded_message)
        return encrypted_msg
        
    
    def padding(self,message):
        print("Length of message is : ",len(message))
        if len(message) % 16 != 0: 
            while len(message) % 16 != 0:
                message = message + "@"
                print("I am in while loop")
            print("padded length in if encryption : ",len(message))
            return message
        else:
            return message
    
    def decrypt(self,msg):
        print("In decryption the length of message is : ",len(msg))
        self.decrypt_msg  = self.cipher.decrypt(msg)
        return self.decrypt_msg





