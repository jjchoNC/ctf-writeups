# Hey detective, can you help me

## Solusi

Salah satu dari anggota tim kami teringat pernah melihat video yang disajikan pada challenge tersebut, dan teringat dengan kata kunci kenko yang merujuk pada cosplayer tersebut.


Setelah mencari pada sosial media instagram, ternyata benar bahwa cosplayer tersebut bernama “Yanzikenko”, dan kami juga berhasil menemukan video yang diberikan oleh panitia pada akun Instagram kenko.

<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/ARA%20CTF%202023/OSINT/Backroom/images/IMG20221221153220.jpg" width="20%" height="auto" />

kemudian kami menggunakan tool https://commentpicker.com/instagram-user-id.php) untuk mencari User ID pada instagram dia dan menemukan bahwa ID nya adalah “44793134117”

<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/ARA%20CTF%202023/OSINT/Backroom/images/IMG20221221153220.jpg" width="20%" height="auto" />

Setelah mencari pada akun Instagram nya kami tidak menemukan hal hal yang terkoneksi dengan deskripsi soal, oleh karena itu kami berpindah ke facebook. Pada facebook kami berusaha mencari post kenko yang berhubungan dengan Universitas, Toko Buku, dan Toko Boneka, setelah scroll scroll facebook kami mendapatkan post yang berhubungan dengan hal tersebut antara lain sebagai berikut:

<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/ARA%20CTF%202023/OSINT/Backroom/images/IMG20221221153220.jpg" width="20%" height="auto" />
Gambar 1

<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/ARA%20CTF%202023/OSINT/Backroom/images/IMG20221221153220.jpg" width="20%" height="auto" />

Gambar 2

<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/ARA%20CTF%202023/OSINT/Backroom/images/IMG20221221153220.jpg" width="20%" height="auto" />

Gambar 3

<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/ARA%20CTF%202023/OSINT/Backroom/images/IMG20221221153220.jpg" width="20%" height="auto" />

Gambar 4

<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/ARA%20CTF%202023/OSINT/Backroom/images/IMG20221221153220.jpg" width="20%" height="auto" />

Gambar 5

<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/ARA%20CTF%202023/OSINT/Backroom/images/IMG20221221153220.jpg" width="20%" height="auto" />

Gambar 6

Pada Gambar 1 ditemukan post dari kenko bahwa dia mengunjungi Toko buku dengan posisi duduk, dapat dilihat pada gambar tersebut ditunjukkan waktu upload nya adalah 3Juni2019-10:25, kemudian pada Gambar 2 dan 3, ditemukan juga post kenko sedang berfoto pada toko boneka dengan maskot tersebut, kemudian kami mencari foto maskot tersebut dengan menggunakan google lens dan menemukan nama maskot nya adalah Molly, setelah itu pada gambar 4 kami mencari kata “Flag” pada akun dari kenko di facebook dan menemukan sebuah komentar dari user yang menyatakan flag tersebut yang berbunyi Y0u4r3ThE0s1nTm45t3R, dan yang terakhir adalah universitas dari kenko yang dapat ditemukan pada postingan facebook kenko (pada gambar 6) yang berada pada Beijing Normal University yang dapat disingkat BNU. Untuk mensubmit flag kami menggabungkan segala hal yang telah kami dapatkan dan flag terakhir adalah

**Flag ARA2023{44793134117\_BNU\_Molly\_3Juni2019-10:25\_Y0u4r3ThE0 s1nTm45t3R}**
