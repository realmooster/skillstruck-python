# Code Checkpoint
# harvest = ["pumpkins", "apples", "corn", "squash", "carrots"]

# harvest.remove("squash")
# harvest.pop(1)

# print(harvest)
# ---------------------------------------------------------
# Challenge 1

# skills = ["Piano", "Soccer", "Coding", "Cooking", "Writing"]

# var = input("um yeah ")
# if var in skills:
#     skills.remove(var)
#     print(skills)
# else:
#     print(no thanks)
# ---------------------------------------------------------
# Challenge 2

# var = input("what are some names bro ").split()

# print(var.pop(2) + " got the bronze medal")
# ---------------------------------------------------------
# Challenge 3

# beans = input("list of beans " ).split()

# if "lima" in beans:
#     beans.remove("lima")
#     print(beans)
# else:
#     print(beans)

# Challenge 4

var = input("something " ).split()

center = int(len(var)/2)

if len(var) % 2 == 0:
    var.pop(center)
    var.pop(center - 1)
else:
	var.pop(center)
print(var)