#mendeklarasikan variabel
x = 10
y = 5

# if
if x > y:
    print('x lebih besar dari y')

# if else
if x < y:
    print('x lebih kecil dari y')
else:
  print('x lebih besar atau sama dengan y') 

#elif
nilai = 75
if nilai >= 90:
   print('Nilai A')
elif nilai >=80:
   print('Nilai B')
elif nilai >= 70:
   print('Nilai C')
else:
  print('Nilai D')

#contoh lain
angka = 8
hasil ='genap' if angka % 2 == 0 else 'ganjil'
print(hasil)
