D&D Puzzle for The Southern Misfits
===================================

You can view this file natively in Chrome with [the Markdown viewer extension](https://chrome.google.com/webstore/detail/markdown-preview/jmchmkecamhbiokiopfpnfgbidieafmd), though the examples will show best [in GitHub](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/).

## Come up with a new party name, guys.
Or you're to be "The Southern Misfits". ;-)

## Context:

You find a sheet of paper on an enemy you've yet to encounter. It says the following:

> **Practice ciphers!**  
>  
> From demo --  
> 'dog'  
> Key 'a' -> 004015007    
> Key 'dog' -> 022082038  
> Let's try it ... key 'dog'  
> dog=4,15,7 -> 4\*1+15\*2+7\*3 = <span style='text-decoration:line-through'>52</span> 55  
> 4+15+7=26 \*3= <span style='text-deocration:line-through'>81</span> 78
>  
> *what the fuck is a log?*  
> log<sub>10</sub>(k\*10<sup>n</sup>) = log<sub>10</sub>(k/10)+n+1 <-- what's that small 10 for?  
> apparently the first thing is about:  
> 1-x=k/10 -> 10-10x=k -> 10-k = 10x -> **1-k/10 = x**
>  
> So the whole thing is   
> -( (1-k/10) + (1-k/10)<sup>2</sup>/2 + (1-k/10)<sup>3</sup>/3 )\*.4343 + n + 1<-- the bastards
>  
> 78=7.8\*10<sup>1</sup> so k=7.8 and n=1  
> -( (1-.78) + (1-.78)<sup>2</sup>/2 + (1-.78)<sup>3</sup>/3 )\*.4343 + 1 + 1 =  
> -(.22+.22<sup>2</sup>/2 + .22<sup>3</sup>/3)\.4343 + 2 =  
> 2-0.248\*0.4343=2-.108=1.89, now round it down --> 1  
> 10<sup>1</sup>=10 so 55/10=5.5 <-- I hate math  
> so factor = 5.5.  
> 4\*5.5=22, 15\*5.5=82.5, 7\*5.5 = 38.5  
> Round down, make 3 numbers  
> **022 082 038** <-- Success!  
> Key a?  
> 1\*1=1, 1=1\*10<sup>0</sup>, so -( .9+.9<sup>2</sup>/2+.9<sup>3</sup>/3)\*.4343+0+1 = 1-.67=0.32 -> 0  
> So 10<sup>0</sup>=1 so 1/1=1 so **004 015 007** <-- haha! maybe I can do math
>  
> Remember space is 27, period 28, question 29.
>  
> Memo: remember the elder everlasting  
>  
> Test for real:  
> 'dog' with real key is --> 007028013  
> 'ercrain' with real key is --> 009034005034001017026  
> Draft message:  
> 043009051030022001026051037028051015017037051037015009051009026005022001041009036  
> 043009051043017022022051001037037001005020051028026051024017007036039024024009034036051009041009  
> 017037051017036051017024030028034037001026037051037028051037015009017034051030022001026036053051007028051026028037051011001017022053


He also has one other sheet of paper on him. It's far less marked up and much more succinct.

> The younger as he is  
> 020046062052020027027062004011062009034032011064

## Help
There is a lot of help built in to this. Nevertheless, you can text me with one INT check per day, and I'll give you hints if it's good enough.

This is hard puzzle -- even *very* hard. It is worth up to 6000 experience, depending on the speed of solution, number of hints, etc.

## Using this

This program is written to make it easy for you to test your hunches and play with your ciphers. First, install Python:

### Windows

- [Python 3, x86](http://python.org/ftp/python/3.3.2/python-3.3.2.msi)
- [Python 3, x64](http://python.org/ftp/python/3.3.2/python-3.3.2.amd64.msi)

### OSX

- [Python 3, Intel](http://python.org/ftp/python/3.3.2/python-3.3.2-macosx10.6.dmg)
- [Python 3, PowerPC](http://python.org/ftp/python/3.3.2/python-3.3.2-macosx10.5.dmg)

### Linux

- [Python 3, Linux](http://python.org/ftp/python/3.3.2/Python-3.3.2.tar.xz)
- On Ubuntu / Debian, you can run `sudo apt-get install python3` in Terminal.

Then, just run the appropriate `runme` file in the downloaded package.

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
````

So, for example:

````python
>>> m.setKey('daria risaley imsh tiss')
>>> m.setMessage('Hello this is a string')
>>> m.encode()
'034021051051064116086034038081116038081116004116081086077038060030'
>>> m.decode()
HELLO THIS IS A STRING
>>> m.decode('different key')
 Q DX
>>> m.key
'DIFFERENT KEY'
>>> m.cipher
'034021051051064116086034038081116038081116004116081086077038060030'
>>> m.decode('daria risaley imsh tiss')
HELLO THIS IS A STRING
````
