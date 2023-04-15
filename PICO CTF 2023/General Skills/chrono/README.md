<h1 align="center">chrono</h1>

## Deskripsi Soal
<p align="justify">How to automate tasks to run at intervals on linux servers?<br>
Additional details will be available after launching your challenge instance.</p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/chrono/Files/6.PNG"  width="50%" height="auto"/>
</p>

## Solusi Challenge 
<p align="justify">Pertama-tama, setelah melakukan "Launch Instance", sambungkan koneksi ssh picoCTF ke WSL dengan cara seperti berikut:</p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/chrono/Files/1.PNG"  width="50%" height="auto"/>
</p>
<p align="justify">Setelah menyambungkan koneksi ke WSL, langsung cek apakah ada file/folder yang tersedia pada machine tersebut.</p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/chrono/Files/2.PNG"  width="50%" height="auto"/>
</p>
<p align="justify">Setelah dicek tidak ada folder ataupun file pada user, kemudian pindah ke directory root dan lakukan pengecekan kembali dan ditemukan folder challenge.</p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/chrono/Files/3.PNG"  width="50%" height="auto"/>
</p>
<p align="justify">Setelah itu, change directory ke folder challenge dan melakukan pengecekkan isi folder tersebut dan ditemukan file metadata.json</p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/chrono/Files/4.PNG"  width="50%" height="auto"/>
</p>
<p align="justify">yang terakhir lihat isi file tersebut dengan menggunakan perintah "cat metadata.json" dan ditemukan flagnya</p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/chrono/Files/5.PNG"  width="75%" height="auto"/>
</p>


## Flag

```
picoCTF{Sch3DUL7NG_T45K3_L1NUX_1b4d8744}
```
