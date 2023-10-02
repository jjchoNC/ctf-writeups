# Asem

Given assembly code :
```
section .text:
global _start
_start:
    lea edx, s    
    mov di, edx   
    lea bh, flag   
    mov bl, bh 
    mov cl, 25h
    add bl, cl  

    L1 : 
        add di, 1  
        mov al, [edx]    
        xchg [bh], al   
        mov ch, [di]       
        xchg [bl], ch    
        dec bl
        add edx, 2
        inc bh
        cmp edx, cl
        jl L1
        ret
section .data:
s db 's', '}', 'l', 'h', 'a', 'u', 's', 'p', 'h', '3', 'r', '5', 'o', '_', 'o', 'h', 't', 'u', '7', 'p', '{', '_', 'p', 'u', '3', 'l', 'm', 'u', '4', 'd', 'n', '_', '4', 'n', 's', '4' 
flag db ''
```

## Solver : 
```py
s = ['s', '}', 'l', 'h', 'a', 'u', 's', 'p', 'h', '3', 'r', '5', 'o',
'_', 'o', 'h', 't', 'u', '7', 'p', '{', '_', 'p', 'u', '3', 'l', 'm',
'u', '4', 'd', 'n', '_', '4', 'n', 's', '4']
flag = ""
for i in range(0,len(s),2):
    print(s[i], end="")
for i in range(1, len(s), 2):
    flag += s[i]
flag = list(flag)
flag = flag[::-1]
print(''.join(flag), end="")
# slashroot7{p3m4n4s4n_dulu_puh_53puh}
```