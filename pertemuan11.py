# nomor 1 
def tampilkan_info():          # ← fungsi tanpa parameter
    print("Fungsi dimulai...")
    print("Memproses data...")
    return                     # return tanpa ekspresi (mengembalikan None)
    print("Ini tidak akan dieksekusi!")


# Memanggil fungsi tanpa argumen
hasil = tampilkan_info()       #  dipanggil tanpa argumen

print(f"Nilai kembalian: {hasil}")

# nomor 2 
def cek_status(status):
    print("Mulai proses...")
    
    if status == False:
        return   # return tanpa ekspresi → berhenti di sini
    
    print("Proses berhasil")

cek_status(False)

# nomor 3 
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print("Hasil:", hasil)

# nomor 4 
def fungsi_malas():
    print("Lagi jalan...")
    return 123   # return dengan ekspresi

fungsi_malas()

# nomor 5 
def cek_data(data):
    if data == "":
        return None
    return data

hasil = cek_data("")

if hasil is None:
    print("Data kosong")

# nomor 6 
def nilai_terbesar(lst):
    terbesar = lst[0]
    
    for angka in lst:
        if angka > terbesar:
            terbesar = angka
            
    return terbesar

print(nilai_terbesar([3, 7, 2, 9, 5]))

# nomor 7
def nilai_terbesar(lst):
    terbesar = lst[0]
    
    for angka in lst:
        if angka > terbesar:
            terbesar = angka
            
    return terbesar


print(nilai_terbesar([3, 7, 2, 9, 5]))
print(nilai_terbesar([1, 4, 2]))
print(nilai_terbesar([10, 20, 5, 15]))

# nomor 8 
def buat_list(n):
    data = []
    for i in range(1, n + 1):
        data.append(i)
    return data

print(buat_list(5))

# nomor 9
def tahun_kabisat(tahun):
    # tahun kabisat jika:
    # habis dibagi 4 dan tidak habis dibagi 100
    # atau habis dibagi 400
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False


data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    hasil = tahun_kabisat(th)
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

# nomor 10
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False


def hari_didalam_bulan(tahun, bulan):
    if bulan < 1 or bulan > 12:
        return None

    if bulan == 2:
        return 29 if tahun_kabisat(tahun) else 28

    if bulan in [4, 6, 9, 11]:
        return 30

    return 31


data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    th = data_uji[i]
    bln = data_bulan[i]
    hasil = hari_didalam_bulan(th, bln)
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")

# nomor 11
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False


def hari_didalam_bulan(tahun, bulan):
    if bulan < 1 or bulan > 12:
        return None

    if bulan == 2:
        return 29 if tahun_kabisat(tahun) else 28

    if bulan in [4, 6, 9, 11]:
        return 30

    return 31


def hari_pada_tahun(tahun, bulan, hari):
    if bulan < 1 or bulan > 12:
        return None

    if hari < 1 or hari > hari_didalam_bulan(tahun, bulan):
        return None

    total = 0
    for b in range(1, bulan):
        total += hari_didalam_bulan(tahun, b)

    return total + hari


print(hari_pada_tahun(2000, 12, 31))  # hasil: 366

# nomor 12
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True


for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()

# nomor 13
def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, bilangan):
        if bilangan % i == 0:
            return False
    return True


for i in range(2, 21):
    if cek_prima(i):
        print(i, end=" ")
print()

# nomor 14 
def Liter100km_ke_mpg(liter):
    # 1 mil = 1609.344 meter
    # 1 gallon = 3.785411784 liter
    return 235.214583 / liter


def mpg_ke_Liter100km(mil):
    return 235.214583 / mil


print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.0))

print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))