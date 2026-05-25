import random

# List of words
words = ["apple", "tiger", "chair", "pizza", "robot"]

# Random word selection
secret_word = random.choice(words)

# Hidden word
guessed_word = ["_"] * len(secret_word)

# Number of attempts
attempts = 6

# Game loop
while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))

    # User input
    guess = input("Enter a letter: ")

    found = False

    # Check guessed letter
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            guessed_word[i] = guess
            found = True

    # Wrong guess
    if not found:
        attempts -= 1
        print("Wrong guess!")

    print("Attempts left:", attempts)

# Final result
if "_" not in guessed_word:
    print("\nYou Won!")
    print("The word was:", secret_word)
else:
    print("\nYou Lost!")
    print("The word was:", secret_word)