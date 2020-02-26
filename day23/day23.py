import timeit
import numpy as np
from functools import reduce
from itertools import product


Charlie_Ang_setup = '''
from __main__ import Charlie_Ang_day23
'''

def Charlie_Ang_day23(board):
    # step 1 check for zero
    if reduce(lambda x,y: x or 0 in y, board, False):
        return False
    # step 2 check for horizontal and vertical values
    for one in board:
        if (reduce(lambda x,y: x + (1 * 10**y), one, 0)) != 1111111110:
            return False
    for one in zip(*board):
        if (reduce(lambda x,y: x + (1 * 10**y), one, 0)) != 1111111110:
            return False
    # step 3 look for quadrants  (this could be better done with numpy reshapes and numaxis, maybe!)
    for x,y in product((0,3,6), repeat=2):
        if (reduce(lambda x,y: x + (1 * 10**y), [] + board[y][x:x+3] + board[y+1][x:x+3] + board[y+2][x:x+3], 0)) != 1111111110:
            return False
    return True

TEST_CODE_Charlie_Ang = '''
result = Charlie_Ang_day23([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 0, 3, 4, 8],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day23
'''

def diana_henninger_day23(board):
    columns = [[] for x in range(9)]
    squares = [[] for x in range(9)]
    j = 0
    for row in board:
        if not len(set(row)) == 9: return False
        i = 0
        for r in row:
            if r not in columns[i]: columns[i].append(r)
            else: return False
            index = ((j//3)*3)+(i//3)
            if r not in squares[index]: squares[index].append(r)
            else: return False
            i+=1
        j += 1
    return True

TEST_CODE_diana_henninger = '''
result = diana_henninger_day23([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 0, 3, 4, 8],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
'''

ggebre_setup = '''
from __main__ import ggebre_day23
'''

def ggebre_day23(board):
    isValid = True
    board_transpose = np.array(board).transpose()  
    
    for row in board:
        if len(set(row)) != 9 or 0 in row:
            isValid = False  
    for row in board_transpose:
        if len(set(row)) != 9 or 0 in row:
            isValid = False 
    for row in range(0,9,3):
        for column in range(0,9,3):
            if len(set(np.reshape(board_transpose[row: row +3, column: column+3], 9))) != 9:
                isValid = False
    return isValid

TEST_CODE_ggebre = '''
result = ggebre_day23([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 0, 3, 4, 8],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
'''

Jens_setup = '''
from __main__ import Jens_day23
'''

def Jens_day23(board):
    for row in board: #check rows
        for i in range(1, 10):
            if not i in row:
                return False
    for n in range(9): #check columns
        column = []
        for m in range(9):
            column.append(board[m][n])
        for i in range(1, 10):
            if not i in column:
                return False
    for x in range(3): #check subgrids
        for y in range(3):
            subgrid = []
            for a in range(3):
                for b in range(3):
                    subgrid.append(board[3*x+a][3*y+b])
            for i in range(1, 10):
                if not i in subgrid:
                    return False
    return True

TEST_CODE_Jens = '''
result = Jens_day23([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 0, 3, 4, 8],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day23
'''

def check_line(line):
    sorted_line = sorted(line)
    return sorted_line == [1, 2, 3, 4, 5, 6, 7, 8, 9]    

def Jose_Catela_day23(board):
    # test for lines
    for line in board:
        if 0 in line:
            return False
        if not check_line(line):
            return False
    # test for rows
    transposed_board = tuple(zip(*board))
    for line in transposed_board:
        if not check_line(line):
            return False
    # test for 3x3 cells
    num_line = 0
    num_col = 0
    blocks = []
    line = []
    while num_line < 9:
        line.append(board[num_line][num_col])
        num_col += 1
        if num_col % 3 == 0:
            num_line += 1
            num_col -= 3
            if num_line % 3 == 0:
                num_line -= 3
                num_col += 3
                blocks.append(line)
                line = []
        if num_col == 9:
            num_col = 0   
            num_line += 3
    for line in blocks:
        if not check_line(line):
            return False
    return True

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day23([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 0, 3, 4, 8],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day23
'''

def Kurt_Hinderer_day23(board):
    valid = True
    row = board
    column = [[board[j][i] for j in range(len(board[i]))] for i in range(len(board))]
    cell = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            current_cell = [board[i][j], board[i][j+1], board[i][j+2], board[i+1][j], board[i+1][j+1], board[i+1][j+2], board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
            cell.append(current_cell)
    full = [row, column, cell]
    for arr in full:
        for test in arr:
            for i in range(1,10):
                if i not in test:
                    valid = False
                    break
    return valid

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day23([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 0, 3, 4, 8],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day23
'''

def Oleksandra_Chmel_day23(board):
    if any(0 in l for l in board): return False
    if min(len(set(l)) == 9 for l in board) == 0: return False    
    boardT = list(zip(*board))
    if min(len(set(l)) == 9 for l in boardT) == 0: return False
    a = np.array(board).reshape(3,3,-1,3).swapaxes(1,2)
    for y in a:
        for x in y:
            if not np.sum(x)==45:
                return False
    return True

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day23([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 0, 3, 4, 8],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
'''

Yang_setup = '''
from __main__ import Yang_day23
'''

def Yang_day23(board):
    for i,row in enumerate(board): 
        if len(set(row)) != 9: return False 
        if i%3==0: 
            for j,k in enumerate(row): 
                if j%3==0: 
                    if len(set(row[j:j+3]+board[i+1][j:j+3]+board[i+2][j:j+3])) != 9: return False 
    for column in zip(*board): 
        if len(set(column)) != 9: return False 
    return True

TEST_CODE_Yang = '''
result = Yang_day23([[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 0, 3, 4, 8],[1, 0, 0, 3, 4, 2, 5, 6, 0],[8, 5, 9, 7, 6, 1, 0, 2, 0],[4, 2, 6, 8, 5, 3, 7, 9, 1],[7, 1, 3, 9, 2, 4, 8, 5, 6],[9, 0, 1, 5, 3, 7, 2, 1, 4],[2, 8, 7, 4, 1, 9, 6, 3, 5],[3, 0, 0, 4, 8, 1, 1, 7, 9]])
'''

print("Time for Charlie_Ang test code: " + str(timeit.timeit(stmt=TEST_CODE_Charlie_Ang, setup=Charlie_Ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
