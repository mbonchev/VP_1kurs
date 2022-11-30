def input_nums(n):
    lst = []

    if isinstance(n, int):
        for i in range(n):
            tempVar = input("Input list element %d: " % (i + 1))
            if tempVar.isnumeric():
                lst.append(tempVar)

    return lst

def sum_list(lst):
    sum = 0
    for i in range(len(lst)):
            if isinstance(lst[i], (int, float)):
                sum += lst[i]      
            elif isinstance(lst[i], str) and lst[i].isnumeric():
                sum += int(lst[i])

    return sum

def max_of_two(a, b):
    greaterNum = ""

    if isinstance(a, (int, float)):
        greaterNum = a
        if isinstance(b, (int, float)):
            if b > a:
                greaterNum = b
    elif isinstance(b, (int, float)):
        greaterNum = b

    return greaterNum



print(input_nums('a'))
list1 = [1, "a", 3.14, "5"]
print(sum_list(list1))
print(max_of_two(2.5, 12))
# print(max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3))))
# print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))