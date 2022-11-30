x = int(input("Input number: "))\

result = 1
for i in range(1, x + 1):
    result *= i

print("Result: %s" % (result))