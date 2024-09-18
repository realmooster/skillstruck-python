#Divides the list into subscripts to then identify them by size. Looks at the first number in each group of 2 by which it is ordered as continues after. (Recursive Algorithim)

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

ask = int(input("#"))

arr.append(ask)

arr.sort()
print(arr)