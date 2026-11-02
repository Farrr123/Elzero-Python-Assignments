#############################################

# subjects = {
#     "Math": "90",
#     "Science": "80",
#     "Language": "70"
# }
#
# def get_score(**subjects):
#     for skey, SValue in mysubjects.items():
#         print(f"{skey} => {SValue}")
#
# get_score(Math=90, Science=80, Language=70)

#############################################

# def get_people_scores(*Name, **Skills):
#     if Name:
#         if Skills:
#             print(f"Hello {Name[0]} This Is Your Score Table: ")
#             for key, value in Skills.items():
#                 print(f"{key} => {value}")
#         else:
#             print(f"Hello {Name[0]} You Have No Scores To Show")
#             return
#
#     else:
#         for key, value in Skills.items():
#             print(f"{key} => {value}")
#
#
#
#
# get_people_scores("Osama", Math=90, Science=80, Language=70)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# get_people_scores(Logic=70, Problems=60)
# get_people_scores("Ahmed")

#############################################

# scores_list = {
#     "Math" : "90%",
#     "Science" : "80%",
#     "Language" : "70%"
# }
#
# def get_the_scores(*Name, **Skills):
#     if Name:
#         if Skills:
#             print(f"Hello {Name[0]} This Is Your Score Table: ")
#             for key, value in Skills.items():
#                 print(f"{key} => {value}")
#         else:
#             print(f"Hello {Name[0]} You Have No Scores To Show")
#     else:
#         for key, value in Skills.items():
#             print(f"{key} => {value}")
#
# get_the_scores("Osama")

#############################################

# DONE
