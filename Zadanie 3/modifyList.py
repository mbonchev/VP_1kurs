n = int(input("Input length of list: "))
inputList = []
for i in range(n):
    inputList.append(int(input("Input %d number: " % (i + 1))))

x = None
while x != 0 and x != 1:
    x = int(input("Input 0 or 1: "))

outputList = []
if x == 0:
    for i in range(n):
        if i % 2 == 0:
            outputList.append(inputList[i] + 5)
        else:
            outputList.append(inputList[i])
else:
    for i in range(n):
        if i % 2 == 0:
            outputList.append(inputList[i])
        else:
            outputList.append(inputList[i] + 10)

print(outputList)