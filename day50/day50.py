import timeit
import functools


Belachkar_Ali_setup = '''
from __main__ import Belachkar_Ali_day50
'''

def Belachkar_Ali_day50(intervals):
    intervals.sort(key=lambda x: x[0])
    p = [intervals[0]]
    for i, d in enumerate(intervals):
        last_t = p[len(p)-1]
        if d[1] <= last_t[1]:
            continue
        if d[0] <= last_t[1] and d[1] > last_t[1]:
            p[len(p)-1] = (p[len(p)-1][0], d[1])
        else:
            p.append(d)
    return sum((r[1] - r[0]) for r in p)

TEST_CODE_Belachkar_Ali = '''
result = Belachkar_Ali_day50([(1, 4), (7, 10), (3, 5)])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day50
'''

def diana_henninger_day50(intervals):
    all = []
    sum = 0
    for i in intervals:
        sum += i[1]-i[0]
        for x in range(i[0],i[1]):
            if x in all: sum-= 1
            else: all.append(x)
    return sum

TEST_CODE_diana_henninger = '''
result = diana_henninger_day50([(1, 4), (7, 10), (3, 5)])
'''

Jens_setup = '''
from __main__ import Jens_day50
'''

def Jens_day50(intervals):
    intervals.sort()
    result = 0
    for i in range(len(intervals)-1):
        while len(intervals) > i+1 and intervals[i][1] >= intervals[i+1][0]:
            if intervals[i+1][1] < intervals[i][1]:
                intervals[i] = (intervals[i][0], intervals[i][1])
            else:
                intervals[i] = (intervals[i][0], intervals[i+1][1])
            intervals.pop(i+1)
    for interval in intervals:
        result += interval[1] - interval[0]
    return result

TEST_CODE_Jens = '''
result = Jens_day50([(1, 4), (7, 10), (3, 5)])
'''

kheireddine_Douli_setup = '''
from __main__ import kheireddine_Douli_day50
'''

def kheireddine_Douli_day50(intervals):
    numbers = []
    for interval in intervals:
        for i in range(interval[0],interval[1]):
            numbers.append(i)
    return len(set(numbers))

TEST_CODE_kheireddine_Douli = '''
result = kheireddine_Douli_day50([(1, 4), (7, 10), (3, 5)])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day50
'''

def Oleksandra_Chmel_day50(intervals):
    if len(intervals) == 1: return intervals[0][1] - intervals[0][0]
    intervals.sort()
    l = [intervals[0]]
    for i in range(1,len(intervals)):
        if l[len(l)-1][1] > intervals[i][0]:
            if intervals[i][1] > l[len(l)-1][1]:
                l[len(l)-1] = (l[len(l)-1][0],intervals[i][1])
        else:
            l.append(intervals[i])
    res = sum([i[1] - i[0] for i in l])
    return res

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day50([(1, 4), (7, 10), (3, 5)])
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day50
'''

def Tushar_Jain_day50(intervals):
    return len(functools.reduce(lambda x, y: x | y,
                                map(lambda x:
                                    set((val for val in range(x[0], x[1]))),
                                    intervals),
                                set()))

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day50([(1, 4), (7, 10), (3, 5)])
'''

Yang_setup = '''
from __main__ import Yang_day50
'''

def soi(intervals):
    ll = [list(intervals[0])] 
    for (begin,end) in intervals[1:]: 
        b = False 
        for i,(x,y) in enumerate(ll): 
            if begin<x and y<end:
                ll[i] = [begin,end]
                b = True
                break
            elif begin<=y and y<end:
                ll[i][1] = end
                b = True
                break
            elif begin<x and x<=end: 
                ll[i][0] = begin 
                b = True
                break 
            elif x<=begin and end<=y:
                b = True
                break
        if not b: ll.append([begin,end]) 
    return ll 

def Yang_day50(ll): 
    k = soi(soi(ll)) 
    return sum(y-x for (x,y) in k)

TEST_CODE_Yang = '''
result = Yang_day50([(1, 4), (7, 10), (3, 5)])
'''

print("Time for Belachkar_Ali test code: " + str(timeit.timeit(stmt=TEST_CODE_Belachkar_Ali, setup=Belachkar_Ali_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for kheireddine_Douli test code: " + str(timeit.timeit(stmt=TEST_CODE_kheireddine_Douli, setup=kheireddine_Douli_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
