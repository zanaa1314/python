# Nomor 1 — Comparison Operator
x=1
y=2
z=1
print(x==y)
print(x==z)
print(x!=y)
print(x!= z)
print(x<y)
print(y<z)
print(x>y)
print(y>z)
print(x<=y)
print(x<=z)
print(y<=z)
print(x>=y)
print(x >= z)
print(y>=z)


# Nomor 2 — Kuis 11
n = int(input("Masukkan nilai n: "))
hasil = n > 100
print(hasil)

# Nomor 3 — Conditional Statement: if tunggal
y = 10

if y == 10:
    print("Jadi nilai y nya adalah 10")

# Nomor 4 — Conditional Statement: Rangkaian if
y = 10

if y > 5:
    print("y lebih besar dari 5")

if y < 10:
    print("y lebih kecil dari 10")

if y == 10:
    print("y nya adalah 10")

# Nomor 5 — Conditional Statement: if-else
y = 10

if y < 10:
    print("y nya lebih kecil dari 10")

else:
    print("y nya lebih besar atau sama dengan 10")

# Nomor 6 — Conditional Statement: if-elif-else
y = 10

if y < 5:
    print("y lebih kecil dari 5")
elif y < 10:
    print("y lebih kecil dari 10")
elif y == 10:
    print("y sama dengan 10")
elif y <= 15:
    print("y lebih besar dari 10 tetapi tidak lebih dari 15")
else:
    print("y lebih besar dari 15")

# Nomor 7 — Membandingkan 2 Angka Input
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

# Memilih angka yang lebih besar
if angka1 > angka2:
    angka_besar = angka1
else:
    angka_besar = angka2

# Menampilkan hasil
print("Angka yang lebih besar adalah", angka_besar)

# Nomor 8 — Kuis 12
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

if angka1 >= angka2 and angka1 >= angka3:
    terbesar = angka1
elif angka2 >= angka1 and angka2 >= angka3:
    terbesar = angka2
else:
    terbesar = angka3

print("Angka terbesar adalah", terbesar)

# Nomor 9 — Fungsi max()
# Membaca 3 angka
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
angka3 = int(input("Masukkan angka ketiga: "))

# Cek angka paling besar
angka_besar = max(angka1, angka2, angka3)

# Print hasil
print("Angka paling besar adalah", angka_besar)

# Nomor 10 — Kuis 13
pendapatan = float(input("Masukkan pendapatan bulanan anda : "))
pajak = 0

# Menghitung pendapatan per tahun
pendapatan_tahunan = pendapatan * 12

# Perhitungan pajak berdasarkan tarif
if pendapatan_tahunan <= 60000000:
    pajak = 0.05 * pendapatan_tahunan
elif pendapatan_tahunan <= 250000000:
    pajak = 0.15 * pendapatan_tahunan
elif pendapatan_tahunan <= 500000000:
    pajak = 0.25 * pendapatan_tahunan
else:
    pajak = 0.30 * pendapatan_tahunan

print("Pajak penghasilan yang harus kamu bayar adalah", pajak, "rupiah")

