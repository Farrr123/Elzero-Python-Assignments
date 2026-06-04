from enum import unique

my_list = [1, 2, 3, 3, 4, 5, 1]

unique_list = [1, 2, 3, 4, 5]

print(unique_list)
print(type(unique_list))
print(unique_list[:-1])

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))
print(nums | letters)
print({*nums, *letters})

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)
my_set.update("A", "B")
my_set.discard("C")
print(my_set)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

user = {
    "HTML" : "90%",
    "CSS" : "80%",
    "Python" : "30%",
    "AI" : "20%"
}

print(f"HTML Progress Is {user['HTML']}")
print(f"CSS Progress Is {user['CSS']}")
print(f"Python Progress Is {user['Python']}")
print(f"AI Progress Is {user['AI']}")

user.update({"JS" : "60%"})
print(f"JS Progress Is {user['JS']}")

# DONE