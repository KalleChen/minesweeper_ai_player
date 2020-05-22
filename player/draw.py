from matplotlib import pyplot as plt
import matplotlib.patches as patches

plt.ion()
fig=plt.axes()
plt.gca().invert_yaxis()
def draw(board,stop):
    """
        just draw board picture and show
    """
    global fig
    fig.clear()
    pos=(0,0)
    x=1/len(board[0])
    y=1/len(board)
    for row in board:
        for element in row:
            if element=='x':
                rect=patches.Rectangle(pos,x,y,linewidth=1,edgecolor='black',facecolor='red')
                fig.add_patch(rect)
                plt.text(pos[0]+x/2, pos[1]+y/2, str(element))
            elif element=='?':
                rect=patches.Rectangle(pos,x,y,linewidth=1,edgecolor='black',facecolor='white')
                fig.add_patch(rect)
                plt.text(pos[0]+x/2, pos[1]+y/2, "?")
            else:
                rect=patches.Rectangle(pos,x,y,linewidth=1,edgecolor='black',facecolor='yellow')
                fig.add_patch(rect)
                plt.text(pos[0]+x/2, pos[1]+y/2, str(element))
            pos=(pos[0]+x,pos[1])
        pos=(0,pos[1]+y)
    if stop==1:
        plt.ioff()
    plt.show()
    plt.pause(0.0000001)
    


