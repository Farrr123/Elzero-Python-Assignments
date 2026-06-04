# num = int(input("Enter a number: "))
# if num == 0:
#     print("please enter a number above 0")
# else:
#     count = 0
#     while num > 1:
#         num -= 1
#         print(num)
#         count += 1
#
#     else :
#         print(f"{count} Numbers Printed Successfully.")

##########################################################

# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
#
# a = 0
# ignored_names = 0
#
# while a < len(friends):
#     friend = friends[a]
#
#     if friend.istitle():
#         print(f"{friend}")
#     else:
#         ignored_names += 1
#     a += 1
#
# print(f"Friends Printed And Ignored Names Count Is {ignored_names}")

##########################################################

# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
#
# while skills:
#     print(f"\"{skills.pop(0)}\"")

##########################################################

my_Friends = []
maximumFriends = 4

while maximumFriends > 0  :
    add_Friend = input("Please Enter Your Friends: ").strip()

    if add_Friend.isupper():
        print("Invalid Name")
        continue
    elif add_Friend.islower():
        formatted_name = add_Friend.capitalize()
        my_Friends.append(formatted_name)
        maximumFriends -= 1
        print(f'Friend {add_Friend} Added => 1st Letter Become Capital')
        print(f"Names Left in List Is {maximumFriends}")
        print(my_Friends)

    else:
        my_Friends.append(add_Friend)
        maximumFriends -= 1
        print(f'Friend {add_Friend} Added')
        print(f"Names Left in List Is {maximumFriends}")
        print(my_Friends)

else:
    print("Maximum Number Of friends Reached")
    print(my_Friends)

##########################################################

# DONE