# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 27/10/2021
# Deskripsi : Problem 3 => Menentukan X bilangan prima atau bukan

# Menerima input X dan menuliskan apakah X bilangan prima atau bukan

# Kamus
# X = int

# Algoritma
print("Masukkan X: ", end="")                       # Meminta input nilai X
X = int(input())
habis_dibagi = 0
# habis_dibagi menunjukkan banyak bilangan i yang membagi habis X
i = 1
# Menentukan bilangan prima atau tidak
# Bilangan prima harus bilangan bulat dan positif
# Bilangan prima hanya habis dibagi oleh 1 dan nilai X
if X >= 0 :
    for i in range( 1, X+1 ) :
        if (X % i == 0):                            # X modulo bilangan-bilangan di i 
            habis_dibagi = habis_dibagi + 1         # Banyaknya bilangan i yang membagi habis x ditambah 1
    if habis_dibagi == 2 :                          
            print(int(X), " adalah bilangan prima") # Jumlah Habis_dibagi sama dengan 2 maka menampilkan bilangan prima
    else : # (X % i != 2)
            print(int(X), " bukan bilangan prima")  # Jumlah Habis_dibagi  tidak sama dengan 2 maka  menampilkan bukan bilangan prima
else : # X < 0
    print(int(X), " bukan bilangan prima") 
