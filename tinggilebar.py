def deret (tinggi, lebar):
    for i in range(1, tinggi * lebar + 1):
        if i % lebar == 0 :
            print(i, end = " ")
            print(" ")
        else:
            print(i, end = " ")
        
tinggi = int(input("Masukkan suatu bilangan untuk menentukan tinggi: "))
lebar = int(input("Masukkan suatu bilangan untuk menentukan lebar: "))
angka = deret(tinggi,lebar)
