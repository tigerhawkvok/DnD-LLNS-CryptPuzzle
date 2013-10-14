import math,re,sys
class Message:
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
        '?':'29'
        }

    def __init__(self,val):
        # Initialization of class
        self.key=None
        if val.isdigit() is False: 
            self.cipher=None
            if re.match("^[A-Za-z .?]*$", val):
                # Just valid characters
                self.message=val.upper()
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
                
    def encode(self,key=None,message=None):
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
                    if re.match("^[A-Za-z .?]*$", message):
                        # Just valid characters
                        self.message=message.upper()
                    else:
                        # Bad input
                        print("Invalid message or ciphertext, attempting to use stored value")
                if self.message is not None:
                    factor=self.getFactor()
                    mc=list(self.message)
                    q=''
                    for c in mc:
                        cmap=int(self.mapping[c])
                        num=str(math.floor(cmap*factor))
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

    def decode(self,key=None,cipher=None):
        import re
        try:        
            if key is None and self.key is None:
                raise Exception("No decryption key provided.")
            elif key is None and self.key is not None:
                key=self.key
            if not re.match("^[A-Za-z .?]*$", key) and key is not None:
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
                        factor=self.getFactor()
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
                            #print(t,i,l)
                        #print(cb)
                        q=''
                        toSym=dict([reversed(i) for i in self.mapping.items()])
                        self.mapping.update(toSym)
                        for c in cb:
                            try:
                                letter=self.mapping[str(math.ceil(int(c)/factor))]
                            except KeyError:
                                letter=''
                            q+=letter
                        print(q)
                        self.message=q
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
                nums.append(self.mapping[letter])
            # Do the math
            numerator=0 # summation holder
            k=0 # second summation holder
            for i in n:
                l=i+1
                numerator+=int(nums[i])*l
                #print(nums[i],l,int(nums[i])*l)
                k+=int(nums[i])
            #print(numerator,k)
            exp=math.floor(math.log(k*len(chars),10)) # maybe use "round" instead ... ?
            denominator=math.pow(10,exp)
            factor=numerator/denominator
            return factor
        except Exception as inst:
            print("ERROR:",inst)
            return None

    def setKey(self,key):
            # Manually set the encryption key
            import re
            try:
                if key is None:
                    raise Exception("No encryption key provided.")
                elif not re.match("^[A-Za-z .?]*$", key) and key is not None:
                    raise Exception("Bad encryption key")
                else:
                    self.key=key
            except Exception as inst:
                print("ERROR:",inst)
                return None

    def setMessage(self,message):
            # Manually set the message
            try:
                if message is not None:
                    import re
                    if re.match("^[A-Za-z .?]*$", message):
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
                    if cipher.isdigit():
                        if len(cipher)%3 is 0:
                            self.cipher=cipher.upper()
                        else:
                            raise Exception("Invalid ciphertext length.")
                    else:
                        raise Exception("Invalid ciphertext. Ciphertext can only have numbers.")
                else:
                    raise Exception("Cipher is empty")
            except Exception as inst:
                print("ERROR:",inst)
                return None
