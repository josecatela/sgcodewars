import timeit
import re


charlie_ang_setup = '''
from __main__ import charlie_ang_day17
'''

def charlie_ang_day17(battlefield):
    # print("Working on " + battlefield)
    if '#' not in battlefield:
        return battlefield.replace("[","").replace("]","")
    safe = []
    for inside_nuclear in re.findall(r'(?<=\[)\w+(?=\])', battlefield):
        count = 0
        i = battlefield.index("[" + inside_nuclear + "]") - 1
        while i >= 0 and battlefield[i] != ']':
            if battlefield[i] == '#': count += 1
            i -= 1
        # print("count on left side is " + str(count))            
        i = battlefield.index("[" + inside_nuclear + "]") + len(inside_nuclear) + 2
        while i < len(battlefield) and battlefield[i] != '[':
            if battlefield[i] == '#': count += 1
            i += 1
        if count < 2:
            safe.append(inside_nuclear)
    return "".join(safe) 

TEST_CODE_charlie_ang = '''
result = charlie_ang_day17('ab#de[fgh]ij#k')
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day17
'''

def Jose_Catela_day17(battlefield):
    if '#' not in battlefield:
        return battlefield.replace('[', '').replace(']','')
    begin1 = 0
    begin2 = 0
    batsize = len(battlefield)
    batlim = batsize - 1
    ab = list(battlefield)
    shelters = []
    for index, letter in enumerate(ab):
        if letter == ']':
            if begin1 < begin2:
                begin1 = index+1
            else:
                begin2 = index+1
        if letter == '[' and (begin1 != 0 or begin2 != 0):
            if begin1 <= begin2:
                shelter = ab[begin1:index]
            else:
                shelter = ab[begin2:index]
            shelters.append(''.join(shelter))
    if begin1 < begin2:
        shelter = ab[begin1:]
    else:
        shelter = ab[begin2:]
    shelters.append(''.join(shelter))
    result = ''
    for shelter in shelters:
        if shelter.count('#') < 2:
            result += shelter[shelter.index('[')+1:shelter.index(']')]
    return result

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day17('ab#de[fgh]ij#k')
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day17
'''

def Kurt_Hinderer_day17(battlefield):
    #if no nukes hit, just print the letters
    if battlefield.find('#') == -1:
        battlefield = battlefield.replace("[","")
        battlefield = battlefield.replace("]","")
    else:
        #start a list of all of the shelters
        #shelters will be tuples (left, protected letters, right)
        shelters = []
        i = 0
        while i < len(battlefield):
            left = battlefield.find("[",i)
            right = battlefield.find("]",i)
            if left != -1 and right != -1 and left < right:
                shelters.append((left, battlefield[left+1:right], right))
            if right == -1:
                i = len(battlefield)
            else:
                i = right + 1
        #find the nukes
        nukes = []
        if len(shelters) > 0:
            nukes.append(battlefield.count("#",0,shelters[0][0]))
        for i in range(len(shelters)-1):
            nukes.append(battlefield.count("#",shelters[i][2],shelters[i+1][0]))
        if len(shelters) > 0:
            nukes.append(battlefield.count("#",shelters[-1][2]))
        #see if the shelters survives
        for i in range(len(shelters)-1,-1,-1):
            if nukes[i] + nukes[i+1] > 1:
                shelters.remove(shelters[i])
        #the survivers come out of the shelters left standing
        battlefield = ""
        for shelter in shelters:
            battlefield += shelter[1]
    return battlefield

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day17('ab#de[fgh]ij#k')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day17
'''

def Oleksandra_Chmel_day17(battlefield):
    if '#' not in battlefield:
        return ''.join(battlefield.replace('[','').replace(']',''))
    else:
        clean = battlefield.split('[')
        l = []
        for x in range(battlefield.count('[')):
            l.append([])        
        for i,e in enumerate(clean):
            try:
                if len(clean[i]) == 0:
                    l[i].append('')
                elif i == 0:
                    l[i].append(clean[i].split(']')[0])
                else:
                    l[i].append(clean[i].split(']')[1])
                l[i].append(clean[i+1].split(']')[0])
                l[i].append(clean[i+1].split(']')[1])
            except IndexError:
                continue        
        s = ''
        num = 0
        try:
            for el in l:
                for elem in el:
                    count = elem.count('#')
                    if count > 0:
                        num += count
                if num <2:
                   s += el[1]
                num = 0
        except IndexError:
            pass
        return s

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day17('ab#de[fgh]ij#k')
'''

print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=10000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
