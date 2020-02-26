import timeit


akash_karan_setup = '''
from __main__ import akash_karan_day47
'''

def akash_karan_day47(fighters, initial_position, moves):
    mv={"up":-1,"down":1,"right":1,"left":-1}
    x,y=initial_position[0],initial_position[1]
    ms=[]
    for m in moves:
        if(m=="right"or m=="left"):
            x+=mv[m]
            ms.append(fighters[y][x%6])
        elif(m=="up" and y!=0):
            y+=mv[m]
            ms.append(fighters[y%2][x%6])
        elif(m=="down" and y!=1):
            y+=mv[m]
            ms.append(fighters[y%2][x%6])
        else:
            ms.append(fighters[y%2][x%6])
    return ms

TEST_CODE_akash_karan = '''
result = akash_karan_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

ccquiel_setup = '''
from __main__ import ccquiel_day47
'''

values = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}

def ccquiel_day47(fighters, initial_position, moves):   
    sel = list()
    cur = initial_position
    for mov in moves:
        mov = values[mov]
        limit_up = cur[0] == 0 and mov[0] == -1
        limit_down = cur[0] == 1 and mov[0] == 1
        if not (limit_up or limit_down):
            cur = (cur[0] + mov[0], cur[1] + mov[1])
        sel.append(fighters[cur[0]][cur[1] % 6])               
    return sel

TEST_CODE_ccquiel = '''
result = ccquiel_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day47
'''

def diana_henninger_day47(fighters, initial_position, moves):
    posx, posy = initial_position
    solution = []
    for m in moves:
        if m == 'up': posy = max(0,posy-1)
        elif m == 'down': posy = min(1, posy+1)
        elif m == 'left': posx = (posx-1)%6
        else: posx = (posx+1)%6
        solution.append(fighters[posy][posx])
    return solution

TEST_CODE_diana_henninger = '''
result = diana_henninger_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

Jens_setup = '''
from __main__ import Jens_day47
'''

def Jens_day47(fighters, position, moves):
    sel, pos = [], list(position)
    for m in moves:
        if m == 'up':
            pos[0] = 0
        elif m == 'down':
            pos[0] = 1
        elif m == 'right':
            pos[1] = (pos[1] + 1) % 6
        elif m == 'left':
            pos[1] = (pos[1] -1) % 6
        sel.append(fighters[pos[0]][pos[1]])
    return sel

TEST_CODE_Jens = '''
result = Jens_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

Matthias_setup = '''
from __main__ import Matthias_day47
'''

def Matthias_day47(fighters, initial_position, moves):
    x = initial_position[1]
    y = initial_position[0]
    result = []
    for i in range(len(moves)):
        if moves[i] == "up":
            if y == 1:
                y = 0
        if moves[i] == "down":
            if y == 0:
                y = 1
        if moves[i] == "right":
            x += 1
            if x == 6:
                x = 0
        if moves[i] == "left":
            x -= 1
            if x == -1:
                x = 5
        result.append(fighters[y][x])
    return result

TEST_CODE_Matthias = '''
result = Matthias_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day47
'''

def Oleksandra_Chmel_day47(fighters, initial_position, moves):
    if moves == []: return []
    ip0, ip1 = list(initial_position)
    x, y = len(fighters), len(fighters[0])
    ans = []
    mm = [[-1,0] if m == 'up' else ([1,0] if m == 'down' else ([0,1] if m == 'right'
            else [0,-1])) for m in moves]
    for m in mm:
        ip0 += m[0]
        ip1 += m[1]
        if ip0 < 0: ip0 = 0
        elif ip0 >= x: ip0 = x - 1
        if ip1 < 0: ip1 = y - 1
        elif ip1 >= y: ip1 = 0
        ans.append(fighters[ip0][ip1])
    return ans

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

Omar_B_setup = '''
from __main__ import Omar_B_day47
'''

def Omar_B_day47(fighters, initial_position, moves):
    l=[]
    x= initial_position[0]
    y= initial_position[1]
    for elt in moves : 
        if elt == 'up':
            if y >0 :
                y-=1
        elif elt == 'down':
            if y < len(fighters)-1 :
                y+=1
        elif elt == 'right':
            x= (x+1)%len(fighters[0])
        elif elt == 'left':
            if x == 0: 
                x = len(fighters[0])-1
            else: 
                x-=1
        l.append(fighters[y][x])
    return l

TEST_CODE_Omar_B = '''
result = Omar_B_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day47
'''

def Tushar_Jain_day47(fighters, initial_position, moves):
    result = []
    ptr = list(initial_position)
    for move in moves:
        if move == 'up':
            ptr[0] = 0
        elif move == 'down':
            ptr[0] = 1
        elif move == 'left':
            ptr[1] -= 1
        elif move == 'right':
            ptr[1] += 1
        ptr[0] = 0 if ptr[0] <= 0 else 1
        ptr[1] %= 6
        result.append(fighters[ptr[0]][ptr[1]])
    return result

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day47
'''

def Vanessa_G_day47(fighters, initial_position, moves):
    result = []
    l = len(fighters[0])
    x, y = initial_position
    for move in moves:
        if move == 'up': x = 0
        elif move == 'down': x = 1
        elif move == 'left': y = y - 1 if y - 1 >= 0 else l - 1
        else: y = y + 1 if y + 1 < l else 0
        result.append(fighters[x][y])
    return result

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day47([[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]],(1,0),["right"]*8)
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Matthias test code: " + str(timeit.timeit(stmt=TEST_CODE_Matthias, setup=Matthias_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Omar_B test code: " + str(timeit.timeit(stmt=TEST_CODE_Omar_B, setup=Omar_B_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
