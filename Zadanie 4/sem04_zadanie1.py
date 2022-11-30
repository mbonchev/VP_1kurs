n = int(input("Input length of dictionary: "))
dict1 = {}
for i in range(n):
    key = input("Input dict key %d: " % (i + 1))
    dict1[key] = input("Input dict value %d: " % (i + 1))

m = int(input("Input length of list: "))
list1 = []
for i in range(m):
    list1.append(input("Input list element %d: " % (i + 1)))

for i in range(m):
    if list1[i] in dict1:
        tempVar = list1[i]
        list1[i] = dict1[tempVar]
        del dict1[tempVar]

print(dict1)
print(list1)