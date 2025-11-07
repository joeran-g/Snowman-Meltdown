import random
import ascii_art as art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def show_snowman(lives, guessed_chars, word_to_guess):
    print()
    if lives == 0 or not guessed_chars:
        print(art.STAGES[3])
        print()
        return
    print(f"{art.STAGES[3 - lives]}")
    print()
    print("Word: ", end="")
    for char in word_to_guess:
        if guessed_chars[char]:
            print(f" {char}", end="")
        else:
            print(" _", end="")
    print()
    print()


def guess_letter():
    while True:
        user_guess = input("Guess a letter: ")
        if len(user_guess) == 1 and not user_guess.isdigit():
            return user_guess
        print("Please enter just one letter\n")


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """
    Get a random word from a list and split it into a dictionary.
    each character will start with the value False, that will turn into True, if guessed right.
    repeatedly ask the user to guess a letter. if the letter isn't in the word, subtract 1 life.
    show the snowman after each round. if the lives get to 0 (the snowman melts), the game is lost.
    """
    secret_word = get_random_word()
    guessed_chars = {}
    for char in [letter for letter in secret_word]:
        guessed_chars[char] = False
    print("\nWelcome to Snowman Meltdown!")
    lives = 3
    player_won = False
    while lives > 0 and not player_won:
        show_snowman(lives, guessed_chars, secret_word)
        guess = guess_letter().lower()
        if guess in secret_word:
            guessed_chars[guess] = True
        else:
            lives -= 1
        if not False in guessed_chars.values():
            print()
            print(f"****** Congratulations! you saved the Snowman! ******\n"
                  f"\t****** You found the word '{secret_word.title()}' ******")
            player_won = True
        elif lives < 1:
            show_snowman(lives, guessed_chars, secret_word)
            print("Oh no! the Snowman has melted away!")
            print(f"The word was: '{secret_word.title()}'")