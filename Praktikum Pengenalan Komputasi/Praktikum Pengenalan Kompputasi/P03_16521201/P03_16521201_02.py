# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 03 November 2021
# Deskripsi : Problem 2 : Program menentukan kondisi akhir tombol.

# KAMUS
# banyaklampu, berapakalimenekan: integer
# tombol : array of integer

# ALGORITMA
# Input banyaklampu dan berapakali menekan tombol
banyaklampu = int(input("Masukkan banyak lampu: "))
berapakalimenekan = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))

# Inisiasi array untuk inputan
# Inisiasi array tombol yang nilainya 0
tombol = [0 for i in range(banyaklampu)]

# Proses
for i in range(berapakalimenekan) :
    # Input tombol yang ditekan 
    n = int(input(f"Tombol yang ditekan ke {i+1}: ")) - 1
    if tombol[n] == 0:      
        tombol[n] = 1               
    else:                                                   
        tombol[n] = 0

    if n+1 != banyaklampu :
        if tombol[n+1] == 0:
            tombol[n+1] = 1
        else:
            tombol[n+1] = 0

    if n != 0:
        if tombol[n-1] == 0 :
            tombol[n-1] = 1
        else:
            tombol[n-1] = 0

# Output
print("Keadaan akhir rangkaian lampu adalah", tombol)