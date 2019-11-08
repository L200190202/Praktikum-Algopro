Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Muhammad Mushlih Rosyid'
>>> NIM = 'L200190202'
>>> x = '1' + NIM[7:]
>>> a = int(x)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Karena data "x" diubah ke tipe data integer
>>> type(b)
<class 'int'>
>>> # Karena data "Nama" mempunyai intruksi "len"
>>> a / b
52.26086956521739
>>> # Karena 202 dibagi 23 adalah 52.26086956521739
>>> a // b
52
>>> # Karena devinisi // adalah pembagian dibulatkan
>>> 10 * (a - 999)
2030
>>> # Karena nilai a dikurangi 999 dan dikali 10 adalah 2030
>>> b ** 2
529
>>> # Karena "**" adalah perpangkatan
>>> a % b
6
>>> # Karena "%" adalah sisa hasil bagi
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Karena "12.5" adalah angka desimal
>>> a / c
96.16
>>> # Karena 1202 dibagi 12.5 adalah 96.16
>>> a // c
96.0
>>> # Karena hasil permbagian dibulatkan dari "a" dan "c" adalah 96.0
>>> a % c
2.0
>>> # Karena sisa hasil bagi dari "a" dan "c" adalah 2.0
>>> c > b
False
>>> # Karena 1202 lebih besar dari 12.5
>>> type(c > b)
<class 'bool'>
>>> # Karena mempunyai 2 kemungkinan yaitu "True" atau "False"
>>> a > b and b > c
True
>>> # Karena nilai a lebih besar dari nilai b dan nilai b lebih besar dar nilai c
>>> a > 1100 or b < 10
True
>>> # Karena nilai a lebih besar dari 1100 atau nilai b lebih kecil dari 10
