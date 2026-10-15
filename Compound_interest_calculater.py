#  python compound interest calcultor 
# Interest calculation is the process of determining the cost of borrowing money or the earnings from lending and investing money over a specific time period


#  Simple Interest

# Interest is calculated only on the initial principal amount for the entire duration.
# • Formula: \(\text{Simple Interest (SI)} = \frac{P \times R \times T}{100}\)
# • Total Amount (\(A\)): \(A = P + \text{SI}\) or \(A = P(1 + r \times t)\)
# • Common Uses: Short-term personal loans, car loans, and basic savings

# 2. Compound Interest

# Interest is calculated on the initial principal plus all previously accumulated interest from earlier periods, creating exponential growth.
# • Formula: \(A = P \left(1 + \frac{r}{n}\right)^{nt}\)
# 	• (where \(n\) is the number of times interest compounds per year and \(t\) is time in years)
# • Common Uses: Fixed deposits (FDs), long-term investments, and housing or credit card balances.


principle = 0 
rate = 0
time = 0

# while principle <= 0:
#     principle =float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("principle can't be less than or equal to zero")

# while rate <= 0:
#     rate =float(input("Enter the rate amount: "))
#     if rate <= 0:
#         print("rate can't be less than or equal to zero")

# while time <= 0:
#     time =int(input("Enter the time in year: "))
#     if time <= 0:
#         print("time can't be less than or equal to zero")


# # print(principle)
# # print(rate)
# # print(time)

# total = princciple *pow( (1 + rate/100), time)
# print(f"balance after {time} year/s: ${total}")



# while principle < 0:
#     principle =float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("principle can't be less than  zero")

# while rate < 0:
#     rate =float(input("Enter the rate amount: "))
#     if rate < 0:
#         print("rate can't be less than  zero")

# while time < 0:
#     time =int(input("Enter the time in year: "))
#     if time <=0:
#         print("time can't be less than  zero")


# total = principle *pow( (1 + rate/100), time)
# print(f"balance after {time} year/s: ${total}")

