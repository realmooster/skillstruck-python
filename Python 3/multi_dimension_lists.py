# Code Checkpoint

# rows = 5
# cols = 5
# list = []

# for i in range(rows):
#     ph = []
#     for j in range(cols):
#         ph.append(5)
#         list.append(ph)
# print(list)

# ---------------------------------------------------------

# Challenge 1

# hey = ["james", "loid", "jacob", "bruno"]
# ln = ["pop", "prince", "flake", "apples"]
# empty = []

# for character in range(len(hey)):
#     yuh = []
#     for last in range(len(ln)):
#         empty.append(hey[character] + " " + ln[last])
# print(empty)

# ---------------------------------------------------------

# Challenge 2

# fruits = ["apple", "grape", "peach", "cinnamon", "vanilla"]
# rows = input("List of Fruits: ").split()
# oops = []

# #Goes through each iteration in rows

# for row in rows:

#     #for each character, "row" it adds to list + first iteration of "fruit". for fruit in fruits is to go through each iteration in fruits.
#     combos = [row + " " + fruit for fruit in fruits]

#     oops.append(combos)
# print(oops)

# ---------------------------------------------------------

# Challenge 3

# cols = [2, 5, 10, 100]
# rows = [int(n) for n in input("numbers to subtract by: ").split()]
# tehe = []
# for row in rows:
#     subtraction = [row - i for i in cols]
#     tehe.append(subtraction)
# print(tehe)