# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 06 Oktober 2021
# Deskripsi : Problem 2, program kalkulator sederhana

#Kamus
# a, b : integer
# c : str

# Jenis operator yang dapat digunakan: 
# + (tambah)
# - (kurang)
# * (kali)
# / (bagi, pembulatan ke bawah)
# % (sisa bagi)

# Algoritma
# input angka pertama
a = int(input("Masukkan angka pertama : "))

# input angka kedua
b = int(input("Masukkan angka pertama : "))

# input jenis operator
c = str(input("Masukkan operator : "))


# proses dan output
if c == '+':                # Melakukan perintah penjumlahan
    print(a, "+", b, "=", a+b)

elif c == '-':              # Melakukan perintah pengurangan
    print(a, "-", b, "=", a-b)

elif c == '*':              # Melakukan perintah perkalian
    print(a, "x", b, "=", a*b)

elif c == "/":              # Melakukan perintah pembagian, pembulatan ke bawah
    print(a, "/", b, "=", a//b)

elif c == "%":              # Melakukan perintah sisa bagi
    print(a, "%", b, "=", a%b)

else:                       # Apabila menginput operator kecuali +, -, *, /, dan %
    print("Tidak dapat diproses")