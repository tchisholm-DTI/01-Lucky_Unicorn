# Asks the user if they have played before
show_instructions = input("Have you played this game before? ") .lower()

# If they say yes, output 'program continues'
if show_instructions == "yes" or "y":
    print("program continues")

# If they say no, output 'display instructions'
elif show_instructions == "no" or "n":
    print("Display instructions")

# If they answer differently, output 'Please answer yes/no'
else:
    print("Please answer yes/no")


