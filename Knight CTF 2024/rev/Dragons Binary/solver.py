import gdb
import binascii

gdb.execute("file dragon.binary")
pwdAddr = 0x4019A6
gdb.execute(f"b *{pwdAddr}")
gdb.execute("r")
gdb.execute("si")
flag = gdb.execute("p/s $rax", to_string=True)
print(bytes.fromhex(flag[7:])[::-1])
gdb.execute("q")