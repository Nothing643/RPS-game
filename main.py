import random

item = {"1": "rock",
        "2": "paper",
        "3": "scissors",
        "rock": "rock",
        "paper": "paper",
        "scissors": "scissors"}

computer = random.choice(["rock", "paper", "scissors"])
user_input = input("Welcome to the game! \nPlease choose 1 for rock, 2 for paper and 3 for scissors: ")
user = item.get(user_input)

if user == None:
    print("Invalid input!")

else:
    print(f"Computer chose {computer} and you chose {user}")

    if user == computer:
        print("It's a tie!")

    elif(user == "1" or user == "rock" and computer == "scissors") or \
        (user == "2" or user == "paper" and computer == "rock") or \
        (user == "3" or user == "scissors" and computer == "paper"):
        print("You win!")
    
    else:
        print("You lose!")