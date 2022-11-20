# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 06 Oktober 2021
# Deskripsi : Problem 1, Menghitung besar pajak 

# Kamus
# penghasilan = int
# pajak = float

# Algoritma
# Input
penghasilan =  int(input("Masukkan penghasilan Tuan Ric: "))
# proses
if penghasilan < 50000000 :                                         # Untuk penghasilan di bawah Rp 50.000.000,00
    pajak = penghasilan * (5/100)                                   # dikenai pajak 5%
elif (penghasilan >= 50000000) and (penghasilan <= 249999999) :     # Untuk penghasilan di dalam rentang Rp 50.000.000,00 - Rp 249.999.999,00
    pajak = penghasilan * (15/100)                                  # dikenai pajak 15%
elif (penghasilan >=150000000) and (penghasilan <= 499999999) :     # Untuk penghasilan di dalam rentang Rp 250.000.000,00 - Rp 4999.999.999,00
    pajak = penghasilan * (25/100)                                  # dikenai pajak 25%
else :                                                              # Untuk penghasilan di atas Rp 499.999.999,00
    pajak = penghasilan * (30/100)                                  # dikenai pajak 30%
# output
print("Pajak yang harus dibayar Tuan Ric sebesar " ,pajak, " rupiah.")