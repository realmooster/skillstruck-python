# --------- Code Checkpoint ---------

# thing = ["one", "two", "three", "four", "five", "six", "seven"]

# print(thing[0:3])

# thing[6] = "yippeee"

# print(thing)
# print(len(thing))

# --------------------------------------------------------

# Challenge 1
# thing = [int(n) for n in input().split()]
# maximum = max(thing)

# print(maximum)

# --------------------------------------------------------

# Challenge 2
# poo = [int(n) for n in input().split()]
# current = poo[0] <---- first digit of lsit

# for x in range(1, len(poo)): <--- matches the range of the list to compare each value to each other 
#     if poo[x] > poo[x-1]: <--- original value and later numbers get compared to number before the current value taken
#         print(poo[x])

# --------------------------------------------------------

#Challenge 3
# yea = [int(n) for n in input().split()]

# yippee = [] <--- new list to input extra numbers in other list / "unique" numbers
# total = 0

# for x in yea:
#     if x not in yippee:
#         yippee.append(x)

# print(len(yippee))

# --------------------------------------------------------

# #Challenge 4
# smth = [int(n) for n in input().split()] 

# for x in range(0, len(smth) - 1, 2): <-------- 'the -1,2 part ensures that there is no index error because it subtracts the len of it by 1 so it wont hit the end of the list and the 2 ensures that it skips 2 each time to get an even number'
#     smth[x], smth[x+1] = smth[x+1], smth[x] <------ swaps the first and second adjecent of list
# print(smth)

# --------------------------------------------------------

# Challenge 5

var = [int(n) for n in input().split()]
total = 0
for x in range(1,len(var) - 1):
    if var[x-1] < var[x] > var[x+1]:
        total +=1
print(total)



