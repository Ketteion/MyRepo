from is_num import is_num

name = []
age = []
q = "y"

while q == "y" or q =="":
    name.append(input("What is your friend's name?\n"))
    age.append(is_num("What is your their age?: "))
    while True:
        q = input("Add another? Y|n: ").lower()
        if q == "y" or q == "" or q == "n" :
            break
        else:
            print("You didn't put in 'y' or 'n'.")

for i, j in zip(name,age):
    print(f"You have a friend named {i} and they are {j} years old.")