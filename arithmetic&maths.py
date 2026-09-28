friends = 5
# sum
# friends = friends + 1
# friends += 1

# Subtraction
# friends = friends - 2
# friends -= 2

# mulitiply
# friends = friends * 2
# friends *= 2

# Division
# friends = friends / 2
# friends /= 2

# Modulus (remainder)
# friends = friends % 2
# friends %= 2

# power/exponent,
# friends = friends ** 2
# friends **= 2

# print(friends)


x = 3.14
y = 4
z = 5
# 1. abs() — Absolute value
# Returns the positive value of a number.
# abs(-10)   // 10
# abs(10)    // 10
# result = abs(y)

# round() — Round to nearest integer
# Rounds a decimal number to the nearest whole number.
# round(4.4)   // 4
# round(4.6)   // 5
# result = round(x)

# 3. pow() — Power
# Used to calculate powers.
# result = pow(2, 3)# //-> 2³ = 8 ->// 8

# max() — Maximum value
# Returns the larger of two values.
# result = max(10, 20)  #20 

# min() — Minimum value
# Returns the smaller value.
# min(10, 20)   # 10

# ceil() — Round upward
# Always rounds toward positive infinity.
# result = ceil(4.2)   #// 5
# result = ceil(7.1)   #// 8

# floor() — Round downward
# Always rounds toward negative infinity.
# result = floor(4.9)   #// 4
# result = floor(7.8)   #// 7

# sqrt() — Square root
# result = sqrt(25)   // 5
# result = sqrt(16)   // 4

# print(result)

import math

# print(math.pi) #3.141592653589793
# print(math.e) #2.718281828459045

# radius = float(input('Enter the radius of a circle: '))
# circumference = 2 * math.pi * radius
# print(f"the circumference is :{circumference }")
# print(f"the circumference is :{round(circumference,2)}")

# radius = float(input('Enter the radius of a circle: '))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is: {area}cm^2")


a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"side c ={c}")