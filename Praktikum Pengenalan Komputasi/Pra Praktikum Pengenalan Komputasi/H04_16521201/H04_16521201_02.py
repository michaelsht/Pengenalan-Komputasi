# NIM/Nama  :  16521201/Michael Sihotang
# Tanggal   :  17/11/2021
# Deskripsi :  Problem 2 -> Program yang menerima N dan M, lalu membaca matriks A berukuran N×M, dan menuliskan
#              berapa banyak bilangan positif di dalam matriks beserta menuliskan isi matriks itu sendiri.

# KAMUS
# N, M : Integer
# A : matriks of integer

# ALGORITMA
# Input N dan M sebagai ukuran baris dan kolom
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))

# Deklarasi array untuk memnuat matriks
A = [[0 for i in range(M)] for i in range(N)] 

# Isisialisasi variabel untuk menghitung jumlah bilangan positif
p = 0 

# Mengisi matriks A
for i in range (N):
    for j in range(M):  
        A[i][j] = int(input("Masukkan Nilai A[{}][{}]: " .format(i+1, j+1)))
        # Menghitung jumlah bilangan positif
        if A[i][j] > 0: 
            p = p + 1      

# Mencetak banyak bilangan positif di matriks
print("Ada", str(p), "bilangan positif di matriks.")

# Mencetak matriks A
for i in range(N):
    for j in range(M):  
        print(A[i][j], end=" ")
    print()
