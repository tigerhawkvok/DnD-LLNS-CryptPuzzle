import math,re

class Message:
    def __init__(self,val):
        # Initialization of class
        if val.isdigit() is False: 
            self.cipher=None
            if re.match("^[A-Za-z .?]*$", val):
                # Just valid characters
                self.message=val
            else:
                # Bad input
                print("Invalid message or ciphertext")
                self.message=None
        else:
            # Just digits
            self.message=None
            # Check padding/encoding
            if len(val)%3 is 0:
                self.cipher=val
            else: 
                # Bad input
                print("Invalid message or ciphertext.")
                self.cipher=None
                
    def encode(self,key=None,*args):
        if key is None:
            return "ERROR: No encryption key provided."
        else:
            try:
                print("Continuing")
            except:
                print("Unexpected error:", sys.exc_info()[0])
