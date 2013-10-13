# Simple wrapper to let them interact at the command prompt
from crypter import Message

print("For use instructions, please see README.md in the same folder.")
try: string=raw_input("Please input the message you'd like to start with: ") 
except NameError: string=input("Please input the message you'd like to start with: ")

m=Message(string)
print("You can now use the command as referenced in README.md to test the message 'm'.")

