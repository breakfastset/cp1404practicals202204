import random

FILENAME = "words.txt"
MENU_PLAY = "P"
MENU_STATISTICS = "S"
MENU_QUIT = "Q"
MENU = """P. Play Game
S. Statistics
Q. Quit"""


def main():
    words = load_data(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()

    while choice != MENU_QUIT:
        if choice == MENU_PLAY:  # Play game
            winning_word = generate_word(words)
            if winning_word is not None:
                play_game(winning_word)
            else:
                print("Your words file might be corrupted")
                exit(1)   # exit with error
        elif choice == MENU_STATISTICS:
            pass
        else:
            print("Wrong option selected!")

        print(MENU)
        choice = input(">>> ").upper()

def load_data(filename):
    words = []
    with open(filename) as in_file:
        lines = in_file.readlines()
        for line in lines:
            words.append(line.strip().lower())
    return words

def play_game(winning_word):
    # print("=== Cheat: " + winning_word)
    tries = 5
    has_won = False

    while not has_won and tries > 0:
        guess = input("Enter a word: ").strip().lower()

        if guess == winning_word:
            has_won = True
        else:
            print_differences(guess, winning_word)
            tries -= 1
            print(f"You have {tries} tries left.")

    if has_won:
        print("You have won!")
    else:
        print("You lose. Try again!")
        print(f"Correct word is {winning_word}")


def print_differences(guess, winning_word):
    character_found_in_right_positions = ""
    character_found_in_wrong_positions = ""
    character_not_found = ""
    for i in range(len(guess)):
        if guess[i] in winning_word:
            if guess[i] == winning_word[i]:
                character_found_in_right_positions += guess[i] + "  "
            else:
                character_found_in_wrong_positions += guess[i] + "  "
        else:
            character_not_found += guess[i] + "  "
    print(f"Chars Found (Correct Pos): {character_found_in_right_positions}")
    print(f"Chars Found (Wrong Pos)  : {character_found_in_wrong_positions}")
    print(f"Chars Not Found          : {character_not_found}")


def generate_word(words):
    if len(words) > 0:
        index = random.randint(0, len(words))
        return words[index]


if __name__ == '__main__':
    main()
