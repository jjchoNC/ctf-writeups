## Challenge Description
Hello there brave programmer!

I am the CEO of TotallySecureBank™, I have a lot of money in my bank account but I forgot my password! My username is admin and I have $100000 in my account.

If you could recover my account you can use my password as a flag (flag would be uoftctf{MyPasswordHere})

You can try the bank software by running java -jar BankChallenge.jar and use the admin user user with the password

Author: Ido
File : [BankChallenge.jar](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF/rev/CEO's%20Lost%20Password/BankChallenge.jar)

## Solution
Use [jd-GUI](https://java-decompiler.github.io/) to decompile ```.class``` file inside the given ```.jar``` file.

Result :
[Main.java](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF/rev/CEO's%20Lost%20Password/Main.java) +
[a.java](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF/rev/CEO's%20Lost%20Password/a.java)

Debug the decompiled code to get the encrypted admin's password.

![Debug](https://github.com/jjchoNC/ctf-writeups/blob/main/UofTCTF/rev/CEO's%20Lost%20Password/images/debug.png)

Encrypted admin password : ```瑥⽦䩧㡡倰噕卖䝃捉㉌永敲畴楺癲湊```

Password Encryption Method: 
```java
boolean a(String var1) {
    return Main.a(var1).equals(this.a);
}
```

```java
static String a(String var0) {
    byte[] var1 = var0.getBytes(StandardCharsets.UTF_8);
    int var2 = (int) b[0] ^ 2125394058;

    while (var2 <= var0.length()) {
        int var3 = (int) b[1] ^ 316324253;

        while (var3 < var1.length) {
            var1[var3] = (byte) (var1[var3] + (var2 - ((int) b[2] ^ 322717984)) * var3 + ((int) b[3] ^ 1817181337));
            ++var3;
            a = (int) b[4] ^ 1916880556;
            if ((a * a + a + ((int) b[5] ^ 1376134906)) % ((int) b[6] ^ 1536615318) == 0) {
            }
        }
        ++var2;
    }

    return new String(Base64.getEncoder().encode(var1), StandardCharsets.UTF_16);
}
```

From this line we know that the encryption method is like :
```py
while i <= len(password):
    j = 0
    while j < len(dec):
        password[j] = ([password][j] + (i - 12) * j + 6) & 0xFF
        j += 1
    i += 1 

Base64.encode(password) -> return as UTF-16 format
```
So to make the decryption method, we just need to change the "+" symbol to "-". 
```py
enc = "瑥⽦䩧㡡倰噕卖䝃捉㉌永敲畴楺癲湊".encode('utf-16be')
print(enc)
import base64
dec = list(base64.b64decode(enc.decode()))
var2 = 1
while var2 <= len(dec):
    var3 = 0
    while var3 < len(dec):
        dec[var3] = (dec[var3] - (var2 - 12) * var3 - 6) & 0xFF
        var3 += 1
    var2 += 1
print(f"uoftctf{{{''.join([chr(i) for i in dec])}}}")

# Flag : uoftctf{%S7rONgadMInPaSSwORd32!%}
```

