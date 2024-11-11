# List
# Menambahkan elemen menggunakan append
angka = [1, 2, 3]
angka.append(4)
print('Angka (menggunakan append):', angka)  # output = [1, 2, 3, 4]

# Menggunakan insert
angka2 = [1, 2, 4, 5]
angka2.insert(2, 3)
print('Angka (menggunakan insert):', angka2)  # output = [1, 2, 3, 4, 5]

# Menghapus elemen
# Menggunakan remove
angka.remove(1)
print('Angka (menggunakan remove):', angka)  # output = [2, 3, 4]

# Menggunakan pop
elemen = angka.pop(2)
print('Angka (menggunakan pop):', angka)  # output = [2, 3]

# Pencarian elemen menggunakan index
index = angka.index(3)
print('Index angka 3:', index)  # output = 1

# Tuple
# Membuat & mengakses elemen
tuple_saya = (1, 2, 3)
elemen = tuple_saya[1]
print('Tuple index ke-1:', elemen)  # output = 2

# Penggabungan tuple
tuple_baru = tuple_saya + (4, 5)
print('Tuple baru:', tuple_baru)  # output = (1, 2, 3, 4, 5)

# Pencarian Tuple (menggunakan operator in)
ada = 2 in tuple_baru
print('Apakah ada angka 2 di variabel tuple_baru?', ada)  # output = True

# Dictionary
# Menambah & mengubah elemen
murid = {'nama': 'Budi', 'umur': 23}
murid['jurusan'] = 'informatika'  # menambah elemen
murid['jurusan'] = 'pertanian'  # mengubah elemen
print('Murid:', murid)

# Menghapus elemen menggunakan pop
umur = murid.pop('umur')
print('Murid (setelah umur dihapus):', murid)

# Pencarian elemen
ada = 'nama' in murid
print('Apakah ada key "nama" pada variabel murid?', ada)  # output True

# Set
# Membuat set dan menambah elemen
set_saya = {1, 2, 3}
set_saya.add(4)
print('Set:', set_saya)  # output = {1, 2, 3, 4}

# Menghapus elemen menggunakan discard
set_saya.discard(3)
print('Hapus set menggunakan discard:', set_saya)  # output = {1, 2, 4}

# Operasi himpunan pada set
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# Gabungan (union)
union_set = set_A.union(set_B)
print('Gabungan:', union_set)  # output = {1, 2, 3, 4, 5, 6, 7, 8}

# Irisan (intersection)
intersection_set = set_A.intersection(set_B)
print('Irisan:', intersection_set)  # output = {4, 5}

# Selisih (difference) untuk set A
difference_set_A = set_A.difference(set_B)
print('Selisih set A:', difference_set_A)  # output = {1, 2, 3}

# Selisih (difference) untuk set B
difference_set_B = set_B.difference(set_A)
print('Selisih set B:', difference_set_B)  # output = {6, 7, 8}
