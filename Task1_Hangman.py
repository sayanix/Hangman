
 
import random
 

WORDS = ["python", "hangman", "variable", "function", "internship"]
 
MAX_ATTEMPTS = 6
 
 
def choose_word():
    
    return random.choice(WORDS)
 
 
def display_word(word, guessed_letters):
    
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()
 
 
def get_guess(guessed_letters):
    
    while True:
        guess = input("Guess a letter: ").lower().strip()
 
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue
 
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
 
        return guess
 
 
def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS
 
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {MAX_ATTEMPTS} incorrect guesses allowed.")
 
    while attempts_left > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
 
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
 
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
 
        # Check win condition: every letter in the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("\n" + display_word(word, guessed_letters))
            print(f"🎉 Congratulations! You guessed the word: '{word}'")
            return
 
    
    print(f"\n💀 You ran out of attempts! The word was: '{word}'")
 
 
def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("Thanks for playing Hangman! Goodbye.")
 
 
if __name__ == "__main__":
    main()
 