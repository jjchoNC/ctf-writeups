import re

re_pattern = re.compile('^uoftctf\\{([bdrw013]){9}\\}$')


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
    return f"{format(a, 'x')}{format(b, 'x')}"


print("                      _     _             ")
print("                     | |   | |            ")
print("  __      _____  _ __| |__ | | ___ _ __   ")
print("  \ \ /\ / / _ \| '__| '_ \| |/ _ \ '__|  ")
print("   \ V  V / (_) | |  | |_) | |  __/ |     ")
print("    \_/\_/ \___/|_|  |_|__/|_|\___|_|     ")
print("                                          ")
print("==========================================")

flag = input('Enter flag: ')

if re_pattern.match(flag):
    a = worble(flag)
    b = worble(flag[::-1])
    c = shmorble(blorble(a, b))
    print("Here's your flag:")
    print(shmorble(blorble(a, b))[::-1])
else:
    print('Incorrect format!')
