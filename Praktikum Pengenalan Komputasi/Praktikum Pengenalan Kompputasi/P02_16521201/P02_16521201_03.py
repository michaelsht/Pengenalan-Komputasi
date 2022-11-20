# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 27 Oktober 2021
# Deskripsi : Problem 3 : Program menentukan nilai maksimal dari perkalian bilangan
# Menginput bilangan N untuk menentukan nilai maksimal dari perkalian bilangan yang berjumlah N

# Kamus
# N : int

# Algoritma
# input 
N = int(input("Masukkan bilangan N : "))
# Inisialisasi
hasil1 = 1
hasil2 = 1
# Inisialisasi variabel baru yaitu k
k = int(N ** 0.5)

# Mencari nilai hasil1
for i in range(N % k):
    hasil1 *= N // k + 1
for i in range(k - N % k):
    hasil1 *= N // k

# Mencari nilai hasil2
k += 1
for i in range(N % k):
    hasil2 *= N // k + 1
for i in range(k - N % k):
    hasil2 *= N // k

# mencari nilai terbesar hasil1 dan hasil2 
if hasil1 < hasil2:
    hasil1 = hasil2
# Untuk N=2 dan N=3
if N == 2 or N == 3:
    hasil1 = N-1

# output
print(f"Nilai maksimalnya adalah {hasil1}")