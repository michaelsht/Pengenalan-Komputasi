# NIM/Nama  :  16521201/Michael Sihotang
# Tanggal   :  17/11/2021
# Deskripsi :  Problem 1 -> Program menentukan volume rumah yang terbentuk

# Program menerima input panjang sisi kubus dan tinggi limas
# Asumsikan bilangan yang dimasukkan adalah bilangan bulat positif

# KAMUS
# s, t : integer
# hasil : float

# ALGORITMA
# definisi fungsi volume kubus
def kubus(s):
    # Mendeklarasikan volume kubus
    # ALGORITMA
    volume = s**3
    return volume

# definisi fungsi volume limas
def limas(s):
    # Mendeklarasikan volume limas
    # ALGORITMA
    volume = s**2*t/3
    return volume

# ALGORITMA UTAMA
# Input
s = int(input("Masukkan panjang sisi kubus: "))     # Menginput panjang sisi kubus
t = int(input("Masukkan tinggi limas: "))           # Menginput tinggi limas
# Proses
# hasil adalah penjumlahan dari volume kubus dan volume limas
hasil = kubus(s) + limas(s)
# Output
print(f"Volume rumah yang terbentuk adalah {hasil} meter kubik.")