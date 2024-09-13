year = int(input("Give me a year: "))
#If the code is divisible by 400 it should be a leap year.
if year % 400 == 0:
    print("Leap")
#If the year is divisible by 100 meaning it ends in 00 it is not a leap year.
elif year % 100 == 0: 
    print("Common")
#If it is divisible by 4 it should be a leap year
elif year % 4 == 0:
    print("Leap")
else:
    print("Common")