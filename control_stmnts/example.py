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
    

