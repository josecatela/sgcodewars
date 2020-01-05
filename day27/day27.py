import timeit
from functools import reduce
import string
import itertools
import math
import re

kilian_setup = '''
from __main__ import kilian_day27
'''

def kilian_day27(chars):
    count = 0
    for paranthese in string:
        if paranthese == '(':
           count += 1
        elif paranthese == ')':
            count -= 1
        if count < 0: return False
    return count == 0

TEST_CODE_kilian = '''
result = kilian_day27("vttussvutvuvvtustsvsvtvu")

'''
Samrat_Mukherjee_setup = '''
from __main__ import Samrat_Mukherjee_day27
'''

def Samrat_Mukherjee_day27(chars):
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
result = Samrat_Mukherjee_day27("vttussvutvuvvtustsvsvtvu")
'''

akash_karan_setup = '''
from __main__ import akash_karan_day27
'''

def akash_karan_day27(chars):
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
result = akash_karan_day27("vttussvutvuvvtustsvsvtvu")
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day27
'''

def akash_agarwal_day27(chars):
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
result = akash_agarwal_day27("vttussvutvuvvtustsvsvtvu")
'''

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

ggebre_setup = '''
from __main__ import ggebre_day27
'''

def ggebre_day27(chars):
    arr = []
    string = new_string.lower()
    string2 = new_string
    for index, x in enumerate(chars):
        if x not in arr : 
            if string.count(x) == 1:
                return string2[index]
            else:
                arr.append(x)
    if len(arr) == len(set(chars)):
          return ""

TEST_CODE_ggebre = '''
result = ggebre_day27("vttussvutvuvvtustsvsvtvu")
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day27
'''

def recursion(chars):    
        
    return loopCount
def vijaya_lakshmi_day27(chars):
    cube = 1
    cubeSum = 0
    while cubeSum <= m:
        if(cubeSum == m):            
            return (cube - 1)
        cubeSum += pow(cube, 3)
        cube += 1
    return -1

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day27("vttussvutvuvvtustsvsvtvu")
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day27
'''

def Prashanth_Kadimisetty_day27(chars):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day27("vttussvutvuvvtustsvsvtvu")
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day27
'''

def Krzysztof_Blach_day27(chars):
    if len(chars) == 0:
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
result = Krzysztof_Blach_day27("vttussvutvuvvtustsvsvtvu")
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


Jens_setup = '''
from __main__ import Jens_day27
'''

def Jens_day27(chars):
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
result = Jens_day27("vttussvutvuvvtustsvsvtvu")
'''

Yang_setup = '''
from __main__ import Yang_day27
'''


def Yang_day27(chars):
    i=1
    while m>0: 
        m-=i**3
        i+=1
    return i-1 if m==0 else -1

TEST_CODE_Yang = '''
result = Yang_day27("vttussvutvuvvtustsvsvtvu")
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day27
'''


def Vanessa_G_day27(chars):
    count_left = 0
    count_right = 0
    for c in string:
        if count_left < count_right: return False
        elif c == '(': count_left += 1
        elif c == ')': count_right += 1
    return count_left == count_right

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day27("vttussvutvuvvtustsvsvtvu")
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

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day27
'''


def Memo_Hurtado_day27(chars):
    alphabet = ('abcdefghijklmnopqrstuvwxyx', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  [chars[0].isupper()]
    alphaSlice = alphabet[alphabet.find(chars[0]):]
    #print(alphaSlice)
    for i in range(0, len(chars)-1):
        if (chars[i] != alphaSlice[i]):
            return alphaSlice[i]
    return alphaSlice[i+1] 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day27("vttussvutvuvvtustsvsvtvu")
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

sjay_setup = '''
from __main__ import sjay_day27
'''


def sjay_day27(chars):
    flag = False
    openpara = list(numb for numb,item in enumerate(chars) if item=="(")
    closepara = list(numb for numb,item in enumerate(chars) if item==")")
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
result = sjay_day27("vttussvutvuvvtustsvsvtvu")
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

#print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=10000)) + " seconds")
#print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=10000)) + " seconds")
#print("Time for Samrat_Mukherjee test code: " + str(timeit.timeit(stmt=TEST_CODE_Samrat_Mukherjee, setup=Samrat_Mukherjee_setup, number=10000)) + " seconds")
#print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=10000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=10000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=10000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=10000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=10000)) + " seconds")
#print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=10000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=10000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=10000)) + " seconds")
#print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=10000)) + " seconds")
#print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=10000)) + " seconds")
#print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=10000)) + " seconds")
print("Time for Daniel_Ruiz test code: " + str(timeit.timeit(stmt=TEST_CODE_Daniel_Ruiz, setup=Daniel_Ruiz_setup, number=10000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
#print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=10000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=10000)) + " seconds")
