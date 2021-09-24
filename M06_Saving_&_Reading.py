gbInput = ""

try:
    with open ("Good_Or_Bad","r") as fGood_Or_Bad:
        for line in fGood_Or_Bad:
            if line == "good":
                print("You had a good day.")
            elif line == "bad":
                print("You had a bad day.")
            else:
                print("You had a [redacted] day.")
except FileNotFoundError:
    with open ("Good_OR_Bad", "w") as fGood_Or_Bad:
        gbInput = input("Did you have a good or bad day?").lower()
        fGood_Or_Bad.write(f"{gbInput}")

