from itertools import product
import re

re_pattern = '^uoftctf\\{([bdrw013]){9}\\}$'
pattern = re.compile(re_pattern)

def worble(s):
    s1 = 5
    s2 = 31

    for n in range(len(s)):
        s1 = (s1 + ord(s[n]) + 7) % 65521
        s2 = (s1 * s2) % 65521
    return (s2 << 16) | s1

def shmorble(s):
    r = ''
    for i in range(len(s)):
        r += s[len(s) - 1 - i]
    return r

def blorble(a, b):
    return format(a, 'x') + format(b, 'x')

characters = "bdrw013"
all_combinations = [''.join(combination) for combination in product(characters, repeat=9)]
for combination in all_combinations:
    flag = "uoftctf{" + combination + "}"
    if pattern.match(flag):
        a = worble(flag)
        b = worble(flag[::-1])
        c = shmorble(blorble(a, b))
        if c == "a81c0750d48f0750"[::-1]:
            print(flag)
            break
    else:
        print("Incorrect format!")

# Flag = uoftctf{d3w0rb13d}