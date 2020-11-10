import random

# Declare python dicts
donald = { "last_name": "Trump",  "first_name": "Donald", "age": 73, "job": "Not president anymore"}
joe = { "last_name": "Biden",  "first_name": "Joe", "age": 77, "job": "New president"}

# Print them
print(donald)
print(joe)

# Ask the user for an input
last_name = input()
print(last_name)

# Guess the number
secret_number = random.randint(1, 100)
guess_number = None
while guess_number != secret_number:
    try:
        guess_number = int(input())
        if guess_number < secret_number:
            print('Higher!')
        elif guess_number > secret_number:
            print('Lower!')
    except ValueError:
        print('You must enter a number to play our guessing number game')


print(f'Found! The secret number was {secret_number}')

# Functions

def evaluate(guess_number, secret_number):
    found = False
    if guess_number < secret_number:
        print('Higher!')
    elif guess_number > secret_number:
        print('Lower!')
    else:
        found = True
    return found

# lambda function

def multiply(x, y):
    return x * y

multiplier = lambda x, y: x*y

# Les imports
import math
print(math.factorial(5))

# Could you implement the factorial by yourself ?

# For loop | array
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  