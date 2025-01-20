<h1 align="center">money-ware</h1>

## Deskripsi Soal
<p align="justify">Flag format: picoCTF{Malwarename} The first letter of the malware name should be capitalized and the rest lowercase.<br>
Your friend just got hacked and has been asked to pay some bitcoins to <i>1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX.</i> He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?</p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/money-ware/Files/1.png"  width="50%" height="auto"/>
</p>

## Solusi Challenge 
<p align="justify">Pertama-tama, karena challenge ini berhubungan dengan bitcoin dan malware, kami memutuskan untuk mengecek address dari bitcoin tersebut ke dalam website <a href="https://www.bitcoinabuse.com/">bitcoin abuse database</a>.</p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/money-ware/Files/2.png"  width="50%" height="auto"/>
</p>
<p align="justify">Ternyata benar, terdapat malware yang terekam pada address bitcoin tersebut dan nama dari malware tersebut adalah <i>"petya"</i></p>
<p align="center">
<img src="https://github.com/jjchoNC/ctf-writeups/blob/main/PICO%20CTF%202023/General%20Skills/money-ware/Files/3.png"  width="50%" height="auto"/>
</p>


## Flag

```
picoCTF{petya}
```
