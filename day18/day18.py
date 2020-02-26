import timeit
from functools import reduce


charlie_ang_setup = '''
from __main__ import charlie_ang_day18
'''

points = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
convert = { \
    'wt': 'w', 'pt': 'p', 'bt': 'b', 'st':'s', \
    'wj': 'm', 'pj': 'q', 'bj': 'd', 'sj': 'z',  \
    'mt': 'w', 'qt': 'p', 'dt': 'b', 'zt':'s', \
    'mj': 'm', 'qj': 'q', 'dj': 'd', 'zj': 'z' }

def charlie_ang_day18(fight):
    # print("Working with {}".format(fight))
    max_index = len(fight) - 1
    result = []
    for i,c in enumerate(fight):
        if points.get(c):
            priests = set()
            if i > 0 and fight[i - 1] in 'jt': 
                priests.add(fight[i - 1])
            if i < max_index and fight[i + 1] in 'jt':
                priests.add(fight[i + 1])
            if len(priests) == 1:
                result.append(convert.get(c + priests.pop()))
            else:
                result.append(c)
    total_points = reduce(lambda x, y: x + points[y] if points.get(y) else x, result, 0)                
    if total_points > 0:
        return "Left side wins!"
    elif total_points < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"

TEST_CODE_charlie_ang = '''
result = charlie_ang_day18('wololooooo')
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day18
'''

def Jose_Catela_day18(fight):
    left = {'w': -4, 'p': -3, 'b': -2, 's': -1}
    left_priest = 't'
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    right_priest = 'j'
    #print(fight)
    result = 0
    fight_lim = len(fight) - 1
    for index, letter in enumerate(fight):
        prev = 0
        if letter in left:
            prev = left[letter]
            if index != 0:
                if fight[index-1] == right_priest:
                    prev = left[letter] * -1
            if index != fight_lim:
                if fight[index+1] == right_priest:
                    prev = left[letter] * -1
            if index != 0:
                if fight[index-1] == left_priest:
                    prev = left[letter]
            if index != fight_lim:
                if fight[index+1] == left_priest:
                    prev = left[letter]
        if letter in right:
            prev = right[letter]
            if index != 0:
                if fight[index-1] == left_priest:
                    prev = right[letter] * -1
            if index != fight_lim:
                if fight[index+1] == left_priest:
                    prev = right[letter] * -1
            if index != 0:
                if fight[index-1] == right_priest:
                    prev = right[letter]
            if index != fight_lim:
                if fight[index+1] == right_priest:
                    prev = right[letter]
        result += prev    
    if result < 0:
        return "Left side wins!"
    elif result > 0:
        return "Right side wins!"
    return  "Let's fight again!"

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day18('wololooooo')
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day18
'''

def Kurt_Hinderer_day18(fight):
    #a dictionary to determine the side and then the ranking of the left and right
    #using number line thinking so left is negative and right is positive
    sides_dic = {'a': 0, 'b': -1, 'c': 0, 'd': 1, 'e': 0, 'f': 0, 'g': 0,
                    'h': 0, 'i': 0, 'j': 1, 'k': 0, 'l': 0, 'm': 1, 'n': 0,
                    'o': 0, 'p': -1, 'q': 1, 'r': 0, 's': -1, 't': -1, 'u': 0,
                    'v': 0, 'w': -1, 'x': 0, 'y': 0, 'z': 1}
    sides_lists = [['t', 's', 'b', 'p', 'w'],
                    ['a', 'c', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'n', 'o', 'r', 'u', 'v', 'x', 'y'],
                    ['j', 'z', 'd', 'q', 'm']]
    #conversion time
    for i in range(0, 3, 2):
        other_side = abs(2-i)
        j = 0
        while j < len(fight):
            priest = fight.find(sides_lists[i][0], j) 
            if priest != -1:
                near1 = [priest - 1, priest + 1]
                for k in near1:
                    if k >=0 and k < len(fight) and fight[k] in sides_lists[other_side]:
                        protected = False
                        near2 = [k-1,k+1]
                        if fight[k] == sides_lists[other_side][0]:
                            protected = True
                        for l in near2:
                            if l >=0 and l<len(fight) and fight[l] == sides_lists[other_side][0]:
                                protected = True
                        if not protected:
                            fight = fight[:k] + sides_lists[i][sides_lists[other_side].index(fight[k])] + fight[k+1:]
                j = priest + 1
            else:
                j = len(fight)
    # determine the winner
    total = 0
    for i in range(len(fight)):
        c = fight[i]
        total += sides_dic[c] * sides_lists[sides_dic[c]+1].index(c)
    if total > 0:
        victory = "Right side wins!"
    elif total < 0:
        victory = "Left side wins!"
    else:
        victory = "Let's fight again!"
    return  victory

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day18('wololooooo')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day18
'''

def Oleksandra_Chmel_day18(fight):
    rd, ld = {'m': 4, 'q': 3, 'd': 2, 'z': 1, 'j': 0}, {'w': 4, 'p': 3, 'b': 2, 's': 1, 't': 0}
    rd_keys, ld_keys = list(rd.keys()), (ld.keys())
    rd_repl = {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z', 't': 'j'}
    ld_repl = {'m': 'w', 'q': 'p', 'd': 'b', 'z': 's', 'j': 't'}
    temp = ''
    try:
        for i,el in enumerate(fight):
            if i == len(fight)-1 and fight[i-1] == 't' and el in rd_keys:
                temp += ld_repl[el]
            elif i == len(fight)-1 and fight[i-1] == 'j' and el in ld_keys:
                temp += rd_repl[el]
            elif i == len(fight)-1:
                temp += el
            elif (fight[i+1] == 't' and fight[i-1] == 'j') or (fight[i+1] == 'j' and fight[i-1] == 't'):
                temp += el
            elif (fight[i+1] == 't' or fight[i-1] == 't') and el in rd_keys:
                temp += ld_repl[el]
            elif (fight[i+1] == 'j' or fight[i-1] == 'j') and el in ld_keys:
                temp += rd_repl[el]
            else:
                temp += el
    except IndexError:
        pass
    right = 0
    left = 0
    right = sum([rd[x] if x in rd_keys else 0 for x in temp])
    left = sum([ld[x] if x in ld_keys else 0 for x in temp])
    if right > left:
        return 'Right side wins!'
    elif left > right:
        return 'Left side wins!'
    else:
        return  'Let\'s fight again!'

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day18('wololooooo')
'''

print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=10000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
