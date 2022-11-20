# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 03 November 2021
# Deskripsi : Problem 1 : Program menentukan berapa huruf vokal dan huruf konsonan dari sebuah string.

# KAMUS
# konsonan, vokal, N : integer
# space, string : string

# ALGORITMA
# Inisialisasi
konsonan = 0
vokal = 0
space = 0
# Input
N = int(input("Masukkan N: "))
string = input("Masukkan string: ")
# Proses
for i in range (N) :
    if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" :
        vokal = vokal + 1
    elif string[i] == " " :
        space = space + 1
    else : 
        konsonan = konsonan + 1
# Output
print(f"Terdapat {vokal} huruf vokal dan {konsonan} huruf konsonan")