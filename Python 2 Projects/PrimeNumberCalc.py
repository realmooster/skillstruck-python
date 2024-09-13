prime = int(input('what is a number: '))
#The list provides the factors that are going to be the output if the number is not prime.
factors = []
#Finds out if the number is prime or not and inputs every value that it can be divisible by, not having a remainder
for x in range(2,prime):
    if prime % x == 0:
        factors.append(x)
#Checks the list if theres anything in it and if the number is greater than 2 (If its less than or equal to 2 it is not prime)
if len(factors) == 0 and prime > 2:
    print(str(prime) + " is a prime number")
else:
    print(factors)