print ("Kalkulator Sederhana")
print ("Pilihan Kalkulasi")
print ("1. Tambah")
print ("2. Kurang")
print ("3. Bagi")
print ("4. Kali")
pil = int(input(">> "))

def add():
    c=a+b
    print ("Hasilnya adalah ",c)
def sub():
    c=a-b
    print ("Hasilnya adalah ",c)
def div():
    c=a/b
    print ("Hasilnya adalah ",c)
def mul():
    c=a*b
    print ("Hasilnya adalah ",c)

if pil == 1:
    a = float(input("Masukan Angka ke-1 >> "))
    b = float(input("Masukan Angka ke-2 >> "))
    add()
elif pil == 2:
    a = float(input("Masukan Angka ke-1 >> "))
    b = float(input("Masukan Angka ke-2 >> "))
    sub()
elif pil == 3:
    a = float(input("Masukan Angka ke-1 >> "))
    b = float(input("Masukan Angka ke-2 >> "))
    div()
elif pil == 4:
    a = float(input("Masukan Angka ke-1 >> "))
    b = float(input("Masukan Angka ke-2 >> "))
    mul()
else:
    print ("Maaf input anda salah")