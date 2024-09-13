#checkpoint

# lasers = [3, 10, 4, 15, 11]
# print(lasers[2] * 10)
# pi = 3.14159265
# print(round(pi,3))
# for x in range(0,10):
#     print(x)
# for x in range(0,10, 2):
#     print(x)

#########################################################

#Challenge 1 
# shuddup = [int(n) for n in input().split()]
# total = 0
# for x in shuddup:
#     total += x       #(for each "x" in list it continues to add total which is 0 to the  "x")
# print(total)

#########################################################

#Challenge 2
# shuddup = [int(n) for n in input().split()]
# total = 1
# for x in shuddup:
#     total *= x
# print(total)

#########################################################

#Challenge 3
# kudos = ["James", 10, "blue", "Zoe", 8, "red", "Dan", 12, "pink", "Shana", 11, "orange", "Sebastian", 9, "yellow", "Cynthia", 13, "green"]
# user_input = input("name, age, or favorite color: ")
# if user_input == "name":
#     print(kudos[0:16:3])
# elif user_input == "age":
#     print(kudos[1:17:3])
# elif user_input == "favorite color":
#     print(kudos[2:18:3])
# else:
#     print("Invalid Input")

#########################################################

options = [.20, .30, .40, .50, .60, .70]

choice = int(input("Which number will you pick? 0-5")) 

scratch_off = options[choice]

price = 29.95

discount = price * scratch_off

total = price - discount

people = int(input("How many people?"))

per_person = total / people 

print(round(per_person,2))