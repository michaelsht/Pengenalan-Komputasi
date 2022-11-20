# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 27 Oktober 2021
# Deskripsi : Problem 2 : Program menghitung berapa kali ember x dan ember y perlu diisi penuh untuk kemudian mengisi kolam z
# Menginput x, y, dan z

# Kamus
# x, y, z : int

# Algoritma
# Menginput x, y, dan z
x = int(input("Masukkan x: "))
y = int(input("Masukkan y:  "))
z = int(input("Masukkan z: "))
# Inisialisasi
jumlah_x = 0
jumlah_y = 0
# Proses dan output
for i in range (1, z+1) :
    for j in range (1, z+1) :
        if ((i * x) + (j * y) == z ):       # Menguji kemungkinan jumlah ember x dan ember y untuk mengisi kolam z
            jumlah_x = i                    # Jumlah berapa kali ember x
            jumlah_y = j                    # Jumlah berapa kali ember y

if (jumlah_x == 0 and jumlah_y == 0) :      # Jika jumlah_x dan jumlah_y sama dengan 0
    print("Tidak Mungkin")                  # Maka Tidak Mungkin
else: # Jumlah _x dan jumlah_y tidak sama dengan 0 sehingga mungkin
    print(f"{jumlah_x} kali ember x, {jumlah_y} kali ember y") 