import random
min = 1
max = 6


roll_again = input("Roll the dice?")
roll_again = roll_again.lower()

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice..")
    print("Values of the dice: ")
    print(random.randint(min, max))
    print(random.randint(min, max))
    roll_again = input("Would you like to roll again? ")
    roll_again = roll_again.lower()
