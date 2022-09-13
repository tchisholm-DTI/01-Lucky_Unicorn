import random
# Functions go here ...


def yes_no(question):
    valid = False
    while not valid:
        response = input(question) .lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please answer yes/no")


def instructions():
    statement_generator("How to Play", "*")

    print()
    print("Choose a starting amount (minimum $1, maximum $10")
    print()
    print("Then press <enter> to play. You will get either a horse, a zebra, a donkey or a unicorn.")
    print()
    print("It costs $1 per round. Depending on your prize you might win some of the money back. Here's the payout amounts...")
    print("Unicorn: $5.00 (balance increases by $4.00")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1.00)")
    print()
    print("Can you avoid the donkeys, get the unicorns and walk home with the money? ")
    print()
    print("Hint: to quit while you are ahead, type 'xxx' instead of pressing <enter> ")
    print()
    statement_generator("Let's get Started ...", "-")
    return ""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))

            # If the amount is too low/too high give
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)


def statement_generator(statement, decoration, lines=None):

    sides = decoration * 5

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    if lines == 1:
        print(statement)

    elif lines == 2:
        print(statement)
        print(top_bottom)

    else:
        print(top_bottom)
        print(statement)
        print(top_bottom)

    return ""


# Main Routine goes here ...
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Ask user how much they want to play with ...
how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play ...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    round_info = "Round Number: {}".format(rounds_played)
    statement_generator(round_info, ".")

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between, 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        decoration = "!"
        balance += 4

    # If the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        decoration = "D"
        balance -= 1

    # The token is either a horse or zebra ...
    # In both cases, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            decoration = "Z"
        balance -= 0.5
    # Output
    feedback = "You got a {}. Your balance is: ${:.2f}".format(chosen, balance)
    print()

    statement_generator(feedback, decoration, 1)

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
        print()
    else:
        play_again = input("Press enter to play again or 'xxx to quit")

statement_generator("Results", "=")
print("Final balance", balance)
print("Thank you for playing the Lucky Unicorn game")
