# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 03 November 2021
# Deskripsi : Problem 3 : Program menghitung berapa banyak kemunculan sebuah string sebagai sebuah substring pada string lain.

# KAMUS
# panjang1, panjang2 : integer
# string1, string2 : string
# sum : integer

# ALGORITMA
# Input
panjang1 = int(input("Masukkan panjang string 1: "))
string1  = input("Masukkan string 1: ")
panjang2 = int(input("Masukkan panjang string 2: "))
string2  = input("Masukkan string 2: ")

# Inisialisasi
sum = 0

# Proses
for i in range(panjang2 - panjang1 + 1) :
    if string2 [i : i + panjang1] == string1:
        sum = sum + 1

# Output
print(f"String 1 muncul sebanyak {sum} kali.")