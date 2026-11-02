Name = "Fady"
Country = "Egypt"
Age = "18"

print(
    '"Hello ' + "'" + Name + "'"
    ", How You Doing"
    ' \\ """ '
    "Your Age Is "
    '"' + Age + '"'
    '" + And Your Country Is: ' + Country
)

print("#" * 50)

print(
    '"Hello ' + "'" + Name + "'"
    ", How You Doing"
    ' \\ \n """ '
    "Your Age Is "
    '"' + Age + '"'
    '" + \nAnd Your Country Is: ' + Country
)

print("#" * 50)

X = "Elzero"

print("second letter Is: " + X[1])
print("third letter Is: " + X[2])
print("last letter Is: " + X[-1])

print("#" * 50)

name = "#@#@Elzero#@#@"

print(name.strip("#@"))

print("#" * 50)

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

print("#" * 50)

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

print("#" * 50)

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

print("#" * 50)

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

print("#" * 50)

name = "Elzero"

print(name.find("z"))

print("#" * 50)

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love", 1))
print(msg.replace("<3", "Love"))

print("#" * 50)

name = "Osama"
age = 38
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

# DONE
