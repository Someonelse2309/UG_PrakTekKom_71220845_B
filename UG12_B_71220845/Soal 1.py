a = int(input("Silahkan input nomor anda >> "))
print(' '*(a-2),"*")
for b in range ((a-2),0,-1):
    print(' '*(b-1),"**")
print ("**"*a)