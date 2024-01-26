## Challenge Description
If you send this to someone, you'll be *dumped...* unless it's someone who knows a thing or two about reverse engineering...

Side Note: A love letter is what inspired the author to become a hacker.

Author: drec

File  : [love-letter-for-you](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Love%20Debug/love-letter-for-you) [ELF file]

## Solution
In the description above there was the word "dump" in italics, so i thought i should dump something. But first of all, Decompile the given ELF file, from the decompiled code we can see that the program doing somtehing on BYTE array on address 0x406000.

![Decompile](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Love%20Debug/images/image.png) 

![arrayAddr](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Love%20Debug/images/arrayAddr.png) 

Note : Because there is no PIE on the ELF file so the address offset is 0x400000 and not randomized.
```bash
checksec love-letter-for-you

[*] '/mnt/c/Users/acer/Desktop/love-letter-for-you'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
```

So we need to debug this program, in this WU, i prefer to use gdb.
```bash
gdb-gef

GEF for linux ready, type `gef' to start, `gef config' to configure
88 commands loaded and 5 functions added for GDB 12.1 in 0.00ms using Python engine 3.10
gef➤  file love-letter-for-you
Reading symbols from love-letter-for-you...
(No debugging symbols found in love-letter-for-you)
gef➤  r
Starting program: /mnt/c/Users/acer/Desktop/love-letter-for-you

     ❤️❤️❤️❤️❤️❤️       ❤️❤️❤️❤️❤️❤️
   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
 ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️ ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
 ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
   ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
    ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
      ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
        ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
           ❤️❤️❤️❤️❤️❤️❤️
             ❤️❤️❤️
              ❤️

Are you amazed? You like it? Say something!
You're just here for the flag, are you?
```
after the program runs and asks for user input. press ```ctrl + c``` on your keyboard to terminates the action of the program and you'll see like this.

![readAddr](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Love%20Debug/images/readAddr.png)

readAddr = 0x404272

Dump the memory from address ```0x406000 to 0x406000 + arraySize``` then search flag inside that dumped file.

Solver script :

```bash
gdb -x solver.py
```
[solver.py](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Love%20Debug/solver.py) 
```py
import gdb
import re

file = "love-letter-for-you"
with open('temp', 'wb') as f:
    f.write(b'\x03')
gdb.execute("file {}".format(file))
readAddr = 0x404272
gdb.execute(f"b *{readAddr}")
arrayAddr = 0x406000
arraySize = 30000
gdb.execute("r < temp")
gdb.execute(f"dump memory {file}-dump {hex(arrayAddr)} {hex(arrayAddr + arraySize)}")

with open(f"{file}-dump", 'rb') as f:
    dump = f.read().replace(b'\x00', b'')

match = re.search(b'uoftctf{(.+?)}', dump)
print(match.group(0).decode())

gdb.execute("q")

# Flag : uoftctf{r3CuR51v3LY_3nuM3r4Bl3_R1zZ}
```


