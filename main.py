import random

name = input("What is your name? ")

print("Good luck", name, "!")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Try to guess th random chosen word!")
guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:

            print(char)

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win!")
        print("The Word is:", word)
        break

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("NOOOOO WROOOONNNGGG!")
        print("You have", turns, "left")

        if turns == 0:
            print("YOU LOSE!")
