from functools import reduce

##################################

print("=" * 40)


def remove_chars(text):
    return text[1:-1]


friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# cleaned_list = map(remove_chars, friends_map)
# for name in cleaned_list:
#     print(name)

cleaned_list_lambda = map(lambda text: text[1:-1], friends_map)

for name in cleaned_list_lambda:
    print(name)

##################################

print("=" * 40)


def get_names(friends):
    return friends[-1] == "m"


friends_filter = ["Osama", "Wissam", "Amal", "Essam", "Gamal", "Othman"]

# filtered_names = filter(get_names, friends_filter)
#
# for name in filtered_names:
#     print(name)

filtered_names_lambda = filter(lambda friends: friends[-1] == "m", friends_filter)

for name in filtered_names_lambda:
    print(name)

##################################

print("=" * 40)


nums = [2, 4, 6, 2]


def calculate(*numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


# result = calculate(*nums)
# print(result)

result_lambda = reduce(lambda x, y: x * y, nums)
print(result_lambda)

##################################

print("=" * 40)


skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

reversed_skills = skills[::-1]

for index, skill in enumerate(reversed_skills, start=50):
    if isinstance(skill, int):
        continue

    print(f'"{index} - {skill}"')

##################################

print("=" * 40)

# DONE
