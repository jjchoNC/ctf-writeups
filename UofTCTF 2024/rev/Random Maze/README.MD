## Challenge Description
a little maze for you! just don't get lost! :3 remember, if you end up somewhere that doesn't look right, it probably isn't!

free hint: the entire flag is lower-alphanumeric ASCII.

Author: cartoonraccoon

File  : [maze](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Random%20Maze/maze) [ELF file]

## Solution
Decompile the given executeable. In the main function, you'll find a first input filtering method.

![pass1](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Random%20Maze/images/pass1.png)

From that lines, we know that the user input must be bigger or equal than 19 and lower than 100 (in ASCII). Each character in inputs also must not be a multiple of 3 [a == 3 * (a / 3)] and 4 [a & 3 != 0]

![pass2](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Random%20Maze/images/pass2.png)

flag[] = "ON#X~o8&" [Encrypted]

sum[] = [0x0CE, 0x0A1, 0x0AE, 0x0AD, 0x64, 0x9F, 0x0D5]

Exploring further (inside traverse function), we will find encryption and flag checker methods. From that lines, we know that the ```input[0] xor flag[0]``` must be a prime number and ```input[i] xor flag[i] + input[i -1] xor flag[i - 1]``` must be equal to ```sum[i - 1]```. So we first need to look for the first character in the input that meets the conditions. To make it easier i use the script below.

[solver.py](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF%202024/rev/Random%20Maze/solver.py)
```py
from Crypto.Util.number import isPrime

enc_flag = "ON#X~o8&"
enc_sum = [0x0CE, 0x0A1, 0x0AE, 0x0AD, 0x64, 0x9F, 0x0D5]
idx = 0
list_prime = [i for i in range(19, 100) if (isPrime(ord(enc_flag[0]) ^ i) and i & 3 != 0 and i//3 != i/3)]
list_salt = []
for i in list_prime:
    list_salt.append(ord(enc_flag[0]) ^ i)

for i in list_salt:
    cr = i
    str = ''
    for j in enc_sum:
        str += chr(abs(cr - j))
        cr = abs(cr - j)
    if str.isalnum() and str.islower():
        print(f"uoftctf{{{chr(i)}{str}}}")
    idx += 1

## Flag = uoftctf{am4z31ng}
```

