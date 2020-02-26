import timeit


ccquiel_setup = '''
from __main__ import ccquiel_day22
'''

def ccquiel_day22(n,k):
    i = 0
    items = [l for l in range(1,n+1)]
    while len(items) > 1:
        i = (i+k-1) % len(items)
        items.pop(i)
    return items[0]

TEST_CODE_ccquiel = '''
result = ccquiel_day22(14,2)
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day22
'''

def charlie_ang_day22(n,k):
    current = 0
    items = [i for i in range(1,n+1)] 
    while len(items) > 1:
        current = (current + k - 1) % len(items)
        items.pop(current)
    return items[0]

TEST_CODE_charlie_ang = '''
result = charlie_ang_day22(14,2)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day22
'''

def diana_henninger_day22(n,k):
    index = 0
    for i in range(1, n + 1):
        index = (index + k) % i
    return index + 1

TEST_CODE_diana_henninger = '''
result = diana_henninger_day22(14,2)
'''

Jens_setup = '''
from __main__ import Jens_day22
'''

def Jens_day22(n,k):
    people = [i for i in range(1, n+1)]
    position = 0
    while len(people) > 1:
        position = (k+position)%len(people)-1
        people.pop(position)
        if position < 0:
            position = len(people)
    return people[0]

TEST_CODE_Jens = '''
result = Jens_day22(14,2)
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day22
'''

def Jose_Catela_day22(n,k):
    soldiers = list(range(1, n+1))
    pos = k - 1
    size = len(soldiers)
    while size > 1:
        while pos >= size:
            pos -= size
        soldiers.pop(pos)
        pos -= 1
        pos += k
        size = len(soldiers)
    return soldiers[0]

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day22(14,2)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day22
'''

def Kurt_Hinderer_day22(n,k):
    list = [i+1 for i in range(n)]
    deadmen = []
    next_dead = 0
    while len(list) > 1:
        next_dead += k - 1
        if next_dead > len(list) - 1:
            next_dead %= len(list)
        deadmen.append(list.pop(next_dead))
    return list[0]

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day22(14,2)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day22
'''

def Oleksandra_Chmel_day22(n,k):
    if n==1: return n
    items = list(range(1,n+1))
    num = k - 1
    while len(items)!=1:        
        try:
            del items[num]
            num += k - 1
        except IndexError:
            num = num-len(items)
    return items[0]

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day22(14,2)
'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
