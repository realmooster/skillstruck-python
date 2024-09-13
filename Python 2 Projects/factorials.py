thing = int(input("range of number: "))
total_sum = 0

for x in range(1,thing+1):
#includes the start = 1 inside the loop because it allows each variation of "x" to repeat instead of it being outside, it would mulitply each iteration instead of adding it to each.
    start = 1
    for i in range(1, x+1):
        start *= i
    #For each factorials, it adds it onto the other.
    total_sum += start
print(total_sum)
