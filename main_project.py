import random
import io
import sys
from art import *

yes: list = ["yes", "yeah", "1", "ye", "y"]
no: list = ["no", "nah", "0", "na", "n"]
skip: str = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
score: int = 0
game_state: bool = None
tree_state: bool = None

wood: bool = False
axe: bool = False

game_state: bool = None


def get_highscore() -> int:
    scores = []
    with open("score.txt", "r") as f:
        for lines in f:
            scores.append(lines.split(": ")[1])
        if len(scores) == 0:
            return 0
    return int(max(scores))


def save_scorefile(name: str, score: int) -> None:
    file_lines = []
    with open("score.txt", "r") as f:
        for lines in f:
            file_lines.append(lines)
    if get_highscore() < score:
        with open("score.txt", "w") as f:
            f.write(f"{name}: {score}\n")

            if len(file_lines) > 10:
                file_lines.pop(10)
            for i in range(len(file_lines)):
                f.write(file_lines[i])

    if get_highscore() > score and len(file_lines) < 11:
        with open("score.txt", "w") as f:
            f.write(f"{name}: {score}\n")


def read_scorefile() -> None:
    print(skip)
    print("SCOREBOARD:")
    with open("score.txt", "r") as f:
        for lines in f:
            print(f"    {lines.replace('\n', '')}")
    print("")


def start_game() -> bool:
    global game_state, score
    score = 0

    answer = input("Do you want to play a game? ")
    while answer.lower() not in yes + no:
        answer = input("Do you want to play a game? ")
    if answer.lower() in yes:
        game_state = True
    elif answer.lower() in no:
        game_state = False
        answer = input("Do you want to see the scoreboard? ")
        if answer.lower() in yes:
            read_scorefile()
        elif answer.lower() in no:
            exit()


def show_inventory() -> None:
    print(skip)
    inventory = []
    if wood and not axe:
        for i in range(len(empty_slot)):
            inventory.append(wood_slot[i] + empty_slot[i] + empty_slot[i])
    if wood and axe:
        for i in range(len(empty_slot)):
            inventory.append(wood_slot[i] + axe_slot[i] + empty_slot[i])

    if not wood and not axe:
        for i in range(len(empty_slot)):
            inventory.append(empty_slot[i] + empty_slot[i] + empty_slot[i])
    for i in range(len(inventory)):
        print(inventory[i])
    input("\nPress enter to continue...")


def update_score() -> None:
    global score
    score += 1


def show_current_score() -> int:
    global score
    return score


def draw_game() -> None:
    global tree_state
    print(skip)
    tree_state = None
    board = []
    if random.randint(0, 2) == 0:
        # there is a chance for a tree to generate
        tree_state = True
        for i in range(len(ground)):
            board.append(steve[i] + ground[i] + tree[i])
    else:
        tree_state = False
        for i in range(len(ground)):
            board.append(steve[i] + ground[i] + ground[i])

    for i in range(len(board)):
        print(board[i])


def death() -> None:
    global game_state
    game_state = False

    print(skip)
    if get_highscore() < show_current_score():
        name = input(
            """\nYOU GOT A HIGH SCORE!
Enter your name:
        """
        )
        save_scorefile(name.upper(), show_current_score())

    elif get_highscore() > show_current_score():
        print(
            f"""YOU DIED!
            Your score was: {show_current_score()} 
            """
        )
    start_game()


def show_options() -> list:
    options_list = ["1. Go right", ". Cut down tree", ". Show inventory"]
    available_options = [options_list[0]]
    counter = 2
    if tree_state:
        available_options.append(f"{counter}{options_list[1]}")
        counter += 1

    if wood:
        available_options.append(f"{counter}{options_list[2]}")
        counter += 1

    return available_options


start_game()


def option_r() -> None:
    if random.randint(0, 4) == 0:
        print(skip)
        print("\nYou ran trough the field")
        print("The snake got you")
        input("\nPress enter to continue...")
        print(skip)
        for i in range(len(snake)):
            print(snake[i])
        input("\nPress enter to continue...")
        death()
    else:
        update_score()


def option_t() -> None:
    global wood
    if random.randint(0, 4) == 0:
        print(skip)
        print("\nYou cut down the tree!")
        print("The tree fell on you")
        input("\nPress enter to continue...")
        print(skip)
        for i in range(len(steve_fallen)):
            print(steve_fallen[i])
        input("\nPress enter to continue...")
        death()
    else:
        input(skip + "You now have wood! Press enter to continue...")
        wood = True
        update_score()


def option_i() -> None:
    show_inventory()


while game_state:
    draw_game()
    print("\nWhat do you want to do?")
    for i in show_options():
        print(f"    {i}")
    option = input("\n    ")

    try:
        int(option)
    except ValueError:
        print("\nWhat do you want to do?")
        for i in show_options():
            print(f"    {i}")
        option = input("\n    ")

    if len(show_options()) == 1:
        while option not in ["1"]:
            print("\nWhat do you want to do?")
            for i in show_options():
                print(f"    {i}")
            option = input("\n    ")

    if len(show_options()) == 2:
        while option not in ["1", "2"]:
            print("\nWhat do you want to do?")
            for i in show_options():
                print(f"    {i}")
            option = input("\n    ")

    if len(show_options()) == 3:
        while option not in ["1", "2", "3"]:
            print("\nWhat do you want to do?")
            for i in show_options():
                print(f"    {i}")
            option = input("\n    ")

    if int(option) == 1:
        option_r()

    elif int(option) == 2 and not tree_state and wood and len(show_options()) == 2:
        option_i()

    elif int(option) == 2 and tree_state and len(show_options()) == 2:
        option_t()

    elif int(option) == 3 and tree_state and wood and len(show_options()) == 3:
        option_i()

    
