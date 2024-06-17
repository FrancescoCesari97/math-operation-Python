
# BASIC OPERATION
# friends = 0

# frineds = friends + 1

# friends += 1

# friends -= 1

# friends *= 2

# friends /= 2

# friends **= 2

# remainder = friends % 2


# BASIC FUNCTION


import math


x = 3.14
y = 4
z = 5

# result = round(x)
# result = abs(y)  # -> distance away from 0 as a whole number
# result = pow(4, 3)  # -> power function
# result = max(x, y, z)
# result = min(x, y, z)


# print(math.pi)
# print(math.e)

# result = math.sqrt(x)
# print(result)

# result = math.ceil(x)
# result = math.floor(x)


# calculate the circumference of a circle


# radius = float(input('Enter the radius of a circle: '))

# circumference = 2 * math.pi * radius

# print(f"the circumference is: {round(circumference, 2)} cm")


# calculate the area of a circle

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"the area is: {round(area, 2)} cm^2")

# NOTE: calculate the hypotenuse of a triangle

A = float(input("Enter A: "))

B = float(input("Enter B: "))

hypotenuse = math.sqrt(pow(A, 2) + pow(B, 2))

print(f"the hypotenuse is {round(hypotenuse)} cm")
