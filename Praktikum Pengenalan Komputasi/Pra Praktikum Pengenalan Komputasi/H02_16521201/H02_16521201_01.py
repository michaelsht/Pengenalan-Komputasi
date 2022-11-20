# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 27/10/2021
# Deskripsi : Problem 1 => Menuliskan N bilangan

# Menerima input N untuk menulis angka 1 sampai N

# Kamus
# N : int

# Algoritma
N = int(input("Masukkan N: "))

for i in range(1, N+1):   # Menuliskan angka 1 sampai N
    print(i, end=" ")