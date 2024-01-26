## Challenge Description

I'm a known repeat offender when it comes to bad encryption habits. But the secrets module is secure, so you'll never be able to guess my key!

Author: SteakEnthusiast

**gen.py**
```py
import os
import secrets

flag = "REDACATED"
xor_key = secrets.token_bytes(8)
print(xor_key)

def xor(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])

encrypted_flag = xor(flag.encode(), xor_key).hex()
print(encrypted_flag)
```
**flag.enc**
```
982a9290d6d4bf88957586bbdcda8681de33c796c691bb9fde1a83d582c886988375838aead0e8c7dc2bc3d7cd97a4
```

## Solve
From the gen.py we know that the ```xor_key``` is a **8 random bytes**. The ```xor_key``` is used repeatedly to encrypt (xor encrypt) the flag. So we can recover the ```xor_key``` if we know the first 8 bytes of the plaintext/flag. Keep in mind that, the first 8 bytes of the flag are "uoftctf{" which is the flag format.

Solver : 
```py
salt = "uoftctf{"
enc = [0x98, 0x2a, 0x92, 0x90, 0xd6, 0xd4, 0xbf, 0x88, 0x95, 0x75, 0x86, 0xbb, 0xdc, 0xda, 0x86, 0x81, 0xde, 0x33, 0xc7, 0x96, 0xc6, 0x91, 0xbb,
       0x9f, 0xde, 0x1a, 0x83, 0xd5, 0x82, 0xc8, 0x86, 0x98, 0x83, 0x75, 0x83, 0x8a, 0xea, 0xd0, 0xe8, 0xc7, 0xdc, 0x2b, 0xc3, 0xd7, 0xcd, 0x97, 0xa4]

def xor(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])

xor_key = [ord(salt[i]) ^ enc[i] for i in range(len(salt))]
dec = xor(enc, xor_key)
print(dec.decode())
# Flag : uoftctf{x0r_iz_r3v3rs1bl3_w17h_kn0wn_p141n73x7}
```