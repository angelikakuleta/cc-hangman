import os


def play(word, lives):

    # initiate variables
    state = []
    tried = set()
    guessed = 0

    # give the initial state 
    for i in range(len(word)): 
        state.append("_")

    while lives > 0 and guessed < len(word):

        print_state(state, lives)

        # case insensitive player input
        player_input = (input("Enter a letter: ")).lower()

        # check if the player want to quit
        if (player_input == "quit"):
            print("Good Bye!")           
            return # finish the game immediately  

        # check if the letter repeated
        if (player_input in tried):
            print_state(state, lives)
            print("The letter is repeated.")
            print_tried(tried)
            input("Press enter to continue..")            
            continue        
        else:            
            tried.add(player_input) # keep the letter 

        # check if the player guessed
        if (player_input in word.lower()): 
            
            # put the guessed letter in the missing fields
            i = 0
            for ch in word: 
                if ch.lower() == player_input:
                    state[i] = ch
                    guessed += 1
                i += 1
        else:
            lives -= 1 # reduce lives
            print_state(state, lives)

            if lives > 0:
                print("Missed!")               
                print_tried(tried)
                print("Try again.")
            else:
                print(game_over)
                return # finish the game immediately
            
            input("\nPress enter to continue..")
   
    print_state(state, lives)
    print(game_win)


def print_state(iterable, lives):
    # clear terminal
    os.system("cls || clear")

    print(hangman_title)
    print(f'\n----------- You have {lives} chances to guess -----------\n')
    print(hangman_states[-lives-1], end ="")

    # print characters with spaces between
    for ch in iterable:
        print(ch, end=" ")

    print(f'\n\n\n--------------------------------------------------\n\n')


def print_tried(iterable):
    print("You already entered: ", end="")
    for ch in iterable:
        print(ch, end=" ")

    print("\n")


hangman_title = '''
     _   _                   __  __             
    | | | | __ _ _ __   __ _|  \/  | __ _ _ __  
    | |_| |/ _` | '_ \ / _` | |\/| |/ _` | '_ \ 
    |  _  | (_| | | | | (_| | |  | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_|  |_|\__,_|_| |_|
                       |___/                        
'''

game_over = '''  ____                         ___                 
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
'''

game_win = '''      __   __                     _       _ 
      \ \ / /__  _   _  __      _(_)_ __ | |
       \ V / _ \| | | | \ \ /\ / / | '_ \| |
        | | (_) | |_| |  \ V  V /| | | | |_|
        |_|\___/ \__,_|   \_/\_/ |_|_| |_(_)
'''

hangman_states = ('''
      ______
      |/
      |
      |
      |
    __|_____        ''','''
      ______
      |/    |
      |
      |
      |
    __|_____        ''','''
      ______
      |/    |
      |     O
      |
      |
    __|_____        ''','''
      ______
      |/    |
      |    (O
      |
      |
    __|_____        ''','''
      ______
      |/    |
      |    (O)
      |
      |
    __|_____        ''','''
      ______
      |/    |
      |    (O)
      |     |
      |
    __|_____        ''','''
      ______
      |/    |
      |    (O)
      |     |
      |    /
    __|_____        ''','''
      ______
      |/    |
      |    (O)
      |     |
      |    / \\
    __|_____        ''')

play('Codecool', 6)