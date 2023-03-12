print ('NAMA  : ILHAM YOGA PRATAMA')
print ('NIM   : 121140081')
print ('KELAS : RB')
print ('=============================')
print()

#Mendefinisikan kelas AkunBank
class AkunBank:
    list_pelanggan = [] #Atribut kelas list_pelanggan yang berisi data pelanggan tiap instansi, dimulai sebagai list kosong

    #Inisialisasi atribut instance pada saat objek dibuat
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan      #Atribut private nomor pelanggan
        self.__nama_pelanggan = nama_pelanggan  #Atribut private nama pelanggan
        self.__jumlah_saldo = jumlah_saldo      #Atribut private jumlah saldo
        AkunBank.list_pelanggan.append(self)    #Atribut kelas berupa list_pelanggan yang menyimpan data pelanggan tiap instansi

    #Fungsi untuk menampilkan menu pilihan aksi yang dapat dilakukan oleh pelanggan
    def lihat_menu(self):
        print("\nSelamat datang di Bank Jago")
        print("Halo {}, ingin melakukan apa?".format(self.__nama_pelanggan))
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

    #Fungsi untuk menampilkan saldo pelanggan
    def lihat_saldo(self):
        print("\n{} memiliki saldo Rp {}".format(self.__nama_pelanggan, self.__jumlah_saldo))

    #Fungsi untuk melakukan penarikan tunai
    def tarik_tunai(self, nominal_tarik):
        #Loop disini akan mengecek apakah saldo mencukupi atau tidak, jika tidak maka program akan memberitahu bahwa saldo tidak cukup
        while self.__jumlah_saldo < nominal_tarik:
            print("Nominal saldo yang Anda punya tidak cukup!")
            nominal_tarik = int(input("Masukkan jumlah nominal yang ingin ditarik: ")) #Pengguna akan disuruh memasukkan nominal yang ingin ditarik kembali

        #Jika saldo cukup maka saldo akan dikurangi dan program akan memberi pernyataan bahwa saldo berhasil ditarik
        self.__jumlah_saldo -= nominal_tarik
        print("Saldo berhasil ditarik!")

    #Fungsi untuk melakukan transfer saldo ke rekening lain
    def transfer(self, nominal_transfer, no_rek_tujuan):
        for pelanggan in AkunBank.list_pelanggan:
            if pelanggan.__no_pelanggan == no_rek_tujuan:   #Cari apakah nomor rekening tujuan terdaftar di list_pelanggan
                pelanggan.__jumlah_saldo += nominal_transfer 
                self.__jumlah_saldo -= nominal_transfer     #Jika ada, kurangi saldo dan tampilkan pesan sukses
                print("Transfer Rp {} ke {} sukses!".format(nominal_transfer, pelanggan.__nama_pelanggan))
                break
            
        #Jika tidak ada, tampilkan pesan gagal dan balik kembali ke menu utama
        else:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama...")

#Membuat objek-objek AkunBank
Akun1 = AkunBank(1234, "Ilham", 5000000000)
Akun1.lihat_menu() #Memanggil fungsi lihat_menu() pada akun1
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

while True:
    nomor_input = int(input("Masukkan nomor input: ")) #Mengambil input dari pengguna dan menyimpannya dalam variabel nomor_input
    if nomor_input == 1: #Jika nomor input yang dimasukkan pengguna adalah 1, maka akan memanggil fungsi lihat_saldo() dan lihat_menu() pada Akun1
        Akun1.lihat_saldo()
        Akun1.lihat_menu()
    elif nomor_input == 2: #Jika nomor input yang dimasukkan pengguna adalah 2, maka akan meminta pengguna untuk memasukkan nominal tarik tunai dan memanggil fungsi tarik_tunai() dan lihat_menu() pada Akun1
        nominal_tarik = int(input("\nMasukkan jumlah nominal yang ingin ditarik: "))
        Akun1.tarik_tunai(nominal_tarik)
        Akun1.lihat_menu()
    elif nomor_input == 3: #Jika nomor input yang dimasukkan pengguna adalah 3, maka akan meminta pengguna untuk memasukkan nominal transfer dan nomor rekening tujuan, dan memanggil fungsi transfer() dan lihat_menu() pada Akun1
        nominal_transfer = int(input("\nMasukkan nominal yang ingin ditransfer: "))
        no_rek_tujuan = int(input("Masukkan no rekening tujuan: "))
        Akun1.transfer(nominal_transfer, no_rek_tujuan)
        Akun1.lihat_menu()
    elif nomor_input == 4:  #Jika nomor input yang dimasukkan pengguna adalah 4, maka program akan keluar dari loop while
        break

    #Jika nomor input yang dimasukkan pengguna bukan 1, 2, 3, atau 4, maka akan menampilkan pesan kesalahan dan memanggil fungsi lihat_menu() pada Akun1
    else:
        print("\nMasukan tidak valid! Silakan masukkan nomor input yang benar.")
        Akun1.lihat_menu()
