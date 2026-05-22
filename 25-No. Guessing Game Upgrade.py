guess = int(input("Guess the number :- "))
import random
attempts = 0
secret_Number = random.randint(1, 100)
while guess != secret_Number:
    if guess<secret_Number:
        print("Too Low! 📉")
    elif guess>secret_Number:
        print("Too High! 📈")
    attempts += 1
    guess = int(input("Guess Again :- "))
print("Congratulations! You Won! 🎉🎉🎉🎉🎉🎉🎉")
print(f"It took you {attempts} attempts.")