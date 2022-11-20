# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 06 Oktober 2021
# Deskripsi : Problem 2, Program menentukan kelas dan harga tiket

# Kamus
# nomor_kursi = int
# posisi_kursi = str

# Algoritma
# Input
nomor_kursi = int(input("Tentukan Nomor Kursi: "))
posisi_kursi = input("Tentukan Posisi Kersi: ")
# proses
if (nomor_kursi >=1 and nomor_kursi <= 20) or (nomor_kursi >=51 and nomor_kursi <= 60) :
    deskripsi_kelas = "Hot Seat"
    if posisi_kursi == "A" or posisi_kursi == "F" : 
        Harga = 1600000
    elif posisi_kursi == "B" or posisi_kursi == "E" :
        Harga = 1550000
    elif posisi_kursi == "C" or posisi_kursi == "D" :
        Harga = 1500000

elif (nomor_kursi >=21 and nomor_kursi <= 50) or (nomor_kursi >=61 and nomor_kursi <= 100) :
    deskripsi_kelas = "Regular"
    if posisi_kursi == "A" or posisi_kursi == "F" : 
        Harga = 1000000
    elif posisi_kursi == "B" or posisi_kursi == "E" :
        Harga = 950000
    elif posisi_kursi == "C" or posisi_kursi == "D" :
        Harga = 900000
# output
print("Tuan Kil memilih kursi " ,deskripsi_kelas, "dengan harga " , Harga)
