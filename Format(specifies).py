# #  format specifies = {value:flags} format a value based on what
#                                   flags are inserted
# .(number)f =  round to that many decimal places (fixed point )
# :(number) = allocate that many spaces 
# :< = left justify
# :> = right justify 
# :^ = center align 
# :+ = use a plus sign to indicate position value 
# := = place sign to leftmost position
# :    = insert a space before position number 
# : , =  comma separator

price1 = 3458.03965
price2 = -26845.56
price3 = 1255.46

# print(f"price 1 is {price1}")
# print(f"price 2 is {price2}")
# print(f"price 3 is {price3}")

# print(f"price 1 is {price1: .2f}")
# print(f"price 2 is {price2: .2f}")
# print(f"price 3 is {price3: .2f}")


# print(f"price 1 is ${price1: .1f}")  # . digits
# print(f"price 2 is ${price2: .1f}")
# print(f"price 3 is ${price3: .1f}")


# print(f"price 1 is {price1: 10}")# create space price 1 is    3.03165
# print(f"price 2 is {price2: 10}")#price 2 is    -265.56
# print(f"price 3 is {price3: 10}")#price 3 is      12.46

# print(f"price 1 is {price1: 010}")#price 1 is  003.03165
# print(f"price 2 is {price2: 010}")
# print(f"price 3 is {price3: 010}")

# print(f"price 1 is {price1: <10}")|#create space is right side 
# print(f"price 2 is {price2: <10}")
# print(f"price 3 is {price3: <10}")

# print(f"price 1 is {price1: >10}")#create space is left side
# print(f"price 2 is {price2: >10}")
# print(f"price 3 is {price3: >10}")

# print(f"price 1 is {price1: ^10}") # menber is centor
# print(f"price 2 is {price2: ^10}")
# print(f"price 3 is {price3: ^10}")

# print(f"price 1 is {price1:+}")# value type 
# print(f"price 2 is {price2:+}")
# print(f"price 3 is {price3:+}")

print(f"price 1 is {price1:,}")
print(f"price 2 is {price2:,}")
print(f"price 3 is {price3:,}")