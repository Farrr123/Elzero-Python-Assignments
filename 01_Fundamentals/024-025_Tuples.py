name = ("Fady",)

print(name)
print(type(name))

print("=" * 50)

friends = ("Osama", "Ahmed", "Sayed")

friends_list = list(friends)
friends_list[0] = "Elzero"
friends = tuple(friends_list)

print(friends)
print(type(friends))
print(len(friends))

print("=" * 50)

nums = (1, 2, 3)
letters = ("A", "B", "C")

Nums_and_Letters_One = nums + letters

print("Nums_and_Letters_One =", Nums_and_Letters_One)
print(type(Nums_and_Letters_One))

my_tuple = (1, 2, 3, 4)
a, b, _, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 4

# DONE
