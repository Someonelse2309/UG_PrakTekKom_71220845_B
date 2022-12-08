a = int(input("Masukan Angka Anda \n>> "))
pil = int(input("Masukan Operasi Yang Ingin Dilakukan (1,2,3)\n1. Penjumlahan (+)\n2. Pengurangan (-)\n3. Perkalian (x)\n>> "))
if pil == 1:
    b = 1
    for i in range (a,0-1):
        print ((a)," + ",b," = ",(a+b))
        b = b + 1
        a = a - 1
elif pil == 2:
    b = 1
    for i in range (a,0,-1):
        print ((a)," - ",b," = ",(a-b))
        b = b + 1
        a = a - 1
elif pill == 3:
    b = 1
    for i in range (a,0,-1):
        print ((a)," x ",b," = ",(a*b))
        b = b + 1
        a = a - 1
else:
    print ("Maaf input anda salah")

