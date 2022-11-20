# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 17/11/2021
# Deskripsi : Problem 1 -> Program yang menerima A dan B, lalu menuliskan semua nilai dari f(A), f(A + 1), . . . , f(B)

# KAMUS
# A,B : integer

# Definisi fungsi f(x)
def f(x): 
    # Mendeklarasikan fungsi f(x) = x^2 - 2x + 5
    # ALGORITMA
    y = x**2 - 2*x + 5
    print(y)

# ALGORITMA PROGRAM UTAMA
A = int(input("Masukkan A: "))      # Input nilai A
B = int(input("Masukkan B: "))      # Input nilai B

# Pengondisian apabila nilai A lebih besar daripada nilai B
# Program mengharapkan nilai B lebih besar daripada nilai A
# Menukar nilai A dan B agar program selanjutnya valid
if A > B:   
    A = A + B
    B = A - B
    A = A - B

#  Mencetak nilai f(A) hingga f(B)
for i in range (A, B+1):    
    print("f("+ str(i) +") = ", end="")
    f(i)          