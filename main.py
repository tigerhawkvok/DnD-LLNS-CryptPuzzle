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
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call decode() directly on your object.")
    else:
        m.decode(*args)

def setKey(*args):
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call setKey() directly on your object.")
    else:
        m.setKey(*args)

def setCipher(*args):
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call setCipher() directly on your object.")
    else:
        m.setCipher(*args)

def setMessage(*args):
    try:
        m
    except NameError:
        # Handle the exception
        print("The message object 'm' is not defined. Please call setMessage() directly on your object.")
    else:
        m.setMessage(*args)

def setkey(*args):
    setKey(*args)
def setcipher(*args):
    setCipher(*args)
def setmessage(*args):
    setMessage(*args)

def loadURL(http_addr,header = {}):
    try:
        import urllib
        try:
            # Python 2.7.x
            url = urllib.urlopen(http_addr)
            obj_raw = url.read()
            url.close()
        except AttributeError:
            # Python 3
            import urllib.request
            request = urllib.request.Request(http_addr,None,header)
            with urllib.request.urlopen(request) as url:
                obj_raw = url.read()
    except urllib.error.URLError:
        # Bad url
        print("Bad URL - ",http_addr)
        return False
    except urllib.error.HTTPError as inst:
        print(inst)
        return False
    except Exception as inst:
        print("Unhandled exception getting URL",inst)
        return False
    return obj_raw
    
def loadPuzzle(noteID = None):
    # Load the raw puzzle text as denoted by the id
    # https://developer.github.com/v3/repos/contents/#custom-media-types
    try:
        noteID = float(noteID)
    except ValueError:
        if noteID != "":
            print("Invalid note ID. Reading newest...")
        noteID = None
    except TypeError:
        print("Getting newest note...")
    path = "https://api.github.com/repos/tigerhawkvok/DnD-LLNS-CryptPuzzle/contents/raw/"
    # Get the current list ...
    listing_byte = loadURL(path)
    if listing_byte is False:
        print("Unable to load note.")
        return False
    listing = listing_byte.decode("utf-8")
    try:
        import simplejson as json
    except ImportError:
        import json
    l = json.loads(listing)
    newest = 0
    newest_name = None
    puzzle_name = None
    for f in l:
        if noteID is not None:
            try:
                if noteID == float(f['name']):
                    puzzle_name = f['name']
                    print("Found puzzle",puzzle_name)
                    break
            except:
                pass
        try:
            if float(f['name']) > newest:
                newest = float(f['name'])
                newest_name = f['name']
        except:
            pass
    if puzzle_name is None:
        puzzle_name = newest_name
        print("Loading Note #",puzzle_name)
    # https://developer.github.com/v3/media/
    api_version = "v3"
    media_type = " application/vnd.github."+api_version+".raw+json"
    header = {"Accept":media_type}
    file_path = path+puzzle_name
    obj_raw = loadURL(file_path,header)
    # It's a bytestream, translate:
    text = obj_raw.decode("utf-8")
    # Strip new lines -- remove this when new lines are handled better.
    output = text.replace("\n","")
    return output

def getPuzzle(noteID = None):
    string = loadPuzzle(noteID)
    from crypter import Message
    global m
    try:
        # Assign if possible ..
        m = Message(string)
    except NameError:
        # Otherwise, return it
        return Message(string)
    

######################
## Main Loop
######################

## If it doesn't exist, create a file saving the time as format:
## 2013-10-13T21:02:38Z
## Then compare the time to the time provided at the key "pushed_at" at
## https://api.github.com/repos/tigerhawkvok/DnD-LLNS-CryptPuzzle
try:
    try:
        import simplejson as json
    except ImportError:
        import json
    obj_raw = loadURL("https://api.github.com/repos/tigerhawkvok/DnD-LLNS-CryptPuzzle/releases")
    if obj_raw is False:
        raise Exception()
    try:
        # This just works with the simplejson library
        obj = json.loads(obj_raw)
    except TypeError:
        # Do the conversion otherwise
        obj_raw = obj_raw.decode("utf-8")
        obj = json.loads(obj_raw)[0]
    try:
        time_key = obj['published_at']
        title = obj['tag_name']+" - "+obj['name']
    except TypeError:
        obj = obj[0]
        time_key = obj['published_at']
        title = obj['tag_name']+" - "+obj['name']
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
        print("New version available!")
        print(title)
        if yn.yn("Your version is out of date with GitHub. Do you want visit GitHub and download a new version?"):
            import os
            try:
                os.unlink(".gitversion")
            except:
                print("Could not delete the version file. Be sure to maually delete '.gitversion' before re-running the new version.")
            print("Launching browser. Rerun the script when you've updated.")
            import webbrowser
            # Can probably download this ...
            webbrowser.open("https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/releases")
            doExit()
        else:
            print("Skipping update.")
except NameError:
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
    print("The current version is ",title)


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

if string[:10] == "getPuzzle(":
    n = string[10:-1]
    m = None
    getPuzzle(n)
else:
    m=Message(string)
