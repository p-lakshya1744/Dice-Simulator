import random

again = True

while again:
    print(random.randint(1,6))
    another_roll = input("Do you want an another roll? (yes/no)")
    if another_roll.lower() == "yes":
        continue
    else:
        break