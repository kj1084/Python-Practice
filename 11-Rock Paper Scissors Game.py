import random
Computer = random.choice(["rock", "paper", "scissors"])
User = input("Enter your choice (rock, paper, scissors) :- ")
if User == "r":
    User = "rock"
elif User == "p":
    User = "paper"
elif User == "s":
    User = "scissors"
while User not in ["rock", "paper", "scissors"]:
    print("Invalid choice!")
    User = input("Enter Again :- ")
    if User == "r":
        User = "rock"
    elif User == "p":
        User = "paper"
    elif User == "s":
        User = "scissors"
print("Computer's choice:", Computer)
if User == Computer:
    print("It's a tie! 🤝")
elif (User == "rock" and Computer == "scissors") or (User == "paper" and Computer == "rock") or (User == "scissors" and Computer == "paper"):
    print("Congratulations! You win! 🎉🎉🎉🎉🎉")
else:
    print("Oooops! You lose! 😢 Better luck next time!")
