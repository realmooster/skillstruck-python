# Code Checkpoint

# this_list = ["dog", "cat", "pig", "zebra", "lion", "monkey", "tiger", "fish", "nemo", "adam"]

# def feeding(this_list):
#     if len(this_list) == 1:
#         this_list = this_list[0]
#         print("The " + this_list + " has been fed")
#     else:
#         middle = len(this_list) // 2
#         first_half = this_list[:middle]
#         second_half = this_list[middle:]
#         feeding(first_half)
#         feeding(second_half)
# feeding(this_list)

#Whole point of recursions is to break down the complex tasks into smaller tasks when it can manage
# -------------------------------------------------------
# Challenge 1

# books = [int(n) for n in input("Input an even list of numbers").split()]

# def pairs(books):
#     if len(books) == 2:
#         books = books[0] + books[1]
#         print(books)
#     else:
#         mid = len(books) // 2
#         first_half = books[:mid]
#         second_half = books[mid:]
#         pairs(first_half)
#         pairs(second_half)

# pairs(books)

# -------------------------------------------------------

# Challenge 2

flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]

def visits(flowers):
    if len(flowers) == 1:
        flowers = flowers[0] * 3
        print(flowers)
    else:
        mid = len(flowers) // 2
        first_half = flowers[:mid]
        second_half = flowers[mid:]
        visits(first_half)
        visits(second_half)
visits(flowers)