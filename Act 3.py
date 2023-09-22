from datetime import datetime

father_name = input("Enter your father's name: ")
birthplace = input("Enter your father's birthplace: ")
birthday = input("Enter your father's birthday (YYYY-MM-DD): ")

birthday_date = datetime.strptime(birthday, "%Y-%m-%d")

current_date = datetime.now()

age = current_date.year - birthday_date.year - ((current_date.month, current_date.day) < (birthday_date.month, birthday_date.day))

print(f"Your father, {father_name}, is {age} years old.")
