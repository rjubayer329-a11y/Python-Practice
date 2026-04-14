grades = []
status = True
while status:
    user_input = int(input("Enter your grades 0-100: "))
    if user_input < 0:
        status = False
    grades.append(user_input)
    

total_grades_entered = len(grades)
highest_grade = max(grades)
sum_grades = sum(grades)

print(f"You entered {total_grades_entered} grade")
print(f"The highest grade is {highest_grade}")
print("The everage of your grades is", sum_grades / total_grades_entered)
