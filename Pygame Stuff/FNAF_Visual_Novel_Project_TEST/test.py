'''
THIS IS A TEST FILE FOR MY FNAF VISUAL NOVEL PROJECT
Ideally, I want the final project to be made using Pygame,
but for now I'm using the console to see what the output would look like.
'''

# Welcome the player
print("Welcome to (Untitled FNAF Fangame)!")

# character variables
Mike = "Mike Schmidt"
Jeremy = "Jeremy Fitzgerald"
Vanessa = "Vanessa Shelly"

# Choose your character
while True:

    try:
        #player_character = input("Choose a character to play as:")
        print("Choose a character to play as:")
        print("   1. " + Mike)
        print("   2. " + Jeremy)
        print("   3. " + Vanessa)

        player_character = input()
        player_choice = int(player_character) # convert input (string) to int
        if player_choice == 1:
            print("You chose Mike Schmidt")
            break
        elif player_choice == 2:
            print("You chose Jeremy Fitzgerald")
            break
        elif player_choice == 3:
            print("You chose Vanessa Shelly")
            break
        else:
            print("That input is not valid. PLease enter a valid number (1, 2, or 3).")
    except ValueError:
        print("Please enter a number:")