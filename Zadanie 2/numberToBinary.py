x = int(input("Input number to be converted into binary: "))
n = int(input("Input the number position to be checked: "))

x = bin(x)[2:]
print(x)

if int(x[n - 1]) == 1:
    print("The %d number is 1" % (n))
else:
    print("The %d number is 0" % (n))
