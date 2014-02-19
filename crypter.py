## D&D Puzzle, Rewilding Campaign
## Initial draft: 2013.10.13, Philip Kahn
## https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle
import math,re
class Message:
    # Consider including numbers in map, newline.
    mapping = {
        'A':'1',
        'B':'2',
        'C':'3',
        'D':'4',
        'E':'5',
        'F':'6',
        'G':'7',
        'H':'8',
        'I':'9',
        'J':'10',
        'K':'11',
        'L':'12',
        'M':'13',
        'N':'14',
        'O':'15',
        'P':'16',
        'Q':'17',
        'R':'18',
        'S':'19',
        'T':'20',
        'U':'21',
        'V':'22',
        'W':'23',
        'X':'24',
        'Y':'25',
        'Z':'26',
        ' ':'27',
        '.':'28',
        '?':'29',
        '-':'30',
        ',':'31',
        '0':'32',
        '1':'33',
        '2':'34',
        '3':'35',
        '4':'36',
        '5':'37',
        '6':'38',
        '7':'39',
        '8':'40',
        '9':'41'
        }
    maplen=len(mapping)
    regex_pattern="^[A-Za-z0-9 .?\-,]*$" # regular expression for valid character set
    regex_hex="^[A-Fa-f0-9]*$"

    def __init__(self,val=None):
        # Initialization of class
        # Do clipboard stuff
        try:
            from pyperclip import pyperclip
            pyperclip.copy('Crytpo Puzzle')
            p=pyperclip.paste()
        except Exception as inst:
            # If we're in Linux, we may need xclip installed
            import os
            try:
                if os.uname()[0] == 'Linux':
                    print('Attempting to install the package xclip ...')
                    os.system('sudo apt-get install xclip')
                    try:
                        from pyperclip import pyperclip
                        pyperclip.copy('Crytpo Puzzle')
                        p=pyperclip.paste()
                    except:
                        print('Could not automatically install xclip. Clipboard functions may not work correctly.')
                else:
                    print('ERROR: Could not enable clipboard functions - ',inst)
            except:
                print('Clipboard functions may not work correctly on your setup')
                try:
                    if os.uname()[0] == 'Linux':
                        print('Please make sure the package "xclip" is installed')
                except: pass
        self.key=None
        try:
            if val is None:
                self.cipher=None
                self.message=None
            else:
                # Message is intialized with any value
                if not re.match(self.regex_hex,val): 
                    self.cipher=None
                    if re.match(self.regex_pattern, val):
                        # Just valid characters
                        self.message=val.upper()
                    else:
                        # Bad input
                        print("Invalid message or ciphertext. Initializing empty object.")
                        self.message=None
                else:
                    # Check padding/encoding
                    if len(val)%3 is 0 or len(val)%5 is 0:
                        self.cipher=val
                        self.message=None
                    else: 
                        # All ciphertext characters are legitimate message characters. 
                        # Probably a mistake, but make it clear to the user and don't assume.
                        print("Invalid ciphertext length. Initializing as a message.")
                        self.cipher=None
                        self.message=val
            print("Ready.")
        except Exception as inst:
            print("UNEXPECTED ERROR: Could not initialize object -",inst)

    def encode(self,key=None,message=None):
        import re
        try:
            if key is None and self.key is None:
                raise Exception("No encryption key provided.")
            elif key is None and self.key is not None:
                key=self.key
            if not re.match(self.regex_pattern, key) and key is not None:
                raise Exception("Bad encryption key")
            else:
                if key is not None:
                    self.key=key.upper()
                if message is not None:
                    if re.match(self.regex_pattern, message):
                        # Just valid characters
                        self.message=message.upper()
                    else:
                        # Bad input
                        print("Invalid message or ciphertext, attempting to use stored value")
                if self.message is not None:
                    factor=self.getFactor()
                    rm=self.rot()
                    mc=list(rm)
                    q=''
                    for c in mc:
                        num=self.mutateLetter(c,factor)
                        q+=num
                    # Deal with the resultant encode
                    self.cipher=q # Store in object
                    print(q) # Display
                    try:
                        from pyperclip import pyperclip
                        pyperclip.copy(q) # Copy to clipboard
                    except Exception:
                        print("The value could not be copied to the clipboard.")
                else:
                    raise Exception("No valid message to encrypt")
        except Exception as inst:
            print("ERROR:", inst)
            return None

    def decode(self,key=None,cipher=None):
        import re
        try:        
            if key is None and self.key is None:
                raise Exception("No decryption key provided.")
            elif key is None and self.key is not None:
                key=self.key
            if not re.match(self.regex_pattern, key) and key is not None:
                raise Exception("Bad decryption key")
            else:
                if key is not None:
                    self.key=key.upper()
                    if cipher is not None and not re.match(self.regex_pattern,key):
                        if len(cipher)%5 is 0:
                            self.cipher=cipher.upper()
                        else:
                            print("Invalid ciphertext length. Attempting to use stored value")
                    elif cipher is not None and not cipher.isdigit():
                        print("Invalid ciphertext. Attempting to use stored value")
                    if self.cipher is not None:
                        # Decrypt
                        factor=self.getFactor()
                        # Bucket the characters in 5
                        cl=list(self.cipher)
                        cb=list()
                        i=1
                        t=''
                        for l in cl:
                            t+=str(l)
                            if i%5 is 0:
                                cb.append(t)
                                t=''
                            i+=1
                        q=''
                        for c in cb:
                            q+=self.mutateLetter(c,factor,False) # rotated inside here
                        self.message=q
                        print(q)
                        try:
                            from pyperclip import pyperclip
                            pyperclip.copy(q) # Copy to clipboard
                        except Exception:
                            print("The value could not be copied to the clipboard.")
                    else:
                        raise Exception("No valid ciphertext to decrypt")
        except Exception as inst:
            print("ERROR:", inst)
            return None


    def getFactor(self):
        # Work with the key
        try:
            if self.key is None:
                raise Exception("No encryption key has been set. Run encode(), decode(), or setKey() with an encryption key first")
            import math
            chars=list(self.key)
            nums=list()
            n=range(len(chars)) # The iterator
            for letter in chars:
                # Difficulty iteration - reduce light dependence on early characters. 
                # This map value needs to be blown up to increase character dependence
                # eg - square, *constant, etc.
                nums.append(self.mapping[letter])
            # Do the math
            numerator=0 # summation holder
            k=0 # second summation holder
            for i in n:
                l=i+1
                # Difficulty iteration - l+=(l^nums[i]) to shift it by bitwise XOR
                # Difficulty iteration - if maplen-l is positive, multiply by it ( weights in other direction)
                numerator+=int(nums[i])*l
                # k+=int(nums[i]) # Difficulty iteration - fold the sum in based on even/odd?
            factor=numerator
            return factor
        except Exception as inst:
            print("ERROR:",inst)
            return None
    
    def rot(self,m=None,n=None):
        # Rotate a message 'm' by 'n'
        try:
            if n is None or str(abs(int(n))).isdigit() is False:
                if m is not None:
                    try:
                        if str(abs(int(m))).isdigit() is True:
                            n=m
                    except TypeError:
                        # abs or something didn't work
                        pass
                else:
                    try:
                        n=len(self.key)
                    except TypeError:
                        # the key hasn't been defined
                        raise Exception("No key has been defined yet, and no rotation size has been provided.")
            else: n=int(n) # just in case
        except Exception as inst:
            print("ERROR: Invalid Rotation Length - ",inst);
            return None
        try:
            if m is not None:
                import re
                if re.match(self.regex_pattern, m):
                    # Just valid characters
                    m=m.upper()
                else:
                    raise Exception("Invalid message text")
            else:
                m=self.message
            chars=list(m)
            rotated=''
            toSym=dict([reversed(i) for i in self.mapping.items()])
            #self.mapping.update(toSym)
            for letter in chars:
                new_num=(int(self.mapping[letter])+n)%self.maplen
                if new_num is 0: new_num=self.maplen
                new_letter=toSym[str(new_num)]
                rotated+=new_letter
            return rotated
        except Exception as inst:
            print("UNEXPECTED ROTATION ERROR:",inst)
            return None
    
    def mutateLetter(self,letter,factor=None,forward=True):
        # Take a letter, and mutate it to the 5-character version
        ## Difficulty iteration -- have the rotation be based on character position in string (defeat frequency)
        ## Difficulty iteration -- round to 1 dec, if %1!=0, double and mod maplen (close matches aren't)
        try:
            if factor is None:
                factor=self.getFactor()
                if factor is None:
                    raise Exception('No factor could be obtained.')
            if forward:
                # Take a letter, get its map, multiply by factor, divide by prime, pad with significand in hex
                # find the biggest prime less than the factor
                letter=letter.upper()
                try:
                    numeric_rep=int(self.mapping[letter])
                except KeyError:
                    raise Exception("Invalid message character '"+letter+"'")
                if str(factor).isdigit() is False: 
                    raise Exception("Bad factor")
                hp=self.getHighestPrime(factor)
                composite=numeric_rep*factor
                import math
                significand=math.floor(composite/hp)
                cipher=composite%hp
                #print('encoding',letter,significand,cipher)
                hsig=hex(significand).split('x')[1]
                hcip=hex(cipher).split('x')[1]
                spad=2-len(hsig)
                cpad=3-len(hcip)
                if cpad is 1: hcip='0'+hcip
                elif cpad is 2: hcip='00'+hcip
                if spad is 1: hsig='0'+hsig
                mutated=hsig+hcip
                return mutated.upper()
            else:
                # undo it!
                import re
                if not re.match(self.regex_hex,letter) or len(letter)%5 is not 0:
                    raise Exception('Invalid cipher character')
                # checked the input, contiue
                significand=int(letter[:2],16)
                cipher=int(letter[2:],16)
                hp=self.getHighestPrime(factor)
                resid=cipher/hp
                frac=significand+resid
                composite=frac*hp
                origmap=str(round(composite/factor)) # rounding errors
                # Now take this digit and remap it to the base characters
                toSym=dict([reversed(i) for i in self.mapping.items()])
                try:
                    q=toSym[origmap]
                    dc=self.rot(q,'-'+str(len(self.key)))
                except KeyError:
                    dc=''
                #print('got',dc,q,'with',factor,hp,letter,frac,composite/factor,'from',origmap)
                return dc
        except Exception as inst:
            print("UNEXPECTED MUTATION ERROR:",inst)
            return None

    def getHighestPrime(self,s=None):
        try:
            if s is None:
                if self.getFactor() is None:
                    raise Exception("No argument provided and no key is set")
                else:
                    s=self.getFactor()
            c1=list()
            ref=list()
            r=range(2,s) # start at 2, lowest prime
            for n in r:
                if n%2 is not 0: 
                    c1.append(n)
            c1.reverse()
            ref=c1
            hprime=s
            for n in ref:
                isPrime=True # default to true, break out if not
                for n2 in c1:
                    if n2 < n: 
                        # only check smaller values
                        if (n/n2)%1 == 0:
                            isPrime=False
                            break
                if isPrime:
                    hprime=n
                    break
            return hprime
        except Exception as inst:
            print("UNEXPECTED PRIME FINDING ERROR:",inst)
            return None

    def setKey(self,key):
            # Manually set the encryption key
            import re
            try:
                if key is None:
                    raise Exception("No encryption key provided.")
                elif not re.match(self.regex_pattern, key) and key is not None:
                    raise Exception("Bad encryption key")
                else:
                    self.key=key.upper()
            except Exception as inst:
                print("ERROR:",inst)
                return None

    def setMessage(self,message):
        # Manually set the message
        try:
            if message is not None:
                import re
                if re.match(self.regex_pattern, message):
                    # Just valid characters
                    self.message=message.upper()
                else:
                    raise Exception("Invalid message text")
            else:
                raise Exception("Message is empty")
        except Exception as inst:
            print("ERROR:",inst)
            return None

    def setCipher(self,cipher):
        # Manually set the cipher
        try:
            if cipher is not None:
                #check if it's a hex
                import re
                if cipher.isdigit():
                    # This has to be first, hex is a subset
                    if len(cipher)%3 is 0:
                        self.cipher=cipher.upper()
                    else:
                        raise Exception("Invalid ciphertext length (dec).")
                elif re.match(self.regex_hex, cipher):
                    if len(cipher)%5 is 0:
                        self.cipher=cipher.upper()
                    else:
                        raise Exception("Invalid ciphertext length (hex).")

                else:
                    raise Exception("Invalid ciphertext. Ciphertext can only have hex numbers (0-9, A-F).")
            else:
                raise Exception("Cipher is empty")
        except Exception as inst:
            print("ERROR:",inst)
            return None

    ## Alternate definitions
    def setcipher(self,*args):
        self.setCipher(*args)
    def setmessage(self,*args):
        self.setMessage(*args)
    def setText(self,*args):
        self.setMessage(*args)
    def settext(self,*args):
        self.setMessage(*args)
    def setkey(self,*args):
        self.setKey(*args)



    ##################################
    # Old Versions for continued use #
    ##################################


    mappingV1 = {
        'A':'1',
        'B':'2',
        'C':'3',
        'D':'4',
        'E':'5',
        'F':'6',
        'G':'7',
        'H':'8',
        'I':'9',
        'J':'10',
        'K':'11',
        'L':'12',
        'M':'13',
        'N':'14',
        'O':'15',
        'P':'16',
        'Q':'17',
        'R':'18',
        'S':'19',
        'T':'20',
        'U':'21',
        'V':'22',
        'W':'23',
        'X':'24',
        'Y':'25',
        'Z':'26',
        ' ':'27',
        '.':'28',
        '?':'29'
        }
    maplenV1=len(mappingV1)

    def getFactorV1(self):
        # Work with the key
        try:
            if self.key is None:
                raise Exception("No encryption key has been set. Run encode(), decode(), or setKey() with an encryption key first")
            import math
            chars=list(self.key)
            nums=list()
            n=range(len(chars)) # The iterator
            for letter in chars:
                nums.append(self.mappingV1[letter])
            # Do the math
            numerator=0 # summation holder
            k=0 # second summation holder
            for i in n:
                l=i+1
                numerator+=int(nums[i])*l
                k+=int(nums[i])
            exp=math.floor(math.log(k*len(chars),10)) 
            denominator=math.pow(10,exp)
            factor=numerator/denominator
            return factor
        except Exception as inst:
            print("ERROR:",inst)
            return None


    def decodeV1(self,key=None,cipher=None):
        import re
        try:        
            if key is None and self.key is None:
                raise Exception("No decryption key provided.")
            elif key is None and self.key is not None:
                key=self.key
            if not re.match(self.regex_pattern, key) and key is not None:
                raise Exception("Bad decryption key")
            else:
                if key is not None:
                    self.key=key.upper()
                    if cipher is not None and cipher.isdigit():
                        if len(cipher)%3 is 0:
                            self.cipher=cipher.upper()
                        else:
                            print("Invalid ciphertext length. Attempting to use stored value")
                    elif cipher is not None and not cipher.isdigit():
                        print("Invalid ciphertext. Attempting to use stored value")
                    if self.cipher is not None:
                        # Decrypt
                        factor=self.getFactorV1()
                        # Bucket the characters in 3
                        cl=list(self.cipher)
                        cb=list()
                        i=1
                        t=''
                        for l in cl:
                            t+=str(l)
                            if i%3 is 0:
                                cb.append(t)
                                t=''
                            i+=1
                        q=''
                        toSym=dict([reversed(i) for i in self.mappingV1.items()])
                        self.mappingV1.update(toSym)
                        for c in cb:
                            try:
                                letter=self.mappingV1[str(int(math.ceil(int(c)/factor)))]
                            except KeyError:
                                # Replace a 'bad' map from a bad key with a blank
                                letter=''
                            q+=letter
                        uq=self.rotV1(q,'-'+str(len(self.key)))
                        print(uq)
                        self.message=uq
                    else:
                        raise Exception("No valid ciphertext to decrypt")
        except Exception as inst:
            print("ERROR:", inst)
            return None

    def rotV1(self,m=None,n=None):
        # Rotate a message 'm' by 'n'
        try:
            if n is None or str(abs(int(n))).isdigit() is False:
                if m is not None:
                    try:
                        if str(abs(int(m))).isdigit() is True:
                            n=m
                    except TypeError:
                        # abs or something didn't work
                        pass
                else:
                    try:
                        n=len(self.key)
                    except TypeError:
                        # the key hasn't been defined
                        raise Exception("No key has been defined yet, and no rotation size has been provided.")
            else: n=int(n) # just in case
        except Exception as inst:
            print("ERROR: Invalid Rotation Length - ",inst);
            return None
        try:
            if m is not None:
                import re
                if re.match(self.regex_pattern, m):
                    # Just valid characters
                    m=m.upper()
                else:
                    raise Exception("Invalid message text")
            else:
                m=self.message
            chars=list(m)
            rotated=''
            toSym=dict([reversed(i) for i in self.mappingV1.items()])
            self.mappingV1.update(toSym)
            for letter in chars:
                new_num=(int(self.mappingV1[letter])+n)%self.maplenV1
                if new_num is 0: new_num=self.maplenV1
                new_letter=self.mappingV1[str(new_num)]
                rotated+=new_letter
            return rotated
        except Exception as inst:
            print("UNEXPECTED ERROR:",inst)
            return None

    def encodeV1(self,key=None,message=None):
        import re
        try:
            if key is None and self.key is None:
                raise Exception("No encryption key provided.")
            elif key is None and self.key is not None:
                key=self.key
            if not re.match("^[A-Za-z .?]*$", key) and key is not None:
                raise Exception("Bad encryption key")
            else:
                if key is not None:
                    self.key=key.upper()
                if message is not None:
                    if re.match(self.regex_pattern, message):
                        # Just valid characters
                        self.message=message.upper()
                    else:
                        # Bad input
                        print("Invalid message or ciphertext, attempting to use stored value")
                if self.message is not None:
                    factor=self.getFactorV1()
                    rm=self.rotV1()
                    mc=list(rm) # self.message)
                    q=''
                    for c in mc:
                        cmap=int(self.mappingV1[c]) # Consider offseting by either message length or key length
                        num=str(int(math.floor(cmap*factor)))
                        if len(num) is not 3:
                            if len(num)==1:
                                num='00'+num
                            else:
                                num='0'+num
                        q+=num
                    self.cipher=q
                    return q
                else:
                    raise Exception("No valid message to encrypt")
        except Exception as inst:
            print("ERROR:", inst)
            return None
