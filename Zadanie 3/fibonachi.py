n = int(input("Input length of sequence: "))
a = 0
b = 1

for i in range(int((n + 1)/ 2)):
    print(a)
    print(b)
    a += b
    b += a