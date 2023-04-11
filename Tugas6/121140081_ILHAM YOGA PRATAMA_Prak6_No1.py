from abc import ABC, abstractmethod  # Mengimpor modul abc untuk membuat kelas abstrak

class AkunBank(ABC):  # Membuat kelas abstrak AkunBank yang mewarisi sifat dari ABC
    def __init__(self, nama, tahun_daftar, saldo):  # Membuat method konstruktor dengan parameter nama, tahun daftar, saldo
        self.nama = nama  # Inisialisasi atribut nama dengan nilai dari parameter nama
        self.tahun_daftar = tahun_daftar  # Inisialisasi atribut tahun_daftar dengan nilai dari parameter tahun_daftar
        self.saldo = saldo  # Inisialisasi atribut saldo dengan nilai dari parameter saldo

    def lihat_saldo(self):  # Membuat method lihat_saldo
        print(f"Saldo {self.nama}: Rp {self.saldo}")  # Menampilkan saldo akun

    @abstractmethod  # Mendekorasikan method transfer_saldo sebagai abstract method
    def transfer_saldo(self, jumlah):  # Membuat method transfer_saldo dengan parameter jumlah
        pass

    @abstractmethod  # Mendekorasikan method lihat_suku_bunga sebagai abstract method
    def lihat_suku_bunga(self):  # Membuat method lihat_suku_bunga
        pass


class AkunGold(AkunBank):  # Membuat kelas AkunGold yang mewarisi sifat dari AkunBank
    def __init__(self, nama, tahun_daftar, saldo):  # Membuat method konstruktor dengan parameter nama, tahun daftar, saldo
        super().__init__(nama, tahun_daftar, saldo) # Memanggil method konstruktor kelas induk

    def transfer_saldo(self, jumlah):  # Membuat method transfer_saldo dengan parameter jumlah
        self.tahun_daftar = 2023 - self.tahun_daftar  # Menghitung lama keanggotaan
        if self.tahun_daftar >= 3 and jumlah > 100000:  # Jika lama keanggotaan >= 3 tahun dan jumlah transfer > 100.000
            biaya_admin = 0  # Biaya admin = 0
        else:
            biaya_admin = 2000  # Selain itu biaya admin = 2000

        if jumlah <= 100000:  # Jika jumlah transfer <= 100.000
            biaya_admin = 0  # Biaya admin = 0

        if self.saldo >= jumlah + biaya_admin:  # Jika saldo cukup untuk melakukan transfer
            self.saldo -= jumlah + biaya_admin  # Mengurangi saldo dengan jumlah transfer dan biaya admin
            print(f"Transfer sebesar Rp {jumlah} berhasil dilakukan. Biaya admin: Rp {biaya_admin}.")  # Menampilkan pesan berhasil transfer
        else:  # Jika saldo tidak cukup untuk melakukan transfer
            print("Saldo tidak mencukupi untuk melakukan transfer.")

    def lihat_suku_bunga(self):
        # Memeriksa apakah tahun daftar akun lebih dari atau sama dengan 3 dan saldo akun lebih dari atau sama dengan 1 miliar
        if self.tahun_daftar >= 3 and self.saldo >= 1000000000:
            # Jika ya, suku bunga bulanan diatur menjadi 1 persen
            bunga_bulanan = 0.01
        # Jika tidak, memeriksa apakah tahun daftar akun kurang dari 3 dan saldo akun lebih dari atau sama dengan 1 miliar
        elif self.tahun_daftar < 3 and self.saldo >= 1000000000:
            # Jika ya, suku bunga bulanan diatur menjadi 2 persen
            bunga_bulanan = 0.02
        # Jika tidak memenuhi kriteria di atas, suku bunga bulanan diatur menjadi 3 persen    
        else:
            bunga_bulanan = 0.03

        # Menampilkan suku bunga bulanan ke layar dengan format tertentu
        print(f"Suku bunga: {bunga_bulanan*100}% per bulan.")
        
class AkunSilver(AkunBank):  # Membuat kelas AkunSilver yang mewarisi sifat dari AkunBank
    def __init__(self, nama, tahun_daftar, saldo):  # Membuat method konstruktor dengan parameter nama, tahun daftar, saldo
        super().__init__(nama, tahun_daftar, saldo) # Memanggil method konstruktor kelas induk

    def transfer_saldo(self, jumlah):  # Membuat method transfer_saldo dengan parameter jumlah
        self.tahun_daftar = 2023 - self.tahun_daftar  # Menghitung lama keanggotaan
        if self.tahun_daftar >= 3 and jumlah > 100000:  # Jika lama keanggotaan >= 3 tahun dan jumlah transfer > 100.000
            biaya_admin = 2000  # Biaya admin = 2000
        else:
            biaya_admin = 5000  # Selain itu biaya admin = 5000

        if jumlah <= 100000:  # Jika jumlah transfer <= 100.000
            biaya_admin = 0  # Biaya admin = 0

        if self.saldo >= jumlah + biaya_admin:  # Jika saldo cukup untuk melakukan transfer
            self.saldo -= jumlah + biaya_admin  # Mengurangi saldo dengan jumlah transfer dan biaya admin
            print(f"Transfer sebesar Rp {jumlah} berhasil dilakukan. Biaya admin: Rp {biaya_admin}.")  # Menampilkan pesan berhasil transfer
        else:  # Jika saldo tidak cukup untuk melakukan transfer
            print("Saldo tidak mencukupi untuk melakukan transfer.")

    def lihat_suku_bunga(self):
        # Memeriksa apakah tahun daftar akun lebih dari atau sama dengan 3 dan saldo akun lebih dari atau sama dengan 1 miliar
        if self.tahun_daftar >= 3 and self.saldo >= 10000000:
            # Jika ya, suku bunga bulanan diatur menjadi 1 persen
            bunga_bulanan = 0.01
        # Jika tidak, memeriksa apakah tahun daftar akun kurang dari 3 dan saldo akun lebih dari atau sama dengan 1 miliar
        elif self.tahun_daftar < 3 and self.saldo >= 10000000:
            # Jika ya, suku bunga bulanan diatur menjadi 2 persen
            bunga_bulanan = 0.02
        # Jika tidak memenuhi kriteria di atas, suku bunga bulanan diatur menjadi 3 persen
        else:
            bunga_bulanan = 0.03

        # Menampilkan suku bunga bulanan ke layar dengan format tertentu
        print(f"Suku bunga: {bunga_bulanan*100}% per bulan.")

# Membuat objek akun1 dan akun2 dengan class AkunGold dan AkunSilver
akun1 = AkunGold("ilham",2015,10000000)
akun2 = AkunSilver("yoga",2015,10000000)

print("AKUN GOLD")  # Mencetak keterangan AKUN GOLD
akun1.lihat_saldo()  # Memanggil method lihat_saldo dari akun1
akun1.lihat_suku_bunga()  # Memanggil method lihat_suku_bunga dari akun1
akun1.transfer_saldo(120000)  # Memanggil method transfer_saldo dari akun1
akun1.lihat_saldo()  # Memanggil method lihat_saldo dari akun1 
print()
print("AKUN SILVER")  # Mencetak keterangan AKUN SILVER
akun2.lihat_saldo()  # Memanggil method lihat_saldo dari akun2
akun2.lihat_suku_bunga()  # Memanggil method lihat_suku_bunga dari akun2
akun2.transfer_saldo(120000)  # Memanggil method transfer_saldo dari akun2
akun2.lihat_saldo()  # Memanggil method lihat_saldo dari akun2
