import random

# Choices as text
choices = ["Rock", "Paper", "Scissors"]

# Choose user input
print("What do you choose?")
usr = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))


if usr not in [0, 1, 2]:
    print("Invalid choice! You must type 0, 1, or 2.")
else:
    # Generate computer choice
    cmp = random.randint(0, 2)

    # Print user choice
    print(f"You chose: {choices[usr]}")
    
    # Print computer choice
    print(f"Computer chose: {choices[cmp]}")

    # Determine winner
    if usr == cmp:
        print("It's a draw!")
    elif (usr == 0 and cmp == 2) or (usr == 1 and cmp == 0) or (usr == 2 and cmp == 1):
        print("You win!")
    else:
        print("You lose!")
