# TUGAS BESAR PENGENALAN KOMPUTASI 
# KELOMPOK 6 
# KELAS 15 PENGENALAN KOMPUTASI 
# Program Absensi Otomatis 
# Spesifikasi : Program ini mencatat kehadiran mahasiswa pada Mata Kuliah Pengenalan Komputasi 
'''
Anggota 
1. Jan Patrick Yeremia 
2. Jeffa Triana Putra
3. Michael Sihotang
4. Muhammad Dhani Depardi
'''
'''
Kamus
absen               : float (Variabel yang menyimpan jam masuk pada hari senin)
absen2              : float (Variabel yang menyimpan jam masuk pada hari selasa)
AbsenSemester       : float (Variabel yang menyatakan jumlah absen mahasiswa)
DataNama            : array of string (Variabel yang menyimpan data nama pada program absensi otomatis)
DataNIM             : array of string (Variabel yang menyimpan data NIM pada program absensi otomatis)
Data_Mahasiswa      : string (Variabel yang menyimpan data mahasiswa ketika diinput didalam program)
getAbsen            : string (sub program yang menyimpan NIM mahasiswa yang diinput)
getnama             : string (sub program yang menyimpan nama mahasiswa yang diinput)
input_benar         : Sub program yang akan mencocokkan nama dan NIM yang tepat
Loop                : Boolean
nama                : string (Variabel untuk menyimpan nama yang diinput)
NIM                 : string (Variabel untuk menyimpan NIM yang diinput)
setNama             : string (Sub program yang menyimpan nama baru mahasiswa saat diedit)
setAbsen            : string (Sub program yang menyimpan NIM baru mahasiswa saat diedit)

'''

#  Di setiap metode class harus selalu ada self sebagai parameter pertamanya
#  Variabel self merujuk kepada objek dari class tersebut
#  Procedure ada didalam class yang bernama Pengenalan_Komputasi
class Pengenalan_Komputasi:
    # Di setiap metode class harus selalu ada self sebagai parameter pertamanya. Variabel self merujuk kepada objek dari class tersebut.
    # fungsi/prosedur yang didefinisikan di dalam suatu kelas disebut dengan Metode
    def __init__(self, nama, NIM):          # procedure yang pertama kali di jalankan atau di proses yang berfungsi untuk melakukan inisialisasi pembuatan object dari class.
        self.nama = str(nama)               # kita tidak perlu memanggil nama procedurenya dan secara otomatis proses yang terdapat di dalam procedure tersebut akan di jalankan
        self.NIM = str(NIM)
    def getNama(self):                      # procedure untuk menyimpan nama
        return self.nama
    def getAbsen(self):                     # procedure untuk menyimpan NIM
        return self.NIM
    def setNama(self, nama):                # procedure untuk menyimpan nama yang sudah diperbaharui
        self.nama = nama
    def setAbsen(self, NIM):                # procedure untuk menyimpan NIM yang sudah diperbaharui
        self.NIM = NIM

# Database 
# DataNama dan DataNIM yang sudah tersimpan didalam program
# Dalam bentuk array of string
DataNama    = ["Jan Patrick Yeremia", "Jeffa Triana Putra","Michael Sihotang","Muhammad Dhani Depardi"]    #Array yang berisikan nama yang terdaftar
DataNIM     = ["16521231", "16521221", "16521201", "16521211"]                                             #Array yang berisikan NIM yang terdaftar

"""
Jan Patrick Yeremia : 231 [indeks 0 dan 0]
Jeffa Triana Putra : 221 [indeks 1 dan 1]
Michael Sihotang : 201 [indeks 2 dan 2]
Muhammad Dhani Depardi : 211 [indeks 3 dan 3]
"""

# Algoritma
# Program output sebagai judul dari program ketika dijalankan
print("\n")
print("===================================================================")
print("       Selamat Datang Di Aplikasi Absensi otomatis mahasiswa       ")
print("===================================================================")

