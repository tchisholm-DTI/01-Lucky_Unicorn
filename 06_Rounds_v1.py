# Set balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play ...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number

    print()
    print("*** Round Number:{} *** ".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
        print()
    else:
        play_again = input("Press enter to play again or 'xxx to quit")

print("Final balance", balance)

