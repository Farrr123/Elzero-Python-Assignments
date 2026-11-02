# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# operation = input("What operation do you want to do? ").strip()
# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# elif operation == "/":
#     print(num1 / num2)
# elif operation == "%":
#     print(num1 % num2)

################################

# age = 17
# print("App Is Suitable For You" if age >= 16 else "App Is Not Suitable For You")

################################

# age = int(input("Enter Age: ").strip())
#
# if age > 10 and age < 100:
#     months = age * 12
#     weeks = age * 52
#     days = age * 365
#     hours = days * 24
#     minutes = hours * 60
#     seconds = minutes * 60
#     print("You Lived For: ")
#     print(f"{months} Months.")
#     print(f"{weeks} Weeks.")
#     print(f"{days:,} Days.")
#     print(f"{hours:,} Hours.")
#     print(f"{minutes:,} Minutes.")
#     print(f"{seconds:,} Seconds.")
# else:
#     print("your age is incorrect")
#
# months = age * 12
# weeks = age * 52
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

################################

country = input("Please Input Your Country: ").strip().lower()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country == "usa":
    country = "USA"
elif country == "ksa":
    country = "KSA"
else:
    country = country.capitalize()

if country in countries:
    print(
        f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}"
    )
else:
    print(f"Your Country Not Eligible For Discount And The Price Is {price}")

# DONE
