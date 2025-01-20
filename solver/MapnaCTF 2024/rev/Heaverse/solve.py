import gdb
import re
from morse3 import Morse as m

gdb.execute("file heaverse")
gdb.execute("b puts")
gdb.execute("r")
enc = (re.findall(r'"(.*?)"', gdb.execute("x/s $rbp", to_string=True)))[0].replace("/", " ")
print(f"MAPNA{{{(m(enc).morseToString()).upper()}}}".replace(" ", "_"))

# MAPNA{JUS7_LIST3N_N0T_REV3RSE}