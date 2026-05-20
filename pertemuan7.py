# nomor 1 
angka = [1, 3, 5, 7, 9, 11, 13]
print("Isi dari list awal : ", angka)

angka [6] = [17]
print ("Ini bagian list baru : ", angka)

angka [1] = angka [5]
print("Ini isi list sekarang : ", angka)

# nomor 2
angka = [1, 3, 5, 7, 9, 11, 13]
print(angka[3])
print(angka)

# nomor 3
angka = [1, 3, 5, 7, 9, 11, 13, 17]
print("Panjang dari list di atas : ", len(angka)) 

# nomor 4 
angka = [ 1, 3, 5, 7, 9, 11, 13, 17] 
del angka[7]
print(len(angka))
print (angka)

# nomor 5
angka = [ 2, 4, 6, 8] 
print(angka[-1])
print(angka[-4])

# nomor 6
topi_list = [1, 2, 3, 4, 5]  # Angka yang tersembunyi di dalam topi pesulap

# minta user input lalu ganti nilai tengah
topi_list[len(topi_list)//2] = int(input("Masukkan angka: "))

# hapus elemen terakhir
topi_list.pop()

# tampilkan panjang list
print(len(topi_list))
print(topi_list)

# nomor 7 
angka = [111, 7, 2, 1]
print(len(angka))
print(angka)

# append
angka.append(4)
print(len(angka))
print(angka)

# insert
angka.insert(1, 222)
print(len(angka))
print(angka)

angka.insert(1, 333)   # Menambahkan 333 di index ke-1
print(len(angka))      # Print panjang list
print(angka)           # Print isi list

# nomor 8
my_list = []  # membuat list kosong

for i in range(5):
    my_list.append(i + 1)

print(my_list)

# nomor 9 
my_list = []  # membuat list kosong

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

# nomor 10
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

# nomor 11 
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

# nomor 12
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

# nomor 13
# Langkah 1: buat list kosong
exo = []

print("Langkah 1:", exo)

# Langkah 2: tambah anggota pakai append()
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")

print("Langkah 2:", exo)

# Langkah 3: tambah anggota pakai perulangan
anggota_baru = ["DO", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]

for i in anggota_baru:
    exo.append(i)

print("Langkah 3:", exo)

# Langkah 4: hapus Kris, Luhan, Tao
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")

print("Langkah 4:", exo)

# Langkah 5: tambah Xiumin di elemen ke-3 dari terakhir
exo.insert(len(exo) - 2, "Xiumin")

print("Langkah 5:", exo)

# jumlah anggota
print("Jumlah anggota exo:", len(exo))