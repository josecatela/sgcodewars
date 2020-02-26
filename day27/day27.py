import timeit


ccquiel_setup = '''
from __main__ import ccquiel_day27
'''

def get_seq(string, slen):
    for i in range(1, slen+1):
        sub = string[:i]
        times = slen // i
        if sub*times == string:
            return sub
    else:
        return False

def ccquiel_day27(chars):
    if not chars: return chars
    seq = chars[0]
    chars_len = len(chars)
    i = 2
    lcount = 0
    while True:
        if i % 2:
            middle = chars[(lcount + (i // 2)) % chars_len]
            seq += middle
        else:
            lcount += 2*i - 1
        i += 1
        lseq = len(seq)
        if lseq >= chars_len:
            subseq = get_seq(seq, lseq)
            if subseq:
                return subseq

TEST_CODE_ccquiel = '''
result = ccquiel_day27("vttussvutvuvvtustsvsvtvu")
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day27
'''

def get_middle(chars, rownum):
    # middle column is defined as (rownum + 1) // 2, where rownum is odd, and column is 1-indexed
    result = chars[(((rownum+1)//2 - 1) + sum(range(rownum))) % len(chars)]
    # print("row {} - {} - {}".format(rownum, [ " ".join(chars[(column + sum(range(rownum))) % len(chars)] for column in range(rownum)) ], result))
    return result

def charlie_ang_day27(chars):
    result = "".join(get_middle(chars, rownum) for rownum in range(1, len(chars)*4, 2))
    for i in range(1, len(result)):
        working = result[:i]
        if len(result.replace(working, "")) == 0:
            result = working
            break
    return result

TEST_CODE_charlie_ang = '''
result = charlie_ang_day27("vttussvutvuvvtustsvsvtvu")
'''

Daniel_Ruiz_setup = '''
from __main__ import Daniel_Ruiz_day27
'''

def Daniel_Ruiz_day27(chars):
    if chars == '':
        return ''
    chars = chars * 10000
    def n_int(n):
        return n*(n+1) // 2
    center = ''
    c = 0
    i= 0
    while n_int(i) <= len(chars):
        if i%2 != 0:
            c += 1
            pos_center = (n_int(i) - c) 
            center += chars[pos_center]
        i += 1
    for x in range(1, len(center)):
        subcenter = center[:x]
        if subcenter * (len(center)//len(subcenter))+(subcenter[:len(center)%len(subcenter)]) == center:
            return(subcenter)

TEST_CODE_Daniel_Ruiz = '''
result = Daniel_Ruiz_day27("vttussvutvuvvtustsvsvtvu")
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day27
'''

def diana_henninger_day27(chars):
    l = len(chars)
    if l==0 : return ''
    elif l==1: return chars
    else:
        solution = ""
        index = 0
        count = 1
        found = 0
        res = ""
        while found < 5:
            solution += chars[(index*count)%len(chars)]
            index += 2
            count += 1
            temp = (solution + solution).find(solution, 1, -1) 
            if temp != -1: 
                res = solution[:temp] 
                found+=1
        return res

TEST_CODE_diana_henninger = '''
result = diana_henninger_day27("vttussvutvuvvtustsvsvtvu")
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day27
'''

def Jose_Catela_day27(chars):
    size = len(chars)
    if size == 0:
        return ""
    size = len(chars)
    center_calc = size * 4
    center = ''
    index_large = 0
    for n in range(center_calc):
        index_large += n * 4
        index = index_large % size
        center += chars[index]
    #print(center)
    for n in range(1, center_calc):
        if center[:n] == center[n:2*n] and center[n:2*n] == center[2*n:3*n] and center[2*n:3*n] == center[3*n:4*n]:
            return center[:n]
    return(center)

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day27("vttussvutvuvvtustsvsvtvu")
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day27
'''

def Kurt_Hinderer_day27(chars):
    center = ""
    n = len(chars)
    if n == 0:
        return center
    elif n % 2 == 0:
        n //= 2
    # get the list of character positions
    pos = []
    for i in range(n):
        pos.append(2*i*(i+1) % len(chars))
    # get the characters in the center
    for num in pos:
        center += chars[num]
    # test if there's are repeat in the center
    for i in range(len(center)//2):
        test = center[:i+1]
        if center == test * (len(center)//len(test)):
            center = test
            break  
    return center

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day27("vttussvutvuvvtustsvsvtvu")
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day27
'''

def Oleksandra_Chmel_day27(chars):
    if chars == '': return ''
    if len(set(chars)) == 1: return chars[0]
    check, num, add, count = chars[0], 0, 4, 1
    length = len(chars)
    while 1:
        check += chars[(num + add) - length * ((num + add) // length)]
        num += add
        count += 1
        add = 4 * count
        if check[:len(check)//5] == check[len(check)//5:2*len(check)//5] == check[2*len(check)//5:3*len(check)//5] == check[3*len(check)//5:4*len(check)//5] == check[4*len(check)//5:]:
            break
    return check[:len(check)//5]

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day27("vttussvutvuvvtustsvsvtvu")
'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=10000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=10000)) + " seconds")
print("Time for Daniel_Ruiz test code: " + str(timeit.timeit(stmt=TEST_CODE_Daniel_Ruiz, setup=Daniel_Ruiz_setup, number=10000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=10000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
