#pseudocode
#get a number from the user
#count from 0 to the user's number by 5
#do not display the number 0
#tell the user goodbye
number = int(input("Please insert a number. "))
count = 0
while (count<number):
    count = count + 5
    print(count)
print("Goodbye.")
