D&D Puzzle for The Southern Misfits
===================================

You can view this file natively in Chrome with [the Markdown viewer extension](https://chrome.google.com/webstore/detail/markdown-preview/jmchmkecamhbiokiopfpnfgbidieafmd), though the examples will show best [in GitHub](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/).

## Come up with a new name, guys.

## Context:

You find a sheet of paper on an enemy you've yet to encounter. It says the following:

(Coming Soon)


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
m.encode('this is a key')
>>> [Outputs ciphertext from plaintext using that key]
m.decode('this is a key')
>>> [Outputs plaintext from ciphertext using that key]
m.encode('key','here is a new plaintext')
>>> [Outputs ciphertext from the new plaintext with the given key]
m.encode()
>>> [Ouputs ciphertext using the stored plaintext and stored key]
m.setKey('a new key')
>>> [Saves the key, returns nothing]
m.setMessage('a new message')
>>> [Saves the message, returns nothing]
m.setCipher('123008923')
>>> [Saves the ciphertext, returns nothing]
m.message
>>> [The stored plaintext]
m.cipher
>>> [The stored ciphertext]
m.key
>>> [The stored key]
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
XOX  C U
````
