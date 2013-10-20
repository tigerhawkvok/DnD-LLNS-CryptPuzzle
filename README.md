D&D Puzzle for The Southern Misfits
===================================

You can view this file natively in Chrome with [the Markdown viewer extension](https://chrome.google.com/webstore/detail/markdown-preview/jmchmkecamhbiokiopfpnfgbidieafmd), though the examples will show best [in GitHub](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/).

The easiest way for you to do this will be to [download the files](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/archive/master.zip) into a directory via the "download" link to your right.

## Come up with a new party name, guys.
Or you're to be "The Southern Misfits"!

## Story Context

You find a sheet of paper on an enemy you've yet to encounter. It says the following:

> **Practice ciphers!**  
>  
> From demo --  
> 'dog'  
> Key 'a' -> 004015007    
> Key 'dog' -> 0380999055  
> Let's try it ... key 'dog'  
> dog=4,15,7 -> 4\*1+15\*2+7\*3 = <span style='text-decoration:line-through'>52</span> 55  
> 4+15+7=26 \*3= <span style='text-deocration:line-through'>81</span> 78
>  
> *what the fuck is a log?*  
> log<sub>10</sub>(k\*10<sup>n</sup>) = log<sub>10</sub>(k/10)+n+1 <-- what's that small 10 for?  
> apparently the first thing is about:  
> 1-x=k/10 -> 10-10x=k -> 10-k = 10x -> **1-k/10 = x**
>  
>> So the whole 'log' thing is   
>> -( (1-k/10) + (1-k/10)<sup>2</sup>/2 + (1-k/10)<sup>3</sup>/3 )\*.4343 + n + 1<-- the bastards
>  
> 78=7.8\*10<sup>1</sup> so k=7.8 and n=1  
> -( (1-.78) + (1-.78)<sup>2</sup>/2 + (1-.78)<sup>3</sup>/3 )\*.4343 + 1 + 1 =  
> -(.22+.22<sup>2</sup>/2 + .22<sup>3</sup>/3)\*.4343 + 2 =  
> 2-0.248\*0.4343=2-.108=1.89, now round it down --> 1  
> 10<sup>1</sup>=10 so 55/10=5.5 <-- I hate math  
> so factor = 5.5.
> Rotate the letters by the length of the key = 3. *Remember to wrap around if it goes around*
> (4+3)\*5.5=38.5, (15+3)\*5.5=99, (7+3)\*5.5 = 55  
> Round down, make 3 numbers  
> **038 099 055** <-- Success!  
> Key a?  
> 1\*1=1, 1=1\*10<sup>0</sup>, so -( .9+.9<sup>2</sup>/2+.9<sup>3</sup>/3)\*.4343+0+1 = 1-.67=0.32 -> 0  
> So 10<sup>0</sup>=1 so 1/1=1 so (4+1)\*1, (15+1)\*1, (7+1)\*1 --> **005 016 008** <-- haha! maybe I can do math
>  
> Remember space is 27, period 28, question 29.
>  
> Memo: remember the elder everlasting  
>  
> Test for real:  
> 'dog' with real key is --> 037003043  
> 'ercrain' with real key is --> 039009036009032047001  
> Draft message:  
>> 018039026005053032001026013003026045047013026013045039026039001036053032017039011  
>> 018039026018047053053026032013013032036051026003001026054047037011015054054039009011026039017039  
>> 047013026047011026047054005003009013032001013026013003026013045039047009026005053032001011028026037003026001003013026041032047053028


He also has one other sheet of paper on him. It's far less marked up and much more succinct.


> The younger as he is  
> 064023039029064004004039048055039052011009055041

## Help
There is a lot of help built in to this. Nevertheless, you can text me with one INT check per day, and I'll give you hints if it's good enough.

This is hard puzzle -- even *very* hard. It is worth up to 7000 experience, depending on the speed of solution, number of hints, etc. Think of this as your version of [Xykon's Moderately-Escapable Forcecage](http://www.giantitp.com/comics/oots0376.html). (Max XP for the first part is 4000, max XP for the second part is 3000)

Please note you're welcome to read the source code. The algorithm is given above in a fun, story way that's probably more doable and parseable in your heads, but if the code works for you have at it. The difficulty of this assumes you have access to the algorithm. You don't strictly need it (there are plain flaws built into the crypto that should let you decipher the text with virtually no knowledge), but it'll help.

## Using this

This program is written to make it easy for you to test your hunches and play with your ciphers. First, install Python:

### Windows

- [Python 3, x86](http://python.org/ftp/python/3.3.2/python-3.3.2.msi)
- [Python 3, x64](http://python.org/ftp/python/3.3.2/python-3.3.2.amd64.msi)
- Don't change the install path, or, if you do (or just for easier launching) [add Python to your $PATH](http://docs.python.org/2/using/windows.html#setting-envvars)

### *Nix
#### OSX

- [Python 3, Intel](http://python.org/ftp/python/3.3.2/python-3.3.2-macosx10.6.dmg)
- [Python 3, PowerPC](http://python.org/ftp/python/3.3.2/python-3.3.2-macosx10.5.dmg)

#### Linux

- [Python 3, Linux](http://python.org/ftp/python/3.3.2/Python-3.3.2.tar.xz)
- On Ubuntu / Debian, you can run `sudo apt-get install python3` in Terminal.
- In Red Hat based distros, or some others, you may use `yum`. 

### Running it

#### Definitions
First, a note on definitions: in encryption, the human-readable normal stuff is called [plaintext](https://en.wikipedia.org/wiki/Plaintext), "cleartext", or the "message". That's exactly what it sounds like.

After it's been run through the encryption protocol, you have a mash that's generally unreadable. That's called the [ciphertext](https://en.wikipedia.org/wiki/Ciphertext). 

#### Executing and using the program
To run the program, just run the appropriate `runme` file in the downloaded package.

**If you have problems on OSX** - navigate to the directory with the files in Terminal, and run `./runme-linux.sh`, which should work fine.

When you run the program, the following commands are available to you:

````python
>>> m.encode('this is a key')
# Outputs ciphertext from plaintext using that key
>>> m.decode('this is a key')
# Outputs plaintext from ciphertext using that key
>>> m.encode('key','here is a new plaintext')
# Outputs ciphertext from the new plaintext with the given key
>>> m.encode()
# Ouputs ciphertext using the stored plaintext and stored key
>>> m.setKey('a new key')
# Saves the key, returns nothing
>>> m.setMessage('a new message')
# Saves the message, returns nothing
>>> m.setCipher('123008923')
# Saves the ciphertext, returns nothing
>>> m.message
# The stored plaintext
>>> m.cipher
# The stored ciphertext
>>> m.key
# The stored key
>>> bob=Message('test message')
# A new object, 'bob', that behaves the same as 'm' above. Initialized with message 'test message'.
>>> sally=Message('001234')
# A new object, 'sally', that behaves as 'bob' and 'm' above, initialized with a ciphertext.
>>> q=Message()
# A new object, 'q', initialized blankly. Behaves as 'bob', 'sally', and 'm' above.
````

So, for example:

````python
>>> m.setKey('daria risaley imsh tiss')
>>> m.setMessage('Hello this is a string')
>>> m.encode()
'008120025025038090060008012055090012055090103090055060051012034004'
>>> m.decode()
HELLO THIS IS A STRING
>>> m.decode('different key')
WGGWZZZNT
>>> m.key
'DIFFERENT KEY' # The different key you just used is stored
>>> m.cipher
'008120025025038090060008012055090012055090103090055060051012034004' # The cipher is unchanged
>>> m.decode('daria risaley imsh tiss')
HELLO THIS IS A STRING # It still recovers
````
