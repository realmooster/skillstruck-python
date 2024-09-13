words = input().split(" ")
letter_count = {}

# Count occurrences of each starting letter
for x in words:
    if x[0] not in letter_count:
        letter_count[x[0]] = 1
    else:
        letter_count[x[0]] += 1

# Find the most common starting letter
letters = ""
counting = 0
#After each instance, both letter, and count gets updated from the dictionary. Letter being equivalent to the key and count being equivalent to the value in dict.
for letter, count in letter_count.items():
    if count > counting:
        letters = letter
        counting = count

list_of_words = []

for each_word in words:
    if each_word[0] == letters:
        list_of_words.append(each_word)

# Print the list of words that start with the most common starting letter
for word in list_of_words:
    print(word)
