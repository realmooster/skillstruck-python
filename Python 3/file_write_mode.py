# Code Checkpoint

# file = open('example.txt', 'w')
# file.write("In short, I love to code!")
# file.close()
# file = open('porcupine.txt', 'w')

# ---------------------------------------------------------

# Challenge 1

# file = open('email.txt','w')
# file.write("Never mind")
# file.close()

# ---------------------------------------------------------

# Challenge 2

answer = input("What do you want to say")
file = open('report.txt', 'w')
file.write(answer)
print(file.read())
file.close