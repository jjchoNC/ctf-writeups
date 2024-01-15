enc = "瑥⽦䩧㡡倰噕卖䝃捉㉌永敲畴楺癲湊".encode('utf-16be')

import base64
dec = list(base64.b64decode(enc.decode()))
var2 = 1
while var2 <= len(dec):
    var3 = 0
    while var3 < len(dec):
        dec[var3] = (dec[var3] - (var2 - 12) * var3 - 6) & 0xFF
        var3 += 1
    var2 += 1
print(f"uoftctf{{{''.join([chr(i) for i in dec])}}}")

# Flag : uoftctf{%S7rONgadMInPaSSwORd32!%}