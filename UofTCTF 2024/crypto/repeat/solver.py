salt = "uoftctf{"
enc = [0x98, 0x2a, 0x92, 0x90, 0xd6, 0xd4, 0xbf, 0x88, 0x95, 0x75, 0x86, 0xbb, 0xdc, 0xda, 0x86, 0x81, 0xde, 0x33, 0xc7, 0x96, 0xc6, 0x91, 0xbb,
       0x9f, 0xde, 0x1a, 0x83, 0xd5, 0x82, 0xc8, 0x86, 0x98, 0x83, 0x75, 0x83, 0x8a, 0xea, 0xd0, 0xe8, 0xc7, 0xdc, 0x2b, 0xc3, 0xd7, 0xcd, 0x97, 0xa4]

def xor(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])

xor_key = [ord(salt[i]) ^ enc[i] for i in range(len(salt))]
dec = xor(enc, xor_key)
print(dec.decode())