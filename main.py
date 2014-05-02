# Simple wrapper to let them interact at the command prompt
from crypter import Message

def doExit():
    import os,sys
    print("\n")
    os._exit(0)
    sys.exit(0)

# Write some cheats to let codes and decodes and such work without calling the object.

def encode(*args):
    # See if object "m" exists; if so, call m.encode()
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call encode() directly on your object.")
    else:
        m.encode(*args)

def decode(*args):
    # See if object "m" exists; if so, call m.encode()
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call decode() directly on your object.")
    else:
        m.decode(*args)

def setKey(*args):
    # See if object "m" exists; if so, call m.encode()
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call setKey() directly on your object.")
    else:
        m.setKey(*args)

def setCipher(*args):
    # See if object "m" exists; if so, call m.encode()
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call setCipher() directly on your object.")
    else:
        m.setCipher(*args)

def setMessage(*args):
    # See if object "m" exists; if so, call m.encode()
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call setMessage() directly on your object.")
    else:
        m.setMessage(*args)

        
## If it doesn't exist, create a file saving the time as format:
## 2013-10-13T21:02:38Z
## Then compare the time to the time provided at the key "pushed_at" at
## https://api.github.com/repos/tigerhawkvok/DnD-LLNS-CryptPuzzle
try:
    import simplejson as json
    try:
        # Python 2.7.x
        import urllib
        url = urllib.urlopen("https://api.github.com/repos/tigerhawkvok/DnD-LLNS-CryptPuzzle")
        obj_raw = url.read()
        url.close()
    except AttributeError:
        # Python 3
        import urllib.request
        with urllib.request.urlopen("https://api.github.com/repos/tigerhawkvok/DnD-LLNS-CryptPuzzle") as url:
            obj_raw = url.read()
    obj = json.loads(obj_raw)
    time_key = obj['pushed_at']
except Exception as inst:
    print("Warning: Could not check remote version.",inst)
        
import time
try:
    f = open(".gitversion")
    read_seconds = f.read()
    f.close()
    if read_seconds == "":
        raise FileNotFoundError
    push_time = time.strptime(time_key,"%Y-%m-%dT%H:%M:%SZ")
    this_time = time.gmtime(float(read_seconds))
    if push_time > this_time:
        # From https://gist.github.com/tigerhawkvok/9542594
        import yn
        if yn.yn("Your version is out of date with GitHub. Do you want visit GitHub and download a new version?"):
            import os
            try:
                os.unlink(".gitversion")
            except:
                print("Could not delete the version file. Be sure to maually delete '.gitversion' before re-running the new version.")
            print("Launching browser. Rerun the script when you've updated.")
            import webbrowser
            webbrowser.open("https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle")
            doExit()
        else:
            print("Skipping update.")
except NamError:
    # In all likelihood, time_key wasn't defined because of an earlier error
    print("Skipping update process")
except FileNotFoundError:
    # It doesn't exist, so create it
    f = open(".gitversion","w")
    read_seconds = time.time()
    f.write(str(read_seconds))
    f.close()
except Exception as inst:
    print("WARNING: Could not check version.",inst)


print("For use instructions and available commands, please see README.md in the same folder.")
try:
    string=raw_input("Please input the message or ciphertext you'd like to start with for message 'm': ") 
except NameError:
    try:
        string=input("Please input the message or ciphertext you'd like to start with for message 'm': ")
    except KeyboardInterrupt:
        doExit()
except KeyboardInterrupt:
    doExit()
    

m=Message(string)

