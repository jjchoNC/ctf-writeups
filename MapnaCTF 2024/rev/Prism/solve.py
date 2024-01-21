import gdb

gdb.execute("file prism")
b = gdb.execute("b start", to_string=True)
print(b)