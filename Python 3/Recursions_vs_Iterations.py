# Code Checkpoint

# ask = int(input("Select a number"))
# x = ask
# def factorial(x):
#     if x <= 1:
#         return 1
#     else:
#         return x * (factorial(x-1))

# print(factorial(x))

# -------------------------------------------------------

# Challenge 1

# list_of_nums = [int(n) for n in input().split()]

# def add_list(list_of_nums):
#     if len(list_of_nums) == 1: 
#         return list_of_nums[0]
#     else:
#         return list_of_nums[0] + add_list(list_of_nums[1:]) 

# print(add_list(list_of_nums))

# -------------------------------------------------------

# Challenge 1
fibonacci_list = []

userinput = int(input('a number'))
n = userinput
def fibonacci_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

for i in range(userinput):
    fibonacci_list.append(fibonacci_sequence(i))
print(fibonacci_list)

