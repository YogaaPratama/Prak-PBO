print ('NAMA  : ILHAM YOGA PRATAMA')
print ('NIM   : 121140081')
print ('KELAS : RB')
print ('=============================')
print()

#mengambil input oanjang bintang yang akan dibentuk dari user
panjangBintang = int(input('Masukkan Panjang Bintang : '))
print()

#proses membuat pola bintang persegi
for i in range(panjangBintang):     #loop pertama digunakan untuk membuat/mengatur baris
    for j in range(panjangBintang): #loop kedua digunakan untuk membuat/mengatur kolom
        print('*',end='')
    print()
