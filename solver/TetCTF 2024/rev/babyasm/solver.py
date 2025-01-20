enc = [38793, 584, 738, 38594, 63809, 647, 833, 63602, 47526, 494, 663, 47333, 67041, 641, 791, 66734, 35553, 561, 673, 35306]
arr = [96, 101, 20, 177, 155, 116, 108, 69, 84, 109,
       103, 110, 111, 95, 116, 103, 97, 72, 20, 59]
xor_key = [19, 55, 32, 36]
for i in range(len(arr)):
    arr[i] ^= xor_key[i % len(xor_key)]
x = [0] * 20
idx = 19

def dec(idx1, idx2):
    global idx
    enc[idx2] -= 83
    if idx1 == 0:
        x[idx2] = (((enc[idx2]) ^ 32) - (x[idx] + arr[idx]))

    if idx1 == 1:
        x[idx2] = (((enc[idx2]) ^ 36) - (enc[idx] - arr[idx]))

    if idx1 == 2:
        x[idx2] = (((enc[idx2]) ^ 19) - (enc[idx] * arr[idx]))

    if idx1 == 3:
        x[idx2] = (((enc[idx2]) ^ 55) - (enc[idx] ^ arr[idx]))
    idx -= 1

def check():
    #reverse the check order
    dec(3, 16)
    dec(2, 19)
    dec(1, 18)
    dec(0, 17)
    dec(3, 12)
    dec(2, 15)
    dec(1, 14)
    dec(0, 13)
    dec(3, 8)
    dec(2, 11)
    dec(1, 10)
    dec(0, 9)
    dec(3, 4)
    dec(2, 7)
    dec(1, 6)
    dec(0, 5)
    dec(3, 0)
    dec(2, 3)
    dec(1, 2)
    dec(0, 1)

check()
print("TetCTF{", end="")
for i in x:
    try:
        print(chr(i - 83), end="")
    except:
        pass