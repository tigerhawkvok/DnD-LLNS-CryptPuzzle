import math,re,sys
class Message:
    mapping = {
        'A':'01',
        'B':'02',
        'C':'03',
        'D':'04',
        'E':'05',
        'F':'06',
        'G':'07',
        'H':'08',
        'I':'09',
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
    toSym=dict([reversed(i) for i in mapping.items()])
    mapping.update(toSym)

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
        if key is None and self.key is None:
            return "ERROR: No encryption key provided."
        elif not re.match("^[A-Za-z .?]*$", key) and key is not None:
            return "ERROR: Bad encryption key"
        else:
            if key is not None:
                self.key=key.upper()
            try:
                import math
                if message is not None:
                    self.message=message.upper()
                if self.message is not None:
                    # Work with the key
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
                        k+=int(nums[i])
                        #print(numerator,k)
                    exp=math.floor(math.log(k*len(chars),10))
                    denominator=math.pow(10,exp)
                    factor=numerator/denominator
                    #print(numerator,exp,denominator,factor)
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
                    print(q)
                    self.cipher=q
                else:
                    return "ERROR: No message to encrypt"
            except:
                print("Unexpected error:", sys.exc_info())

    def decode(self,key=None,cipher=None):
        if key is None and self.key is None:
            return "ERROR: No decryption key provided."
        elif not re.match("^[A-Za-z .?]*$", key) and key is not None:
            return "ERROR: Bad decryption key"
        else:
            if key is not None:
                self.key=key.upper()
            try:        
                import math
                if cipher is not None:
                    self.cipher=cipher.upper()
                if self.cipher is not None:
                    # Decrypt
                    return
                else:
                    return "ERROR: No ciphertext to decrypt"
            except:
                print("Unexpected error:", sys.exc_info())
