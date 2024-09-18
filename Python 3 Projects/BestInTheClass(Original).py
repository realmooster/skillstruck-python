empty = []

count = int(input('how many children took this test'))

def children():
    global score
    global count

    while count > 0:
        score = [n for n in input("Enter the student name and grade: ").split(" ")]
        score[1] = int(score[1])
        count -= 1
        empty.append(score)
    print(empty)

def get_top_scores():
    global highestScores
    global largestNumber
    
    largestNumber = 0
    highestScores = []

    for student in empty:
        name = student[0]
        score = student[1]

        if score > largestNumber:
            largestNumber = score
            highestScores = [name]

        elif score == largestNumber:
            highestScores.append(name)
    print(highestScores)

children()  
get_top_scores()
