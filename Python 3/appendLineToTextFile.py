# # Code Checkpoint

# file = open("example.txt", "a")
# file.write("I love programming!")
# print(file.read())

# ---------------------------------------------------------

# Challenge 1

# file = ('letter.txt', 'a')
# file.write("From your Pen Pal")
# print(file.read())

# ---------------------------------------------------------

# Challenge 2

# file = ('report.txt', 'a')
# file.write("Quote was said by Gandhi")
# print(file.read())

# ---------------------------------------------------------

# Challenge 3

response = input("add anything")
file = ('report.txt', 'a')
file.write(response)
print(file.read())