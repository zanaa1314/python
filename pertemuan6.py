# nomor 1 perulangan while 1 
while True:
print("perulangan ini bakal lanjut terus") 

# nomor 2 perulangan while 2 
angka = 5
while angka > 2:
	print(angka)
	angka -= 1

# nomor 3 contoh kasus mengiring angka ganjil dan genap menggunakan while
#membuat variabel angka ganjil dan angka genap
angka_genap = 0
angka_ganjil = 0

#membaca angka pertama
angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

while angka != 0:  # cek apakah angka tidak sama dengan 0
    if angka % 2 == 1:  # mengecek apakah angka ganjil
        angka_ganjil += 1
    else:
        angka_genap += 1

    # membaca angka selanjutnya
    angka = int(input("Masukkan suatu angka atau ketik angka 0 untuk berhenti: "))

# menampilkan total angka
print("Jumlah Angka Ganjil:", angka_ganjil)
print("Jumlah Angka Genap:", angka_genap)

# nomor 4 implementasi while
secret_number = 777

print("Selamat datang di game saya, Muggle!")
print("Masukkan suatu angka dan tebak angka berapa yang saya pilih untuk kamu.")
print("Jadi, berapa angka rahasianya?")

angka = int(input("Masukkan angka: "))

while angka != secret_number:
    print("Hahaha, kamu nyangkut di loop saya")
    angka = int(input("Masukkan angka lagi: "))

print("Selamat, Muggle! kamu bebas sekarang.")

# nomor 5 perulangan for : bandingkan nilai a, b, c, d, e
for a in range(10):
	print("Nilai a saat ini adalah", a)
	
for b in range(2,8):
	print("Nilai b saat ini adalah", b)

for c in range(2,8,3):
	print("Nilai c saat ini adalah", c)
	
for d in range(1,1):
	print("Nilai d saat ini adalah", d)
	
for e in range(2,1): 
	print("Nilai e saat ini adalah", e)

# nomor 6 perulangan dengan for contoh : eksponensial 2 
kuadrat = 1 
for angka in range(11): 
	print("2 pangkat", angka, " adalah", kuadrat)
	kuadrat *= 2

# nomor 7 contoh break dan continue
# Contoh break
print("Instruksi break : ")
for i in range(1,6):
	if i == 4: 
		break
	print("Bagian ini ada di dalam loop",i)
print("Kalo bagian ini, ada di luar loop.")

# Contoh continue 
print("\n Instruksi continue : ")
for i in range(1,5):
	if i == 2:
		continue
	print("Bagian ini juga ada di dalam loop", i)
print("Kalo bagian ini, ada di luar loop juga.")

# nomor 8 implementasi break
secret_number = 888

print("Selamat datang di game saya, Muggle!")
print("Masukkan suatu angka dan tebak angka berapa yang saya pilih untuk kamu.")

while True:
    angka = int(input("Masukkan angka tebakanmu: "))

    if angka == secret_number:
        print("Selamat, Muggle! kamu bebas sekarang.")
        break
    else:
        print("Hahaha, kamu nyangkut di loop saya.")

# nomor 9 implementasi continue
# meminta user memasukkan suatu kata
user_word = input("Masukkan sebuah kata: ")

# mengubah kata menjadi huruf kapital
user_word = user_word.upper()

# membaca setiap huruf dalam kata
for huruf in user_word:
    
    # jika huruf vokal maka dilewati
    if huruf == "A" or huruf == "I" or huruf == "U" or huruf == "E" or huruf == "O":
        continue
    
    # jika bukan vokal maka dicetak
    else:
        print(huruf, end=" ")

# nomor 10 perulanhan while dgn else
i = 1
while 1 < 5: 
	print(i)
	i += 1 
else: 
	print("else :", i)

# nomor 11 perulangan for dgn else
for i in range(5):
	print(i)
else:
	print("else : ", i)
# atau 
i = 222
for i in range(3,1):
	print(i)
else: 
	print("else : ", i

# nomor 12 operasi logika dalam py
x = 100
y = not not x

print(y)

# nomor 13 operasi logical vs bit
x = 15
y = 22

log = x and y
print(log)

bit = x and y
print(bit)

logneg = not x 
print(logneg)

bitneg = ~x
print(bitneg)

# nomor 14 binary shifting
x = 77
x_right = x >> 1 
x_left = x << 2 
print(x, x_left, x_right)

# nomor 15 latihan bitwise operator dan binary shifting
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)