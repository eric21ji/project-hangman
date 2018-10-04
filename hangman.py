# hangman.py 

def main():
    secret_word = get_secret_word()
    correct_guesses = ""
    wrong_guesses = ""

    while (not word_is_solved(secret_word, correct_guesses) and
            not player_is_dead(wrong_guesses)):
        display_platform(wrong_guesses)
        display_letters(secret_word, correct_guesses)
        guess = get_guess()

        # if guess is a word:
            # if guess is correct:
                # win
            # else:
                # lose

        # HANDLE SINGLE LETTER GUESS
        # if guess is in the word, the add it to the correct guesses
        # otherwise, add it to the incorrect guesses

    if word_solved(secret_word, correct_guesses):
        show_win_screen()
    else:
        show_lose_screen()


def get_secret_word():
    """Will return a single word from a list of words.
    Returns:
        Single word from a list
    """
    pass


def word_is_solved(word, guesses):
    """Will check to see if a word has been completely solved.
    Args:
        word (str): The secret word
        guesses (str): The string containing all correct guesses
    Returns:
        bool: True if word is solved, False if word is not.
    """
    pass


def player_is_dead(wrong_guesses):
    """Determines if the player is dead (too many guesses).
    Args:
        bad_guesses (str): A string containing all of the wrong guesses
    Returns
        bool: True if dead, False otherwise
    """
    pass


def display_platform(wrong_guesses):
    """Displays (prints) hanging platform based on how many incorrect guesses.
    Args:
        wrong_guesses (str): A string containing all wrong guesses.
    """
    pass


def get_blanked_word(word, guesses):
    """Displays (prints) the letter-board,
    underscores (_) for letters not yet guessed.
    Args:
        word (str): The secret word
        guesses (str): A string of correct guesses
    """
    letters = list(word)
    guesses = list(set(guesses))
    word_list = list(word)

    for k in range(len(word)):
        if(letters[k] != " "):
            letters[k] = "_"

    for guess_letter in guesses:
      num_of_guess_letters = word.count(guess_letter)
      for j in range(num_of_guess_letters):
          if(guess_letter in word):
              ind = word_list.index(guess_letter)
              letters[ind] = guess_letter
              word_list[ind] = "_"

    return " ".join(letters)


def get_guess():
    """Will take the user's guess. Ensures the input is valid.
    """
    pass


def show_win_screen():
    """Will display ASCII art for a win screen"""
    pass


def show_lose_screen():
    """Will display ASCII art for a lose screen"""
    pass


if __name__ == "__main__":
    main()
