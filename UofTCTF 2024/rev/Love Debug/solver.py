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