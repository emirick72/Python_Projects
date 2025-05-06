import random

# Define the roll function to roll the 6 sided dice
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    # Check if the user inputs a valid number
    # If they do, then break out of the loop
    # If they don't, keep going
    if players.isdigit():
        players = int(players) # Convert a string to an integer
        # Check if int > 1 and int < 4
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")        
    else:
        print("Invalid response. Please enter a valid number.")


max_score = 50
player_scores = [0 for _ in range(players)]

# Go through player turns
while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started")
        print("You total score is:", player_scores[player_idx], "\n")
        current_score = 0

        # Simulate the player's turn
        while True:
            should_roll = input("Would you like to roll? (Y for yes): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Next player's turn!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            
            print("Your score is: ", current_score)
        
        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx + 1, "is the winner with a score of: ", max_score, "!")