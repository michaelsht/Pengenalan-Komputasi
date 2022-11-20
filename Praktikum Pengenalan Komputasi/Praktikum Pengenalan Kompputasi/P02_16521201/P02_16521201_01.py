# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 27 Oktober 2021
# Deskripsi : Problem 1 : Program menentukan berapa banyak langkah yang diperlukan untuk mengubah N menjadi 1
# Menginput bilangan N lalu menentukan banyak langkah untuk mengubah N menjadi 1

# Kamus
# N : int

# Algoritma
# Menginput nilai N
N = int(input("Masukkan bilangan N: "))

# Inisialisasi
langkah = 0

# Proses
while N > 1 :
    if N%2 == 0 :
        N /= 2
        langkah = langkah + 1
    else : 
        N -= 1
        langkah = langkah + 1

# Output
print(f"Banyak langkah yang diperlukan adalah {langkah}")