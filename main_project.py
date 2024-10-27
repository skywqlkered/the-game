import random
score = None
game_state = None
tree_state = None

wood = None
axe = None
crafting_table = None

ground = [
    "                   ",
    "                   ",
    "                   ",
    "                   ",
    "                   ",
    "                   ",
    "                   ",
    "                   ",
    "_______\\/__________",
]

tree = [
    "                   ",
    "        _____      ",
    "     __|     |__   ",
    "    |           |  ",
    "    |           |  ",
    "    |____   ____|  ",
    "        |  |       ",
    "        |  |       ",
    "________|  |_______",
]

tree1 = [
    "                   ",
    "        _____      ",
    "     __|     |__   ",
    "    |           |  ",
    "    |           |  ",
    "    |____   ____|  ",
    "        |  |       ",
    "        \\  |       ",
    "________|  |_______",
]

tree2 = [
    "                   ",
    "        ____       ",
    "     __|    |__    ",
    "    |          |   ",
    "    |          |   ",
    "    |___    ___|   ",
    "        |__|       ",
    "         __        ",
    "________|  |_______",
]

tree_fallen = [
    "                           ",
    "                           ",
    "                           ",
    "                           ",
    "                           ",
    "               _____       ",
    "          ____|     |__    ",
    "  __      ____       __|   ",
    "_|  |_________|_____|______",
]

steve = [
    "                   ",
    "                   ",
    "                   ",
    "        ___        ",
    "       |   |       ",
    "       |___|       ",
    "      ___|___      ",
    "     /   |   \\     ",
    "________/ \\________",
]

steve_fallen = [
    "                         ",
    "                         ",
    "                         ",
    "            ____   \\/    ",
    "         __|    |___|__  ",
    "        |__      ______  ",
    "           |____|/ _|_ \\ ",
    "                  |x x|  ",
    "__________________|___|__",
]

empty_slot = [
    " ______ ",
    "|      | ",
    "|      | ",
    "|______| "
]

axe_slot = [
    " ______  ",
    "|  |D) | ",
    "|  |   | ",
    "|__|___| "
]

wood_slot = [
    " ______ ",
    "|  __  | ",
    "| |__| | ",
    "|______| "
]
game_state = None


def start_game() -> bool:
    global game_state
    yes: list = ["yes", "yeah", "1", "ye", "y"]
    no: list = ["no", "nah", "0", "na", "n"]

    answer = input("Do you want to play a game? ")
    while answer.lower() not in yes + no:
        answer = input("Do you want to play a game? ")
    if answer.lower() in yes:
        game_state = True
    elif answer.lower() in no:
        game_state = False

def show_inventory() -> None:
    pass

def update_score() -> int:
    global score
    score =+ 1
    

def show_score()-> int:
    global score
    return score

def draw_game() -> None:
    global tree_state
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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
            board.append(steve[i] + ground[i]+ ground[i])

    for i in range(len(board)):
        print(board[i])


start_game()
print(game_state)
while game_state:
    draw_game()
    print("\n")
    if not tree_state:
        option = int(
            input(
                """What do you want to do?
        1. Go right\n
        """
            )
        )

        if option == 1:
            update_score()
            draw_game()

    if tree_state:
        option = int(
            input(
                """What do you want to do?
        1. Go right
        2. Cut down tree\n
        """
            )
        )

        if option == 1:
            update_score()
            draw_game()
        elif option == 2:
            if random.randint(0, 4) == 0:
                print(f"\nYour score is {show_score()}\n")

                raise Exception("You died!")
            else:
                input("You now have wood! Press enter to continue...")
                wood = True
                update_score()
                draw_game()
    
    
