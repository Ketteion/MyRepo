#Pseudocode:
#get a number from the user
#compare that number to 10
#if the number is 10, tell the user they are correct
#if the number is greater than 10, tell the user the number is too high
#if the number is less than 10, tell the user the number is too low
#tell the user goodbye at the end of the program

num = int(input("Please input a number: "))
if num == 10:
    print("Your number is correct.")
elif num>10:
    print("Your number is too high.")
else:
    print("Your number is too low.")
print("Goodbye.")