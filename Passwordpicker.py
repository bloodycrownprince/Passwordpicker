import random 
import string
print("Welcome to the Password picker")

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow',
            'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

while True:
    adjective  = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.choice(numbers)
    special_char = random.choice(string.punctuation)
    
    password = adjective + noun + str(number) + special_char
    print(f"You Password is : {password}")
    
    response = input("Would you like another password? Type Y or N ")
    if response == "N":
        break