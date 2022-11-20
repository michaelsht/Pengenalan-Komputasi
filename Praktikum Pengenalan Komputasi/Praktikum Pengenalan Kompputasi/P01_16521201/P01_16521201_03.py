# NIM/Nama  : 16521201/Michael Sihotang
# Tanggal   : 06 Oktober 2021
# Deskripsi : Problem 3, Membuat program apakah data Tuan Dip mungkin atau tidak mungkin

# Kamus
# a,b,c = int

# Algoritma
a = int(input("Banyak kaki yang menginjak lantai: "))
b = int(input("Banyak orang tua: "))
c = int(input("Banyak anak: "))

if (a%2 == 0) : 
    if(a == 2 * (b+c)) :
        print("Data Tuan Dip mungkin benar.")
    elif(a > 2 * (b+c)) : 
        print("Data Tuan Dip Tidak Mungkin Benar")
    elif(a < 2 * (b+c)) :
        if (a >= 2 * b) :
            if(c <= 2 * b) :
                print("Data Tuan Dip mungkin benar")
            elif(a > 2 * b) :
                if (a <= 2 * b + 2 * (c% (2*b))) :
                    print("Data Tuan Dip tidak mungkin benar")
                elif (a > 2 * b + 2 * (c% (2*b))) : 
                    print("Data Tuan Dip tidak mungkin benar")
        elif (a < 2 * b) :
            print("Data Tuan Dip tidak mungkin benar")
else : 
    print("Data Tuan Dip tidak mungkin benar")