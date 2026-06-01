# 1.
kucing = ("Caca", "Cici", "Mici")
kucingku = "Joy", "Cemong"
kucing_kosong = ()

print(kucing)
print(kucingku)
print(kucing_kosong)

# 2.
kucing = ("Caca", "Cici", "Mici", "Cemong", "Joy")
print(kucing[0])  
print(kucing[-1]) 
print(kucing[:1]) 
print(kucing[:2])  

for element in kucing:  
    print(element)

# 3.
kucing = ("Caca", "Cici", "Mici", "Cemong", "Joy")
print(kucing)     

kucing.append("Lala")
print(kucing)  

del kucing
print(kucing) 

kucing ["Caca"] = ["chiko"]
print(kucing)

# 4.
nomor = (25, 30, 80, 10, 59)

n1 = nomor + (15, 7)
n2 = nomor *2

print(len(n2))
print(n1)
print(n2)
print(7 in nomor)
print(-7 not in nomor)

# 5.
data = ("Rozaan", 19, "Mahasiswa")

nama, umur, status = data

print(nama)
print(umur)
print(status)

# 6.
mahasiswa = {
    "nama": "Mas Ojan",
    "nomor hp": "2530801080"
}

print(mahasiswa)

# 7.
buku = {
    "judul": "Python Dasar",
    "harga": 75000
}

print(buku["judul"])

# 8.
mobil = {
    "merk": "Toyota",
    "tahun": 2022
}

print(mobil.keys())

# 9.
data_siswa = {"nama": "raffi", "umur": 19, "sekolah": "MAHASISWA 2"}

nilai_saja = data_siswa.values()

print(nilai_saja)

# 10.
mobil = {"merk": "Toyota", "warna": "Hitam"}

pasangan = mobil.items()

print(pasangan)

# 11.
stok = {"apel": 10, "jeruk": 5}

stok_baru = {"jeruk": 12, "mangga": 8}

stok.update(stok_baru)

print(stok)

# 12.
laptop = {"brand": "Asus", "ram": "16GB", "ssd": "512GB"}

item_terakhir = laptop.popitem()

print("Item yang dihapus:", item_terakhir)

print("Sisa dictionary:", laptop)

# 13.
dictionary = {
    "rozaan" : 97,
    "dava" : 85,
    "rapi" : 83,
    "azha" : 99
}

for nama in dictionary.keys():
    print("nilai", nama, "->", dictionary[nama])

dictionary["azha"] = 90
del dictionary["rapi"]

print("\nversi modifikasi")
for nama in dictionary.keys():
    print("nilai", nama, "->", dictionary[nama])

# 14.
try:
    angka = int(input("masukan angka: "))
    hasil = angka * 2 + 15
    print(hasil)

except ValueError:
    print("input harus angka")

# 15.
try:
    angka = int(input("Masukan angka: "))
    hasil = 100 / angka + 15   
    print("Hasil:", hasil)

except (ValueError, ZeroDivisionError):
    print("Terjadi error: input harus angka atau tidak boleh nol")