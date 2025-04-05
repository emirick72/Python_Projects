# This is a simple calculator program
# Author: Emily Rick
# April 5, 2025

# Welcome user to the program
print("This is a simple calculator. It can do basic arithmetic operations.")

while True:
    # Declare variables
    usernum1 = float(input("Please enter the first number: "))
    operator = input("Please choose an operator (+, -, *, /, %): ")
    usernum2 = float(input("Please choose the second number: "))

    # TODO: Do the operations on the chosen numbers
    if operator == "+":
        answer = usernum1 + usernum2
        print(answer)
    elif operator == "-":
        answer = usernum1 - usernum2
        print(answer)
    elif operator == "*":
        answer = usernum1 * usernum2
        print(answer)
    elif operator == "/":
        answer = usernum1 / usernum2
        print(answer)
    elif operator == "%":
        answer = usernum1 % usernum2
        print(answer)
    else:
        print(f"{operator} is not valid.")
    
    new_calculation = input("Type 'new' to do a new operation or type 'exit' to exit the program: ")
    if new_calculation == "new":
        continue
    else:
        break
