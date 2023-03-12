print ('NAMA  : ILHAM YOGA PRATAMA')
print ('NIM   : 121140081')
print ('KELAS : RB')
print ('=============================')
print()

class Mahasiswa:
    #Atribut public (dapat diakses dari mana saja)
    ipk = 0

    def __init__(self, nama, nim):
        #Atribut private (hanya dapat diakses di dalam class Mahasiswa)
        self.__nama = nama
        #Atribut protected (hanya dapat diakses di dalam class Mahasiswa)
        self._nim = nim

    def tampilkan_dataDiri(self):
        #Fungsi public (dapat di akses dari mana saja)
        print("Perkenalkan nama saya " + self.__nama + " dengan NIM " + str(self._nim))

    def tampilkan_ipk(self):
        #Fungsi public (dapat di akses dari mana saja)
        return self.ipk

#Membuat objek dari class Mahasiswa
Mahasiswa1 = Mahasiswa("ILHAM", "121140081")

#Mengakses atribut dan fungsi
Mahasiswa1.tampilkan_dataDiri()     #Output: Perkenalkan nama saya ILHAM dengan NIM 121140081.
Mahasiswa1.ipk = 3.75
print(Mahasiswa1.tampilkan_ipk())   #Output: 3.75
Mahasiswa1._nim = "123456789"       #Masih bisa di akses dari luar class karena hal ini hanya bersifat "convention"
print(Mahasiswa1._nim)              #Output: 123456789
Mahasiswa1.__nama = "Budi"          #Nama tidak akan berubah karena atribut ini bersifat private dan tidak dapat diakses dari luar kelas Mahasiswa
Mahasiswa1.tampilkan_dataDiri()     #Nama akan tetap seperti awal di class Mahasiswa yaitu "ILHAM"
