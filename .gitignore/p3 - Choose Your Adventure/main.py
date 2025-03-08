#Understanding structure: The main function is at the bottom while the left right and checker function is at the top, because we will use them in the main, later. 
#Separate the checker function first. 


def get_valid_response(prompt, valid_response):
    response = input(prompt).strip().lower()
    return response if response in valid_response else get_valid_response(prompt, valid_response)

def left():
    answer = get_valid_response("You have come to a river. There is a very narrow bridge you can take or you can walk to a shallow looking part of the river and swim across. Bridge or swim? ",['swim', 'bridge'])

    if answer == 'swim':
        print('You have made it safely to the other side of the river.')

        answer = get_valid_response('You find a hooded man beside a camfire. Man offers you words. Do you take mans words?', ['yes', 'no'])

        if answer == 'yes':
            print('He tells you of a treasure he is searching for in the area.')

        else:
            print('The man has nothing to offer you. ')

    else:
        print('There was a croc waiting under the bridge for an unsuspecting pray. The bridge broke and you fell into the crocs mouth. Game over. ')

def right():
    answer = get_valid_response('You climb a steep incline and at the top, find track marks on the dirt. Do you follow the track marks or do you continue down the unknown path? Type track marks or unknown path. ', ['track marks', 'unknown path'])

    if answer == 'track marks':
        print('You stumbled across a group of bandits who robbed you and tied you to a tree. Game over. ')
    else:
        print('You came across caravaneers who offered you a ride to the nearest town. ')

def game():
    name = input("Type your name. ").strip()

    answer = get_valid_response('You have come to a dirt road and there are 2 paths ahead of you, left or right. Which way do you want to go? ', ['left', 'right'])

    if answer == 'left':
        left()
    else:
        right()

    print(f'Thanks for playing {name}. ')

if __name__ == '__main__':
    game()





'''name = input("Type your name. ").strip()
print(f"Welcome {name} to this adventure!")

answer = input("You have come to a dirt road and there are 2 paths ahead of you, left or right. Which way do you want to go? ").strip().lower()

if answer not in ['left', 'right']:
    print("This path does not exist.")
elif answer == 'left':
    answer = input('You have come to a river. There is a very narrow bridge you can take or you can walk to a shallow looking part of the river and swim across. Bridge or swim? ').strip().lower()
    if 'swim' not in answer or 'bridge' not in answer:
        print("You have not chosen the bridge or to swim.")
    if 'swim' in answer:
        print('You have made it safely to the other side of the river.')
        answer = input("You find a hooded man beside a camfire. Man offers you words. Do you take mans words?").strip().lower()
        if answer not in ['yes', 'no']:
            print("You choice is not valid")
        if 'yes' in answer:
            print('He tells you of a treasure he is searching for in the area.')
        else:
            print("The man has nothing to offer you. ")

    else:
        print("There was a croc waiting under the bridge for an unsuspecting pray. The bridge broke and you fell into the crocs mouth. Game over. ")

else:
    answer = input("You climb a steep incline and at the top, find track marks on the dirt. Do you follow the track marks or do you continue down the unknown path? Type track marks or unknown path").strip().lower()

    if 'track' not in answer or 'unknown' not in answer:
        print("You choice is not valid")
    if 'track' in answer:
        print('You stumbled across a group of bandits who robbed you and tied you to a tree. Game over.')
    else:
        print("You came across caravaneers who offered you a ride to the nearest town. ")

print(f"Thanks for trying {name}. ")'''