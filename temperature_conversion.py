# ⭐ temperature conversion program 🌡️

unit = input("Is this temperature in celsius or fahrenheit? (c/f):")
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = round((temp * 9/5) + 32, 2)
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit == "f":
    temp = round((temp - 32) * 5/9, 2)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is not a valid unit. Please enter 'c' for Celsius or 'f' for Fahrenheit.")