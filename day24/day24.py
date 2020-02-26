import timeit
import numpy as np
from copy import deepcopy


Jose_Catela_setup = '''
from __main__ import Jose_Catela_day24
'''

def existsInRow(row, num, puzzle):
    for col in range(0,9):
        if puzzle[row][col] == num:
            return True
    return False
def existsInCol(col, num, puzzle):
    for row in range(0,9):
        if puzzle[row][col] == num:
            return True
    return False
def existsInCell(rowCell, colCell, num, puzzle):
    for row in range(0,3):
        for col in range(0,3):
            if puzzle[row+rowCell][col+colCell] == num:
                return True
    return False
def canInsert(row, col, num, puzzle):
    if num == 0 or existsInRow(row, num, puzzle) or existsInCol(col, num, puzzle) or existsInCell(row - row % 3, col - col % 3, num, puzzle):
        return False
    return True
def Jose_Catela_day24(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    # print(puzzle)
    solved = deepcopy(puzzle)
    pos = 0
    back = False
    while pos < 81:
        row = pos // 9
        col = pos % 9
        if puzzle[row][col] == 0:
            num = solved[row][col] + 1
            # print(num)
            while num < 10:
                if canInsert(row, col, num, solved):
                    solved[row][col] = num
                    back = False
                    break
                num += 1
            if num == 10:
                back = True
                solved[row][col] = 0
        if back:
            pos -= 1
        else:
            pos += 1        
    return solved

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day24([[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day24
'''

def Kurt_Hinderer_day24(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    board = set_up_board(puzzle)
    # alternates between two methods, this is the switch
    eliminate = True
    while not test_complete(print_board(board)):
        if eliminate:
            board = remove_possibilites(board)
        else:
            board = find_unique(board)
        eliminate = not eliminate
    return print_board(board)
#change the board into lists where all possible values are in the list
def set_up_board(puzzle):
    board = []
    for i in range(len(puzzle)):
        board.append([])
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != 0:
                board[i].append([puzzle[i][j]])
            else:
                board[i].append([1,2,3,4,5,6,7,8,9])
    return board
# returns it without the lists in the cells, puts 0 if there is more than one option
def print_board(board):
    puzzle = []
    for i in range(len(board)):
        puzzle.append([])
        for j in range(len(board[i])):
            if len(board[i][j]) == 1:
                puzzle[i].append(board[i][j][0])
            else:
                puzzle[i].append(0)
    return puzzle
# removes possibilites if it's a definite in the same row, column, or box.
def remove_possibilites(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board[i][j]) == 1:
                number = board[i][j][0]
                for k in range(len(board[i])):
                    if j != k and number in board[i][k]:
                        board[i][k].remove(number)
                for k in range(len(board)):
                    if i != k and number in board[k][j]:
                        board[k][j].remove(number)
                box_x = i//3 * 3
                box_y = j//3 * 3
                for k in range(3):
                    for l in range(3):
                        if i != box_x + k and j != box_y + l and number in board[box_x + k][box_y + l]:
                            board[box_x + k][box_y + l].remove(number)
    return board
# checks to see if a possiblity is unique in a row, column, or box.
def find_unique(board):
    #rows
    for i in range(9):
        for num in range(1,10):
            found1 = False
            found2 = False
            location = -1
            for j in range(9):
                if num in board[i][j]:
                    if not found1:
                        found1 = True
                        location = j
                    elif not found2:
                        found2 = True
            if not found2 and location > -1:
                board[i][location] = [num]
    #columns
    for i in range(9):
        for num in range(1,10):
            found1 = False
            found2 = False
            location = -1
            for j in range(9):
                if num in board[j][i]:
                    if not found1:
                        found1 = True
                        location = j
                    elif not found2:
                        found2 = True
            if not found2 and location > -1:
                board[location][i] = [num]
    #boxes
    for i in range(9):
        i_y = i//3
        i_x = i%3
        for num in range(1,10):
            found1 = False
            found2 = False
            location = -1
            for j in range(9):
                j_y = j//3
                j_x = j%3
                if num in board[i_x*3+j_x][i_y*3+j_y]:
                    if not found1:
                        found1 = True
                        location = j
                    elif not found2:
                        found2 = True
            if not found2 and location > -1:
                board[i_x*3+location%3][i_y*3+location//3] = [num]
    return board
# check to see if we're done (reused code).
def test_complete(board):
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
result = Kurt_Hinderer_day24([[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day24
'''

def Oleksandra_Chmel_day24(puzzle):
    unique = '123456789'
    solution = [[unique if el==0 else str(el) for el in l] for l in puzzle]
    length = len(solution)
    def brute_force(board):
        de = [''] * length
        for i,l in enumerate(board):
            for ind,el in enumerate(l):
                if len(el) == 1:
                    de[i] += el
        for i,l in enumerate(board):
            for ind,el in enumerate(l):
                if len(el) != 1:
                    board[i][ind] = ''.join(['' if elem in de[i] else elem for elem in el])
        boardT = list(map(list, zip(*board)))
        de = [''] * length
        for i,l in enumerate(boardT):
            for ind,el in enumerate(l):
                if len(el) == 1:
                    de[i] += el
        for i,l in enumerate(boardT):
            for ind,el in enumerate(l):
                if len(el) != 1:
                    boardT[i][ind] = ''.join(['' if elem in de[i] else elem for elem in el])
        board = list(map(list, zip(*boardT)))
        a = np.array(board).reshape(3,3,-1,3).swapaxes(1,2).tolist()
        de = [['','',''],['','',''],['','','']]
        for i,l in enumerate(a):
            for ind,el in enumerate(l):
                for index,elem in enumerate(el):
                    for x,m in enumerate(elem):
                        if len(m) == 1:
                            de[i][ind] += m
        for i,l in enumerate(a):
            for ind,el in enumerate(l):
                for index,elem in enumerate(el):
                    for x,m in enumerate(elem):
                        if len(m) != 1:
                            a[i][ind][index][x] = ''.join(['' if s in de[i][ind] else s for s in m])
        return np.array(a).swapaxes(2,1).reshape(9,9).tolist()
    while sum([len(a)for line in solution for a in line]) != 81:
        solution = brute_force(solution)
    for i,l in enumerate(solution):
        for ind,el in enumerate(l):
            solution[i][ind] = int(el)
    return solution

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day24([[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]])
'''

print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=1000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=1000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=1000)) + " seconds")
