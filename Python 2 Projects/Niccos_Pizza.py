def pizzas(large,medium,small):
    friends = int(input("How many people are eating? "))
    large_count = friends // large
    remainder_friends = friends % large
# Finds how many large pizzas needed then using modulus to find remainer for next
    medium_count = remainder_friends // medium
    remainder_friends %= medium
# The double // means it divides but only finds integers. Modulus for the small pizza
    small_count = remainder_friends // small
# Cannot do just one / because if there's no remainder, it will result to 0.0 with the program only wanting an integer not a float.
    print("You will need", large_count, "large pizzas,",medium_count, "medium pizzas, and", small_count, "small pizzas." )

pizzas(7,3,1)


# or .format