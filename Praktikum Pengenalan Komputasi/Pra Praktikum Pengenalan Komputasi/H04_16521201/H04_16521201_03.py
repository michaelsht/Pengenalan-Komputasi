# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 17/11/2021
# Deskripsi : Problem 3 -> Program yang menerima masukan N dan menuliskan matriks segitiga pascal berukuran N×N.

# KAMUS
# N : Integer
# P : matriks of integer

# ALGORITMA
# Input nilai N sebagai ukuran baris dan kolom
N = int(input("Masukkan N: "))

# Deklarasi array untuk memnuat matriks
P = [[0 for j in range(N)] for i in range(N)] # deklarasi array untuk membuat matriks pascal

# Mengisi matriks P
for i in range(N):
    for j in range(N):
        # mengisi baris pertama dengan nilai 1
        if i == 0:
            P[i][j] = 1
        # mengisi baris lainnya berupa jumlah dari elemen kiri dan atasnya
        else:
            P[i][j] = P[i][j-1] + P[i-1][j]
        # mencetak matriks P
        print(P[i][j], end=" ") # mencetak matriks P
    print()