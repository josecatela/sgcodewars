import timeit
from itertools import product, groupby, combinations


ccquiel_setup = '''
from __main__ import ccquiel_day40
'''

def get_string(s, indices):
    way = ''
    for i, c in enumerate(s):
        way += c if i in indices else '-'
    return way

def ccquiel_day40(s):
    ways = set()
    bb, nn, aa = [], [], []
    for index, c in enumerate(s):
        if c == 'b': bb.append(index)
        elif c == 'n': nn.append(index)
        elif c == 'a': aa.append(index)
    for b in bb:
        for bn in combinations(nn, 2):
            indices = [b] + list(bn)
            a1, a2, a3 = [], [], []
            for a in aa:
                if indices[0] < a < indices[1]:
                   a1.append(a)
                if indices[1] < a < indices[2]:
                   a2.append(a)
                if indices[2] < a:
                   a3.append(a)
            for x in product(a1, a2, a3):
                way_indices = list(indices) + list(x)
                ways.add(get_string(s, way_indices))
    return ways

TEST_CODE_ccquiel = '''
result = ccquiel_day40('bbananana')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day40
'''

def Oleksandra_Chmel_day40(s):
    b = 'banana'
    ans = set()
    if s == b: ans.add(b); return ans
    if len(''.join(c[0] for c in groupby(s))) < 6: return ans
    s_check = ''
    count = 0
    for letter in s:
        if letter == b[count]:
            s_check += letter
            count += 1
            if s_check == b: break
    if s_check != b: return ans
    def interp(original_word, word, letter, size):
        empty = [letter]*size
        for comb in combinations(range(size), len(word)):
            newstring = list(empty)
            temp = ''
            for ind,letter in zip(comb,word):
                newstring[ind] = letter
                temp += original_word[ind]
            if word == temp:
                yield (''.join(newstring)) 
    ans.update([i for i in interp(s, b, '-', len(s))])
    return ans

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day40('bbananana')
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day40
'''

def Tushar_Jain_day40(s):
    GOLDEN = 'banana'
    contents = ['']
    if len(s) < len(GOLDEN):
        return None
    for letter in s[-1::-1]:
        tempcontents = ['-' + item for item in contents if GOLDEN.endswith(('-' + item).replace('-', ''))]
        if letter in ['b', 'a', 'n']:
            tempcontents += [letter + item for item in contents if GOLDEN.endswith((letter + item).replace('-', ''))]
        contents = tempcontents
    return set((content for content in contents if content.replace('-', '') == GOLDEN))

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day40('bbananana')
'''

Yang_setup = '''
from __main__ import Yang_day40
'''

def Yang_day40(s):
    d = {'b':[],'a':[],'n':[]}
    for i,x in enumerate(s):         
        d[x].append(i)
    ll = [d['b'],d['a'],d['n'],d['a'],d['n'],d['a']]
    banana = ['b','a','n','a','n','a']
    pos = list(product(*ll)) 
    k = set() 
    size = ['-']*len(s)
    for each in pos: 
        if sorted(each) == list(each): 
            for i,x in enumerate(each): 
                size[x] = banana[i] 
            k.add(''.join(size))
            size = ['-']*len(s)
    return k

TEST_CODE_Yang = '''
result = Yang_day40('bbananana')
'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=10000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=10000)) + " seconds")
