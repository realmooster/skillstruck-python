# # Code Checkpoint

# coins = {
#     "pennies" : 0.01,
#     "nickels" : 0.05,
#     "dimes" : 0.1,
#     "quarters" : 0.25
# }

# coins["silver dollar"] = 1
# coins.pop("pennies")
# print(coins)
# print(len(coins))

# --------------------------------------------------------

# Challenge 1

# dictionary = { 1: "bicycle", 2: "soccer balls", 3: "piano books" }

# one = input(": ")
# two = input(": ")
# three = input(": ")

# dictionary[4] = one ---- all asks for number first
# dictionary[5] = two ---- ^^
# dictionary[6] = three ---- ^^

# print(dictionary)

# --------------------------------------------------------

# Challenge 2

# work = {
# 	"Monday": 3,
# 	"Tuesday": 4, 
# 	"Wednesday": 2,
# 	"Thursday": 1, 
# 	"Friday": 1, 
# }

# work["Saturday"] = 69 
# work.pop("Wednesday")
# print(len(work))

# if "Friday" in work:
# 	print("Friday is in work")

# print(work)

# --------------------------------------------------------

# Challenge 3

# text = [str(n) for n in input().split()]
# times_seen = {} <---- empty dictionary for values

# for word in text:
#     if word in times_seen:
#         times_seen[word] += 1 <--- if an occurence of a word already, adds one to the initial value
#     else:
#         times_seen[word] = 1 <------ if haven't seen word yet, puts a starting input of 1
#     print(times_seen[word]) <----- prints the total value of occurences inside the dictionary "times_seen"

# # --------------------------------------------------------

# Challenge 4

# apple = int(input(": "))
# banana = int(input(": "))
# strawberry = int(input(": "))
# shopping = {}

# if apple > 5:
#     shopping["apples"] = apple - 5

# if banana > 7:
#     shopping["bananas"] = banana - 7

# if strawberry > 3:
#     shopping["strawberries"] = strawberry - 3
# print(shopping)

# --------------------------------------------------------

# Challenge 5

# text = [str(n) for n in input().split()]
# yuh = {}

# for name in text:
#     yuh[name] = "yes"
# print(yuh)

