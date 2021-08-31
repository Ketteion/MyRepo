#create a program that makes a list of the user's favorite foods
#the list should be any size that the user wants
#print out the list for the user
food_list = []
while True:
    question = (input("Add another food? \nY|n: ")).lower()
    if question == "y" or question == "":
        food_list.append(input("Input one of your favorite foods: "))
    elif question == "n":
        break
    else:
        print("You did not type y or n.")
        continue

for i in food_list:
    print(i)