#Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)  # Fixed: Changed 'prices' to 'price'

print("\n------YOUR CART-------")

# Print all foods side-by-side
for food in foods:
    print(food, end=" ")
print()  # Moves to the next line after printing foods

# Calculate the total using sum()
total = sum(prices)

print(f"Your total is: ${total:.2f}")  # Added :.2f to format as a proper currency (e.g., $5.00)
