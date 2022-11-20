# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 03/11/2021
# Deskripsi : Program menentukan apakah masukan termasuk palindrom atau tidak

# Masukan yang diterima adalah string dengan panjang N
# Anggap panjang masukan yang diterima sesuai dengan N

# KAMUS
# N = int
# X(string yang akan diubah) = str
# i = int

# ALGORITMA
# Inisialisasi
i = 0
# Input
N = int(input("Masukkan panjang string: "))
X = input("Masukkan string: ")
# Proses
cek = True # cek = true, kesalahan m = belum ditemukan 
for i in range (0, N) :
    if X[i] == X[N-1-i] and cek == True :
        i +=  1
    else :
        cek = False
# Output
if cek == True :
    print(str(X), "adalah palindrom")
else :
    print(str(X), "bukan palindrom")