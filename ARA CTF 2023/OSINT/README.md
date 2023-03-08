# OSINT

## Time Machine

> There was a secret leaked on Official ARA Website. It can only seen on January 22nd 2023. Can you turn back the time?

- Solusi Challenge

Dalam challenge diatas, deskripsi menyebutkan untuk mendapatkan flag yang ada pada website ARA pada tanggal 22 Januari 2023. Untuk mendapatkannya, kami menggunakan Internet Archive Wayback Machine (https://archive.org/web/)

![](images/image-001.png)

![](images/image-002.png)

Untuk mendapatkan flag, lakukan view page source dan gunakan ctrl + f untuk mencari flag sesuai dengan format flag.

**Flag :ARA2023{d1gIt4l\_f00tpr1nt\_1s\_sC4ry}**


## Backroom

> I found a place that give me a backroom vibes. I think I like this place, so I give this place 5 star. Can you find this place?

- Solusi Challenge

Pada challenge diatas diberikan foto suatu tempat, kita menggunakan exiftool untuk mendapatkan GPS latitude dan GPS longitude.

![](images/image-004.png)

Setelah itu, kita dapat mencarinya melalui https://www.gps-coordinates.net/

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.007.jpeg)

Setelah mendapatkan lokasi dari foto tersebut, kita dapat menemukan flag dari challenge ini pada kolom ulasan Google tentang lokasi tersebut.

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.008.jpeg)

**Flag :ARA2023{c4r3full\_w1th\_y0uR\_m3tad4ta}**


## Hey detective, can you help me

- Solusi

Salah satu dari anggota tim kami teringat pernah melihat video yang disajikan pada challenge tersebut, dan teringat dengan kata kunci kenko yang merujuk pada cosplayer tersebut.

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.010.jpeg)

Setelah mencari pada sosial media instagram, ternyata benar bahwa cosplayer tersebut bernama “Yanzikenko”, dan kami juga berhasil menemukan video yang diberikan oleh panitia pada akun Instagram kenko.

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.011.jpeg)

kemudian kami menggunakan tool https://commentpicker.com/instagram-user-id.php) untuk mencari User ID pada instagram dia dan menemukan bahwa ID nya adalah “44793134117”

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.012.png)

Setelah mencari pada akun Instagram nya kami tidak menemukan hal hal yang terkoneksi dengan deskripsi soal, oleh karena itu kami berpindah ke facebook. Pada facebook kami berusaha mencari post kenko yang berhubungan dengan Universitas, Toko Buku, dan Toko Boneka, setelah scroll scroll facebook kami mendapatkan post yang berhubungan dengan hal tersebut antara lain sebagai berikut:

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.013.jpeg)

Gambar 1

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.014.jpeg)

Gambar 2

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.015.jpeg)

Gambar 3

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.016.jpeg)

Gambar 4

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.017.jpeg)

Gambar 5

![](Aspose.Words.dd5bdc20-b2db-4d6a-b030-6f166ebb0d2d.018.jpeg)

Gambar 6

Pada Gambar 1 ditemukan post dari kenko bahwa dia mengunjungi Toko buku dengan posisi duduk, dapat dilihat pada gambar tersebut ditunjukkan waktu upload nya adalah 3Juni2019-10:25, kemudian pada Gambar 2 dan 3, ditemukan juga post kenko sedang berfoto pada toko boneka dengan maskot tersebut, kemudian kami mencari foto maskot tersebut dengan menggunakan google lens dan menemukan nama maskot nya adalah Molly, setelah itu pada gambar 4 kami mencari kata “Flag” pada akun dari kenko di facebook dan menemukan sebuah komentar dari user yang menyatakan flag tersebut yang berbunyi Y0u4r3ThE0s1nTm45t3R, dan yang terakhir adalah universitas dari kenko yang dapat ditemukan pada postingan facebook kenko (pada gambar 6) yang berada pada Beijing Normal University yang dapat disingkat BNU. Untuk mensubmit flag kami menggabungkan segala hal yang telah kami dapatkan dan flag terakhir adalah

**Flag ARA2023{44793134117\_BNU\_Molly\_3Juni2019-10:25\_Y0u4r3ThE0 s1nTm45t3R}**
