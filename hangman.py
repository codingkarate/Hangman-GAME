import random

# List of words to choose from
words = ['python', 'hangman', 'programming', 'challenge', 'development', 'random', 'terminal']

# Select a random word
word_to_guess = random.choice(words)
guessed_letters = set()
attempts_remaining = 6  # Max incorrect attempts allowed

# Create a display for the word
display_word = ['_' for _ in word_to_guess]

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while attempts_remaining > 0 and '_' in display_word:
    print("\nWord: " + ' '.join(display_word))
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Attempts remaining: {attempts_remaining}")
    
    guess = input("Enter a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetical character.")
        continue
    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.")
        continue

    guessed_letters.add(guess)
    
    if guess in word_to_guess:
        print("✅ Correct guess!")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[i] = guess
    else:
        print("❌ Incorrect guess.")
        attempts_remaining -= 1