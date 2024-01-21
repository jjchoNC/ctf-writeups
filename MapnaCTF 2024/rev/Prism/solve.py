import gdb

gdb.execute("file prism")
gdb.execute("start")
baseAddr = int(gdb.execute("p/a $pc", to_string=True)[5:],16) - 0x30d0
# print(hex(baseAddr))

# Got it by following strlen function call when decompiling the elf file
printFake = 0x31C4
printFlag = 0x3330 
gdb.execute(f"b *{hex(baseAddr + printFake)}")
gdb.execute(f'c')
gdb.execute(f'j *{hex(baseAddr + printFlag)}')
