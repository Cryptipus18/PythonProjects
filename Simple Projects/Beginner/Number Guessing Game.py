def guess(x, y,no_of_guesses=0):
    while x != y:
        try:
            x = int(input("Guess a number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if x < y:
            print ("Higher!")
            no_of_guesses += 1
        elif x > y:
            print("Lower!")
            no_of_guesses += 1
        else:
            print("Correct!")
            print("You guessed the number", number)
            print("Number of guesses:", no_of_guesses + 1)
            break
    print("Want to play again? (y/n)")
    choice = input().lower()
    if choice == 'y':
        guess(None, y)
    else:
        print("Thanks for playing!")    

import random
number = random.randint(1,10)


print("Welcome to the Number Guessing Game!")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")
difficulty = input("Choose a difficulty (1, 2, or 3): ")
match(difficulty):
    case "1":
        number = random.randint(1,10)
    case "2":
        number = random.randint(1,50)
    case "3":
        number = random.randint(1,100)
    case _:
        print("Invalid choice, defaulting to Easy (1-10).")
        number = random.randint(1,10)
user = None
guess(user, number)