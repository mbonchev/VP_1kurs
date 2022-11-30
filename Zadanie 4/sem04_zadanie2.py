def list_avg(lst, multiplier = 1):
    sum = 0
    divider = 0

    if isinstance(multiplier, int):
        for i in range(len(lst)):
            if isinstance(lst[i], (int, float)):
                lst[i] *= multiplier
                sum += lst[i]
                divider += 1
            elif isinstance(lst[i], str) and lst[i].isnumeric():
                lst[i] = int(lst[i]) * multiplier
                sum += int(lst[i])
                divider += 1
    else:
        "Multiplier is not an integer!"
        return

    if divider == 0:
        print("Error: Division by zero!")
        return
    print("Average is: %.1f" % (sum / divider))

list1 = ['4', 1.5, "@7$", 3.5, (1, "hi")]
list2 = ['6', 3, 3.0]
list3 = ['%$', {}]
list4 = []
list_avg(list1)