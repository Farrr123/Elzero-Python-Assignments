"""Examples of raising and handling exceptions."""

NUM = input("Add Your Number: ")

if len(NUM) > 1:
    raise ValueError("Only One Character Allowed")

if not NUM.isdigit():
    raise ValueError("Only Numbers Allowed")

if NUM == "0":
    raise ValueError("Number Must Be Larger Than 0")

print("#" * 20)
print(f"The Number Is {NUM}")
print("#" * 20)


####################################################


LETTER = input("Add Letter From A to Z: ")

try:
    if len(LETTER) != 1:
        raise ValueError("You Must Write One Character Only")

    if LETTER not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        raise ValueError("The Letter Not In A - Z")

except ValueError as error:
    print(error)

else:
    print(f"You Typed {LETTER}")


####################################################


def calculate(num1: int, num2: int) -> int:
    """Return the sum of two numbers."""
    return num1 + num2


print(calculate(20, 30))
