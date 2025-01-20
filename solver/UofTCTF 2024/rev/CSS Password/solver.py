import re

pattern = re.compile(
    r'.wrapper:has\(\.byte:nth-child\((\d+)\) \.latch:nth-child\((\d+)\) \.latch__(\w+):active\) .checker:nth-of-type\((\d+)\) .checker__state:nth-child\((\d+)\) {\n\s+transform: translateX\(([-\d]+)%\);\n\s+transition: transform 0s;')

text = open("css-password.html").read()
matches = pattern.findall(text)

bin = [[0] * 8 for _ in range(19)]
for match in matches:
    if match[2] == "set":
        byteNo = int(match[0])
        latchNo = int(match[1])
        binary = match[5]
        (bin[byteNo-1])[latchNo-1] = 1 if binary == "-100" else 0

for _ in bin:
    print(chr(int(''.join(map(str, _)),2)),end="")

# Flag: uoftctf{CsS_l0g1c_is_fun_3h}
