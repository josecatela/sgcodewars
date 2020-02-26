import timeit


ccquiel_setup = '''
from __main__ import ccquiel_day21
'''

def ccquiel_day21(items,k):
    result = list()
    len_items = len(items)
    i = 1
    for item in items:
        if i % k == 0:
            result.append(item)
        else:
            items.append(item)
        if len(result) == len_items:
            break
        i += 1
    return result

TEST_CODE_ccquiel = '''
result = ccquiel_day21([1,2,3,4,5,6,7],3)
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day21
'''

def charlie_ang_day21(items,k):
    current = 0
    result = [] 
    while len(items) > 0:
        current += k
        while current > len(items):
            current -= len(items)
        # print("popping {} of {}".format(current, items))
        result.append(items.pop(current-1))
        current -= 1
    return result

TEST_CODE_charlie_ang = '''
result = charlie_ang_day21([1,2,3,4,5,6,7],3)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day21
'''

def diana_henninger_day21(items,k):
    result = []
    if(len(items))==0: return result
    k -= 1
    index = k % len(items)
    while len(items)>1:
        result.append(items.pop(index))
        index = (index+k) % len(items)
    result.append(items.pop())
    return result

TEST_CODE_diana_henninger = '''
result = diana_henninger_day21([1,2,3,4,5,6,7],3)
'''

Jens_setup = '''
from __main__ import Jens_day21
'''

def Jens_day21(items,k):
    permutation = []
    position = 0
    while items:
        position = (k+position)%len(items)-1
        permutation.append(items.pop(position))
        if position < 0:
            position = len(items)
    return permutation

TEST_CODE_Jens = '''
result = Jens_day21([1,2,3,4,5,6,7],3)
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day21
'''

def Jose_Catela_day21(items,k):
    if not items:
        return []
    if len(items) == 1:
        return items
    josephus = []
    pos = k - 1
    while items:
        while pos >= len(items) and len(items) != 0:
            pos -= len(items)
        josephus.append(items.pop(pos))
        pos -= 1
        pos += k
    return josephus

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day21([1,2,3,4,5,6,7],3)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day21
'''

def Kurt_Hinderer_day21(items,k):
    deadmen = []
    next_dead = 0
    while len(items) > 0:
        next_dead += k - 1
        if len(items) - 1 == 0:
            next_dead = 0
        elif next_dead > len(items) - 1:
            next_dead %= len(items)
        deadmen.append(items.pop(next_dead))
    return deadmen

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day21([1,2,3,4,5,6,7],3)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day21
'''

def Oleksandra_Chmel_day21(items,k):
    if len(items)==0: return []
    n = k - 1
    seq = []
    while len(items)!=0:        
        try:
            seq.append(items[n])
            del items[n]
            n += k - 1
        except IndexError:
            n = n-len(items)
    return seq

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day21([1,2,3,4,5,6,7],3)
'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
