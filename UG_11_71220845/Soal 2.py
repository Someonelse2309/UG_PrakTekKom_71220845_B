print ("Alat Pengecek Palindrome")
print ("Masukan kata anda")
a = str(input(">> "))
print ("")
def funPalindrome():
    if a == a[::-1]:
        print ("Palindrome")
        print ("Jika dibalik ",a[::-1])
    else:
        print ("Bukan Palindrome")
        print ("Jika dibalik ",a[::-1])

funPalindrome()