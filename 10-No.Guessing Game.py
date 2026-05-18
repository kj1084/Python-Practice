guess = int(input("Guess the number :- "))
secret_Number=7
while guess != secret_Number:
    if guess<secret_Number:
        print("Too Low! 📉")
    elif guess>secret_Number:
        print("Too High! 📈")
    guess = int(input("Guess Again :- "))
print("Congratulations! You Won! 🎉🎉🎉🎉🎉🎉🎉")