import os
from random import randint


hangman_title = """
       _   _                   __  __
      | | | | __ _ _ __   __ _|  \\/  | __ _ _ __
      | |_| |/ _` | '_ \\ / _` | |\\/| |/ _` | '_ \\
      |  _  | (_| | | | | (_| | |  | | (_| | | | |
      |_| |_|\\__,_|_| |_|\\__, |_|  |_|\\__,_|_| |_|
                         |___/
"""

game_over = """   ______                        ____
  / ____/___ _____ ___  ___     / __ \\_   _____  _____
 / / __/ __ `/ __ `__ \\/ _ \\   / / / / | / / _ \\/ ___/
/ /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /
\\____/\\__,_/_/ /_/ /_/\\___/   \\____/ |___/\\___/_/

"""

game_win = """       __  __                        _       __
       \\ \\/ /___  __  __   _      __(_)___  / /
        \\  / __ \\/ / / /  | | /| / / / __ \\/ /
        / / /_/ / /_/ /   | |/ |/ / / / / /_/
       /_/\\____/\\__,_/    |__/|__/_/_/ /_(_)

"""

hangman_states = ("""
      ______
      |/
      |
      |
      |
    __|_____        """, """
      ______
      |/    |
      |
      |
      |
    __|_____        """, """
      ______
      |/    |
      |     O
      |
      |
    __|_____        """, """
      ______
      |/    |
      |    \\O
      |
      |
    __|_____        """,  """
      ______
      |/    |
      |    \\O/
      |
      |
    __|_____        """, """
      ______
      |/    |
      |    \\O/
      |     |
      |
    __|_____        """, """
      ______
      |/    |
      |    \\O/
      |     |
      |    /
    __|_____        """, """
      ______
      |/    |
      |    \\O/
      |     |
      |    / \\
    __|_____        """)


def get_menu_option():
    os.system("cls || clear")
    print(hangman_title)
    print("""\n---------------------- Choose a level -----------------------\n
1 - easy
2 - medium
3 - hard
Enter \"quit\" to end the game.\n""")
    return input().lower()


def load_words(step):
    words = []
    try:
        with open("countries-and-capitals.txt") as f:
            lines = f.readlines()
    except FileNotFoundError as err:
        raise err

    # iterate through the lines of a file
    for i in range(0, len(lines), step):

        # get the first word of the line without whitespaces
        split_words = lines[i].split("|")
        word = split_words[0].strip()

        if len(word) > 0:
            words.append(word)
    return words


def play(word, lives):
    # initiate variables
    state = generate_state(word)
    entered_letters = set()

    while lives > 0 and "_" in state:
        print_state(state, lives)
        player_input = (input("Enter a letter: ")).lower()

        # check if the player want to quit
        if (player_input == "quit"):
            print("Good Bye!")
            return  # finish the game immediately

        # check if the character is a single letter
        if (len(player_input) != 1 or not player_input.isalpha()):
            print_state(state, lives)
            print("Wrong value entered.\n")
            input("Press enter to continue..")
            continue

        # check if the letter repeated
        if (player_input in entered_letters):
            print_state(state, lives)
            print("The letter is repeated.")
            print_entered_letters(entered_letters)
            input("Press enter to continue..")
            continue
        else:
            entered_letters.add(player_input)  # keep the letter

        # check if the player guessed
        if (player_input in word.lower()):
            fill_in_the_state(player_input, state, word)  # put the guessed letter in the missing fields
        else:
            lives -= 1  # reduce lives
            print_state(state, lives)

            if lives > 0:
                print("Missed!")
                print_entered_letters(entered_letters)
                print("Try again.")
            else:
                print(game_over)
                return  # finish the game immediately

            input("\nPress enter to continue..")

    print_state(state, lives)
    print(game_win)


def generate_state(word):
    state = []
    for i in range(len(word)):
        if word[i] == " ":
            state.append(" ")
        else:
            state.append("_")
    return state


def print_state(state, lives):
    # clear terminal
    os.system("cls || clear")

    print(hangman_title)
    print(f"\n------------- You have {lives} {'chances' if lives > 1 else 'chance'} to guess -------------\n")
    print(hangman_states[-lives-1], end="")

    # print characters with spaces between
    for ch in state:
        print(ch, end=" ")

    print("\n\n\n------------------------------------------------------\n\n")


def print_entered_letters(entered_letters):
    print("You already entered: ", end="")
    for ch in entered_letters:
        print(ch, end=" ")

    print("\n")


def fill_in_the_state(letter, state, word):
    i = 0
    for ch in word:
        if ch.lower() == letter:
            state[i] = ch
        i += 1


def main():
    leaves = None

    while not leaves:
        player_input = get_menu_option()

        if player_input == "1":
            leaves = 7
        elif player_input == "2":
            leaves = 5
        elif player_input == "3":
            leaves = 3
        elif player_input == "quit":
            return

    try:
        words = load_words(leaves//2)
    except FileNotFoundError:
        print("Could not open file")
        return

    word = words[randint(0, len(words))]  # get a random word
    play(word, leaves)  # start game


if __name__ == "__main__":
    main()
