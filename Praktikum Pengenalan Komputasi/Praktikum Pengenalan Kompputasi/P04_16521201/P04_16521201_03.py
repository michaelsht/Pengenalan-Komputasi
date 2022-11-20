# NIM/Nama  :  16521201/Michael Sihotang
# Tanggal   :  17/11/2021
# Deskripsi :  Problem 3 -> Program menentukan keliling dari pulau

# KAMUS
# brs, klm : integer
# A : matriks of integer

# ALGORITMA
# Input
brs = int(input("Masukkan nilai brs: "))        # Input nilai baris
klm = int(input("Masukkan nilai klm: "))        # Input nilai kolom

# Deklarasi array untuk memnuat matriks
A = [[0 for j in range(klm)] for i in range(brs)]

# Proses
for i in range(brs):
    for j in range(klm):
        print("Masukkan nilai petak baris", int(i + 1), "kolom", int(j + 1), end= ": ")
        A[i][j] = int(input())

# Inisialisasi keliling
keliling = 0

# Proses
for i in range(brs):
    for j in range(klm):
        if A[i][j] == 1:
            # Mengecek bagian kiri
            if (j == 0):
                keliling = keliling + 1
            elif (A[i][j - 1] == 0):
                keliling = keliling + 1
            
            # Mengecek bagian kanan
            if (j == (klm - 1)):
                keliling = keliling + 1
            elif (A[i][j + 1] == 0):
                keliling = keliling + 1

            # Mengecek bagian atas
            if (i == 0):
                keliling = keliling + 1
            elif (A[i - 1][j] == 0):
                keliling = keliling + 1

            # Mengecek bagian bawah
            if (i == (brs - 1)):
                keliling = keliling + 1
            elif (A[i + 1][j] == 0):
                keliling = keliling + 1

# Output
print("Keliling pulau tersebut adalah", str(keliling) + ".")