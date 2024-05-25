# calculates the averge student height from a list using loops

student_heights = input("input a list of student height: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)    

# # sum of height
# totalsum = 0
# for sum in student_heights:
#     totalsum = totalsum + sum

# # length of list
# leng = 0
# for x in student_heights:
#     leng +=1

# # calculating average
# average_heigth_student = totalsum / leng
# print(f"average_heigth_student =  {average_heigth_student}")

# second method using sum and len funtion
sumheight = sum(student_heights)
sumlenght = len(student_heights)
average_heigth_students = sumheight/sumlenght
print(average_heigth_students)