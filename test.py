from controller import controller
from player import play,draw
import time
import matplotlib.pyplot as plt
if __name__=="__main__": 
    max_time=0
    x=[float(i/100) for i in range(20,162)]
    y=[0 for i in range(20,161)]
    task=0
    t=0
    while(1):
        # print("t: ",t)
        # t+=1
        # start = time.time()
        
        board,init_point=controller.start('hard')
        play.init(board, init_point)
        while(1):
            point,point_type=play.fill(board)
            if point==-1 or point==-2:
                break
            if point_type==-1:
                board[int(point/len(board[0]))][int(point%len(board[0]))]='x'
            else:
                hint=controller.ask_hint(point)
                if hint != -1:
                    board[int(point/len(board[0]))][int(point%len(board[0]))]=hint
                    play.clause_generate(board,point)
                else:
                    print(point,point_type,init_point)
                    play.print_board(board)
                    time.sleep(10)
            # draw.draw(board,0)
        print(point)
        if point==-1:
            break
        # end=time.time()
        
        # if end-start>max_time and point!=-2:
        #     max_time = end-start
        # if point!=-2:
        #     print(end-start)
        #     print(task)
        #     task+=1
        #     for xth in range(len(x)-1):
        #         if end-start<x[xth+1] and end-start>=x[xth]:
        #             y[xth]+=1
    # x.pop()
    # plt.bar(x,y,width=0.01)
    # plt.show()
    # print(max_time)
    # print(y)
    draw.draw(board,1)
