# # Code Checkpoint

# ride = {
#     "Nick" : 180,
#     "Tao" : 196,
#     "Frank" : 209,
#     "Brady" : 99,
#     "Grim" : 101
# }

# for x in ride.values():
#     if x >= 100:
#         print("This person is tall enough to ride.")
#     else:
#         print("This person is too short to ride.")

# --------------------------------------------------------

# Challenge 1
 
# dictionary = { 
#     7: "first",
#     3: "second",
#     4: "third",
#     8: "fourth",
#     9: "fifth" 
# }

# my_list = [int(n) for n in input().split()]
 
# for x in my_list:
#     if x in dictionary:
#         print("Yes")
#     else:
#         print("No")

# --------------------------------------------------------

# Challenge 2

# dictionary = {}

# # Get the list of words from user input and split into individual words
# words = input("Create a list of words: ").split()

# # Populate the dictionary with word counts
# for x in words:
#     if x not in dictionary:
#         dictionary[x] = 0
#     dictionary[x] += 1

# # Find the maximum frequency
# max_freq = max(dictionary.values())

# # Collect all words with the maximum frequency
# most_frequent_words = []
# for x, y in dictionary.items():
#     if y == max_freq:
#         most_frequent_words.append(x)
# print(most_frequent_words[0]) <--- the [] makes it so it brings out the value from the list

# --------------------------------------------------------

# Challenge 3

# keys = int(input(": "))

# multiply = {}

# for x in range(keys):
#     thing = x
#     if x not in multiply:
#         multiply[x] = thing*thing
# print(multiply)

# --------------------------------------------------------

# Input the number of word pairs
# yea = int(input(": "))
# dictionary = {}

# # Input each word pair
# for x in range(yea):
#     word = input("Enter word: ")
#     synonym = input("Enter synonym: ")
#     # Add the word and its synonym to the dictionary
#     dictionary[word] = synonym
#     dictionary[synonym] = word

# # Input the word to look up
# lookup_word = input("Enter a word to look up: ")

# # Output the synonym of the entered word
# if lookup_word in dictionary:
#     print(dictionary[lookup_word]) <--- finds the value that is correlated to the key+
# else:
#     print("Word not found in thesaurus.")

# --------------------------------------------------------

# Input the number of vote sections
n = int(input("How many vote sections were collected?"))

votes_total = {}
for _ in range(n):
    candidate = input("name ")
    num_votes = int(input("# "))
    # If the candidate is already in the dictionary, add the new votes to the existing total
    if candidate in votes_total:
        votes_total[candidate] += num_votes
    # If the candidate is not in the dictionary, initialize their vote count
    else:
        votes_total[candidate] = num_votes

# Print the final totals for each candidate
print(votes_total)
