# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 06 Oktober 2021
# Deskripsi : Problem 3, program Kategori Bilangan

# Kamus
# X : int

# Algoritma
# Memasukkan nilai X
X = int(input("Masukkan X: "))

# proses dan output
if X == 0:                          # Untuk menunjukkan bilangan nol
    print("X adalah bilangan nol")
elif X > 0 and X % 2 == 0:          # Untuk menunjukkan bilangan positif genap
    print("X adalah bilangan positif genap")
elif X > 0 and X % 2 != 0:          # Untuk menunjukkan bilangan positif ganjil
    print("x adalah bilangan positif ganjil")
else:                               # Untuk menunjukkan bilangan negatif
    print("X adalah bilangan negatif")