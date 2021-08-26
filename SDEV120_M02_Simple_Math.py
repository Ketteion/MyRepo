#get two numbers from user
#add, subtract, multiply, and divide the two numbers together and save the values to variables
#print the results on one line

num1 = int(input("Please type a number: "))
num2 = int(input("Please type another number: "))
addition = str((num1 + num2))
subtraction = str((num1 - num2))
multiplication = str((num1 * num2))
division = str((num1 / num2))
print(addition + " " + subtraction + " " + multiplication + " " + division)