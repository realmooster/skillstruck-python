# Code Checkpoint

# friends = { "Shane" : 10, "Samantha" : 9, "Shiloh" : 12, "Sean" : 11 }

# friends["Sebastian"] = 8

# friends.pop("Shiloh")
# print(friends)

# --------------------------------------------------------

# Challenge 1

# shapes = {
# "Triangle": 8,
# "Circle": 15,
# "Square": 10,
# "Rectangle" : 12
# }

# heyy = input("THINGY: ")
# height = int(input("THINGY: "))

# shapes[heyy] = height

# print(shapes)

# --------------------------------------------------------

# Challenge 2

# trees = { "aspen" : 75, "pine" : 82, "maple" : 60, "oak" : 65, "willow" : 80, "cottonwood" : 100 }
# touchme = input("THINGY: ")
# trees.pop(touchme)
# print(trees)

# --------------------------------------------------------

# Challenge 3

# goals = { "piano" : 5, "run" : 3, "paint" : 2, "serve" : 7, "homework" : 7}

# ello = input("THINGY: ")
# goals.pop(ello)
# print(goals)

# --------------------------------------------------------

# Challenge 4

pookie = {}

oof = input("dinosaurr: ")
yessir = int(input("number: "))

pookie[oof] = yessir
while oof != "triceratops":
    oof = input("dinosaurr: ")
    yessir = int(input("number: "))
    pookie[oof] = yessir
print(pookie)  