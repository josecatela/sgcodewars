import timeit
from functools import reduce
import string
import itertools
import math

kilian_setup = '''
from __main__ import kilian_day19
'''

def kilian_day19(m):
    n=0
    vol = 0
    while vol <= m:
        vol += n ** 3
        if vol == m:
            return n
        n += 1
    return -1

TEST_CODE_kilian = '''
result = kilian_day19(1071225)
'''

akash_karan_setup = '''
from __main__ import akash_karan_day19
'''

def akash_karan_day19(m):
    i=0
    res=0
    while(res<m):
        res+=i**3
        i+=1
    if(res==m):
        return i-1
    else:
        return  -1

TEST_CODE_akash_karan = '''
result = akash_karan_day19(1071225)
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day19
'''

def akash_agarwal_day19(m):
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
result = akash_agarwal_day19(1071225)
'''

ccquiel_setup = '''
from __main__ import ccquiel_day19
'''

def ccquiel_day19(m):
    start = int((2*(m)**(1/2))**(1/2))
    n = start
    ms = 0
    for i in range(start):
        ms += i**3
    while ms < m:
        ms += n**3
        if ms == m:
            return n
        n += 1
    return -1

TEST_CODE_ccquiel = '''
result = ccquiel_day19(1071225)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day19
'''

def diana_henninger_day19(m):
    count = 0
    sum = 0
    while sum < m:
        sum += count**3
        count +=1
    if sum == m: return count-1
    return -1


TEST_CODE_diana_henninger = '''
result = diana_henninger_day19(1071225)
'''

ggebre_setup = '''
from __main__ import ggebre_day19
'''

def ggebre_day19(m):
    n_to_string = [digit for digit in str(m)]
    loop_count = 0
    while len(n_to_string) > 1:
        multiplication = 1
        for digit in n_to_string:
            multiplication *= int(digit)
        n_to_string = str(multiplication)
        loop_count += 1
    return loop_count

TEST_CODE_ggebre = '''
result = ggebre_day19(1071225)
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day19
'''

def recursion(m):    
        
    return loopCount
def vijaya_lakshmi_day19(m):
    cube = 1
    cubeSum = 0
    while cubeSum <= m:
        if(cubeSum == m):            
            return (cube - 1)
        cubeSum += pow(cube, 3)
        cube += 1
    return -1

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day19(1071225)
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day19
'''

def Prashanth_Kadimisetty_day19(m):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day19(1071225)
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day19
'''

def Krzysztof_Blach_day19(m):
    if m == 0: return 0
    i = 1
    while True:
        m -= i ** 3
        if m == 0:
            return i
        elif m > 0:
            i += 1
        else:
            return -1

TEST_CODE_Krzysztof_Blach = '''
result = Krzysztof_Blach_day19(1071225)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day19
'''


def Kurt_Hinderer_day19(m):
    # Well, this is more of math challenge (by my way of thinking).
    # sigma(n^3) = (sigma(n))^2. Proof first sigma(n) = n(n+1)/2
    # If n = 1, then sigma(1^3) = 1 = (sigma(n))^2. Using mathematical induction
    # we assume that the equation above works for all values up to n-1,
    # then we need to show the nth case works.
    # Well sigma(n^3) = n^3 + sigma((n-1)^3) = n^3 + (sigma(n-1))^2 
    # = n^3 ((n-1)(n)/2)^2 = 4n^3/4 + (n^4 - 2n^3 + n^2)/4 
    # = (n^4 + 2n^3 + n^2)/4 = (sigma(n))^2.
    #
    # Therefore all we have to do is find if there exists an integer n such that
    # n(n+1)/2 = sqrt(m). Using the quadratic formula,
    # n = (sqrt(8*sqrt(m) + 1) - 1)/2
    import decimal
    m = decimal.Decimal(m)
    n = ((8*m.sqrt()+1).sqrt() -1)/2
    if n%1 == 0:
        return n
    else:
        return -1


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day19(1071225)
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day19
'''

def Jose_Catela_day19(m):
    comp = 0
    it = 0
    while True:
        it += 1
        comp += (it ** 3)
        if comp == m:
            return it
        elif comp > m:
            return -1

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day19(1071225)
'''


Jens_setup = '''
from __main__ import Jens_day19
'''

def Jens_day19(m):
    result, count = 0, 0
    while result < m:
        count += 1
        result += count**3
        if result == m:
            return count
    return -1

TEST_CODE_Jens = '''
result = Jens_day19(1071225)
'''

Yang_setup = '''
from __main__ import Yang_day19
'''


def Yang_day19(m):
    i=1
    while m>0: 
        m-=i**3
        i+=1
    return i-1 if m==0 else -1

TEST_CODE_Yang = '''
result = Yang_day19(1071225)
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day19
'''


def Vanessa_G_day19(m):
    result, i = 0, 0
    while result < m:
        result += i ** 3
        if result == m: return i
        i += 1
    return -1

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day19(1071225)
'''

Daniel_Ruiz_setup = '''
from __main__ import Daniel_Ruiz_day19
'''


def Daniel_Ruiz_day19(m):
    result, i = 0, 0
    while result < m:
        result += i ** 3
        if result == m: return i
        i += 1
    return -1

TEST_CODE_Daniel_Ruiz = '''
result = Daniel_Ruiz_day19(1071225)
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day19
'''


def Memo_Hurtado_day19(m):
    alphabet = ('abcdefghijklmnopqrstuvwxyx', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  [chars[0].isupper()]
    alphaSlice = alphabet[alphabet.find(chars[0]):]
    #print(alphaSlice)
    for i in range(0, len(m)-1):
        if (chars[i] != alphaSlice[i]):
            return alphaSlice[i]
    return alphaSlice[i+1] 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day19(1071225)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day19
'''


def Oleksandra_Chmel_day19(m):
    n, answer = 1, 1
    while answer < m:
        n += 1
        answer += n**3
    if answer == m:
        return n
    else:
        return -1


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day19(1071225)
'''

sjay_setup = '''
from __main__ import sjay_day19
'''


def sjay_day19(m):
    flag = False
    sum=0
    for num in range(1,int(math.pow(m,1/3))):
        sum = sum + num**3
        if sum == m:
            flag = True
            break
        elif sum > m:
            flag=False
            break
    if flag==True:
        return int(num)
    else:
        return -1


TEST_CODE_sjay = '''
result = sjay_day19(1071225)
'''


charlie_ang_setup = '''
from __main__ import charlie_ang_day19
'''

def charlie_ang_day19(m):
    so_far = n =  1
    while so_far < m:
        n += 1
        so_far += n**3
    return n if so_far == m else -1


TEST_CODE_charlie_ang = '''
result = charlie_ang_day19(1071225)
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=10000)) + " seconds")
#print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=10000)) + " seconds")
print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=10000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=10000)) + " seconds")
print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=10000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=10000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=10000)) + " seconds")
#print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=10000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=10000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=10000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=10000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=10000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=10000)) + " seconds")
print("Time for Daniel_Ruiz test code: " + str(timeit.timeit(stmt=TEST_CODE_Daniel_Ruiz, setup=Daniel_Ruiz_setup, number=10000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=10000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=10000)) + " seconds")
