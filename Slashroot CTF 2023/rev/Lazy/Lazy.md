# Lazy
Given an ELF file that encrypt a string.

## Solver
Encrypted result :
```
Input  : abc
Result : 97 98 99

Inpur  : ab
Result : 98 99
```
Map every encrypted char with the original one.
```py
a = [119, 112, 51, 108, 97, 85, 52, 108, 112, 85, 122, 52, 102, 54, 55, 106, 85, 113, 51, 108, 85, 104, 104, 52, 105, 113, 51, 76, 124, 48, 112, 101, 101, 114, 108, 113, 99, 104, 113]
load = [124, 119, 85, 62, 63, 48, 49, 50, 51, 52, 53, 54, 55, 93, 94, 95, 77, 78, 79, 80, 81, 82, 83, 84, 69, 70, 71, 72, 73, 74, 75, 76, 64, 88, 89, 90, 65, 66, 67, 125, 126, 127, 109, 110, 111, 112, 113, 114, 115, 116, 101, 102, 103, 104, 105, 106, 107, 108, 96, 120, 121,122, 97, 98, 99][::-1]
text = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}{")
flag = ""
for i in a:
    for j in range(len(load)):
        if (i == load[j]):
            flag += text[j]
print(flag[::-1])

# slashroot7{H4sk3ll_h4s_j01n3d_th3_ch4t}
```