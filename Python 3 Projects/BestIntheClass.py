array = []
student_num = int(input("How many students took the test?"))

while student_num > 0:
    score = [n for n in input("Enter the student name and grade separated by a space").split(" ")]
    array.append(score)
    student_num -= 1

def get_top_scores(input_list):
    max = 0
    top_students = []
    for x in range(len(input_list)):
        if int(input_list[x][1]) > max:
            max = int(input_list[x][1])
            top_students = [input_list[x][0]]
        elif int(input_list[x][1]) == max:
            top_students.append(input_list[x][0])
    print(top_students)

get_top_scores(array)

