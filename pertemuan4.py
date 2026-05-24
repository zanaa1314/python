# Nomor 1
print("Masukkan nama kamu:")
nama_kamu = input()

print("Halo", nama_kamu)


# Nomor 2
nama = input("Masukkan nama kamu: ")

print("Halo", nama)


# Nomor 3
anything = input("Masukkan angka: ")

something = anything ** 2.0

print(anything, "pangkat 2 adalah", something)


# Nomor 4
anything = float(input("Masukkan angka: "))

something = anything ** 2.0

print(anything, "pangkat 2 adalah", something)


# Nomor 5
leg_a = float(input("Masukkan panjang sisi pertama: "))
leg_b = float(input("Masukkan panjang sisi kedua: "))

hypo = (leg_a**2 + leg_b**2) ** 0.5

print("Panjang sisi hipotenusa adalah", hypo)


# Nomor 6
leg_a = float(input("Masukkan panjang sisi pertama: "))
leg_b = float(input("Masukkan panjang sisi kedua: "))

print("Panjang sisi hipotenusa adalah", (leg_a**2 + leg_b**2) ** 0.5)


# Nomor 7
fnam = input("Masukkan nama depan: ")
lnam = input("Masukkan nama belakang: ")

print("Terimakasih.")
print("Nama lengkap anda adalah " + fnam + " " + lnam)


# Nomor 8
print("+" + 10 * "-" + "+")

print(("|" + 10 * " " + "|\n") * 5, end="")

print("+" + 10 * "-" + "+")


# Nomor 9
leg_a = float(input("Masukkan panjang sisi pertama: "))
leg_b = float(input("Masukkan panjang sisi kedua: "))

hypo = str((leg_a**2 + leg_b**2) ** 0.5)

print("Panjang sisi hipotenusa adalah " + hypo)


# Nomor 10
x = input("Masukkan angka: ")

print(type(x))


# Nomor 11
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("Selesai")


# Nomor 12
x = float(input("Masukkan nilai x: "))

y = 1.0 / (x + 1.0 / (x + 1.0 / (x + 1.0 / x)))

print(y)


# Nomor 13
jam = 12
menit = 17
durasi = 59

menit = menit + durasi
jam = jam + menit // 60
menit = menit % 60

print("Waktu selesai:", jam, ":", menit)
