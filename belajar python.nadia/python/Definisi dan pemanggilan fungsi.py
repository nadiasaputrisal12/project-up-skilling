# fungsi
def salam():
  print('Halo, Selamat Datang!')
# memanggil fungsi
salam()

#Fungsi dengan parameter
def salam_nama(nama):
  print(f'Halo, (nama)')
#Pemanggil fungsi
salam_nama('Octavia')

# fungsi dengan multiple parameter
def hitung_penjumlahan(angka1, angka2):
  hasil = angka1 + angka2
  return hasil
#memanggil fungsi
hasil= hitung_penjumlahan(3, 5)
print(f'Hasil penjumlahan: (hasil)')

# fungsi dengan nilai default
def salam_default(nama='teman'):
    print(f'halo, {nama}')

# memanggil fungsi
salam_default()
salam_default('oky')