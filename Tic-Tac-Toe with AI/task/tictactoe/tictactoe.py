def print_game_board(input_cells: str):
    input_cells = input_cells.replace("_", " ")
    print("---------")
    print("| {} {} {} |".format(input_cells[0], input_cells[1], input_cells[2]))
    print("| {} {} {} |".format(input_cells[3], input_cells[4], input_cells[5]))
    print("| {} {} {} |".format(input_cells[6], input_cells[7], input_cells[8]))
    print("---------")
    pass


def convert_to_list_position(user_move: list):
    if user_move == [1, 3]:
        return 0
    elif user_move == [2, 3]:
        return 1
    elif user_move == [3, 3]:
        return 2
    elif user_move == [1, 2]:
        return 3
    elif user_move == [2, 2]:
        return 4
    elif user_move == [3, 2]:
        return 5
    elif user_move == [1, 1]:
        return 6
    elif user_move == [2, 1]:
        return 7
    elif user_move == [3, 1]:
        return 8
    else:
        pass


def get_user_move(game_board: str, user_symbol: str):
    while True:
        user_move = list(input("Enter cells: ").replace(" ", ""))
        if any([not char.isdigit() for char in user_move]):
            print("You should enter numbers!")
        elif len(user_move) > 2:
            print("Too many numbers. Input should be two numbers only!")
        elif any([int(x) > 3 for x in user_move]) or any([int(x) < 1 for x in user_move]):
            print("Coordinates should be from 1 to 3!")
        else:
            list_pos = convert_to_list_position([int(x) for x in user_move])
            if game_board[list_pos] == "_":
                game_board = game_board[:list_pos] + user_symbol + game_board[list_pos+1:]
                return game_board
            else:
                print("This cell is occupied! Choose another one!")


def check_for_winner(game_board: str):
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != "_":
        return game_board[0] + " wins"
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "_":
        return game_board[3] + " wins"
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "_":
        return game_board[6] + " wins"
    elif game_board[0] == game_board[3] == game_board[6] and game_board[0] != "_":
        return game_board[0] + " wins"
    elif game_board[1] == game_board[4] == game_board[7] and game_board[1] != "_":
        return game_board[1] + " wins"
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "_":
        return game_board[2] + " wins"
    elif game_board[0] == game_board[4] == game_board[8] and game_board[0] != "_":
        return game_board[0] + " wins"
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != "_":
        return game_board[2] + " wins"
    elif any([x == "_" for x in game_board]):
        return "Game not finished"
    else:
        return "Draw"


def calc_user_symbol(game_board: str):
    if game_board.count("X") < game_board.count("O") or game_board.count("X") == game_board.count("O"):
        return "X"
    else:
        return "O"


if __name__ == '__main__':
    in_gb = input("Enter game board: ")
    print_game_board(in_gb)
    gb = get_user_move(in_gb, calc_user_symbol(in_gb))
    print_game_board(gb)
    print(check_for_winner(gb))
