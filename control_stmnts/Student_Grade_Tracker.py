# Collecting the nformations from the user

student_ID = input("Enter Student ID: ") # string
student_name = input("Enter Student Name: ")  # string
student_attendance = int(input("Enter Student Attendance: ")) # int
student_score = int(input("Enter Student Score: "))  # interger

total_score = 0 + student_score
count = 1

while True:
    choice = input("Do you want to enter another Score? Yes/No :")  # str

    if choice == "Yes":
        another_score = int(input("Enter Another Score: "))  # interger
        total_score += another_score
        count += 1
        # print(another_score)
    else:
        break 

print(f"Number of scores is : {count}")
print(f"Total Score is: {total_score}")

if count > 0:
    average = total_score/count
    print(f"Average Score is: {average}")
    # print(type(count)) - integer

while average:
    if average >= 85 and average <= 100:
        print(f"Student {student_name} with ID {student_ID} has scored A grade")
        break
    elif average >= 70 and average <= 84:
        print(f"Student {student_name} with ID {student_ID} has scored B grade")
        break
    elif average >= 50 and average <= 69:
        print(f"Student {student_name} with ID {student_ID} has scored C grade")
        break
    elif average <= 49 and average >= 0:
        print(f"Student {student_name} with ID {student_ID} has scored FAIL grade")
        break
    else:
        print("Please enter the marks between the range of 0 - 100")
        break

if student_attendance >= 75:
    Good_attendance = True
    Grade = True
   
    if Grade >= 85 and Good_attendance:
        print(f"OK Good: Student {student_name} with ID {student_ID} has good attendance")
        print(f"Congratulations: Student {student_name} with ID {student_ID} is eligible for award")
    else:
        print(f"Sorry: Student {student_name} with ID {student_ID} is not eligible for award")
else:
    print(f"Warning: Student {student_name} with ID {student_ID} has low attendance")

print(f"Student ID is: {student_ID}")
print(f"Student name is: {student_name}")
print(f"Attendance is: {student_attendance}%")
print(f"Total Score is: {total_score}")
print(f"Average of Scores is: {average}")
print(f"Number of Scores is: {count}")

if average >+ 0:
    if average >= 85 and average <= 100:
        Grade = 'A'
    elif average >= 70 and average <= 84:
        Grade = 'B'
    elif average >= 50 and average <= 69:
        Grade = 'C'
    elif average <= 49 and average >= 0:
        Grade = 'FAIL'
    else:
        Grade = 'Invalid Score'

    print(f"Student Grade is: {Grade}")



# Total_score = student_score + another_score
# print(Total_score)


