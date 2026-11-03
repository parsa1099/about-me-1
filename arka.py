import random

number = random.randint(1, 100)
guess = int(input("Guess the number: "))
print("Correct!" if guess == number else f"Wrong! Number was {number}")
