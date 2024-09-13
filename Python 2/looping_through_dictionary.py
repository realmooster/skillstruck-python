# Code Checkpoint

# measurement = {"length" : 1, "width" : 2, "depth" : 19}

# for x in measurement.values():
#     print(x)

# --------------------------------------------------------

# Challenge 1

# aman = int(input("How many in Amanda's group?"))
# jake = int(input("How many in Jane's group?"))

# group = {
# 	"Fred" : 12,
# 	"Jackson" : 15,
# 	"Sophie" : 20,
# 	"Amanda" : aman,
# 	"Jane" : jake,
# }

# total = 0

# for x in group.values():
# 	total += x
	
# print(total)

# --------------------------------------------------------

# Challenge 2
# digit = int(input(": "))
# dip = int(input(": "))
# total = 0

# group = {
#     3: 10,
#     5: 3,
#     10: 6,
#     4: 30,
#     digit: dip
# }

# for x,y in group.items():
#     total += x*y
# print(total)

# --------------------------------------------------------

# # Challenge 3 

# first = int(input("Pick the height of box5: "))		
# group = {
# 	"box1" : 5,
# 	"box2" : 2,
# 	"box3" : 10,
# 	"box4" : 3,
# 	"box5" : first
# }
# total_volume = 0

# for height in group.values():
#     volume = 25 * height <---- all the boxes have the same surface area on the bottom which gets multiplied by the height inputted from the dictionary
#     total_volume += volume
# print(total_volume) 

# --------------------------------------------------------

# Challenge 4
# name = input("What is another name? ")
# shoes = int(input("How many shoes does " + name + " have? "))
# group = {
#     "Sally": 10,
#     "Cameron": 3,
#     "Spencer": 6,
#     name: shoes,
# }

# for x, y in group.items():
#     print(x + " has " + str(y) + " pairs of shoes.")

# --------------------------------------------------------

# Challenge 5


# name = input("a name: ")
# groupOfnames = {
#     4 : "Jared",
#     5 : "McKann",
#     6 : "Kyle",
#     7 : "Summer",
#     8 : name,
# }

# for x in groupOfnames:
#     groupOfnames[x] = groupOfnames[x] + " Nelson" <---- basically the same thing as dictionary[key], which would change the key for each value of "x" 

# print(groupOfnames)
    