## Program Akun
## dibuat oleh Mushlih L200190202
import random
angka = random.randint(0,1000)

Nama = 'Muhammad Mushlih Rosyid'
TanggalLahir = '30 Maret 2001'
NamaSingkat = Nama[0] + '. ' + Nama[9] + '. ' + Nama[16:23]
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[8:13]
Password = Nama[0:3] + str(angka)
