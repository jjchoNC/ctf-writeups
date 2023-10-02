# Dargon's Lair
Given an ELF file and IP & port for TCP connection.

## Solver
#### Game Mechanic
```
User choose [1] (Freeze attack) : 
user HP -= 0
dragon HP -= 0

User choose [2] (Poison attacl) :
user HP -= 1750
dragon HP -= 280

User choose [3] (Heal) :
user HP += 50

```
So we need to heal 35 times after using poison attack. Make a payload to beat the boss and send it given tcp connection.
```py
payload = open('payload.txt', 'w')
hp = 1800
bos = 32430
while bos > 0:
    if hp == 50:
        heal = 35
        while(heal):
            payload.write('3\n')
            hp += 50
            heal -= 1
    else:
        bos -= 280
        hp -= 1750
        payload.write('2\n')
```
Got encrypted flag.
```bash
------------------------------------------
| Congratulations on your victory Chief! |
------------------------------------------
flag: <*0e-$3 e $7+ !e1- e!7$"*+e6)$< 7e$&-, 3 ( +1
```
Find the encryption method by decompiling the ELF file.
```c
     if ( dword_5DA134 <= 0 )
      {
        sub_44AF70(v20);
        sub_475E30(v19);
        sub_46FB70(&unk_5DD520, "------------------------------------------\n");
        sub_46FB70(&unk_5DD520, "| Congratulations on your victory Chief! |\n");
        sub_46FB70(&unk_5DD520, "------------------------------------------\n");
        sub_44B960(v20, "flag.txt", 8LL);
        sub_478980(v20, v19);
        v18 = sub_404874(90LL, 9LL);
        for ( i = 0; ; ++i )
        {
          v7 = i;
          if ( v7 >= sub_476170(v19) || !*(_BYTE *)sub_476480(v19, i) )
            break;
          v5 = (_BYTE *)sub_476480(v19, i);
          v6 = v18 ^ *v5;
          *(_BYTE *)sub_476480(v19, i) = v6;
        }
        v9 = sub_46FB70(&unk_5DD520, "flag: ");
        v10 = sub_478970(v9, v19);
        sub_46E660(v10, sub_46F450);
        byte_5DA138 = 0;
        sub_475F40(v19);
        sub_44CD80(v20);
        goto LABEL_42;
```
We know that the encryption method only use xor for each character in the original flag. When i tried to run a program on local, the result was different on every run even the original flag is same. So we need to bruteforce the xor key.
```py
enc = '''<*0e-$3 e $7+ !e1- e!7$"*+e6)$< 7e$&-, 3 ( +1'''
p = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'''
for key in range(1000):
    d = ""
    temp = enc
    for char in temp:
        dc = chr(ord(char) ^ key)
        if dc not in p:
            break
        d += dc
    else:
        print(f"slashroot7{{{d}}}")
    #slashroot7{you have earned the dragon slayer achievement}
```
