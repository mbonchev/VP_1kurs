# # Old solution
# n = int(input("Input number: "))
# expression = ""

# for i in range(n):
#     for j in range(i + 1):
#         expression += str(n)
#     expression += " + "
# expression = expression[:-3]

# sum = eval(expression)

# print("%s = %d" % (expression, sum))



# New solution
n = int(input("Input number: "))
expression = ""
addition = ""
sum = 0

for i in range(n):
    for j in range(i + 1):
        expression += str(n)
    expression += " + "
    addition += str(n)
    sum += int(addition)
    print(sum)
expression = expression[:-3]

print("%s = %d" % (expression, sum))
