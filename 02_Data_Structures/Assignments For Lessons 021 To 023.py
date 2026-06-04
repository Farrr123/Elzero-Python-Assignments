friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends[1])
print(friends.pop(0))
print(friends.pop(1))

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0::2])
print(friends[1::2])

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4:])
print(friends[3:5:])

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends.remove("Ali")
friends.remove("Mahmoud")
friends.insert(3, "Elzero")
friends.insert(4, "Elzero")

print(friends)

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Nasser")
friends.insert(5, "Salem")

print(friends)

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.remove("Nasser"); friends.remove("Osama")  # noqa: E702
friends.remove("Salem")

print(friends)

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)

print(friends)

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort(reverse=True)
print(friends)

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[4][0])
print(technologies[4][-1])

# DONE