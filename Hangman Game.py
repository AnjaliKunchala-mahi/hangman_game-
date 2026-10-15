import random

def hangman():
    words = ["python", "apple", "tiger", "hello", "chair"]
    word = random.choice(words)

    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman Game!")

    while attempts > 0:
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)
        print("Attempts left:", attempts)

        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

    else:
        print("Game over! The word was:", word)

hangman()