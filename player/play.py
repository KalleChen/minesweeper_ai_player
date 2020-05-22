from player.print_board import print_board
from itertools import combinations
KB=[]
KB0=[]
def init(board,init_point):
    """
        just initialize KB and KB0
    """
    global KB
    global KB0
    KB0=[]
    KB=[]
    for point in init_point:
        KB.append([-(point+1)])

def fill(board):
    """
        Find out which is mine or safe
    """
    if len(KB0)==len(board[0])*len(board) or len(KB)==0:
        return -1,-1
    count=0
    while(1):
        flag=-1
        point=0
        point_type=0
        for clause in range(len(KB)):
            if len(KB[clause])==1:
                flag=clause
                break
        if flag==-1 and count==1:
            return -2,-1            # stuck game
        if flag!=-1:
            if KB[flag][0]>0:
                point=KB[flag][0]
                point_type=-1
            else:
                point=-KB[flag][0]
                point_type=1
            if(KB[flag] in KB0):
                KB.remove(KB[flag])
                continue
            KB0.append(KB[flag])
            KB.remove(KB[flag])
            new_clauses=[]
            for clause in KB:
                new_clause=maching(clause,KB0[len(KB0)-1])
                if new_clause!=[]:
                    new_clauses.append(new_clause)
            for new_clause in new_clauses:
                insert(new_clause)
            return point-1,point_type
        else:
            pair_maching()
            count+=1

def maching(clause1,clause2):
    """
        maching two clause if new clause come out, return it
    """
    count=0
    delete=0
    new_clause=[]
    for element in clause2:
        if -element in clause1:
            delete=element
            count+=1
    if count==1:
        for element in clause1:
            if element != -delete:
                new_clause.append(element)
        for element in clause2:
            if element != delete and element not in new_clause:
                new_clause.append(element)
    return new_clause

def insert(insert_clause):
    """
        insert a clause into KB
    """
    global KB
    global KB0
    for element in KB0:
        if -element[0] in insert_clause:
            insert_clause.remove(-element[0])
        if element[0] == insert_clause:
            insert_clause=[]
    if insert_clause!=[]:
        delete=[]
        flag=0
        for clause in KB:
            count=0
            for element in insert_clause:
                if element in clause:
                    count+=1
            if count==len(insert_clause):
                if count>=len(clause):
                    flag=1
                else:
                    delete.append(clause)
            elif count==len(clause):
                if count<len(insert_clause):
                    flag=1
        
        for clause in delete:
            KB.remove(clause)
        if flag==0:
            KB.append(insert_clause)

def pair_maching():
    """
        pairwise maching KB 
    """
    global KB
    new_clauses=[]
    for i in range(len(KB)-1):
        for j in range(i+1,len(KB)):
            if len(KB[i])<=2 or len(KB[j])<=2:
                new_clause=maching(KB[i],KB[j])
                if new_clause !=[]:
                    new_clauses.append(new_clause)
    for new_clause in new_clauses:
        insert(new_clause)

def clause_generate(board,point):
    """
        use hint to generate new clause
    """
    clauses=[]
    cells=[]
    mines=0
    for i in range(-1,2):
        for  j in range(-1,2):
            if int(point/len(board[0]))+i>=0 and int(point/len(board[0]))+i<len(board) and int(point%len(board[0]))+j>=0 and int(point%len(board[0]))+j<len(board[0]):
                if board[int(point/len(board[0]))+i][int(point%len(board[0]))+j]=='?':
                    cells.append(point+i*len(board[0])+j+1)
                if board[int(point/len(board[0]))+i][int(point%len(board[0]))+j]=='x':
                    mines+=1
    m=len(cells)
    n=board[int(point/len(board[0]))][int(point%len(board[0]))]-mines
    if m==n:
        for cell in cells:
            clauses.append([cell])
    if n==0:
        for cell in cells:
            clauses.append([-cell])
    if m>n and n>0:
        for clause in list(combinations(cells,m-n+1)):
            clauses.append(list(clause))
        neg_cells=[-x for x in cells]
        for clause in list(combinations(neg_cells,n+1)):
            clauses.append(list(clause))
    for clause in clauses:
        insert(clause)

