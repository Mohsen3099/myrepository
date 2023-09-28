import random

def hangman():
    word_list = ["python", "hangman", "game", "programming", "code"]
    word = random.choice(word_list)
    guesses = 6
    guessed_letters = []
    guessed_word = "_" * len(word)

    print("Let's play Hangman!")

    while guesses > 0 and "_" in guessed_word:
        print("\nWord: ", end="")
        for letter in guessed_word:
            print(letter, end=" ")
        print("\n")
        print(f"Guesses left: {guesses}")

        guessed_letter = input("Guess a letter: ").lower()
       
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guessed_letter in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guessed_letter)

        if guessed_letter in word:
            for i in range(len(word)):
                if word[i] == guessed_letter:
                    guessed_word = guessed_word[:i] + guessed_letter + guessed_word[i+1:]
        else:
            print("Incorrect guess!")
            guesses -= 1

    print("\n")

    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of guesses. The word was: {word}")

hangman()