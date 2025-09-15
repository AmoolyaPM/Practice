# Trial
class student:
    pass

    a = 10
    b = 30
    print(a+b)

atm_pin = 9874
user_input = 0

while user_input != atm_pin:
    user_input = int(input("Enter PIN: "))
    
print("You can withdraw")