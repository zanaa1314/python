# nomor 1 
my_list = [3, 1, 9, 7, 5]
swapped = True # inisialisasi awal untuk memasuki loop

while swapped:
	swapped = False # untuk mengindikasi tudak ada pertukaran elemen 
	for i in range(len(my_list) - 1):
		if my_list[i] > my_list[i + 1]:
			swapped = True
			my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
			
print(my_list)

# nomor 2
my_list = []
swapped = True
angka = int(input("Masukkan panjang elemen list yang ingin diurutkan : "))

for i in range(angka):
	val = float(input("Masukkan elemen list : "))
	my_list.append(val)
	
	while swapped:
		swapped = False
		for i in range(len(my_list) - 1):
			if my_list[i] > my_list[i + 1]:
				swapped = True
				my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
				
print("\n Terurut : ")
print(my_list)

# nomor 3
list_aku = [11, 19, 27, 15, 13]
list_aku.sort()
print(list_aku)	

# nomor 4 
list = [10, 7, 9, 6, 8]
list.reverse()
print(list)

# nomor 5
list_1 = [5]
list_2 = list_1
list_1[0]= 10
print(list_2)

# nomor 6
list_saya = [9, 7, 5, 3, 1]
list_baru = list_saya[1:3]
print(list_baru)

# nomor 7
list_saya = [9, 7, 5, 3, 1]
list_baru = list_saya[1:-1]
print(list_baru)

# nomor 8
list_saya = [9, 7, 5, 3, 1]
list_baru = list_saya[-1:1]
print(list_baru)

# nomor 9 
list_saya = [9, 7, 5, 3, 1]
list_baru = list_saya[:3]
print(list_baru)

# nomor 10 
list_saya = [9, 7, 5, 3, 1]
list_baru = list_saya[3:]
print(list_baru)

# nomor 11 
list_saya = [9, 7, 5, 3, 1]
list_baru = list_saya[:]
print(list_baru)

# nomor 12 
list_saya = [9, 7, 5, 3, 1]
del list_saya [1 : 3]
print(list_saya)

# nomor 13 
list_saya = [9, 7, 5, 3, 1]
del list_saya[:]
print(list_saya)

# nomor 14
list_saya = [9, 7, 5, 3, 1]
del list_saya

# nomor 15
list_saya = [10, 15, 20, 25, 30]

print (20 in list_saya)

# nomor 16 
list_saya = [10, 15, 20, 25, 30]

print (20 not in list_saya)

# nomor 17
list_saya = [20, 8, 10, 16, 6, 2, 4, 18, 14, 12, ]
largest = list_saya[0]

for i in range (1, len(list_saya)):
	if list_saya[i] > largest:
		largest = list_saya[i]
	
print(largest)

# nomor 18
list_saya = [20, 8, 10, 16, 6, 2, 4, 18, 14, 12, ]
largest = list_saya[0]

for i in list_saya:
	if i > largest:
		largest = i
	
print(largest)

# nomor 19
list_saya = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False 

for i in range (len (list_saya)):
	found = list_saya[i] == to_find
	if found: 
		break
if found: 
	print("Elemennya ada di indeks ke - ", i)
else: 
	print("Wah elemennya engga ketemu")

# nomor 20
tebakan = [3, 7, 11, 42, 34, 49]
hasil_undi = [5, 9, 11, 42, 3, 49]

jumlah_benar = 0

for angka in tebakan:
    if angka in hasil_undi:
        jumlah_benar += 1

print("Jumlah tebakan yang benar =", jumlah_benar)

# nomor 21 
list_awal = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list_unik = []

for angka in list_awal:
    if angka not in list_unik:
        list_unik.append(angka)

print("List tanpa duplikat:", list_unik)