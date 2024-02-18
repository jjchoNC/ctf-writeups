import gdb
from Crypto.Util.number import long_to_bytes

gdb.execute("file minimax")
gdb.execute("start")
baseAddr = int(gdb.execute("p/a $pc", to_string=True)[5:19],16) - 0x0000000000001F37
checkWin = baseAddr + 0x2049
gdb.execute(f"b *{hex(checkWin)}")
gdb.execute(f"c")
gdb.execute(f"set $eax = 0x1")
getHex = baseAddr + 0x1577
gdb.execute(f"b *{hex(getHex)}")
gdb.execute(f"c")
val1 = gdb.execute("x/s $rax", to_string=True).strip().split("\t")[1].strip('"')
val2 = gdb.execute("x/gx $rbp-0x90", to_string=True).strip().split("\t")[1].strip('"')
val3 = gdb.execute("x/gx $rbp-0x88", to_string=True).strip().split("\t")[1].strip('"')
gdb.execute(f"shell clear")
print(long_to_bytes(int(val1, 16) * int(val2,16) * int(val3,16)).decode())