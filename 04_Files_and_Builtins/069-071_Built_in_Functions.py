print("=" * 50)

#############################################

values = (0, 1, 2)

my_var = 0

if any(values):
    my_var = 0

my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    print("Good")

else:
    print("Bad")

#############################################


v = 40  # For example 5

my_range = list(range(v))  # range (4, 3, 2, 1)

print(sum(my_range, v))
# + pow(v, v, v))  # 820
# pow (base, exp, mod) => power **
# pow(v, v, v)) = 0

print("=" * 50)

#############################################

n = 21

numbers_list = list(range(n))

if round(sum(numbers_list) / n) == max(0, 3, 10, 2, -100, -23, 9):
    print("Good")

# Output => Good

print("=" * 50)

#############################################


# my_all
def my_all(items):
    for item in items:
        if not item:
            return False
    return True


print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False


# my_any
def my_any(items):
    for item in items:
        if item:
            return True
    return False


print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False


# my_min
def my_min(nums):
    for num in nums:
        minimum = num
        break

    for num in nums:
        if num < minimum:
            minimum = num

    return minimum


print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100


# my_max
def my_max(nums):
    for num in nums:
        maximum = num
        break

    for num in nums:
        if num > maximum:
            maximum = num

    return maximum


print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700

print("=" * 50)

#############################################

# DONE
