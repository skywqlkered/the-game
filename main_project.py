import random
from art import *

yes: list = ["yes", "yeah", "1", "ye", "y"]
no: list = ["no", "nah", "0", "na", "n"]
skip: str = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" #this skips a lot of lines
score: int = 0 # global score variable
game_state: bool = None 
tree_state: bool = None

wood: bool = False # becomes true if user has wood
axe: bool = False # i dont think this is still used

game_state: bool = None


def get_highscore() -> int: # returns the highest score from the score file
    scores = []
    with open("score.txt", "r") as f:
        for lines in f:
            scores.append(lines.split(": ")[1])
        if len(scores) == 0: # returns 0 if the file is empty
            return 0
    return int(max(scores)) # typecasting W


def save_scorefile(name: str, score: int) -> None:
    file_lines = []
    with open("score.txt", "r") as f: # gathers the lines from the score file
        for lines in f:
            file_lines.append(lines)
    if get_highscore() < score: # save the new highscore above the other scores
        with open("score.txt", "w") as f:
            f.write(f"{name}: {score}\n")

            if len(file_lines) > 10: # remove the 10th item so the scoreboard stays at 10 i think
                file_lines.pop(10)
            for i in range(len(file_lines)):
                f.write(file_lines[i])

    if get_highscore() > score and len(file_lines) < 11:
        with open("score.txt", "w") as f:
            f.write(f"{name}: {score}\n")


def read_scorefile() -> None: # prints the scoreboard with an indent
    print(skip)
    print("SCOREBOARD:")
    with open("score.txt", "r") as f:
        for lines in f:
            print(f"    {lines.replace('\n', '')}")
    print("")


def start_game() -> bool | None: # asks the user if they want to play
    global game_state, score
    score = 0
    global wood, tree_state
    wood = False
    tree_state = False

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


def show_inventory() -> None: # prints the inventory
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


def show_current_score() -> int: # kinda useless but why not?
    global score
    return score


def draw_game() -> None: # prints the gameboard
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


def death() -> None: # prints the death screen and checks for a highscore
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


def show_options() -> list: # returns a list of available options based on the states
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


def walk_animation() -> None: # prints the walking animation
    print(skip)
    for i in range(len(ground)):
        print(ground[i] + steve[i] + ground[i])

    input("\nPress enter to continue...")

    print(skip)

    for i in range(len(ground)):
        print(ground[i] + ground[i] + steve[i])

    input("\nPress enter to continue...")


def tree_animation() -> None: # prints the tree animation
    print(skip)
    for i in range(len(tree1)):
        print(tree1[i])
    input("\nPress enter to continue...")
    print(skip)
    for i in range(len(tree2)):
        print(tree2[i])
    input("\nPress enter to continue...")
    print(skip)
    for i in range(len(tree_fallen)):
        print(tree_fallen[i])
    input("\nPress enter to continue...")
    print(skip)


start_game()


def option_r() -> None: # called when user chooses right
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
        walk_animation()
        update_score()


def option_t() -> None: # called when user chooses the tree
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
        tree_animation()
        if wood:
            input(skip + "You can't carry more wood, you're too weak. Press enter to continue...")
        
        if not wood:
            input(skip + "You now have wood! Press enter to continue...")
            wood = True
            update_score()
        


def option_i() -> None: # called when user chooses the inventory
    show_inventory()


while game_state: # the game loop
    draw_game() # start with a new board
    print("\nWhat do you want to do?") # gives the user the illusion of choice
    for i in show_options():
        print(f"    {i}")
    option = input("\n    ")

    try: # makes sure the user input can be converted to an int
        int(option)
    except ValueError:
        print("\nWhat do you want to do?")
        for i in show_options():
            print(f"    {i}")
        option = input("\n    ")

    if len(show_options()) == 1: # prevents wrong inputs
        while option not in ["1"]:
            print("\nWhat do you want to do?")
            for i in show_options():
                print(f"    {i}")
            option = input("\n    ")

    if len(show_options()) == 2: # prevents wrong inputs
        while option not in ["1", "2"]:
            print("\nWhat do you want to do?")
            for i in show_options():
                print(f"    {i}")
            option = input("\n    ")

    if len(show_options()) == 3: # prevents wrong inputs
        while option not in ["1", "2", "3"]:
            print("\nWhat do you want to do?")
            for i in show_options():
                print(f"    {i}")
            option = input("\n    ")

    if int(option) == 1: # calles right
        option_r()

    elif int(option) == 2 and not tree_state and wood and len(show_options()) == 2:
        option_i() # calls inventory when there is no tree and there is wood

    elif int(option) == 2 and tree_state and len(show_options()) == 2:
        option_t() # calls tree when there is a tree

    elif int(option) == 3 and tree_state and wood and len(show_options()) == 3:
        option_i() # calls inventory when there is a tree and there is wood

    elif int(option) == 2 and tree_state and wood and len(show_options()) == 3:
        option_t() # calls tree when there is a tree and there is wood