name = []
mealCost = []
q = "y"
totalCost = 0
averageCost = 0

#get user inputs
#get name and price of their meal

while q == "y" or q == "":
    name.append(input("What is your name?\n"))
    mealCost.append(int(input("How much does your meal cost? ")))
    while True:
        q = input("Add another? Y|n: ").lower()
        if q == "y" or q == "" or q == "n":
            break
        else:
            print("you did not input a valid response.")
            continue

#get total cost of all meals
for i in mealCost:
    totalCost = totalCost + i

#get average by dividing total cost by number of people
averageCost = totalCost / len(name)

#compare cost of person's meal to the average cost
#tell the user whether the cost of their meal was higher or lower than the average
for k , j in zip(name , mealCost):
    if j > averageCost:
        print(f"{k}'s Meal is {j - averageCost} higher than the average meal price.")
    elif j < averageCost:
        print(f"{k}'s Meal is {averageCost - j} lower than the average meal price.")
    else:
        print("heheh")