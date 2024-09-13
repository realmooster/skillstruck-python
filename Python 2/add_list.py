#Checkpoint Code

# flowers = ["rose", "tulip", "lilac", "sunflower"]

# flowers.append("hey")
# flowers.extend(["apple", "hay"])
# flowers.insert(2, "turtle")

#########################################################

#Challenge 1

# treats = ["popcorn", "popsicles", "soda", "chips", "cookies"]

# take1 = input("put a word ")
# take2 = input("put a word ")

# treats.extend([take1,take2])
# print(treats)

#########################################################

#Challenge 2

# old = ["sharpshooter", "volleyball", "water"]
# new = ["pewpew", "notpewpew"]

# old.extend(new)
# print(old)

#########################################################

#Challenge 3 ------------- HARD -------------

# spell = []
# #place holder to put any strings inside
# question = input("What word do you want spelled out?",)

# spell.append(question)
# #adds the input in the list
# spell.extend(question)
# #cuts up the input which is a string into the list
# spell.append(question)
# #adds the input back onto the end
# print(spell)

#########################################################

#Challenge 4

# mitch = int(input("How old is Mitch?"))

# family = ["Amanda", "Levi", "Nicole", "Lilly"]

# if mitch >= 15:
#     family.insert(0, "Mitch")
# elif 15 > mitch >= 13:
#     family.insert(1, "Mitch")
# elif 13 > mitch >= 10:
#     family.insert(2, "Mitch")
# elif 10 > mitch >= 6:
#     family.insert(3, "Mitch")
# else:
#     family.insert(4,"Mitch")

# print(family)

#Challenge 5

my_list = [int(n) for n in input("Input a list of numbers: ").split()] 
cash_back = []

for x in my_list:
    if x >= 5:
        cash_back.append(round(x * 0.1, 1))

print(cash_back)
