import math

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

x = x2 - x1
y = y2 - y1

length = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
print("Довжина вектора = ", round(length, 6))
