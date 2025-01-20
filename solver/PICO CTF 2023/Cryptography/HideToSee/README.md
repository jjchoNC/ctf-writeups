<h1 align="center">HideToSee</h1>

## Deskripsi Soal
<p align="justify">How about some hide and seek heh? Look at this image <a href="https://github.com/Haalloobim/ctf-writeups/blob/main/PICO%20CTF%202023/Cryptography/HideToSee/file/atbash.jpg">here<a/>.</p>
<p align="center">
<img src="https://github.com/Haalloobim/ctf-writeups/blob/main/PICO%20CTF%202023/Cryptography/HideToSee/file/Capture.JPG"  width="50%" height="auto"/>
</p>

## Solusi Challenge 
<p align="justify">Pertama-tama, kami mengekstrak file yang diberikan menggunakan tool online yaitu <a href="https://futureboy.us/stegano/decinput.html">FutureBoys Steganographic Decoder</a> dan mendapatkan string yang telah di encode seperti berikut:</p>

<p align="center">
<img src="https://github.com/Haalloobim/ctf-writeups/blob/main/PICO%20CTF%202023/Cryptography/HideToSee/file/Capture1.JPG"  width="50%" height="auto"/>
</p>

```
krxlXGU{zgyzhs_xizxp_8z0uvwwx}
```

<p align="justify">Setelah menemukan strings yang telah terencode tersebut, kami menggunakan <a href="https://www.dcode.fr/atbash-cipher">dcode</a> untuk mendekripsi strings tersebut dengan atbash cipher dikarenakan pada file jpg sebelumnya menunjukkan gambar dari atbash cipher, setelah mendekripsi strings tersebut, Flag berasil didapatkan.</p>

<p align="center">
<img src="https://github.com/Haalloobim/ctf-writeups/blob/main/PICO%20CTF%202023/Cryptography/HideToSee/file/Capture2.JPG"  width="50%" height="auto"/>
</p>


## Flag

```
picoCTF{atbash_crack_8a0feddc}
```
