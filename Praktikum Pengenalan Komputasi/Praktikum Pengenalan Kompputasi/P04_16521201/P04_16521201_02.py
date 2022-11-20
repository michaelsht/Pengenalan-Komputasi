# NIM/Nama  :  16521201/Michael Sihotang
# Tanggal   :  17/11/2021
# Deskripsi :  Problem 2 -> Program menentukan berapa banyak sebuah string dapat membentuk kata berbeda

# KAMUS
# panjang : integer
# string : string
# huruf : array of string
# frekuensi : array of integer

# ALGORITMA
# definisi fungsi faktorial
def faktorial(x):
    # mendeklarasikan fungsi faktorial bilangan
    # Inisialisasi hasil
    hasil = 1
    # ALGORITMA
    for i in range (1, x + 1):
        hasil = hasil * i
    return hasil

# ALGORITMA UTAMA
# Input
panjang = int(input("Masukkan panjang string: "))       # Menginput panjang string
string = input("Masukkan string: ")                     # Menginput string

# Inisialisasi
huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
frekuensi = [0 for i in range(26)]

# Proses
# Menentukan ada berapa karakter yang muncul berulang
for i in range(panjang):
    for j in range(26):
        if string[i] == huruf[j]:
            frekuensi[j] += 1

# Menghitung hasil permutasi
permutasi = faktorial(panjang)

for i in range(26):
    if frekuensi[i] > 1:
        permutasi /= faktorial(frekuensi[i])

# Output
print("String tersebut dapat membentuk", int(permutasi), "kata berbeda")