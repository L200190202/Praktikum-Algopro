Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Muhammad Mushlih Rosyid"
>>> NIM = 202
>>> Tinggi = 1.71
>>> Berat = 65
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Karena "Aku" adalah deretan huruf
>>> Aku[0]
2001
>>> # Karena data pertama "Aku" adalah "TahunLahir" yang bernilai 2001
>>> a = NIM % 4; Aku[a]
1.71
>>> # Karena sisa hasil bagi dari 202 dibagi 4 adalah 0, jadi jawabanya adalah data "a" dari "Aku" yaitu 1.71
>>> type(Aku[a])
<class 'float'>
>>> # Karena 1.71 adalah bertipe float
>>> Aku[a:4]
(1.71, 202)
>>> # Karena niali "a" dari type data "Aku" adalah "Tinggi" dan 4 nilainya mentok di "NIM"
>>> type(Aku[4])
<class 'str'>
>>> # Karena object kelima dari "Aku" adalah "Nama" yang bernilai "Muhammad MUshlih Rosyid"
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # Karena nilai pertama dari "Aku" adalah "TahunLahir" yang mempunyai nilai "2001"
>>> type(Data)
<class 'list'>
>>> # Karena "Data" adalah deretan objek yang elemenya dapat diubah
>>> type(Data[4])
<class 'str'>
>>> # Karena data ke 4 dari "Data" adalah "NIM" yang bernilai "202" yang merupakan tanda baca
>>> Data[4][5]
'm'
>>> # Karena data kelima dari "Data" adalah "Nama" yang bernilai "Muhammad Mushlih Rosyid" dan data kelima dari "Nama" adalah huruf m
>>> Data[4][a:6]
'hamm'
>>> # Karena data kelima dari "Data" adalah "Nama" yang bernilai "Muhammad Mushlih Rosyid" dan kata dari a sampai 6 adalah hamm
>>> Data[0] = 'ok'; Data
['ok', 65, 1.71, 202, 'Muhammad Mushlih Rosyid']
>>> # Karena Nilai pertama dari "Data" diubah menjadi "ok" dan program menulisan semua isi dari "Data" yaitu "Berat" "Tinggi" "NIM" "Nama" besrta nilainya
>>> Data[-a]
202
>>> # Karena nilai "-a" dari "Data" adalah "NIM" yang mempunyai nilai "202"
>>> range(a)
range(0, 2)
>>> # karena "a" mempunyai jarak (0, 2)
