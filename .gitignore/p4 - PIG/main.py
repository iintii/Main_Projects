import random

MAX_SCORE = 25

def roll():
    return random.randint(1, 6)

def get_players():
    while True:
        try:
            players = int(input("Enter the number of players (2 - 4): "))
            if 2 <= players <= 4:
                return players
        except ValueError:
            print("Invalid input, please enter a number between 2 and 4.")

def turn(index):
    current_score = 0
    player_choice = False

    while input(f"Player {index + 1}, would you like to roll? (y to roll): ").strip().lower() == 'y':
        player_choice = True
        value = roll()
        if value == 1:
            print("You rolled a 1! Turn over.")
            return 0, player_choice
        current_score += value
        print(f"You rolled a {value}. Current score: {current_score}")
    return current_score, player_choice

def main():
    players = get_players()
    player_scores = [0] * players
    choose = 0

    while True:
        for index in range(players):
            print(f"\nPlayer {index + 1}'s turn. Current score: {player_scores[index]}")
            score, player_choice = turn(index)            
            player_scores[index] += score
            
            
            if not player_choice: 
                choose += 1
            else:
                choose = 0 #Resets the check for all players opting out. If this line isnt implimented, choose will keep on adding to itself even after 1 turn. this makes sure that if anyone in that turn says 'y', the game continues. 
            if choose == players:
                print("Thanks for not playing. ")
                return

            if player_scores[index] >= MAX_SCORE:
                print(f"Player {index + 1} wins with a score of {player_scores[index]}!")
                return #doesnt matter how nested return is, it indicates the end of the function. 
            

if __name__ == "__main__":
    main()
