import random

number = random.randint(1, 20)

print("Guess the number between 1 and 20")

for i in range(3):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! Correct guess.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print("Game over!")
    print("Correct number was:", number)