code = {"a": "q", "b": "x", "c": "j", "d": "z", "e": "v", "f": "p", "g": "k", "h": "u", "i": "w", "j": "y", "k": "b", "l": "t", "m": "r", "n": "d", "o": "h", "p": "s", "q": "e", "r": "a", "s": "i", "t": "f", "u": "l", "v": "g", "w": "o", "x": "n", "y": "c", "z": "m", " ": "1" }

sentence = (input("one sentence: "))
#The variable 'encoded' is to create an empty space that adds to a string to append later.
encoded = ''
#For each character in 'sentence' it checks for the characters = in the dictionary and then adds the 'value' or appends it to the empty string.
for char in sentence:
    if char in code:
        encoded += code[char]

print(encoded)

