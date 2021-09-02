def is_num(question):
    while True:
        try:
            num = int(input(question))
            break
        except ValueError:
            print("You did not put in a number.")
            continue
    return num