contact = []
answer = "y"
#Answer is originally set as "y"
while answer == "y":
    name = input("Name of Contact. First and Last: ")
    #Reassigned answer to an input for y or n which could stop it or loop it
    answer = input("more contacts? : y or n : ")
    contact.append(name)
    #Sorts the contacts alphabetically
    contact.sort()
print(contact)