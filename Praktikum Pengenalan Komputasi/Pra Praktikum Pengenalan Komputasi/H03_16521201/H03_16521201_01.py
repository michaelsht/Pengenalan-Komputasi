# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 03/11/2021
# Deskripsi : Program menuliskan kembali masukan secara terbalik

# Menerima masukan N buah bilangan yang dianggap integer
# Kemudian menuliskan kembali bilangan tersebut secara terbalik

# KAMUS
# N, banyaknya bilangan : int
# TabInt : array of int
# i : int

# ALGORITMA
# Inisialisasi
i = 0

# Input
N = int(input("Masukkan N: "))

# Deklarasi array
# Mengsisinya dengan nilai default 0
TabInt = [0 for i in range(0, N)]

# mengisi array
for i in range(0,N):
    TabInt[i] = int(input())

# mencetak isi array secara terbalik
print("Hasil dibalik: ")
for i in range(N-1, -1, -1):
    print(TabInt[i])
