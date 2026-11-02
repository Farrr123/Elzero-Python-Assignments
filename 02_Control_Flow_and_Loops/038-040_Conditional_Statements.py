# Name = input("What\'s Your Name? ")
# Name = Name.capitalize().strip()
# print(f"Hello {Name},Happy To See You Here.")

print("=" * 50)

# Age = int(input("Please enter Your Age? ").strip())
# if Age < 16:
#         print(f"Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# else:
#         print(f"Hello Your Age Is {Age}, All Articles Is Suitable For You")

print("=" * 50)

# fName = input("What is your first name? ").strip().capitalize()
# sName = input("What is your Second name? ").strip().capitalize()
# print(f"Hello {fName} {sName[0]}.")

print("=" * 50)

Email = input("What's your Email?").strip().lower()
UserName = Email[: Email.index("@")]
UserDomain = Email[Email.index("@") + 1 : Email.index(".")]
UserTLDomain = Email[Email.index(".") + 1 :]

print(f"Your Name Is {UserName}")
print(f"Your Domain Is {UserDomain}")
print(f"Your TLDomain Is {UserTLDomain}")

# DONE
