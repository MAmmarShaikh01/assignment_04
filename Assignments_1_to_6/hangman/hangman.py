import random
from words import words  # Make sure this is a list, not a set
import string

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word(words)  # 'words' must be a list
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    print("🎉 Welcome to Hangman!")
    print("Guess the word, one letter at a time!")

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left and you have used these letters:", ' '.join(used_letters))
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_display))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"✅ Good guess! {user_letter} is in the word.")
            else:
                lives -= 1
                print(f"❌ {user_letter} is not in the word.")
        elif user_letter in used_letters:
            print("⚠️ You have already used that letter. Try again.")
        else:
            print("❌ Invalid character. Please try again.")

    if lives == 0:
        print("\n💀 You died, sorry. The word was:", word)
    else:
        print("\n🎉 You guessed the word", word, "!! You win! 🏆")

hangman()
