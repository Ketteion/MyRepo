def is_num(question):
    while True:
        try:
            x = float(input(question))
            break
        except ValueError:
            print("\nThat is not a number.\n")
            continue
    return x

shopping_cart = []
response = "y"

while response == "y" or response == "":
    shopping_cart.append(is_num("Enter the price of your item: $"))
    while True:
        response = input("Add more items to your cart? Y|n: ").lower()
        if response == "y" or response == "" or response == "n":
            break
        else:
            print("Please input only a yes or a no.")
            continue


if len(shopping_cart) < 11:
    total = sum(shopping_cart)
elif len(shopping_cart) < 23:
    total = sum(shopping_cart) * 0.85
elif len(shopping_cart) > 22:
    total = sum(shopping_cart) * 0.75
tax = total * 1.08
print(f"The total is: ${tax:.{2}f}.")
