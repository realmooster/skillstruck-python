#Bubble Sort finds the largest number and adds it to the top of the list

ask_user = int(input("What number do u want"))

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

arr.append(ask_user)
arr.sort()
print(arr)