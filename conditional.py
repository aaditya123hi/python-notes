#  conditional expressions  = A one -line shortcut for the if-else statement(ternary operator)
#                                            print or assign one of two values based on a condition
#                                             x if condition else y

from unittest import result
a = 6 
b =5
age =20
temperature = 30
user_role = "admin"

num = 10 

# print ("positive"if  num > 0 else "negative")
# result = "EVEN" if num%2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if  a < b else b
# status = "Adult" if age >= 18 else "child"
# weather  = "HOT " if temperature  >= 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)