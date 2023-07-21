student_heights = input("Give the heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

Sum = 0
for s_heights in student_heights:
    Sum += s_heights

print(f"Total height {Sum}")

count = 0
for student_number in student_heights:
    count += 1

avg = Sum / count

print(avg)
