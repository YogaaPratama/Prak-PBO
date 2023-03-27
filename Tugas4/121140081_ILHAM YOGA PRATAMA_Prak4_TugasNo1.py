print ('NAMA  : ILHAM YOGA PRATAMA')
print ('NIM   : 121140081')
print ('KELAS : RB')
print ('=============================')
print()

#Membuat class Komputer dengan atribut nama, jenis, harga, dan merk
class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

#Membuat class Processor yang merupakan turunan dari class Komputer
class Processor(Komputer):
    #Konstruktor class Processor dengan atribut merk, jenis, harga, jumlah_core, dan kecepatan_processor
    def __init__(self, merk, jenis, harga, jumlah_core, kecepatan_processor):
        #Memanggil konstruktor class Komputer dengan atribut nama, jenis, harga, dan merk
        super().__init__('Processor', jenis, harga, merk)
        #Menambahkan atribut jumlah_core dan kecepatan_processor pada class Processor
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

#Membuat class RAM yang merupakan turunan dari class Komputer
class RAM(Komputer):
    #Konstruktor class RAM dengan atribut merk, jenis, harga, dan kapasitas
    def __init__(self, merk, jenis, harga, kapasitas):
        #Memanggil konstruktor class Komputer dengan atribut nama, jenis, harga, dan merk
        super().__init__('RAM', jenis, harga, merk)
        #Menambahkan atribut kapasitas pada class RAM
        self.kapasitas = kapasitas

#Membuat class HDD yang merupakan turunan dari class Komputer
class HDD(Komputer):
    #Konstruktor class HDD dengan atribut merk, jenis, harga, kapasitas, dan rpm
    def __init__(self, merk, jenis, harga, kapasitas, rpm):
        #Memanggil konstruktor class Komputer dengan atribut nama, jenis, harga, dan merk
        super().__init__('HDD', jenis, harga, merk)
        #Menambahkan atribut kapasitas dan rpm pada class HDD
        self.kapasitas = kapasitas
        self.rpm = rpm

#Membuat class VGA yang merupakan turunan dari class Komputer
class VGA(Komputer):
    #Konstruktor class VGA dengan atribut merk, jenis, harga, dan kapasitas
    def __init__(self, merk, jenis, harga, kapasitas):
        #Memanggil konstruktor class Komputer dengan atribut nama, jenis, harga, dan merk
        super().__init__('VGA', jenis, harga, merk)
        #Menambahkan atribut kapasitas pada class VGA
        self.kapasitas = kapasitas

#Membuat class PSU yang merupakan turunan dari class Komputer
class PSU(Komputer):
    #Konstruktor class PSU dengan atribut merk, jenis, harga, dan daya
    def __init__(self, merk, jenis, harga, daya):
        #Memanggil konstruktor class Komputer dengan atribut nama, jenis, harga, dan merk
        super().__init__('PSU', jenis, harga, merk)
        #Menambahkan atribut daya pada class PSU
        self.daya = daya

#Membuat beberapa objek untuk ditambahkan ke dalam list rakit
p1 = Processor('Intel','Core i7 7740X',4350000,4,'4.3GHz')
p2 = Processor('AMD','Ryzen 5 3600',250000,4,'4.3GHz')
ram1 = RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
ram2 = RAM('G.SKILL','DDR4 2400MHz',328000,'4GB')
hdd1 = HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200)
hdd2 = HDD('Seagate','HDD 2.5 inch',295000,'1000GB',7200)
vga1 = VGA('Asus','VGA GTX 1050',250000,'2GB')
vga2 = VGA('Asus','1060Ti',250000,'8GB')
psu1 = PSU('Corsair','Corsair V550',250000,'500W')
psu2 = PSU('Corsair','Corsair V550',250000,'500W')

#Membuat list rakit dan menambahkan objek-objek di atas ke dalamnya
rakit = [[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]]

#Melakukan looping untuk menampilkan komponen-komponen tiap komputer yang dirakit
for i in range(len(rakit)):
    print(f"Komputer {i+1}")
    for j in rakit[i]:
        print(f"{j.nama} {j.jenis} produksi {j.merk}")
    print("\n")
