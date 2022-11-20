# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 03/11/2021
# Deskripsi : Program menentukan apakah B anagram dari A atau tidak

# Masukan yang diterima adalah elemen dari A dan B (integer), asumsikan  maksimal 10
# Sebanyak banyakA elemen A dan banyakB elemen dari B

# KAMUS
# banyakA, banyakB = int
# TabIntA, TabIntB = int (maksimal 10)
# x (masukan yang diterima) = int
# a, b : Tabel frekuensi banyakA dan banyakB
# i = int
# j = int

# ALGORITMA
# Inisialisasi
i = 0
j = 0 
# Deklarasi array x
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Deklarasi tabel frekuensi
a = [0 for i in range (0, 11)]
b = [0 for i in range (0, 11)]

# Input
banyakA = int(input("Masukkan banyaknya elemen A: "))
# deklarasi array TabIntA
TabIntA = [0 for i in range(0, banyakA)]
# mengisi array 
for i in range(0, banyakA):
    print("Masukkan elemen A ke-", i+1, " : ", end="")
    TabIntA[i] = int(input())
    for j in range(0,10):
        if TabIntA[i] ==  x[j] :
            a[j] += 1
        else : # TabIntA[i] !=  x[j]
            j += 1

banyakB = int(input("Masukkan banyaknya elemen B: "))
# Deklarasi array TabIntB
TabIntB = [0 for i in range(0, banyakB)]
# Mengisi array
for i in range(0, banyakB):
    print("Masukkan elemen B ke-", i+1, " : ", end="")
    TabIntB[i] = int(input())
    for j in range(0, 10):
        if TabIntB[i] ==  x[j] :
            b[j] += 1
        else : # TabIntB[i] !=  x[j]
            j += 1
# Hasil
if a == b :
    print("B adalah anagram dari A")
else : # banyakA != banyakB or a != b
    print("B bukan anagram dari A")
