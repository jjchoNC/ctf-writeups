import subprocess
import gdb

checkAddr = 0x401A86
gdb.execute("file knight_armoury")
gdb.execute(f"""b *{checkAddr}""")
gdb.execute("r < knight_armoury")
enc = gdb.execute("x/s $rsi", to_string=True)
enc = enc[11:-2] + "\n"
subprocess.run("nc 198.58.104.183 11337", shell=True, input=enc, text=True)
# KCTF{kN1gHT_aRm0uRy_aCC3ss_GranTed}