# finding heigest value in list using loop

student_score = input("input a list of student score: ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)  

score = 0
for x in student_score:
    if score < x:
        score = x
print(f"student heigest score is : {score}")        

