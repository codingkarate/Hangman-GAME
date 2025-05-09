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