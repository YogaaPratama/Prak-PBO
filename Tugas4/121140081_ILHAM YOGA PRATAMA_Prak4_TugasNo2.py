print ('NAMA  : ILHAM YOGA PRATAMA')
print ('NIM   : 121140081')
print ('KELAS : RB')
print ('=============================')
print()

class Robot:
    jumlah_turn = 0  # Menginisialisasi jumlah turn robot
    hidup = True  # Menginisialisasi status hidup robot

    def __init__(self, nama, darah, damage):  # Menginisialisasi atribut robot
        self.nama = nama  # Nama robot
        self.darah = int(darah)  # Jumlah darah robot (dikonversi ke integer)
        self.damage = int(damage)  # Jumlah damage robot (dikonversi ke integer)

    def lakukan_aksi(self, robot):  # Method untuk melakukan aksi (serang) ke robot lawan
        if self.nama == "Antares":  # Jika robot ini bernama Antares
            if self.jumlah_turn % 3 == 0:  # Jika jumlah turn ini habis dibagi 3
                self.damage *= 1.5  # Damage robot ini menjadi 1,5 kali lipat
                self.terima_aksi(robot, self.damage)  # Serang robot lawan dengan damage yang baru
                self.damage /= 1.5  # Kembalikan damage robot ini ke semula
            else:
                self.terima_aksi(robot, self.damage)  # Serang robot lawan dengan damage yang tetap
        elif self.nama == "Alphasetia":  # Jika robot ini bernama Alphasetia
            if self.jumlah_turn % 2 == 0:  # Jika jumlah turn ini habis dibagi 2
                self.darah += 4000  # Jumlah darah robot ini bertambah 4000
                self.terima_aksi(robot, self.damage)  # Serang robot lawan dengan damage yang tetap
                print("Alphasetia mendapatkan darah tambahan sebesar 4000 HP")  # Cetak pesan
            else:
                self.terima_aksi(robot, self.damage)  # Serang robot lawan dengan damage yang tetap
        elif self.nama == "Lecalicus":  # Jika robot ini bernama Lecalicus
            if self.jumlah_turn % 4 == 0:  # Jika jumlah turn ini habis dibagi 4
                self.damage *= 2  # Damage robot ini menjadi 2 kali lipat
                self.darah += 7000  # Jumlah darah robot ini bertambah 7000
                self.terima_aksi(robot, self.damage)  # Serang robot lawan dengan damage yang baru
                self.damage /= 2  # Kembalikan damage robot ini ke semula
                print("Lecalicus mendapatkan darah tambahan sebesar 7000 HP")  # Cetak pesan
            else:
                self.terima_aksi(robot, self.damage)  # Serang robot lawan dengan damage yang tetap

    def terima_aksi(self, robot, damage):  # Method untuk menerima serangan dari robot lawan
        if damage > robot.darah:  # Jika damage lebih besar dari jumlah darah robot lawan
            robot.darah = 0  # Jumlah darah robot lawan menjadi 0
            robot.hidup = False  # Status hidup robot lawan menjadi False
            print(f"{robot.nama} menerima damage sebesar {int(damage)} DMG")  # Cetak pesan
            print(f"{robot.nama} telah mati!")  # Cetak pesan
        else:
            # jika damage kurang dari atau sama dengan darah robot
            # kurangi darah robot dengan damage
            robot.darah -= damage
            # cetak pesan damage yang diterima oleh robot
            print(f"{robot.nama} menerima damage sebesar {int(damage)} DMG")

class Antares(Robot):
    def __init__(self):
        # memanggil method init dari class Robot dan memberikan nilai argument sesuai dengan robot Antares
        Robot.__init__(self, "Antares", 50000, 5000)

class Alphasetia(Robot):
    def __init__(self):
        # memanggil method init dari class Robot dan memberikan nilai argument sesuai dengan robot Alphasetia
        Robot.__init__(self, "Alphasetia", 40000, 6000)

class Lecalicus(Robot):
    def __init__(self):
        # memanggil method init dari class Robot dan memberikan nilai argument sesuai dengan robot Lecalicus
        Robot.__init__(self, "Lecalicus", 45000, 5500)

a = True
print("Selamat datang di pertandingan robot Yamako")

