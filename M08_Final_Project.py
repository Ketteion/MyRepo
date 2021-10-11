#ask the user the name of the store they manage
#ask the user how much money the store made
#count in 100's, 50's, 20's, 10's, 5's, 1's, quarters, nickels, dimes, and pennies
#after getting the total amount of money in the store, ask the user if they manage more stores
#if they say yes, add up earnings of another store
#after the user is done adding stores, ask the user if they want to save the information
#if they say 'yes' to saving, save the data to a new txt file

#this function verifies that a user's input is a number
def is_num(question):
    while True:
        try:
            x = int(input(question))
            break
        except ValueError:
            print("That is not a number.")
            continue
    return x

#this function will ask the user about a store and ask how much money is at the store
#the function will get a total of the types of bills and coins and add them together
class store():
    def __init__(self):
        self.name = input("What is the name of your store?\n")
        self.hundreds = is_num("How many hundreds are at that store?\n")
        self.fifties = is_num("How many fifties are at that store?\n")
        self.twenties = is_num("How many twenties are at that store?\n")
        self.tens = is_num("How many tens are at that store?\n")
        self.fives = is_num("How many fives are at that store?\n")
        self.ones = is_num("How many ones are at that store?\n")
        self.quarters = is_num("How many quarters are at that store?\n")
        self.dimes = is_num("How many dimes are at that store?\n")
        self.nickels = is_num("How many nickels are at that store?\n")
        self.pennies = is_num("How many pennies are at that store?\n")
        self.total = (self.hundreds*100)+(self.fifties*50)+(self.twenties*20)+(self.tens*10)+(self.fives*5)+(self.ones)+(self.quarters*0.25)+(self.dimes*0.1)+(self.nickels*0.05)+(self.pennies*0.01)


def main():
    storeList = []
    response = "y"
    saveResponse = ""
    while response != "n":
        storeList.append(store())
        while True:
            response = input("Do you want to add another store? Y|n\n").lower()
            if response == "y" or response == "":
                break
            elif response == "n":
                break
            else:
                print("You did not input 'y' or 'n'.")
                continue
    saveResponse = input("Do you want to save your information on a text file? Y|n").lower()
    if saveResponse == "y":
        with open ('Store_List.txt','w') as file:
            for i in storeList:
                file.write(f"{i.name} has ${i.total}")
        print("A text file has been created. Exiting program.")
        exit
    else:
        print("Your information was not saved. Exiting program.")
        exit

if __name__ == "__main__":
    main()
else:
    exit