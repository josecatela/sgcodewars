import timeit
from functools import reduce
import string
import itertools
import math
import re

kilian_setup = '''
from __main__ import kilian_day26
'''

def kilian_day26(chars, n):
    count = 0
    for paranthese in string:
        if paranthese == '(':
           count += 1
        elif paranthese == ')':
            count -= 1
        if count < 0: return False
    return count == 0

TEST_CODE_kilian = '''
result = kilian_day26("1234",6)

'''
Samrat_Mukherjee_setup = '''
from __main__ import Samrat_Mukherjee_day26
'''

def Samrat_Mukherjee_day26(chars, n):
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
result = Samrat_Mukherjee_day26("1234",6)
'''

akash_karan_setup = '''
from __main__ import akash_karan_day26
'''

def akash_karan_day26(chars, n):
    ct=0
    le=len(chars)
    pat=""
    for i in range(n+1):
        pa=" "*(n-i)
        pat+=pa
        for k in range(i):
            pat+=chars[ct%le]+" "
            ct+=1
        pat=pat[:-1]+"\n"
    p=" "*(n-1)+"|"+"\n"
    p=p*(n//3)
    pat+=p    
    return pat[n:-1]

TEST_CODE_akash_karan = '''
result = akash_karan_day26("1234",6)
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day26
'''

def akash_agarwal_day26(chars, n):
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
result = akash_agarwal_day26("1234",6)
'''

ccquiel_setup = '''
from __main__ import ccquiel_day26
'''

