from is_num import is_num

calcType = ""
result = 0
a = 0
b = 0

#ask user which calculation they want to do
q = "y"
while q == "y" or q == "":
        calcType = input("Would you like to do addition, subtraction, multiplication, or division?\n").lower()
        if calcType == "addition":
            a = is_num("Please input your first number.\n")
            b = is_num("Please input your second number.\n")
            print(f"The result is {a+b}.")
            q = input("Would you like to do another calculation? Y|n\n").lower()
            if q == "y" or q == "" or q == "n":
                break
            else:
                print("You did not input a valid response.")
                continue
        elif calcType == "subtraction":
            a = is_num("Please input your first number.\n")
            b = is_num("Please input your second number.\n")
            print(f"The result is {a - b}.")
            q = input("Would you like to do another calculation? Y|n\n").lower()
            if q == "y" or q == "" or q == "n":
                continue
            elif q == "n":
                break
            else:
                print("You did not input a valid response.")
                continue
        elif calcType == "multiplication":
            a = is_num("Please input your first number.\n")
            b = is_num("Please input your second number.\n")
            print(f"The result is {a * b}.")
            q = input("Would you like to do another calculation? Y|n\n").lower()
            if q == "y" or q == "" or q == "n":
                break
            else:
                print("You did not input a valid response.")
                continue
        elif calcType == "division":
            a = is_num("Please input your first number.\n")
            b = is_num("Please input your second number.\n")
            try:
                print(f"The result is {a / b}.")
            except ZeroDivisionError:
                print("You cannot divide by zero.")
            q = input("Would you like to do another calculation? Y|n\n").lower()
            if q == "y" or q == "" or q == "n":
                break
            else:
                print("You did not input a valid response.")
                continue
        else:
            print("You did not put in a valid response.")
            continue

