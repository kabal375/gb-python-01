from random import randint

def create_grid():
# This function creates a blank playboard
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    board.insert(0,  [1, 2, 3, 4, 5, 6, 7, 8, 9]) # list of possible turns
    return board

def print_board(board):
# This function prints the board
    print("---+---+---")
    for r in range(3):
        print("", board[1 + r*3], "|", board[2 + r*3], "|", board[3 + r*3])
        print("---+---+---")
    return board

def check_win(board: list, sign: str) -> bool:
    if board[1] == board[2] == board[3] == sign or\
        board[4] == board[5] == board[6] == sign or\
        board[7] == board[8] == board[9] == sign or\
        board[1] == board[4] == board[7] == sign or\
        board[2] == board[5] == board[8] == sign or\
        board[3] == board[6] == board[9] == sign or\
        board[1] == board[5] == board[9] == sign or\
        board[3] == board[5] == board[7] == sign:
        return True
    else:
        return False

def make_player_turn(board: list, sign: str):
    is_legal_turn = False
    while not is_legal_turn:
        field = int(input(f'Введите номер поля для ввода {sign}: '))
        is_legal_turn = set_turn(board, field, sign)

def make_bot_turn(board: list, sign: str):
    list_of_turns = board[0]
    field = list_of_turns[randint(1, len(list_of_turns)) - 1]
    set_turn(board, field, sign)

def next_turn(board: list, signs: tuple, current_sign: int):
    if current_sign == 1:
        make_player_turn(board, signs[1])
    else:
        make_bot_turn(board, signs[0])

    return not current_sign

def check_turn(list_of_turns: list, field: int) -> bool:
    if field not in list_of_turns:
        print('Данное поле занято')
        return False
    else:
        return True

def set_turn(board: list, field: int, sign: str) -> bool:
    list_of_turns = board[0]
    if check_turn(list_of_turns, field):
        board[field] = sign
        list_of_turns.remove(field)
        return True
    else:
        return False

board = create_grid()

print_board(board)
signs = ('0', 'X')
current_sign = 1

end_of_game = False

while not end_of_game:
    next_sign = next_turn(board, signs, current_sign)
    print_board(board)

    if check_win(board, signs[current_sign]):
        if current_sign == 1:
            print("Победа игрока!")
        else:
            print('Победа бота!')
        end_of_game = True

    if len(board[0]) == 0:
        end_of_game = True
        print("GAME OVER!")

    current_sign = next_sign