def ccquiel_day26(chars, n):
    tree = str()
    chars_len = len(chars)
    lcount = 0
    for i in range(1, n+1):
        leaves = ' '.join([chars[(lcount + j) % chars_len] for j in range(i)])
        tree += ' '*(n - i) + leaves + '\n'
        lcount += i
    trunk = (' '*(n-1) + '|\n')*(n // 3)
    tree += trunk[:-1]
    return tree

TEST_CODE_ccquiel = '''
result = ccquiel_day26("1234",6)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day26
'''

def diana_henninger_day26(chars, n):
    tree = ""
    index = 0
    for i in range(n): # each line
        tree += (n-i-1) * ' ' #space
        for j in range(i+1):  #each char
            tree += chars[index%len(chars)] + ' '
            index += 1
        tree = tree[:-1] +'\n'
    for k in range(n//3): # trunk
        tree += (n-1) * ' ' + '|' + '\n'
    return tree[:-1]


TEST_CODE_diana_henninger = '''
result = diana_henninger_day26("1234",6)
'''

ggebre_setup = '''
from __main__ import ggebre_day26
'''

def ggebre_day26(chars, n):
    arr = []
    string = new_string.lower()
    string2 = new_string
    for index, x in enumerate(chars, n):
        if x not in arr : 
            if string.count(x) == 1:
                return string2[index]
            else:
                arr.append(x)
    if len(arr) == len(set(chars, n)):
          return ""

TEST_CODE_ggebre = '''
result = ggebre_day26("1234",6)
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day26
'''

def recursion(chars, n):    
        
    return loopCount
def vijaya_lakshmi_day26(chars, n):
    cube = 1
    cubeSum = 0
    while cubeSum <= m:
        if(cubeSum == m):            
            return (cube - 1)
        cubeSum += pow(cube, 3)
        cube += 1
    return -1

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day26("1234",6)
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day26
'''

def Prashanth_Kadimisetty_day26(chars, n):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day26("1234",6)
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day26
'''

def Krzysztof_Blach_day26(chars, n):
    if len(chars, n) == 0:
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
result = Krzysztof_Blach_day26("1234",6)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day26
'''


def Kurt_Hinderer_day26(chars, n):
    character = 0
    tree = ""
    if len(chars) == 0:
        return tree
    for i in range(n):
        tree += " " * (n - i - 1)
        for j in range(i + 1):
            tree += chars[character % len(chars)]
            character += 1
            if j < i:
                tree += " "
        tree += "\n"
    for i in range(n//3):
        tree += " " * (n - 1) + "|"
        if i < n//3 -1:
            tree += "\n"
    return tree


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day26("1234",6)
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day26
'''

def Jose_Catela_day26(chars, n):
    spaces = n - 1
    tree = ''
    pos = 0
    npos = len(chars)
    for k in range(n):
        tree += ' ' * spaces
        spaces -= 1
        for j in range(k+1):
            tree += chars[pos]
            pos += 1
            if pos == npos:
                pos = 0
            if j != k:
                tree += ' '
        tree += '\n'
    base_size = n // 3
    for k in range(base_size):
        tree += ' ' * ( n - 1)
        tree += '|'
        if k != base_size - 1:
            tree += '\n'
    return(tree)

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day26("1234",6)
'''


Jens_setup = '''
from __main__ import Jens_day26
'''

def Jens_day26(chars, n):
    tree_string, count = '', 0        
    for i in range(n):           # create leaves
        tree_string += (n-1-i)*' ' + (i)*'* ' + '*\n'
    for i in range(0, len(tree_string)-1): # decorate
        if tree_string[i] == '*':                  
            tree_string = tree_string[:i] + chars[count%len(chars)] + tree_string[i+1:]
            count += 1
    for i in range(n//3):         # create trunk
        tree_string += (n-1)*' ' + '|\n' 
    return(tree_string[:-1])

TEST_CODE_Jens = '''
result = Jens_day26("1234",6)
'''

Yang_setup = '''
from __main__ import Yang_day26
'''


def Yang_day26(chars, n):
    i=1
    while m>0: 
        m-=i**3
        i+=1
    return i-1 if m==0 else -1

TEST_CODE_Yang = '''
result = Yang_day26("1234",6)
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day26
'''


def Vanessa_G_day26(chars, n):
    count_left = 0
    count_right = 0
    for c in string:
        if count_left < count_right: return False
        elif c == '(': count_left += 1
        elif c == ')': count_right += 1
    return count_left == count_right

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day26("1234",6)
'''

Daniel_Ruiz_setup = '''
from __main__ import Daniel_Ruiz_day26
'''


def Daniel_Ruiz_day26(chars, n):
    result, i = 0, 0
    while result < m:
        result += i ** 3
        if result == m: return i
        i += 1
    return -1

TEST_CODE_Daniel_Ruiz = '''
result = Daniel_Ruiz_day26("1234",6)
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day26
'''


def Memo_Hurtado_day26(chars, n):
    alphabet = ('abcdefghijklmnopqrstuvwxyx', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  [chars[0].isupper()]
    alphaSlice = alphabet[alphabet.find(chars[0]):]
    #print(alphaSlice)
    for i in range(0, len(chars, n)-1):
        if (chars[i] != alphaSlice[i]):
            return alphaSlice[i]
    return alphaSlice[i+1] 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day26("1234",6)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day26
'''


def Oleksandra_Chmel_day26(chars, n):
    length = sum([x for x in range(1,n+1)])
    new_chars = chars * (length // len(chars)) + chars[:length%len(chars)]
    tree = ''
    for t in range(1,n+1):
        tree += ' ' * (n-t) + new_chars[0:t].replace('',' ').strip() + '\n'
        new_chars = new_chars[t:]
    return (tree + n//3 * (' ' * (n - 1) + '|' + '\n'))[:-1]


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day26("1234",6)
'''

sjay_setup = '''
from __main__ import sjay_day26
'''


def sjay_day26(chars, n):
    flag = False
    openpara = list(numb for numb,item in enumerate(chars, n) if item=="(")
    closepara = list(numb for numb,item in enumerate(chars, n) if item==")")
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
result = sjay_day26("1234",6)
'''


charlie_ang_setup = '''
from __main__ import charlie_ang_day26
'''

def charlie_ang_day26(chars, n):
    # first define width as being width = (n*2-1)
    result = [ " ".join(chars[(column + sum(range(rownum+1))) % len(chars)] for column in range(rownum+1)) for rownum in range(n) ]
    result += [ '|' for i in range(n//3)]
    return "\n".join(row.center(n*2-1).rstrip()  for row in result)


TEST_CODE_charlie_ang = '''
result = charlie_ang_day26("1234",6)
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
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
