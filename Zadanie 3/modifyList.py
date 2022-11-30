n = int(input("Input length of list: "))
inputList = []
for i in range(n):
    inputList.append(int(input("Input %d number: " % (i + 1))))

x = None
while x != 0 and x != 1:
    x = int(input("Input 0 or 1: "))

if x == 0:
    for i in range(n):
        if i % 2 == 0:
            inputList[i] += 5
else:
    for i in range(n):
        if i % 2 == 1:
            inputList[i] += 10

print(inputList)