# Inisialisasi Data_Mahasiswa yaitu kosong dan akan diisi saat program dijalankan
Data_Mahasiswa = {} # Inisialisasi Data_Mahasiswa
# Perintah untuk memasukkan nama dan NIM Mahasiswa
nama    = input("Masukan Nama Mahasiswa : ")
NIM     = input("Masukan NIM : ")
print("\n")
"""
Kamus lokal :
input_benar (nama,NIM)
"""
# Procedure untuk mencocokkan nama dan NIM yang tepat
def input_benar (nama, NIM):
    if nama == DataNama[0] and NIM == (DataNIM[0]): 
        return True
    elif nama == DataNama[1] and NIM == (DataNIM[1]):
        return True
    elif nama == DataNama[2] and NIM == (DataNIM[2]):
        return True
    elif nama == DataNama[3] and NIM == (DataNIM[3]):
        return True
    else:
        return False

# Dijalankannya class Pengenalan_Komputasi
# Menggunakan procedure yang pertama
Mahasiswa = Pengenalan_Komputasi(nama, NIM)

# Pengisian inisialisasi Data_Mahasiswa yaitu nama dan NIM yang diinput
Data_Mahasiswa[NIM] = Mahasiswa

# Proses mencek apakah nama dan NIM yang diinput terdapat dalam arrayy DataNama dan DataNIM
if input_benar(nama,NIM) == True: 
    print("==============Menu Utama===============")
    print(f"Selamat datang {nama} - {NIM}")
    
    # Menampilkan Menu Utama pada aplikasi absensi otomatis ini
    print("============================Menu Utama=============================")
    print("1. Tambah Data       ")
    print("2. Hapus Data        ")
    print("3. Status Kehadiran    ")
    print("4. Data Mahasiswa        ")
    print("5. Edit Nama Mahasiswa   ")
    print("6. Edit NIM Mahasiswa  ")
    print("0. Keluar            ")
        
    # Inisialisasi AbsenSemester sebanyak 0
    AbsenSemester=0 
    # Inisialisasi loop bernilai True
    loop=True
        
    # Selama lopp bernilai True maka prograam akan berjalan
    while loop:
        print("\n\n")
        # Perintah untuk menginput Menu berapa yang akan dijalankan
        menu = input("Masukan Menu : ")
        # Pengondisian apabila memilih menu 1 yaitu Tambah Data
        if menu == "1":
            # Inisialisasi data
            data='y'
            # Menjalankan looping data
            while data=='y':
                # Inisialisasi hari
                hari = 1
                # Menjalankan looping hari
                while hari !=0:
                    print("1. Senin")
                    print("2. Selasa")
                    print("3. Rabu")
                    print("4. Kamis")
                    print("5. Jumat")
                    print("")
                    print("Input Angka saja")
                        
                    # Perintah untuk memasukkan hari absensi
                    print("")
                    hari = input("Pilih hari \t\t: ")
                    print("")
                        
                    # Pengondisian Ketika memilih hari Senin
                    if hari=='1':
                        # Perintah untuk menginput jam masuk
                        print("Absensi dibuka mulai pukul 06.00 sampai dengan pukul 07.00")
                        print("")
                        print("Masukkan Jam Masuk dengan format Jam:Menit")
                        print("")
                        absen=float(input("Jam Masuk \t\t: "))
                            
                        # Pengondisian ketika absensi dilaksanakan pada rentang pukul 06.00 - 07.00
                        if absen <= 7.00 and absen >=6.00 :
                            # AbsenSemester bertambah 1 karena tepat waktu    
                            AbsenSemester+=1
                            print("")
                            print("==============================================")
                            print("Absen Berhasil, Kuliah akan dimulai pukul 7.00")
                            print("==============================================")
                            print("")
                            
                        # Pengondisian ketika absen dilaksanakan sebelum pukul 06.00
                        elif absen < 6.00 :
                            print("")
                            print("=================================")
                            print("Absen belum tersedia di waktu ini")
                            print("=================================")
                            print("")
                    
                        # Pengondisian ketika absen dilaksanakan setelah pukul 07.00
                        # Kondisi ini disebut terlambat
                        elif absen > 7.00 :
                            print("")
                            print("=================================")
                            print("Absen Gagal, Anda sudah terlambat")
                            print("=================================")
                            print("")
                    
                        # Ketika jam yang diinput tidak sesuai
                        else:
                            print("COBA LAGI")

                    # Pengondisian ketika memilih hari selasa
                    elif hari=='2':
                        # Perintah untuk menginput jam masuk
                        print("Absensi dibuka mulai pukul 07.00 sampai dengan pukul 08.00")
                        print("")
                        print("Masukkan Jam Masuk dengan format Jam:Menit")
                        print("")
                        absen2=float(input("Jam Masuk \t\t: "))
                            
                        # Pengondisian ketika absensi dilaksanakan pada rentang pukul 07.00 - 08.00
                        if absen2 <= 8.00 and absen2 >= 7.00 :
                            # AbsenSemester bertambah 1 karena tepat waktu
                            AbsenSemester+=1
                            print("")
                            print("==============================================")
                            print("Absen Berhasil, Kuliah akan dimulai pukul 08.00")
                            print("==============================================")
                            print("")

                        # Pengondisian ketika absen dilaksanakan sebelum pukul 07.00
                        elif absen2 < 7.00 :
                            print("")
                            print("=================================")
                            print("Absen belum tersedia di waktu ini")
                            print("=================================")
                            print("")

                        # Pengondisian ketika absen dilaksanakan setelah pukul 08.00
                        # Kondisi ini disebut terlambat
                        elif absen2 > 8.00:
                            print("")
                            print("=================================")
                            print("Absen Gagal, Anda sudah terlambat")
                            print("=================================")
                            print("")
                        
                        # Ketika jam yang diinput tidak sesuai
                        else:
                            print("COBA LAGI")

                    # Dikarenakan kelas pengenalan komputasi hanya ada pada hari senin dan selasa
                    # Maka, apabilamenginput 3, 4, ataupun 5
                    # Output memberitahu bahwa Tidak Ada Kelas Pada Hari Tersebut
                    else:
                        print("================================")
                        print("<<<<TIDAK ADA KELAS HARI INI>>>>")
                        print("================================")
                        print("")
                        break
                    break
                break
            
        # Pengondisian ketika memilih menu 2 yaitu menghapus data
        elif menu == "2":
            # Perintah untuk menginput NIM
            input("Masukan NIM : ")
            # Jika NIM ada pada Data_Mahasiswa
            if (NIM in Data_Mahasiswa):
                # Menghapus data tersebut dari Data_Mahasiswa
                del Data_Mahasiswa[NIM]
                
            # Apabila NIM yang diinput tidak sesuai
            else:
                print("Data Tidak Ditemukan")
            
        # Pengondisian ketika memilih menu 3 yaitu Status Kehadiran
        elif menu == "3":
            for i in Data_Mahasiswa:
                # Perintah mencetak Nama Mahasiswa dari Data_Mahasiswa yang disimpan
                print("Nama Mahasiswa : ", Data_Mahasiswa[i].getNama())
                # Perintah mencetak NIM mahasiswa dari Data_Mahasiswa yang disimpan
                print("NIM : ", Data_Mahasiswa[i].getAbsen())
                # Perintah mencetak Angka Kehadiran didalam bentuk %
                print(f"Angka kehadiran {(AbsenSemester/10)*100}%")
            
        # Pengondisian ketika memilih menu 4 yaitu Data Mahasiswa
        elif menu == "4":
            # Pada menu ini harus memasukkan NIM yang digunakan saat login
            print("Apabila anda baru saja mengubah NIM, tetap input NIM pada saat Login")
            print(" ")
            # Perintah untuk memasukkan NIM
            NIM = input("Masukan NIM : ")
            # Pengondisian ketika NIM ada didalam Data_Mahasiswa
            if NIM in Data_Mahasiswa:
                # Perintah mencetak Nama Mahasiswa dan NIM dari Data_Mahasiswa yang disimpan oleh program
                print("Nama Mahasiswa : ", Data_Mahasiswa[NIM].getNama())
                print("NIM : ", Data_Mahasiswa[NIM].getAbsen())
                
            # Pengondisian ketika NIM tidak ada didalam Data_Mahasiswa
            else:
                print("Data Tidak Ditemukan")
            
        # Pengondisian ketika memilih menu 5 yaitu Edit Nama Mahasiswa
        elif menu == "5":
            # Perintah untuk menginput NIM
            NIM = input("Masukan NIM : ")
                
            # Pengondisian ketika NIM ada didalam Data_Mahasiswa
            if NIM in Data_Mahasiswa:
                # Perintah untuk menginput nama baru
                namaBaru = input("Masukan Nama Baru : ")
                # namaBaru yang diinput hanya bisa nama yang sudah ada didalam array
                if namaBaru == "Jan Patrick Yeremia" :
                    # Nama mahasiswa akan berganti menjadi namaBaru
                    # Menggunakan procedure setNama
                    Data_Mahasiswa[NIM].setNama(namaBaru)
                    
                elif namaBaru == "Jeffa Triana Putra" :
                    # Nama mahasiswa akan berganti menjadi namaBaru
                    # Menggunakan procedure setNama
                    Data_Mahasiswa[NIM].setNama(namaBaru)
                    
                elif namaBaru == "Michael Sihotang" :
                    # Nama mahasiswa akan berganti menjadi namaBaru
                    # Menggunakan procedure setNama
                    Data_Mahasiswa[NIM].setNama(namaBaru)
                    
                elif namaBaru == "Muhammad Dhani Depardi" :
                    # Nama mahasiswa akan berganti menjadi namaBaru
                    # Menggunakan procedure setNama
                    Data_Mahasiswa[NIM].setNama(namaBaru)
                    
                # Ketika namaBaru yang diinput tidak ada didalam array
                else :
                    print("Nama tidak terdaftar")
                
            # Pengondisian ketika NIM yang diinput tidak ada didalan Data_Mahasiswa
            else:
                print("Data Tidak Ditemukan")
            
        # Pengondisian ketika memilih menu 6 yaitu Edit NIM Mahasiswa
        elif menu == "6":
            # Perintah untuk menginput NIM
            NIM = input("Masukan NIM : ")
                
            # Pengondisian ketika NIM yang diinput ada didalan Data_Mahasiswa
            if NIM in Data_Mahasiswa:
                # Perintah untuk menginput NIM Baru
                absenBaru = input("Masukan NIM Baru : ")
                if absenBaru == "16521201" :
                    # NIM mahasiswa akan berganti menjadi absenBaru
                    # Menggunakan procedure setAbsen
                    Data_Mahasiswa[NIM].setAbsen(absenBaru)
                    
                elif absenBaru == "16521211" :
                    # NIM mahasiswa akan berganti menjadi absenBaru
                    # Menggunakan procedure setAbsen
                    Data_Mahasiswa[NIM].setAbsen(absenBaru)
                    
                elif absenBaru == "16521221" :
                    # NIM mahasiswa akan berganti menjadi absenBaru
                    # Menggunakan procedure setAbsen
                    Data_Mahasiswa[NIM].setAbsen(absenBaru)
                    
                elif absenBaru == "16521231":
                    # NIM mahasiswa akan berganti menjadi absenBaru
                    # Menggunakan procedure setAbsen
                    Data_Mahasiswa[NIM].setAbsen(absenBaru)
                    
                else :
                    print("NIM tidak terdaftar")
                
            # Pengondisian ketika NIM yang diinput tidak ada didalan Data_Mahasiswa
            else:
                print("Data Tidak Ditemukan")
            
        # Pengondisian ketika memilih menu 0
        elif menu == "0":
            # Mencetak informasi bahwa pengguna sudah keluar dari aplikasi absensi
            print("Anda telah keluar dari aplikasi absensi")
            # loop bernilai False maka program selesai
            loop = False
            
        # Pengondisian ketika menginput tidak sesuai perintah
        else:
            print("Command not Found ")

# Pengondisian ketika nama dan NIM yang diinput tidak terdaftar
else:
    print(" ")
    print("Nama atau NIM salah, silakan login kembali")
    print(" ")