import timeit


ccquiel_setup = '''
from __main__ import ccquiel_day25
'''

def ccquiel_day25(string):
    seen = set()
    lstring = string.lower()
    for i, s in enumerate(lstring):
        if s not in lstring[i+1:] and s not in seen:
            return string[i]
        else:
            seen.add(s)
    return ''

TEST_CODE_ccquiel = '''
result = ccquiel_day25('Go hang a salami, Im a lasagna hog!')
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day25
'''

def charlie_ang_day25(string):
    string_lower = string.lower()
    eliminated = set()
    for i,c in enumerate(string_lower):
        if c not in string_lower[i+1:] and c not in eliminated:
            return string[i]
        eliminated.add(c)
    return ""

TEST_CODE_charlie_ang = '''
result = charlie_ang_day25('Go hang a salami, Im a lasagna hog!')
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day25
'''

def diana_henninger_day25(string):
    rep = []
    letter = ''
    for s in string:
        if s.upper() not in rep and s.lower() not in rep: letter += s
        else: 
            letter = letter.replace(s.upper(),'')
            letter = letter.replace(s.lower(),'')
        rep.append(s)
    if letter=='': return letter
    return letter[0]

TEST_CODE_diana_henninger = '''
result = diana_henninger_day25('Go hang a salami, Im a lasagna hog!')
'''

ggebre_setup = '''
from __main__ import ggebre_day25
'''

def ggebre_day25(new_string):
    arr = []
    string = new_string.lower()
    string2 = new_string
    for index, x in enumerate(string):
        if x not in arr : 
            if string.count(x) == 1:
                return string2[index]
            else:
                arr.append(x)
    if len(arr) == len(set(string)):
          return ""

TEST_CODE_ggebre = '''
result = ggebre_day25('Go hang a salami, Im a lasagna hog!')
'''

Jens_setup = '''
from __main__ import Jens_day25
'''

def Jens_day25(string):
    for letter in string:
        if string.lower().count(letter.lower()) == 1:
            return letter
    return ''

TEST_CODE_Jens = '''
result = Jens_day25('Go hang a salami, Im a lasagna hog!')
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day25
'''

def Jose_Catela_day25(string):
    letters = []
    repeated = []
    for letter in string:
        if letter in letters or letter.lower() in letters:
            repeated.append(letter.lower())
        letters.append(letter)
        letters.append(letter.lower())
    for letter in letters:
        if letter.lower() not in repeated:
            return letter
    return ''

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day25('Go hang a salami, Im a lasagna hog!')
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day25
'''

def Kurt_Hinderer_day25(string):
    non_repeat = ''
    i = 0
    lower_string = string.lower()
    searched_list = []
    while i < len(lower_string) and non_repeat == '':
        if lower_string[i] not in searched_list:
            if lower_string.find(lower_string[i],i+1) == -1:
                non_repeat = lower_string[i]
            else:
                searched_list.append(lower_string[i])
        i += 1
    if non_repeat != '' and len(string) > 0:
        non_repeat = string[i-1]
    return non_repeat

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day25('Go hang a salami, Im a lasagna hog!')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day25
'''

def Oleksandra_Chmel_day25(string):
    for i,e in enumerate(string):
        if string.lower().count(e.lower()) ==1:
            return string[i]
    return ''

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day25('Go hang a salami, Im a lasagna hog!')
'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