#meminta input pilihan robot dan menyimpannya dalam variabel Pilih_robot
Pilih_robot = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
while a:
    # jika Pilih_robot sama dengan 1
    if Pilih_robot == 1:
        # membuat objek MyRobot dengan class Antares
        MyRobot = Antares()
        # menghentikan looping while
        break
    # jika Pilih_robot sama dengan 2
    elif Pilih_robot == 2:
        # membuat objek MyRobot dengan class Alphasetia
        MyRobot = Alphasetia()
        # menghentikan looping while
        break
    # jika Pilih_robot sama dengan 3
    elif Pilih_robot == 3:
        # membuat objek MyRobot dengan class Lecalicus
        MyRobot = Lecalicus()
        # menghentikan looping while
        break
    else :
        #jika user memasukkan input bukan 1,2,3 cetak pesan "Pilihan tidak tersedia!"
        print("Pilihan tidak tersedia!")
        #secara otomatis program akan meminta user memilih ulang nama robot
        Pilih_robot = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))

#meminta input pilihan robot dan menyimpannya dalam variabel Pilih_lawan
Pilih_lawan = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
while a:
    # jika Pilih_robot sama dengan 1
    if Pilih_lawan == 1:
        # membuat objek musuh dengan class Antares
        musuh = Antares()
        # menghentikan looping while
        break
    # jika Pilih_robot sama dengan 2
    elif Pilih_lawan == 2:
        # membuat objek musuh dengan class Alphasetia
        musuh = Alphasetia()
        # menghentikan looping while
        break
    # jika Pilih_robot sama dengan 3
    elif Pilih_lawan == 3:
        # membuat objek musuh dengan class Lecalicus
        musuh = Lecalicus()
        # menghentikan looping while
        break
    else :
        #jika user memasukkan input bukan 1,2,3 cetak pesan "Pilihan tidak tersedia!"
        print("Pilihan tidak tersedia!")
        #secara otomatis program akan meminta user memilih ulang nama robot
        Pilih_lawan = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))

#memberi informasi kekuatan tangan
print("\nSelanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
print()

#perulangan while akan terus berjalan selama robot pemain dan lawan masih hidup
while MyRobot.hidup and musuh.hidup:
    Robot.jumlah_turn += 1 #jumlah turn pada objek kelas Robot ditambah satu pada setiap perulangan
    print(f"Turn saat ini: {Robot.jumlah_turn}") #informasi jumlah turn saat ini
    print(f"Robotmu ({MyRobot.nama} - {int(MyRobot.darah)} HP), robot lawan ({musuh.nama} - {int(musuh.darah)} HP)")#informasi status robot pemain (nama dan HP) dan robot lawan (nama dan HP)

    #input dari pemain untuk memilih tangan yang akan digunakan oleh robot
    My_turn = int(input(f"Pilih tangan robotmu ({MyRobot.nama}) : "))
    while a:
        #While loop akan terus berulang jika input bernilai 1, 2, atau 3
        if My_turn > 0 and My_turn < 4:
            break
        else:
            #jika user memasukkan input bukan 1,2,3 cetak pesan "Pilihan tidak tersedia!"
            print("Pilihan tidak tersedia!")
            #secara otomatis program akan meminta user memilih ulang tangan/kekuatan robot
            My_turn = int(input(f"Pilih tangan robotmu ({MyRobot.nama}) : "))
    Enemy_turn = int(input(f"Pilih tangan robot lawan ({musuh.nama}) : "))
    while a:
        #While loop akan terus berulang jika input bernilai 1, 2, atau 3
        if Enemy_turn > 0 and Enemy_turn < 4:
            break
        else:
            #jika user memasukkan input bukan 1,2,3 cetak pesan "Pilihan tidak tersedia!"
            print("Pilihan tidak tersedia!")
            #secara otomatis program akan meminta user memilih ulang tangan/kekuatan robot
            Enemy_turn = int(input(f"Pilih tangan robot lawan ({musuh.nama}) : "))

    #Menentukan hasil permainan berdasarkan pilihan tangan kedua robot
    if My_turn == 1:
        if Enemy_turn == 1:
            print("Seri!")
        elif Enemy_turn == 2:
            musuh.lakukan_aksi(MyRobot)
        elif Enemy_turn ==3:
            MyRobot.lakukan_aksi(musuh)
    elif My_turn == 2:
        if Enemy_turn == 1:
            MyRobot.lakukan_aksi(musuh)
        elif Enemy_turn == 2:
            print("Seri!")
        elif Enemy_turn ==3:
            musuh.lakukan_aksi(MyRobot)
    elif My_turn == 3:
        if Enemy_turn == 1:
            musuh.lakukan_aksi(MyRobot)
        elif Enemy_turn == 2:
            MyRobot.lakukan_aksi(musuh)
        elif Enemy_turn ==3:
            print("Seri!")
    print()

#menampilkan informasi bahwa pertandingan telah berakhir
print("Pertandingan berakhir!")
