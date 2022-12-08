pil2 = "y"
while pil2==('y' or "Y"):
        a = int(input("Masukan Angka Anda \n>> "))
        pil = int(input("Masukan Operasi Yang Ingin Dilakukan (1,2,3)\n1. Penjumlahan (+)\n2. Pengurangan (-)\n3. Perkalian (x)\n>> "))
        if pil == 1:
            b = 1
            for i in range (a,0-1):
                print ((a)," + ",b," = ",(a+b))
                b = b + 1
                a = a - 1
            pil2 = input("Apakah anda mau membuat kalkulasi lain? (Y/T)\n>> ")
        elif pil == 2:
            b = 1
            for i in range (a,0,-1):
                print ((a)," - ",b," = ",(a-b))
                b = b + 1
                a = a - 1
            pil2 = input("Apakah anda mau membuat kalkulasi lain? (Y/T)\n>> ")
        elif pil == 3:
            b = 1
            for i in range (a,0,-1):
                print ((a)," x ",b," = ",(a*b))
                b = b + 1
                a = a - 1
            pil2 = input("Apakah anda mau membuat kalkulasi lain? (Y/T)\n>> ")
        else:
            print ("Maaf input anda salah")
            pil2 = input("Apakah anda mau membuat kalkulasi lain? (Y/T)\n>> ")
if pil2 == ('T' or 't'):
    print ("Terima kasih")
else:
    pil2=='y'
