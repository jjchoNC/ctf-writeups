## Challenge Description
last time we had a worbler, it failed miserably and left everyone sad, and no one got their flags. now we have another one, maybe it'll work this time?

output:
```
                      _     _             
                     | |   | |            
  __      _____  _ __| |__ | | ___ _ __   
  \ \ /\ / / _ \| '__| '_ \| |/ _ \ '__|  
   \ V  V / (_) | |  | |_) | |  __/ |     
    \_/\_/ \___/|_|  |_.__/|_|\___|_|     
                                          
==========================================
Enter flag: *redacted*
Here's your flag:  a81c0750d48f0750
```
Author: cartoonraccoon

Files : [wobler](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/All%20Worbled%20Up/worbler) [Python Opcodes]

## Solution
Ask your friend (chatGPT) to convert the python opcodes to a normal python code [[chall.py](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/All%20Worbled%20Up/chall.py)].

From the regex pattern 
```py
re_pattern = re.compile('^uoftctf\\{([bdrw013]){9}\\}$')
``` 
we know the flag consists of uoftctf{} which contains 9 characters from "bdrw013" so we can carry out a bruteforce attack using the following script.

[solver.py](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/All%20Worbled%20Up/solver.py)
```py
from itertools import product
import re

re_pattern = '^uoftctf\\{([bdrw013]){9}\\}$'
pattern = re.compile(re_pattern)

def worble(s):
    s1 = 5
    s2 = 31

    for n in range(len(s)):
        s1 = (s1 + ord(s[n]) + 7) % 65521
        s2 = (s1 * s2) % 65521
    return (s2 << 16) | s1

def shmorble(s):
    r = ''
    for i in range(len(s)):
        r += s[len(s) - 1 - i]
    return r

def blorble(a, b):
    return format(a, 'x') + format(b, 'x')

characters = "bdrw013"
all_combinations = [''.join(combination) for combination in product(characters, repeat=9)]
for combination in all_combinations:
    flag = "uoftctf{" + combination + "}"
    if pattern.match(flag):
        a = worble(flag)
        b = worble(flag[::-1])
        c = shmorble(blorble(a, b))
        if c == "a81c0750d48f0750"[::-1]:
            print(flag)
            break
    else:
        print("Incorrect format!")

# Flag = uoftctf{d3w0rb13d}
```



