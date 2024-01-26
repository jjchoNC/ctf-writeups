import gdb

checkAddr = 0x401A86
gdb.execute("file knight_armoury")
gdb.execute(f"""b *{checkAddr}""")
gdb.execute("r < knight_armoury")
enc = gdb.execute("x/s $rsi", to_string=True)
gdb.execute("shell clear")
print(enc)
gdb.execute("q")