# nomor 1
pion_putih = "A"
baris = [pion_putih for i in range(8)]
print(baris)

# nomor 2
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(data[2][1]) 

# nomor 3 
data = [
    [  
        [1, 2, 3],
        [4, 5, 6]
    ],
    [  
        [7, 8, 9],
        [10, 11, 12]
    ]
]

for layer in data:
    for baris in layer:
        print(baris)
    print()  # spasi antar layer

# nomor 4 
def nama_lengkap(nama1, nama2, nama3):
    print("Nama lengkap:", nama1, nama2, nama3)

nama1 = input("Masukkan nama depan : ")
nama2 = input("Masukkan nama tengah : ")
nama3 = input("Masukkan nama belakang : ")

nama_lengkap(nama1, nama2, nama3)

# nomor 5
hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]

print(hasil)

# nomor 6 
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(data)

# nomor 7
data = [[2, 4], [6, 8], [10, 12]]

# Flatten
hasil = [item for sublist in data for item in sublist]

print(hasil)

# nomor 8
def luas_persegi_panjang(panjang, lebar):
    print("Luas:", panjang * lebar)

# Pemanggilan fungsi
luas_persegi_panjang(8, 5)