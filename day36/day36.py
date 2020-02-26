import timeit


akash_karan_setup = '''
from __main__ import akash_karan_day36
'''

def akash_karan_day36(maze, directions):
    for i,x in enumerate(maze):
        for j,y in enumerate(x):
            if y==2:
                xco=j
                yco=i
                break
    for d in directions:
        if d=="N":
            yco-=1
        if d=="E":
            xco+=1
        if d=="W":
            xco-=1
        if d=="S":
            yco+=1
        try:
            if(xco<0 or yco<0):
                return "Dead"
            if(maze[yco][xco]==1):
                return "Dead"
            if(maze[yco][xco]==3):
                return "Finish"
        except:
            return "Dead"
    return "Lost"

TEST_CODE_akash_karan = '''
result = akash_karan_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

ccquiel_setup = '''
from __main__ import ccquiel_day36
'''

def ccquiel_day36(maze, directions):
    N = len(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                break
    curr = start
    for d in directions:
        if d == 'N':
            curr = (curr[0] - 1, curr[1])
        elif d == 'S':
            curr = (curr[0] + 1, curr[1])
        elif d == 'E':
            curr = (curr[0], curr[1] + 1)
        elif d == 'W':
            curr = (curr[0], curr[1] - 1)
        if not (0 <= curr[0] < N) or not (0 <= curr[1] < N):
            return 'Dead'
        val = maze[curr[0]][curr[1]]
        if val == 1:
            return 'Dead'
        if val == 3:
            return 'Finish'
    else:
        return 'Lost'

TEST_CODE_ccquiel = '''
result = ccquiel_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day36
'''

def diana_henninger_day36(maze, directions):
    pos_y = -1
    pos_x = None
    for line in maze: # find start point
        pos_y +=1
        if 2 in line: 
            pos_x = line.index(2)
            break
    for d in directions:
        if d == "N": pos_y -= 1  
        elif d == "S": pos_y += 1
        elif d == "E": pos_x += 1
        elif d == "W": pos_x -= 1
        if pos_y < 0 or pos_y >= len(maze): return "Dead" # outside border
        if pos_x < 0 or pos_x >= len(maze[0]): return "Dead" #outside border
        if maze[pos_y][pos_x] == 1: return "Dead" # hit wall
        elif maze[pos_y][pos_x] == 3: return "Finish"
    return "Lost"

TEST_CODE_diana_henninger = '''
result = diana_henninger_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

Jens_setup = '''
from __main__ import Jens_day36
'''

def Jens_day36(maze, directions):
    for row in range(len(maze)):
        for element in range(len(maze[row])):
            if maze[row][element] == 2:
                position = [row, element]
                break
    for direction in directions:
        if direction == 'N':
            position[0] -= 1
        elif direction == 'S':
            position[0] += 1
        elif direction == 'W':
            position[1] -= 1
        elif direction == 'E':
            position[1] += 1
        if position[0] < 0 or position[0] >= len(maze) or \
           position[1] < 0 or position[1] >= len(maze):
            return 'Dead'
        if maze[position[0]][position[1]] == 1:
            return 'Dead'
        if maze[position[0]][position[1]] == 3:
            return 'Finish'
    return 'Lost'       

TEST_CODE_Jens = '''
result = Jens_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day36
'''

def Kurt_Hinderer_day36(maze, directions):
    dir_dict = {'N': (-1,0), 'S':(1,0), 'E':(0,1), 'W':(0,-1)}
    #find start
    start_found = False
    i = 0
    while not start_found and i < len(maze):
        if 2 in maze[i]:
            new_loc = (i, maze[i].index(2))
            start_found = True
        i += 1
    if not start_found:
        return "Never entered"
    #run the maze
    for move in directions:
        vect = dir_dict[move]
        new_loc = (new_loc[0]+vect[0], new_loc[1]+vect[1])
        if new_loc[0]<0 or new_loc[0]>=len(maze) or new_loc[1] <0 or new_loc[1] >=len(maze[0]):
            #off board
            return "Dead"
        if maze[new_loc[0]][new_loc[1]] == 1:
            return "Dead"
        elif maze[new_loc[0]][new_loc[1]] == 3:
            return "Finish"
    return "Lost"

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

Navneet_Kumar_setup = '''
from __main__ import Navneet_Kumar_day36
'''

