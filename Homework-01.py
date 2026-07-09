from persiantools.jdatetime import JalaliDate

def average(ages=[]) -> float:
    return sum(ages) / len(ages)

def calculate_age(year_of_birth: int) -> int:
    current_year: int = JalaliDate.today().year
    age: int = current_year - year_of_birth
    return age

def print_full_name(first_name: str, last_name: str) -> None:
    full_name: str = (first_name + "   " + last_name).upper()
    print(full_name)

def main() -> None:
    ages = []
    students = []
    while True:
        first_name = input("enter first name:")
        last_name = input("enter last name:")
        birth_year = int(input("enter birth year:"))
        age = calculate_age(birth_year)
        students.append({
                "first_name": first_name,
                "last_name": last_name,
                "birth_year": birth_year,
            })
        
        ages.append(age)
        print("Do you want to add another student? (y/n)")
        if input() == "n":
            break
    print("students:")
    for student in students:
        print_full_name(student["first_name"], student["last_name"])
    print("age average would be " + str(average(ages)))

main()


# JalaliDate.today()
# cd desktop      
# # python test.py

# students = []

# first_name = input("Enter first name : ")
# last_name = input("Enter last name : ")
# birth_year = int(input("Enter birth year : "))

# student_1 = {"first_name": first_name, "last_name": last_name, "birth_year": birth_year}

# students.append(student_1)

# first_name = input("Enter first name : ")
# last_name = input("Enter last name : ")
# birth_year = int(input("Enter birth year : "))

# student_2 = {"first_name": first_name, "last_name": last_name, "birth_year": birth_year}

# students.append(student_2)

# print(students)

# full_name_st1 = students[0]["first_name"] + " " + students[0]["last_name"]
# full_name_st1 = full_name_st1.upper()
# age_st1 = 2025 - students[0]["birth_year"]
# full_name_st2 = students[1]["first_name"] + " " + students[1]["last_name"]
# full_name_st2 = full_name_st2.upper()
# age_st2 = 2025 - students[1]["birth_year"]

# age_avg = (age_st1 + age_st2) / 2
# ages = [age_st1, age_st2]
# age_avg = sum(ages) / len(ages)


# print(full_name_st1)
# print(age_st1)
# print("-------------------")
# print(full_name_st2)
# print(age_st2)
# print("-------------------")

# print(age_avg)

# def average(ages=[]) -> float:
#     return = sum(ages) / len(ages)
# def calculate_age(year_of_birth) -> int:
