from controller import controller
from player import play, draw
import time
if __name__ == "__main__":
    """
        Here to start the game 
        controller.start will give you a space board and initial point,
        and there are three level you can choose "easy", "medium:, "hard"
        play.fill will find out the point which is sure to be mine or safe
        and just repeat this until the board is filled completely
    """
    board, init_point = controller.start('hard')
    play.init(board, init_point)
    while(1):
        point, point_type = play.fill(board)
        if point == -1 or point == -2:
            break
        if point_type == -1:
            board[int(point/len(board[0]))][int(point % len(board[0]))] = 'x'
        else:
            hint = controller.ask_hint(point)
            if hint != -1:
                board[int(point/len(board[0]))][int(point %len(board[0]))] = hint
                play.clause_generate(board, point)
            else:
                print(point, point_type, init_point)
                play.print_board(board)
                time.sleep(10)
        draw.draw(board, 0)

    if point == -2:
        print("Stuck Game")
        print("ans:")
        draw.draw(board, 1)
    else:
        print("ans:")
        controller.print_ans()
        controller.check_ans(board)
        draw.draw(board, 1)