def update_current_point(current, dir):
    return list(map(lambda x,y:x+y ,current,dir))

def Navneet_Kumar_day36(maze, directions):
    # Code Here
    start_point = 0
    end_point = 0
    for i,arr in enumerate(maze):
        for j,x in enumerate(arr):
            if x==2:
                start_point = [i,j]
            if x==3:
                end_point = [i,j]
    direction = {
    'N':[-1,0], 'S': [1, 0], 'E':[0,1], 'W': [0,-1]}
    current = start_point
    for d in directions:
        current = update_current_point(current, direction[d])
        if (current[0]<0 or current[1]<0 or current[0]>=len(maze) or current[1]>=len(maze[1])):
            return "Dead"
        if maze[current[0]][current[1]]==1 :
            return "Dead"
        if maze[current[0]][current[1]]==3:
            return "Finish"
    return "Lost"

TEST_CODE_Navneet_Kumar = '''
result = Navneet_Kumar_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day36
'''

def Oleksandra_Chmel_day36(maze, directions):
    dd  = [[-1,0] if d == 'N' else ([1,0] if d == 'S' else ([0,1] if d == 'E' else [0,-1])) 
            for d in directions]
    def find(m):
        for i,e in enumerate(maze):
            try:
                j = e.index(m)
            except ValueError:
                continue
            yield [i, j]
    start = list(find(2))
    # finish = list(find(3))
    last = [None,None]
    last[0], last[1] = start[0][0], start[0][1]
    for step in dd:
        if maze[last[0]][last[1]] == 0 or maze[last[0]][last[1]] == 2:
            last[0] += step[0]
            last[1] += step[1]
        if last[0]<0 or last[1]<0 or last[0]>len(maze)-1 or last[1]>len(maze)-1: return 'Dead'
        if maze[last[0]][last[1]] == 1: return 'Dead'
        if maze[last[0]][last[1]] == 3: return 'Finish'
    return 'Lost'

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day36
'''

def get_status(maze, N, current, finish):
    if current[0] < 0 or current[0] >= N or current[1] < 0 or current[1] >= N or maze[current[1]][current[0]] == 1:
        return 'Dead'
    if current == finish:
        return 'Finish'
    return None

def Tushar_Jain_day36(maze, directions):
    N = len(maze)
    start = None
    finish = None
    for y in range(N):
        for x in range(N):
            if(maze[y][x] == 2):
                start = [x, y]
            if(maze[y][x] == 3):
                finish = [x, y]
    if not start:
        return 'Dead'
    current = list(start)
    for walk in directions:
        if get_status(maze, N, current, finish):
            return get_status(maze, N, current, finish)
        if walk == 'N':
            current[1] -= 1
        elif walk == 'E':
            current[0] += 1
        elif walk == 'W':
            current[0] -= 1
        elif walk == 'S':
            current[1] += 1
        else:
            return 'Dead'
    if get_status(maze, N, current, finish):
        return get_status(maze, N, current, finish)
    return 'Lost'

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

Yang_setup = '''
from __main__ import Yang_day36
'''

def Yang_day36(maze, directions):
    begin,end=[],[]
    for y,row in enumerate(maze): 
        for x,ele in enumerate(row): 
            if ele==2: 
                begin = [x,y] 
            elif ele==3: 
                end = [x,y]
    for x in directions: 
        if x=="N": 
            begin[1]-=1 
        elif x=="S": 
            begin[1]+=1 
        elif x=="W": 
            begin[0]-=1 
        elif x=="E": 
            begin[0]+=1 
        if begin == end: 
            return "Finish" 
        if begin[1]+1>len(maze) or begin[0]+1>len(maze[0]) or begin[0]<0 or begin[1]<0: 
            return "Dead"
        elif maze[begin[1]][begin[0]] == 1: 
            return "Dead"
    return "Lost"

TEST_CODE_Yang = '''
result = Yang_day36([[1,1,1,1,1,1,1],[1,0,0,0,0,0,3],[1,0,1,0,1,0,1],[0,0,1,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,0,0,0,1],[1,2,1,0,1,0,1]],["N","N","N","N","N","E","E","E","E","E"])
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Navneet_Kumar test code: " + str(timeit.timeit(stmt=TEST_CODE_Navneet_Kumar, setup=Navneet_Kumar_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
