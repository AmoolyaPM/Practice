actual_otp = 9874
# print(type(actual_otp))

attempts = 3

while attempts:
    user_otp = input("Enter OTP: ")
    if len(user_otp) != 4:
        print(type(len(user_otp)))
        print("OTP must be 4 digits only")
    else:
        break
    




    
if student_score <= 0:
        if another_score == "Yes":
            student_score1 = int(input("Enter Student Score: "))  # interger
            print(student_score1)
        score += 1 
    else:
        break
while score:
    if student_score >= 90:
        print(f"Student {student_name} with ID {student_ID} has scored A grade")
        break
    elif student_score >= 80:
        print(f"Student {student_name} with ID {student_ID} has scored B grade")
        break
    elif student_score >= 70:
        print(f"Student {student_name} with ID {student_ID} has scored C grade")
        break
    elif student_score >= 60:
        print(f"Student {student_name} with ID {student_ID} has scored D grade")
        break
    else:
        print(f"Student {student_name} with ID {student_ID} has scored F grade")
        break

if student_attendance < 75:
    print(f"Warning: Student {student_name} with ID {student_ID} has low attendance")
else:
    Good_attendance = True
    print(f"OK Good: Student {student_name} with ID {student_ID} has good attendance")
    
if A_Grade and Good_attendance:
    print(f"Congratulations: Student {student_name} with ID {student_ID} is eligible for award")
else:
    break
