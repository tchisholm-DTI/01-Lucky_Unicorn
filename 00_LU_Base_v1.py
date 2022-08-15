import random
# Functions go here ...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question) .lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer yes/no")


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
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


# Main Routine goes here ...
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
    print("*** Round Number: {} *** ".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between, 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4

    # If the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    # The token is either a horse or zebra ...
    # In both cases, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5
    # Output
    print("You got a {}. Your balance is: ${:.2f}".format(chosen, balance))
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
        print()
    else:
        play_again = input("Press enter to play again or 'xxx to quit")

print("Final balance", balance)
