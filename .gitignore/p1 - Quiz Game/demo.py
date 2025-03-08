
def quiz_game(questions):
    print("Hello to the Quiz!")
    if input("Do you want to play? ").strip().lower() != 'yes': #.strip is used to remove trailing white spaces. #word wrap is enabled/ disabled using alt + z
        print("Quitting the Game.")
        return #Just exits the function

    score = sum(1 for question, c_ans in questions.items() if c_ans in input(f"{question} ").strip().lower()) 
    print(f"You got {score} questions correct!")
    #question, c_ans in questions.items() defining the variables in relation to how variables would be extracted from a dictionary using .items(). We store both ques and ans in those variables then state the condition. input(f"{question}") asks the question but stores the answer provided by the user. Thats why we check if correct_ans is == the ans inputted by user, if it is then 1. Then sum the 1s. 


if __name__ == "__main__": #__name__ is a special variable in python that returns "__main__" if a file is run directly. because files could be ran indirectly if it is imported as a module in another file. import ..... (If you import main.py into another module: import main > The condition if __name__ == "__main__": evaluates to False, so greet() is not called automatically. You can still call main.greet() explicitly if needed.)

    questions = { "What does CPU stand for?": "central processing unit", "What does GPU stand for?": "graphics processing unit", "What does RAM stand for?": "random access memory", "What does PSU stand for?": "power supply"} #First degining the dictionary, then calling the quiz game function with the questions dictionary as a parameter. Only if if __name__ == "__main__":
    quiz_game(questions)








'''print("Hello to the Quiz!")

playing = input("Do you want to play? ") #Prompts user input. The input is stored in playing. 

if not playing or playing.lower() != "yes":
    quit() #quit Program

print("Ok! Lets Play.")
score = 0

#1
answer = input("What does CPU stand for? ")
if "central processing unit" in answer.lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#2
answer = input("What does GPU stand for? ")
if "graphics processing unit" in answer.lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#3
answer = input("What does RAM stand for? ")
if "random access memory" in answer.lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#4
answer = input("What does PSU stand for? ")
if "power supply" in answer.lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")'''