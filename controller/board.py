import random
import math
class board():
    """
        class has:
                board:ans board
                play:board which is given player to player
                mines:mine points
                init_point:initial point to give to player
    """
    def __init__(self,x,y):
        self.board = [[0 for i in range(x)] for j in range(y)]
        minesNum=5 if x==5 else 10 if x==9 else 25 if x==16 else 99
        points=random.sample(range(0,x*y),minesNum+round(math.sqrt(x*y)))
        self.mines=points[0:minesNum]
        self.init_point=points[minesNum:]
        for mine in self.mines:
            self.board[int(mine/x)][int(mine%x)]='x'
            for i in range(-1,2):
                for j in range(-1,2):
                    if int(mine/x)+i>=0 and int(mine/x)+i<y and int(mine%x)+j>=0 and int(mine%x)+j<x:
                        if self.board[int(mine/x)+i][int(mine%x)+j]!='x':
                            self.board[int(mine/x)+i][int(mine%x)+j]+=1
        self.play=[['?' for i in range(x)]for j in range(y)]

    def print_board(self):
        for row in self.board:
            for element in row:
                print(element,end=' ')
            print()
    def print_play(self):
        for row in self.play:
            for element in row:
                print(element,end=' ')
            print()

