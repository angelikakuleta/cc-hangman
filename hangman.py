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

        print_state(state)

        # case insensitive player input
        player_input = (input("Enter a letter: ")).lower()

        # check if the player want to quit
        if (player_input == "quit"):
            print("Good Bye!")           
            return # finish the game immediately 

        # check if the letter repeated
        if (player_input in tried): 
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

            if lives > 0:
                print("Missed!")               
                print_tried(tried)
                print("Try again.")
            else:
                print("Sorry, you lose.")
                return # finish the game immediately
            
            input("\nPress enter to continue..")
   
    print_state(state)
    print("Congratulation!")


def print_state(iterable):
    # clear terminal
    os.system("cls || clear")

    # print characters with spaces between
    for ch in iterable:
        print(ch, end=" ")

    print("\n")


def print_tried(iterable):
    print("You already tried:")
    for ch in iterable:
        print(ch, end=" ")

    print("\n")


play('Codecool', 6)