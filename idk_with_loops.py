my_list = []
yes_list = ["y","Y","Yes","yes","sure","ok", ""]
no_list = ["n","no","N","nope","nah"]
while True:
    question = input("Add another?\n Y|n: ").lower()
    if question in yes_list:
        my_list.append(input("Give me a friend's name: "))
    elif question in no_list:
        break
    else:
        print("You did not select y or n")
        continue

for i in my_list:
    print(i + " is my friend! :)")