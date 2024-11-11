# perulangan while
while True:
    print('=' * 50)
    print('Pilih Operasi')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')

    try:
        # Meminta input dari pengguna
        inputUser = int(input('Masukkan pilihan operasi (1/2/3/4): '))
        num1 = float(input('Masukkan Angka Pertama: '))
        num2 = float(input('Masukkan Angka Kedua: '))
        print('')

        # percabangan
        if inputUser == 1:
            hasil = num1 + num2
            print(f'Hasil Penjumlahan: {hasil}')
        elif inputUser == 2:
            hasil = num1 - num2
            print(f'Hasil Pengurangan: {hasil}')
        elif inputUser == 3:
            hasil = num1 * num2
            print(f'Hasil Perkalian: {hasil}')
        elif inputUser == 4:
            if num1 == 0 and num2 == 0:
                print('Hasil tidak terhingga.')
            elif num2 == 0:
                print('Error: Pembagian tidak diperbolehkan dengan 0.')
            else:
                hasil = num1 / num2
                print(f'Hasil Pembagian: {hasil}')
        else:
            print('Masukkan angka operasi dengan benar.')

    except ValueError:
        print('')
        print('Masukkan Angka dengan benar.')

    # Menanyakan apakah pengguna ingin keluar
    print('')
    kondisi = input('Apakah Anda ingin keluar (y/n)? ')
    if kondisi.lower() == 'y':
        break
