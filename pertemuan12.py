# nomor 1 
def penjumlahan(x):
    bilangan = 15
    return x + 15

print(penjumlahan(44)) 
print(bilangan) 

# nomor 2 
angka_awal = 5

def tambah_lima(x) :
    return x + angka_awal

print(tambah_lima(10)) 
print(angka_awal) 

# nomor 3 
def tambah_sepuluh(x):  
    angka = 10          
    return x + angka    

print(tambah_sepuluh(15)) 

# nomor 4 
bilangan = 5
print(bilangan)

def return_bilangan():
	global bilangan
	bilangan = 2 
	return bilangan 
	
print(return_bilangan())
print(bilangan)

# nomor 5 
def hitung_imt(berat, tinggi):
    imt = berat / (tinggi * tinggi)
    return imt

# input dari user
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

# hitung IMT
index_massa_tubuh = hitung_imt(berat, tinggi)

# kategori
kategori = ["Normal", "Gemuk", "Obesitas"]

# penentuan kategori
if 18.5 <= index_massa_tubuh <= 25.0:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[0])
elif 25.0 < index_massa_tubuh <= 27.0:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[1])
else:
    print("Index massa tubuh anda adalah", round(index_massa_tubuh, 2), "termasuk kategori", kategori[2], "- Anda harus diet!")

# nomor 6
def cek_segitiga(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Sisi tidak valid"
    
    return "Segitiga valid" if (a + b > c and b + c > a and c + a > b) else "Bukan segitiga"

print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 1, 3))

# nomor 7 
def segitiga2(n):
    # perulangan dari n sampai 1 (mundur)
    for i in range(n, 0, -1):
        # mencetak bintang sebanyak i
        print("*" * i)

# memanggil fungsi dengan nilai 5
segitiga2(5)

# nomor 8 
def segitiga3(n):
    # perulangan dari 1 sampai n
    for i in range(1, n + 1):
        # " " * (n - i) untuk spasi di depan
        # "*" * i untuk jumlah bintang
        print(" " * (n - i) + "*" * i)

# memanggil fungsi
segitiga3(5)

# nomor 9 
def faktorial(n):
    hasil = 1  # nilai awal

    # perulangan dari 1 sampai n
    for i in range(1, n + 1):
        hasil *= i  # hasil dikali i

    return hasil  # mengembalikan hasil

angka = 5
print("Faktorial dari", angka, "adalah", faktorial(angka))

# nomor 10 
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    hasil_jumlah = 0  

    for _ in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2
        elem_1 = elem_2
        elem_2 = hasil_jumlah

    return elem_2

for i in range(1, 10):
    print(i, "->", fibonacci(i))

# nomor 11 
def factorial(n):
    if n < 0:
        return None      
    if n == 0 or n == 1:
        return 1             
    return n * factorial(n - 1)

for i in range(6):
    print(i, "->", factorial(i))

# nomor 12 
def fibonacci(n):
    if n < 1:
        return None      
    if n < 3:
        return 1             
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(i, "->", fibonacci(i))