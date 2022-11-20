# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 27/10/2021
# Deskripsi : Problem 2 => Menuliskan bilangan 10^x terkecil yang lebih besar dari N

# Menerima input N dan menuliskan bilangan 10^x terkecil yang lebih besar dari N

# Kamus
# N, a, b = int

# Algoritma
N = int(input("Masukkan N: "))         # Menginput nilai N
a = -1                                  # pangkat awal 
b = 0                                   # calon output

while (N+1 > b) :                       # menguji nilai input
    a = a + 1
    b = 10**a
    
print (b)