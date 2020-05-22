from controller import board
play=0
def start(level):
    """
        use level to generate a new board to player
            easy:9x9
            medium:16x16
            hard:30x16
    """
    global play
    if level=="easy":
        play=board.board(9,9)
    elif level=='medium':
        play=board.board(16,16)
    elif level=='hard':
        play=board.board(30,16)
    return play.play,play.init_point
def print_ans():
    global play
    play.print_board()
def ask_hint(point):
    global play
    if point not in play.mines:
        return play.board[int(point/len(play.board[0]))][int(point%len(play.board[0]))]
    else:
        return -1
def check_ans(board):
    """
        check the player's ans is correct or not
    """
    global play
    if board==play.board:
        print("Correct")
    else:
        print("wrong")

