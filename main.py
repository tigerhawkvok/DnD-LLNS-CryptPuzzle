# Simple wrapper to let them interact at the command prompt
from crypter import Message

print("For use instructions and available commands, please see README.md in the same folder.")
try: string=raw_input("Please input the message or ciphertext you'd like to start with for message 'm': ") 
except NameError: string=input("Please input the message or ciphertext you'd like to start with for message 'm': ")

m=Message(string)

