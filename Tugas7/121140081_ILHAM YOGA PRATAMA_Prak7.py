import os  # import modul os untuk melakukan operasi pada sistem operasi
import tkinter as tk  # import modul tkinter untuk membuat GUI
from tkinter import filedialog, messagebox  # import beberapa fungsi dari modul tkinter

# Fungsi untuk membuat direktori, menerima parameter path
def create_folder(path):
    # Jika path belum ada, membuat direktori baru
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        # Jika terjadi OSError, menampilkan pesan error dan mengembalikan False
        except OSError:
            messagebox.showerror("Error", "Failed to create directory")
            return False
    # Jika berhasil membuat direktori, mengembalikan True    
    return True

# Fungsi untuk melakukan enkripsi teks menggunakan kunci tertentu
def encrypt_text(key, plaintext):
    # Inisialisasi teks sandi kosong
    ciphertext = ""
    # Inisialisasi indeks kunci ke 0
    key_index = 0
    # Looping untuk setiap karakter di teks masukan
    for char in plaintext:
        # Cek apakah karakter tersebut huruf atau angka
        if char.isalnum():
            # Ambil karakter kunci pada indeks yang sedang diiterasi
            key_char = key[key_index]
            # Ubah karakter kunci menjadi huruf kapital
            key_char = key_char.upper()
            # Hitung jarak pergeseran (shift) berdasarkan huruf kunci
            shift = ord(key_char) - ord('A')
            # Jika karakter tersebut huruf kapital
            if char.isupper():
                # Enkripsi karakter tersebut dengan algoritma Caesar Cipher (menggunakan shift)
                char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            # Jika karakter tersebut huruf kecil
            else:
                # Enkripsi karakter tersebut dengan algoritma Caesar Cipher (menggunakan shift)
                char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            # Pindah ke indeks kunci selanjutnya (dengan loop pada panjang kunci)
            key_index = (key_index + 1) % len(key)
        # Tambahkan karakter tersebut ke dalam teks sandi
        ciphertext += char
    # Kembalikan teks sandi yang telah dihasilkan
    return ciphertext

# Fungsi untuk melakukan dekripsi teks yang telah dienkripsi dengan menggunakan kunci yang sama
def decrypt_text(key, ciphertext):
    # Inisialisasi teks biasa kosong
    plaintext = ""
    # Inisialisasi indeks kunci ke 0
    key_index = 0
    # Looping untuk setiap karakter di teks sandi
    for char in ciphertext:
        # Cek apakah karakter tersebut huruf atau angka
        if char.isalnum():
            # Ambil karakter kunci pada indeks yang sedang diiterasi
            key_char = key[key_index]
            # Ubah karakter kunci menjadi huruf kapital
            key_char = key_char.upper()
            # Hitung jarak pergeseran (shift) berdasarkan huruf kunci
            shift = ord(key_char) - ord('A')
            # Jika karakter tersebut huruf kapital
            if char.isupper():
                # Dekripsi karakter tersebut dengan algoritma Caesar Cipher (menggunakan shift yang sama dengan enkripsi)
                char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            # Jika karakter tersebut huruf kecil
            else:
                # Dekripsi karakter tersebut dengan algoritma Caesar Cipher (menggunakan shift yang sama dengan enkripsi)
                char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            # Pindah ke indeks kunci selanjutnya (dengan loop pada panjang kunci)
            key_index = (key_index + 1) % len(key)
        # Tambahkan karakter tersebut ke dalam teks
        plaintext += char
    # Kembalikan teks biasa yang telah didekripsi
    return plaintext

# Fungsi untuk membuka file yang berisi plaintext
def open_file():
    # Membuka dialog untuk memilih file teks
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    # Jika file dipilih (tidak kosong)
    if file_path:
        # Membuka file teks yang dipilih
        with open(file_path, "r") as f:
            plaintext = f.read()
        # Menghapus teks pada widget teks masukan
        plaintext_text.delete("1.0", "end")
        # Menampilkan isi file pada widget teks masukan
        plaintext_text.insert("end", plaintext)

# Membuat fungsi untuk mengenkripsi file
def encrypt_file():
    key = key_entry.get() # Mengambil input kunci dari pengguna
    plaintext = plaintext_text.get("1.0", "end").strip() # Mengambil input plaintext dari pengguna
    # Menampilkan pesan kesalahan jika kunci atau plaintext tidak dimasukkan
    if not key or not plaintext:
        messagebox.showwarning("Warning", "Please enter key and plaintext")
        return
    # Memanggil fungsi enkripsi dan menyimpan hasil enkripsi ke variabel ciphertext
    ciphertext = encrypt_text(key, plaintext)
    # Menyimpan hasil enkripsi ke file
    save_file(ciphertext)

# Membuat fungsi untuk mendekripsi file
def decrypt_file():
    key = key_entry.get() # Mengambil input kunci dari pengguna
    ciphertext = plaintext_text.get("1.0", "end").strip() # Mengambil input ciphertext dari pengguna
    # Menampilkan pesan kesalahan jika kunci atau ciphertext tidak dimasukkan
    if not key or not ciphertext:
        messagebox.showwarning("Warning", "Please enter key and ciphertext")
        return
    # Memanggil fungsi dekripsi dan menyimpan hasil dekripsi ke variabel plaintext
    plaintext = decrypt_text(key, ciphertext)
    # Menyimpan hasil dekripsi ke file
    save_file(plaintext)

# Membuat fungsi untuk menyimpan hasil enkripsi atau dekripsi ke file
def save_file(ciphertext):
    # Menentukan lokasi direktori untuk menyimpan file hasil enkripsi/dekripsi
    path = os.path.join(os.getcwd(), "encrypted_files")
    # Membuat folder jika belum ada
    if not create_folder(path):
        return
    # Meminta pengguna untuk menentukan lokasi file untuk menyimpan hasil enkripsi/dekripsi
    file_path = filedialog.asksaveasfilename(initialdir=path, defaultextension=".txt")
    # Menulis hasil enkripsi/dekripsi ke file
    if file_path:
        with open(file_path, "w") as f:
            f.write(ciphertext)
        # Menampilkan pesan berhasil jika file berhasil disimpan
        messagebox.showinfo("Success", "File saved successfully")

# Membuat tampilan GUI menggunakan Tkinter
root = tk.Tk() # Membuat instance root
root.title("Vigenere Cipher") # Menentukan judul window

# Membuat header label
header_label = tk.Label(root, text="Vigenere Cipher", font=("Arial", 18))
header_label.pack(pady=10)

# Membuat label dan entry untuk kunci
key_label = tk.Label(root, text="Enter Key:")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack(pady=5)

# Membuat label dan text box untuk plaintext
plaintext_label = tk.Label(root, text="Enter Plaintext:")
plaintext_label.pack()
plaintext_text = tk.Text(root, height=10)
plaintext_text.pack(pady=5)

# Membuat frame untuk button
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Membuat tombol untuk membuka file
open_button = tk.Button(button_frame, text="Open File", command=open_file)
open_button.pack(side="left", padx=5)

# Membuat tombol untuk mengenkripsi
encrypt_button = tk.Button(button_frame, text="Encrypt", command=encrypt_file)
encrypt_button.pack(side="left", padx=5)

# Membuat tombol untuk mendeskripsi
decrypt_button = tk.Button(button_frame, text="Decrypt", command=decrypt_file)
decrypt_button.pack(side="left", padx=5)

# Menampilkan tampilan utama aplikasi dan menunggu input dari pengguna
root.mainloop()
