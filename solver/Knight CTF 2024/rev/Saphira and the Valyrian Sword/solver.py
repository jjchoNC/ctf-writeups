import time
import subprocess

def enc(a1, user):
    v2 = a1
    v3 = 0
    v6 = 0
    v7 = 1
    for i in user:
        v3 += ord(i)
    while v2 > 0:
        v5 = v2 % 10
        v2 //= 10
        v6 += v7 * (v3 ^ v5)
        v7 *= 10
    v3 = 0
    while v6 > 0:
        v3 = 10 * v3 + v6 % 0xA
        v6 //= 0xA
    return a1 ^ v3

a1 = int(time.time())
subprocess.run("nc 198.58.104.183 21337", shell=True, input=str(enc(a1, "Geoffrey")) + "\n", text=True)
# KCTF{k1LL_tHE_Saphira_dRAgon_wITH_thE_sWORD}
