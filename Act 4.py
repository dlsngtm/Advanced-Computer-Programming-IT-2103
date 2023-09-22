english_grade = float(input("Enter your English grade: "))
filipino_grade = float(input("Enter your Filipino grade: "))
science_grade = float(input("Enter your Science grade: "))
math_grade = float(input("Enter your Math grade: "))
araling_panlipunan_grade = float(input("Enter your Araling Panlipunan grade: "))
physical_grade = float(input("Enter your Physical Education grade: "))

total_grades = (english_grade + filipino_grade + science_grade + math_grade + araling_panlipunan_grade + physical_grade)
average_grade = total_grades / 6

print("Your average grade is:", average_grade)