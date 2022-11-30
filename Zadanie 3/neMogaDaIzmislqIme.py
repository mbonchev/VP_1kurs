n = int(input("Input number: "))
expression = ""

for i in range(n):
    for j in range(i + 1):
        expression += str(n)
    expression += " + "
expression = expression[:-3]

sum = eval(expression)

print("%s = %d" % (expression, sum))