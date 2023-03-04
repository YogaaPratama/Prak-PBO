print ('NAMA  : ILHAM YOGA PRATAMA')
print ('NIM   : 121140081')
print ('KELAS : RB')
print ('=============================')
print ('======= Program Login =======')
print ('=============================')
print()

#inisialisasi variabel username dan password
username = "informatika"
password = "12345678"

lagi = 'y' #inisialisasi variabel lagi = 'y' untuk menanyakan kepada user apakah ingin lanjut atau tidak
a = 0      #inisialisasi variabel a = 0 sebagai kesempatan awal login yang akan dilakukan

#perulangan while dijalankan karena nilai awal dari variabel lagi == 'y'
while lagi == 'y':
    #user memasukkan username dan password
    name = str(input('Username anda : '))
    pw = str(input('Password anda : '))
    #mengecek apakah username dan password yang diinputkan diatas benar atau salah
    if name==username and pw==password :
        print ('Berhasil login!')
        break
    else :
        print ('Username atau password salah coba lagi')

    a=a+1 #jika password dan username salah kita menambahkan 1 pada varibel 'a'

    #mengecek apakah pengguna sudah melakukan percobaan lebih dari 3 kali
    if a>3:
        print('Sudah lebih 3x percobaan, Akun anda terblokir')
        break
    print()

    #menanyakan kepada user apakah ingin melakukan percobaan login lagi atau tidak
    lagi=str(input('Input username dan password lagi? y/t : '))
    print()
