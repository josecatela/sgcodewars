import timeit
from functools import reduce
import string
import itertools
import math
import re

kilian_setup = '''
from __main__ import kilian_day21
'''

def kilian_day21(items,k):
    count = 0
    for paranthese in string:
        if paranthese == '(':
           count += 1
        elif paranthese == ')':
            count -= 1
        if count < 0: return False
    return count == 0

TEST_CODE_kilian = '''
result = kilian_day21([1,2,3,4,5,6,7],3)

'''
Samrat_Mukherjee_setup = '''
from __main__ import Samrat_Mukherjee_day21
'''

def Samrat_Mukherjee_day21(items,k):
    #your code here
    stack  = []
    for char in string:
        if char == '(':
            stack.append(char)
        else:
            try:
                if char == ')':
                    del stack[-1]
            except:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

TEST_CODE_Samrat_Mukherjee = '''
result = Samrat_Mukherjee_day21([1,2,3,4,5,6,7],3)
'''

akash_karan_setup = '''
from __main__ import akash_karan_day21
'''

def akash_karan_day21(items,k):
    fl=0
    s=[]
    for i in string:
        if(i==")" and fl==0 ):
            return False
        elif(i=="("):
            s.append("(")
            fl=1
        elif(i==")"):
            try:
                s.pop()
            except(IndexError):
                return False
            fl=1
    return not len(s)

TEST_CODE_akash_karan = '''
result = akash_karan_day21([1,2,3,4,5,6,7],3)
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day21
'''

def akash_agarwal_day21(items,k):
    di={"NORTH":1, "WEST":-1j, "SOUTH":-1, "EAST":1j}
    l,t1=[],0
    for i in arr:
        if (t1+di[i]==0):
            l.pop()                     #if north-south or east-west comes one after another
            if not(len(l)):t1=0         #then pop the prev and dont add the current
            else: t1=di[l[-1]]          #update the prev element after pop element
        else:
            l.append(i)
            t1=di[i]
    return l 

TEST_CODE_akash_agarwal = '''
result = akash_agarwal_day21([1,2,3,4,5,6,7],3)
'''

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

ggebre_setup = '''
from __main__ import ggebre_day21
'''

def ggebre_day21(items,k):
    n_to_string = [digit for digit in str(items,k)]
    loop_count = 0
    while len(n_to_string) > 1:
        multiplication = 1
        for digit in n_to_string:
            multiplication *= int(digit)
        n_to_string = str(multiplication)
        loop_count += 1
    return loop_count

TEST_CODE_ggebre = '''
result = ggebre_day21([1,2,3,4,5,6,7],3)
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day21
'''

def recursion(items,k):    
        
    return loopCount
def vijaya_lakshmi_day21(items,k):
    cube = 1
    cubeSum = 0
    while cubeSum <= m:
        if(cubeSum == m):            
            return (cube - 1)
        cubeSum += pow(cube, 3)
        cube += 1
    return -1

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day21([1,2,3,4,5,6,7],3)
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day21
'''

def Prashanth_Kadimisetty_day21(items,k):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day21([1,2,3,4,5,6,7],3)
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day21
'''

def Krzysztof_Blach_day21(items,k):
    if len(items,k) == 0:
        return True
    paren_str = ''
    for char in string:
        if char == '(' or char == ')':
            paren_str += char
    for i in range(len(paren_str) - 1):
        if paren_str[i] == '(' and paren_str[i + 1] == ')':
            return valid_parentheses(paren_str[:i] + paren_str[i + 2:])
    return False

TEST_CODE_Krzysztof_Blach = '''
result = Krzysztof_Blach_day21([1,2,3,4,5,6,7],3)
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

Yang_setup = '''
from __main__ import Yang_day21
'''


def Yang_day21(items,k):
    i=1
    while m>0: 
        m-=i**3
        i+=1
    return i-1 if m==0 else -1

TEST_CODE_Yang = '''
result = Yang_day21([1,2,3,4,5,6,7],3)
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day21
'''


def Vanessa_G_day21(items,k):
    count_left = 0
    count_right = 0
    for c in string:
        if count_left < count_right: return False
        elif c == '(': count_left += 1
        elif c == ')': count_right += 1
    return count_left == count_right

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day21([1,2,3,4,5,6,7],3)
'''

Daniel_Ruiz_setup = '''
from __main__ import Daniel_Ruiz_day21
'''


def Daniel_Ruiz_day21(items,k):
    result, i = 0, 0
    while result < m:
        result += i ** 3
        if result == m: return i
        i += 1
    return -1

TEST_CODE_Daniel_Ruiz = '''
result = Daniel_Ruiz_day21([1,2,3,4,5,6,7],3)
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day21
'''


def Memo_Hurtado_day21(items,k):
    alphabet = ('abcdefghijklmnopqrstuvwxyx', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  [chars[0].isupper()]
    alphaSlice = alphabet[alphabet.find(chars[0]):]
    #print(alphaSlice)
    for i in range(0, len(items,k)-1):
        if (chars[i] != alphaSlice[i]):
            return alphaSlice[i]
    return alphaSlice[i+1] 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day21([1,2,3,4,5,6,7],3)
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

sjay_setup = '''
from __main__ import sjay_day21
'''


def sjay_day21(items,k):
    flag = False
    openpara = list(numb for numb,item in enumerate(items,k) if item=="(")
    closepara = list(numb for numb,item in enumerate(items,k) if item==")")
    data = zip(openpara,closepara)
    #print(openpara,closepara)
    for item in data:
        #print(item)
        if isinstance(item[0],int)and isinstance(item[1],int):
            if item[0] < item[1]:
                flag = True
            else:
                flag = False
                break
        else:
            flag=False
            break
    if len(openpara)==0 and len(closepara)==0:
        flag=True
    elif len(openpara)!= len(closepara):
        flag=False
    return flag


TEST_CODE_sjay = '''
result = sjay_day21([1,2,3,4,5,6,7],3)
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

#print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
#print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=100000)) + " seconds")
#print("Time for Samrat_Mukherjee test code: " + str(timeit.timeit(stmt=TEST_CODE_Samrat_Mukherjee, setup=Samrat_Mukherjee_setup, number=100000)) + " seconds")
#print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
#print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=100000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
#print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
#print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
#print("Time for Daniel_Ruiz test code: " + str(timeit.timeit(stmt=TEST_CODE_Daniel_Ruiz, setup=Daniel_Ruiz_setup, number=100000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
#print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
