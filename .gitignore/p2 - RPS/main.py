import random #importing modules

def play_RPC():
    user_wins, comp_wins, rpc_list = 0, 0, ["rock", "paper", "scissor"]
    win_conditions = {"rock": "scissor", "scissor": "paper", "paper": "rock"}

    #walrus operator := is used to assign values to variables in a single line. 

    while True: 
        #if (user_input := input("Type Rock / Paper / Scissor or Q to quit: ").strip().lower()) == "q":    break EXAMPLE OF WALRUS OPERATOR

        u_input = input("Type Rock / Paper / Scissor or Q to quit. Answer: ").strip().lower()
        if u_input == 'q': break #Loop is only exitted when user input is q


        if u_input not in rpc_list:
            print("Invalid input. Please choose Rock, Paper, or Scissor.")
            continue #exclusively check any other form of answers
            
        comp_choice = random.choice(rpc_list) #choice() picks a random from the list

        result = ("You win." if win_conditions[u_input] == comp_choice else "Its a tie." if u_input == comp_choice else "You Lose.") #In parenthesis for clarity. Leveraging dict for comparison. win_conditions[u_input] gives the losing pair of r, p or s. 

        user_wins += result == "You win." #Leverage Boolean addition. if result is win, then result == 'you win' returns true. We know that true means 1 and false means 0, so true will add. 
        comp_wins += result == "You Lose." #If its you lose, user has lost, we add to comp wins. 
        print(f"Computer picked {comp_choice}. {result}. ")
    
    
    print(f"Your score: {user_wins}. Computer's score: {comp_wins}. ")

if __name__ == "__main__": #main guard
    play_RPC()




'''user_wins = 0
comp_wins = 0
rpc_list = ["rock", "paper", "scissor"]

while True:
    u_input = input("Type Rock / Paper / Scissor or Q to quit. Answer: ").lower()
    if u_input == "q":
        break
    if u_input not in rpc_list:
        continue
    rand = random.randint(0, 2) # 2 inclusive

    comp_answer = rpc_list[rand]

    print(f"Computer picked {comp_answer}. ")

    #The reason we dont need to continue, is because this is a while loop so while statements are true, it will go back to the top of the loop
    if u_input == 'rock' and comp_answer == 'scissor':
        print("You win!")
        user_wins += 1
        

    elif u_input == 'scissor' and comp_answer == 'paper':
        print("You win!")
        user_wins += 1

    elif u_input == 'paper' and comp_answer == 'rock':
        print("You win!")
        user_wins += 1

    else:
        print("You lose. ")
        comp_wins += 1

print(f"Your Score is {user_wins}. Computers Score is {comp_wins}. ")
        '''

