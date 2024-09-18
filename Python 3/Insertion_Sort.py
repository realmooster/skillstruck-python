# Insertion sort finds the next unsorted value and places it in the next order using index values

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

ask = int(input("#"))

arr.append(ask)

arr.sort()
print(arr)