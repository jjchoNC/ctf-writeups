<h1 align="center">ReadMyCert</h1>

## Deskripsi Soal
<p align="justify">How about we take you on an adventure on exploring certificate signing requests.
Take a look at this CSR file <a href="https://github.com/Haalloobim/ctf-writeups/blob/main/PICO%20CTF%202023/Cryptography/ReadMyCert/Files/readmycert.csr">here<a/>.</p>
<p align="center">
<img src="https://github.com/Haalloobim/ctf-writeups/blob/main/PICO%20CTF%202023/Cryptography/ReadMyCert/Files/1.png"  width="50%" height="auto"/>
</p>

## Solusi Challenge 
<p align="justify">Ketika membuka fike readmycert.csr terdapat sebuah string yang merupakan sebuah certificate request seperti berikut ini.</p>
<p align="center">
<img src="https://github.com/Haalloobim/ctf-writeups/blob/main/PICO%20CTF%202023/Cryptography/ReadMyCert/Files/2.png"  width="50%" height="auto"/>
</p>
<p align="justify">Setelah mengetahui Hal tesebut kami menggunakan tool online untuk mendecode arti yang dimaksudkan dari certificate request tersebut
menggunakan tool yang bernama <a href="https://www.sslshopper.com/csr-decoder.html">CSR Decoder<a/>, dan menemukan hasil sebagai berikut ini:</p>
<p align="center">
<img src="https://github.com/Haalloobim/ctf-writeups/blob/main/PICO%20CTF%202023/Cryptography/ReadMyCert/Files/3.png"  width="50%" height="auto"/>
</p>

<p align="justify"></p>

<p align="center">

</p>


## Flag

```
picoCTF{read_mycert_693f7c03}
```