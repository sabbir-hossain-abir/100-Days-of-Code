student_score = input("Input a list of students score: ").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

Max = 0

for max_score in student_score:
    if max_score > Max:
        Max = max_score
print(Max)
