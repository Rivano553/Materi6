angka1 = int(input("Masukan Bilangan Pertama: "))
angka2 = int(input("Masukan Bilangan Kedua: "))
if angka1 > 0 and angka2 > 0 :
    if angka1 < angka2:
        print("Angka Pertama Lebih Kecil Dari Pada Angka Kedua")
    if angka1 == angka2:
        print("Bilangan Pertama Sama Dengan Bilangan Kedua")
    if angka1 > angka2:
        print("Angka Pertama Lebih Besar Dari Pada Angka Kedua")
else:
    print("Bilangan tibah boleh negatif")
