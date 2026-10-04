# python weigth converter

weigth  = float(input("Enter weugth in kg:"))
unit = input("Enter unit to convert to (g, mg, lb, oz): ")

if unit == "g":
    converted_weight = weigth * 1000
    print(f"{weigth} kg is equal to {converted_weight} g")      
elif unit == "mg":
    converted_weight = weigth * 1000000
    print(f"{weigth} kg is equal to {converted_weight} mg")
elif unit == "lb":
    converted_weight = weigth * 2.20462
    print(f"{weigth} kg is equal to {converted_weight} lb") 
elif unit == "oz":
    converted_weight = weigth * 35.274
    print(f"{weigth} kg is equal to {converted_weight} oz")
else:
    print("Invalid unit. Please enter g, mg, lb, or oz.")

print(f"your weigth is:{weigth} kg and converted to {unit} is: {converted_weight} {unit}")