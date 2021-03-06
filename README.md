D&D Puzzle for The Southern Misfits
===================================

## New Function!

I've made life easy for you guys. If you want to load a specific puzzle version, when the message is asked to be input, just input `getPuzzle(NUMBER)`, where `NUMBER` is the number of the puzzle. For multipart puzzles, the subsequent parts are like "2.1" or "1.1".

If you want to load the newest puzzle, it's easier still. Just input `getPuzzle()`:

<!-- Image -->
<img src="https://raw.githubusercontent.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/master/helper/getpuzz_samp.png" alt="Sample Screenshot" style="text-align:center;margin:0 auto"/>

## Cross-Platform issues

I've tried to add a cross-platform implementation of `getch()`. It should work, but if it doesn't, let me know or [update the code on this Gist](https://gist.github.com/tigerhawkvok/9542594), and [instead download the code from this commit](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/tree/d08dc656150ebec2bb1c340b581e54e960d515d3).

## Introduction

The use of this cipher will slowly morph over time as the creators "improve" their algorithm, or if they suspect that you guys have broken it, but [the old behaviour is still accessible](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle#using-old-versions-of-the-program). You can [download the current version here](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/archive/master.zip).

Good local `*.md` viewer is [MarkView for Chrome](https://chrome.google.com/webstore/detail/markview/iaddkimmopgchbbnmfmdcophmlnghkim) which parses "Github-Flavored Markdown", unlike the last one I linked.

## Story Context

### Current Message

The most recent result was given to you by Clathar at the Western Enclave, found on a large bird that was *Magic Missile*d down by a low level scout under his command. [You can read it here.](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/blob/master/Note3.md)


### Part 1 Puzzles

[Part 1 decrypted puzzles](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/blob/master/Part1_Decrypted.md)

#### Ercrain's Note (Puzzle 1)

Here is the original puzzle, which is the second note you found (in Ercrain's room): [Note1.md](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/blob/master/Note1.md)

You can find the original context, and latest original version [over here in the history](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/tree/aaf57a871fcea402a9fbe1a313d51dbc8b65ddf5). It'll be helpful if you need a refresher.

#### Message to Ercrain re: Akresh, Skozzin (Puzzle 2)

Here is the second puzzle, or the first one you found: [Note2.md](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/blob/master/Note2.md)


## Help
### Using old versions of the program

You can use the old `encode()` and `decode()` functions by calling `encodeV1()` and `decodeV1()`. Similarly, the old factor generation is there with `getFactorV1()`, and also V2 equivalents (`encodeV1()`, `decodeV2()`, and `getFactorV2()`).

Thus, to borrow from the old example:

```python
>>> m.setKey('daria risaley imsh tiss')
>>> m.setMessage('Hello this is a string')
>>> m.encodeV1()
'008120025025038090060008012055090012055090103090055060051012034004'
>>> m.decodeV1()
HELLO THIS IS A STRING
>>>m.decode()
MZ3ZIZU # whoops! Obviously different
>>> m.getFactorV1()
4.304
```


### Rolls for hints
You can text me with one INT check per day, and I'll give you hints if it's good enough. The [example at the bottom](https://github.com/tigerhawkvok/DnD-LLNS-CryptPuzzle#executing-and-using-the-program) is itself always a hint, too.

### XP
Think of this as your version of [Xykon's Moderately-Escapable Forcecage](http://www.giantitp.com/comics/oots0376.html). It's always going to be possible, but hard. The XP I'll determine based on the iteration, how many you've previoussly broken, iteration difficulty, etc. You can be pretty sure that it'll always be >=1k XP.

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

> ##### Aside for OSX
>
> OSX doesn't let you have an executable batch file by default. So, the first time you launch, you'll need to run 
>
> `sudo chmod 0777 runme-osx.command`
> 
> at the terminal, like so:
>
> <img src="https://raw.githubusercontent.com/tigerhawkvok/DnD-LLNS-CryptPuzzle/master/helper/45ec4abd3e03300ee552718b48e1821a.png" alt="Sample Screenshot" style="text-align:center;margin:0 auto"/>
>
> Once you do, it'll execute just fine, either by double-clicking or manually running the `runme-osx.command` file from the terminal.

When you run the program, the following commands are available to you:

````python
>>> m.encode('this is a key')
# Outputs ciphertext from plaintext using that key
>>> m.decode('this is a key')
# Outputs plaintext from ciphertext using that key
>>> m.encode('key','here is a new plaintext')
# Outputs ciphertext from the new plaintext with the given key
>>> m.encode()
>>> encode()
# Ouputs ciphertext using the stored plaintext and stored key
# You can cheat and encode and decode on the default object 'm' without using it
>>> m.setKey('a new key')
# Saves the key, returns nothing
>>> m.setMessage('a new message')
# Saves the message, returns nothing
>>> m.setCipher('1230089D23')
# Saves the ciphertext, returns nothing
>>> m.message
# The stored plaintext
>>> m.cipher
# The stored ciphertext
>>> m.key
# The stored key
>>> bob=Message('test message')
# A new object, 'bob', that behaves the same as 'm' above. Initialized with message 'test message'.
>>> sally=Message('0A001D11234')
# A new object, 'sally', that behaves as 'bob' and 'm' above, initialized with a ciphertext.
>>> q=Message()
# A new object, 'q', initialized blankly. Behaves as 'bob', 'sally', and 'm' above.
````

So, for example:

```python
>>> m.setKey('daria risaley imsh tiss')
>>> m.setMessage('Hello this is a string')
>>> m.encode()
'1F0D91C0C4230F5230F52610A0903F0200E1F0D9200E0010070903F200E0010070903F180A80903F010070200E2911F200E0251031E0D2'
>>> m.decode()
'HELLO THIS IS A STRING'
>>> m.decode('different key')
'ROVVY5-RS?5S?5K5?-.SXQ'
>>> m.key
'DIFFERENT KEY' # The different key you just used is stored
>>> m.cipher
'1F0D91C0C4230F5230F52610A0903F0200E1F0D9200E0010070903F200E0010070903F180A80903F010070200E2911F200E0251031E0D2' # The cipher is unchanged
>>> m.decode('daria risaley imsh tiss')
HELLO THIS IS A STRING # It still recovers
```
