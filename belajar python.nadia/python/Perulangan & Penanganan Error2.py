# for loop dengan list
angka = [1, 2, 3, 4, 5]
for i in angka:
    print(i)

# for loop dengan range
for i in range(5):
    print(f'Perulangan ke-{i}')

# while loop
i = 0
while i < 5:  # Menghindari infinite loop
    print(f'i bernilai {i}')
    i += 1

# try-except untuk penanganan error
try:
    a = int(input('Masukkan angka pertama: '))
    b = int(input('Masukkan angka kedua: '))
    hasil = a / b
    print(f'Hasil: {hasil}')
except ZeroDivisionError:
    print('Error: Tidak bisa membagi dengan nol!')
except ValueError:
    print('Error: Input harus berupa angka!')

# Menggabungkan perulangan & penanganan error
while True:
    try:
        angka = int(input('Masukkan angka: '))
        print(f'Angka yang dimasukkan: {angka}')
        break
    except ValueError:
        print('Error: Harap masukkan angka yang valid!')
