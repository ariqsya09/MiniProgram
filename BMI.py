berat = int(input('Masukkan berat anda ( dalam kg ) : '))
tinggi = int(input('Masukkan tinggi anda ( dalam cm ) : '))
jenisKelamin = input('Jenis kelamin (ketik "l" / "p"): ')
jenisKelaminLow = jenisKelamin.lower()

tinggiFix = tinggi / 100

bmi = int(berat / (tinggiFix * tinggiFix))

if jenisKelaminLow == 'l':
    if bmi < 17:
        print('BMI anda', bmi, ': Anda termasuk dalam kategori kurus')
    elif bmi >= 17 and bmi < 23:
        print('BMI anda', bmi, ': Anda termasuk dalam kategori normal')
    elif bmi >= 23 and bmi < 27:
        print('BMI anda', bmi, ': Anda termasuk dalam kategori kegemukan')
    elif bmi >= 27:
        print('BMI anda', bmi, ': Anda termasuk dalam kategori obesitas')

elif jenisKelaminLow == 'p':
    if bmi < 18:
        print('BMI anda', bmi, ': Anda termasuk dalam kategori kurus')
    elif bmi >= 18 and bmi < 25:
        print('BMI anda', bmi, ': Anda termasuk dalam kategori normal')
    elif bmi >= 25 and bmi < 27:
        print('BMI anda', bmi, ': Anda termasuk dalam kategori kegemukan')
    elif bmi >= 27:
        print('BMI anda', bmi, ': Anda termasuk dalam kategori obesitas')


