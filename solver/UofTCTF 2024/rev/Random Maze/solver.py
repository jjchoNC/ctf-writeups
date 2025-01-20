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