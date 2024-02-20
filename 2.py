
board_size = 3
board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    print('_'*4* board_size)
    for i in range(board_size):
        print((' '*3+'|')*3)
        print(board[i*3],' |', board[1+i*3],'|',board[2+i*3],'|')
        print(('_' * 3 + '|') *3)
    pass
def game_step(index, char):
    if index >10 or index <1 or board[index-1] in ('X','0'):
        return False

    board[index-1] = char
    return True
def check_win():
    win = False
    win_combination = (
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    )
    for pos in win_combination:
        if board[pos[0]]== "X" == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]




    return win



def start_game():
    current_player = 'X'
    step = 1
    draw_board()
    while (step<9) and (check_win() == False):
        index = input("Ходит игрок " + current_player + ' Введите номер поля:')
        if int(index) == '0':
            break
        if game_step(int(index),current_player):
            print('Ход')
            if current_player == "X":
                current_player ='O'
            else:
                current_player = 'X'


            draw_board()
            step += 1
        else:
            print('Неверный ход')
    if step ==10:
        print('игра окончена')
    else:
        print("Выиграл ", check_win())

    pass
start_game()



