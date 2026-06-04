######################################################

# def calculate(n1, n2, op = "Add"):
#     op = op.lower()
#     if type(n1) != int or type(n2) != int:
#         print("Invalid Input")
#
#     elif op in ["add", "a"]:
#         return n1 + n2
#
#     elif op in ["subtract", "s"]:
#         return n1 - n2
#
#     elif op in ["multiply", "m"]:
#         return n1 * n2
#
#
# print(calculate(10, 20)) # 30
# print(calculate(10, 20, "AdD")) # 30
# print(calculate(10, 20, "a")) # 30
# print(calculate(10, 20, "A")) # 30
#
# print(calculate(10, 20, "S")) # -10
# print(calculate(10, 20, "subTRACT")) # -10
#
# print(calculate(10, 20, "Multiply")) # 200
# print(calculate(10, 20, "m")) # 200

######################################################

# def addition(*nums):
#     total = 0
#     for num in nums:
#         if num == 10:
#             continue
#         elif num == 5:
#             total -= 5
#         else:
#             total += num
#     return total
#
# print(addition(10, 20, 30, 10, 15)) # 65
# print(addition(10, 20, 30, 10, 15, 5, 100)) # 160

######################################################

# def show_skills(name, *skills):
#     if len(skills) == 0:
#         print(f"Hello {name} You Have No Skills To Show")
#     else:
#         print(f"Hello {name} Your Skills Is")
#         for skill in skills:
#             print(f"- {skill}")
#
# show_skills("Osama", "HTML", "CSS", "JS", "Python")

######################################################

def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"

print(say_hello("Osama", 38, "Egypt"))

######################################################

# DONE