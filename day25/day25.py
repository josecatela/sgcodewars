import timeit
from functools import reduce
import string
import itertools
import math
import re

kilian_setup = '''
from __main__ import kilian_day22
'''

def kilian_day22(string):
    count = 0
    for paranthese in string:
        if paranthese == '(':
           count += 1
        elif paranthese == ')':
            count -= 1
        if count < 0: return False
    return count == 0

TEST_CODE_kilian = '''
result = kilian_day22('Go hang a salami, Im a lasagna hog!')

'''
Samrat_Mukherjee_setup = '''
from __main__ import Samrat_Mukherjee_day22
'''

def Samrat_Mukherjee_day22(string):
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
result = Samrat_Mukherjee_day22('Go hang a salami, Im a lasagna hog!')
'''

akash_karan_setup = '''
from __main__ import akash_karan_day22
'''

def akash_karan_day22(string):
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
result = akash_karan_day22('Go hang a salami, Im a lasagna hog!')
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day22
'''

def akash_agarwal_day22(string):
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
result = akash_agarwal_day22('Go hang a salami, Im a lasagna hog!')
'''

ccquiel_setup = '''
from __main__ import ccquiel_day22
'''

def ccquiel_day22(string):
    seen = set()
    lstring = string.lower()
    for i, s in enumerate(lstring):
        if s not in lstring[i+1:] and s not in seen:
            return string[i]
        else:
            seen.add(s)
    return ''

TEST_CODE_ccquiel = '''
result = ccquiel_day22('Go hang a salami, Im a lasagna hog!')
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day22
'''

def diana_henninger_day22(string):
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
result = diana_henninger_day22('Go hang a salami, Im a lasagna hog!')
'''

ggebre_setup = '''
from __main__ import ggebre_day22
'''

def ggebre_day22(string):
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
result = ggebre_day22('Go hang a salami, Im a lasagna hog!')
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day22
'''

def recursion(string):    
        
    return loopCount
def vijaya_lakshmi_day22(string):
    cube = 1
    cubeSum = 0
    while cubeSum <= m:
        if(cubeSum == m):            
            return (cube - 1)
        cubeSum += pow(cube, 3)
        cube += 1
    return -1

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day22('Go hang a salami, Im a lasagna hog!')
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day22
'''

def Prashanth_Kadimisetty_day22(string):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day22('Go hang a salami, Im a lasagna hog!')
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day22
'''

def Krzysztof_Blach_day22(string):
    if len(string) == 0:
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
result = Krzysztof_Blach_day22('Go hang a salami, Im a lasagna hog!')
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day22
'''


def Kurt_Hinderer_day22(string):
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
result = Kurt_Hinderer_day22('Go hang a salami, Im a lasagna hog!')
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day22
'''

def Jose_Catela_day22(string):
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
result = Jose_Catela_day22('Go hang a salami, Im a lasagna hog!')
'''


Jens_setup = '''
from __main__ import Jens_day22
'''

def Jens_day22(string):
    for letter in string:
        if string.lower().count(letter.lower()) == 1:
            return letter
    return ''

TEST_CODE_Jens = '''
result = Jens_day22('Go hang a salami, Im a lasagna hog!')
'''

Yang_setup = '''
from __main__ import Yang_day22
'''


def Yang_day22(string):
    i=1
    while m>0: 
        m-=i**3
        i+=1
    return i-1 if m==0 else -1

TEST_CODE_Yang = '''
result = Yang_day22('Go hang a salami, Im a lasagna hog!')
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day22
'''


def Vanessa_G_day22(string):
    count_left = 0
    count_right = 0
    for c in string:
        if count_left < count_right: return False
        elif c == '(': count_left += 1
        elif c == ')': count_right += 1
    return count_left == count_right

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day22('Go hang a salami, Im a lasagna hog!')
'''

Daniel_Ruiz_setup = '''
from __main__ import Daniel_Ruiz_day22
'''


def Daniel_Ruiz_day22(string):
    result, i = 0, 0
    while result < m:
        result += i ** 3
        if result == m: return i
        i += 1
    return -1

TEST_CODE_Daniel_Ruiz = '''
result = Daniel_Ruiz_day22('Go hang a salami, Im a lasagna hog!')
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day22
'''


def Memo_Hurtado_day22(string):
    alphabet = ('abcdefghijklmnopqrstuvwxyx', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  [chars[0].isupper()]
    alphaSlice = alphabet[alphabet.find(chars[0]):]
    #print(alphaSlice)
    for i in range(0, len(string)-1):
        if (chars[i] != alphaSlice[i]):
            return alphaSlice[i]
    return alphaSlice[i+1] 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day22('Go hang a salami, Im a lasagna hog!')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day22
'''


def Oleksandra_Chmel_day22(string):
    for i,e in enumerate(string):
        if string.lower().count(e.lower()) ==1:
            return string[i]
    return ''


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day22('Go hang a salami, Im a lasagna hog!')
'''

sjay_setup = '''
from __main__ import sjay_day22
'''


def sjay_day22(string):
    flag = False
    openpara = list(numb for numb,item in enumerate(string) if item=="(")
    closepara = list(numb for numb,item in enumerate(string) if item==")")
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
result = sjay_day22('Go hang a salami, Im a lasagna hog!')
'''


charlie_ang_setup = '''
from __main__ import charlie_ang_day22
'''

def charlie_ang_day22(string):
    string_lower = string.lower()
    eliminated = set()
    for i,c in enumerate(string_lower):
        if c not in string_lower[i+1:] and c not in eliminated:
            return string[i]
        eliminated.add(c)
    return ""


TEST_CODE_charlie_ang = '''
result = charlie_ang_day22('Go hang a salami, Im a lasagna hog!')
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
