# logical opertaors = evaluate multiple conditions (or, and, not)
    #    or = True if at least one condition is true
    #   and = True if all conditions are true
    #    not = True if condition is false     

# temp = 36
# is_raining = False
# if temp > 35 or temp < 0 or is_raining:
#     print("The weather is bad today")
# else:
#     print("The weather is good today")

temp = 30
is_raining = False
is_sunny = True
if temp >= 28 and is_sunny and not is_raining:
    print("The is Hot outside ☀️")
    print(" It is ssunny and not raining 🌞")
elif temp <= 0 and is_raining:
    print("The weather is bad today ❄️")
    print("It is cold and raining 🌧️")
elif temp <= 0 and not is_sunny:
    print("The weather is bad today ❄️")
    print("It is cold and not sunny 🌨️")

# 