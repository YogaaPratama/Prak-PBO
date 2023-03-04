print ('NAMA  : ILHAM YOGA PRATAMA')
print ('NIM   : 121140081')
print ('KELAS : RB')
print ('=============================')
print()

#contoh kelas 'DataDiri' dengan atribut 'nama', 'nim', 'kelas_PBO', 'jumlah_SKS'
class DataDiri:
    def __init__(self, nama, nim, kelas_PBO, jumlah_SKS):
        self.nama = nama             #inisialisasi atribut 'nama'
        self.nim = nim               #inisialisasi atribut 'nim'
        self.kelas_PBO = kelas_PBO   #inisialisasi atribut 'kelas_PBO'
        self.jumlah_SKS = jumlah_SKS #inisialisasi atribut 'jumlah_SKS'


    #method 'tampilkan_data' untuk menampilkan keterangan data diri
    def tampilkan_data(self):
        print(str(self.nama), "dengan NIM", str(self.nim), "dari kelas PBO", str(self.kelas_PBO), "mengambil mata kuliah semester 4 dengan jumlah", str(self.jumlah_SKS), "SKS")


#inputan data diri yang dilakukan oleh user
nama = str(input("Masukkan Nama : "))
nim = str(input("Masukkan NIM : "))
jumlah_SKS = str(input("Masukkan Jumlah SKS : "))


#contoh pembuatan objek dari kelas 'DataDiri' dan pemanggilan method 'tampilkan_data' untuk menampilkan keterangan data diri
mhs = DataDiri(nama, nim, "RB", jumlah_SKS) #membuat objek 'mhs'
mhs.tampilkan_data() #memanggil method 'tampilkan_data' untuk menampilkan keterangan data diri
