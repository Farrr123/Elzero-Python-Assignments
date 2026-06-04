##########################################

# my_nums = [15, 81, 5, 17, 20, 21, 13]
# counter = 0
# my_nums.sort(reverse=True)
#
# for num in my_nums:
#     if num % 5 == 0:
#         counter += 1
#         print(f"#{counter} => {num}")
# print("All Numbers Printed")

##########################################

# my_Range = range(1,21)
# target = [8, 6, 12]
# for num in my_Range:
#     if num in target:
#         continue
#     print(f"{num:02d}")
# print("All Numbers Printed")

##########################################

# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
#
# points = {
#     'A': 100,
#     'B': 80,
#     'C': 40
# }
#
# total_points = 0
# for key, value in my_ranks.items():
#     total_points += points[value]
#     print(f"My Rank in {key} is: {value} And This Equal {points[value]} points.")
#
# print(f"total points {total_points}")

##########################################

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

points = {
    'A': 100,
    'B': 80,
    'C': 40,
    'D': 20,
}


for student in students:
    print(f"\"------------------------------\"\n\"-- Student Name => {student} --\"\n\"------------------------------\"")
    total_points = 0
    for key, value in students[student].items():
            total_points += points[value]
            print(f"- {key} => {points[value]} points")
    print(f"Total Points For {student} Is {total_points}")

##########################################

# DONE