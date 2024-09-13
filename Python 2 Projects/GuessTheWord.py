wordbox = ['applesauce"', 'ginger', 'apples', 'pens',
'pineapples', 'building', 'dog', 'cat', 'skateboard', 'airplane', 'existence']

number = int(input("choose a number: "))
this = wordbox[number]

#List is to split a word into individual letters in a list []
letters = list(this)
turns = 12

while turns > 0:
    myletter = input("letter")
    turns -= 1
    if myletter in letters:
        print(myletter)
    if myletter not in letters:
        print("-")
