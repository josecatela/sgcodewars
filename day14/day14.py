import timeit
from functools import reduce
import string

kilian_setup = '''
from __main__ import kilian_day14
'''

def kilian_day14(chars):
    i = 1
    while i < len(chars):
        if (arr[i] == 'NORTH') and (arr[i - 1] == 'SOUTH'):
            del arr[i-1]
            del arr[i-1]
        elif (arr[i] == 'SOUTH') and (arr[i - 1] == 'NORTH'):
            del arr[i-1]
            del arr[i-1]
        elif (arr[i] == 'WEST') and (arr[i - 1] == 'EAST'):
            del arr[i-1]
            del arr[i-1]
        elif (arr[i] == 'EAST') and (arr[i - 1] == 'WEST'):
            del arr[i-1]
            del arr[i-1]
        elif i == len(chars) - 1:
            break
        elif (arr[i] == 'NORTH') and (arr[i + 1] == 'SOUTH'):
            del arr[i]
            del arr[i]
        elif (arr[i] == 'SOUTH') and (arr[i + 1] == 'NORTH'):
            del arr[i]
            del arr[i]
        elif (arr[i] == 'WEST') and (arr[i + 1] == 'EAST'):
            del arr[i]
            del arr[i]
        elif (arr[i] == 'EAST') and (arr[i + 1] == 'WEST'):
            del arr[i]
            del arr[i]
        else:
            i += 1
    return arr

TEST_CODE_kilian = '''
result = kilian_day14(['a','b','c','d','f'])
'''

akash_karan_setup = '''
from __main__ import akash_karan_day14
'''

def akash_karan_day14(chars):
    n=len(chars)+1
    return chr(int((n/2)*(2*ord(chars[0])+(n-1)))-sum(list(map(lambda x:ord(x),chars))))

TEST_CODE_akash_karan = '''
result = akash_karan_day14(['a','b','c','d','f'])
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day14
'''

def akash_agarwal_day14(chars):
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
result = akash_agarwal_day14(['a','b','c','d','f'])
'''

ccquiel_setup = '''
from __main__ import ccquiel_day14
'''

def ccquiel_day14(chars):
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for s in abc[abc.index(chars[0]):]:
        if s not in chars:
            return s

TEST_CODE_ccquiel = '''
result = ccquiel_day14(['a','b','c','d','f'])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day14
'''

def diana_henninger_day14(chars):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
                "u","v","w","x","y","z"]
    j = alphabet.index(chars[0].lower())
    for i in range(len(chars)):
        c = chars[i]
        a = alphabet[j]
        if c.isupper(): a = a.upper()
        if(c != a): return a
        j += 1


TEST_CODE_diana_henninger = '''
result = diana_henninger_day14(['a','b','c','d','f'])
'''

ggebre_setup = '''
from __main__ import ggebre_day14
'''

def ggebre_day14(chars):
    n_to_string = [digit for digit in str(chars)]
    loop_count = 0
    while len(n_to_string) > 1:
        multiplication = 1
        for digit in n_to_string:
            multiplication *= int(digit)
        n_to_string = str(multiplication)
        loop_count += 1
    return loop_count

TEST_CODE_ggebre = '''
result = ggebre_day14(['a','b','c','d','f'])
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day14
'''

def recursion(chars):    
        
    return loopCount
def vijaya_lakshmi_day14(chars):
    firstLetter = ord(chars[0])
    loopCount = 0
    for everyChar in chars:
        if ord(everyChar) is not firstLetter + loopCount:
            return chr(firstLetter + loopCount)
        else:
            loopCount += 1

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day14(['a','b','c','d','f'])
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day14
'''

def Prashanth_Kadimisetty_day14(chars):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day14(['a','b','c','d','f'])
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day14
'''

def Krzysztof_Blach_day14(chars):
    count = 0
    while len(str(chars)) > 1:
        count += 1
        mult = 1
        digits = [int(el) for el in str(chars)]
        for digit in digits:
            mult = mult * digit
        n = mult
    return count

TEST_CODE_Krzysztof_Blach = '''
result = Krzysztof_Blach_day14(['a','b','c','d','f'])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day14
'''


def Kurt_Hinderer_day14(chars):
    #get the ascii code of the first letter
    ascii_letter_code = ord(chars[0])
    found_missing = False
    #loop until the missing ascii codes is found
    i = 0
    while not found_missing and i < len(chars) - 1:
        if ord(chars[i+1]) != ascii_letter_code + i + 1:
            found_missing = True
        i +=1
    return(chr(ascii_letter_code + i))


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day14(['a','b','c','d','f'])
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day14
'''

def Jose_Catela_day14(chars):
    index = 0
    while index < len(chars) - 1:
        if(ord(chars[index+1])-ord(chars[index])) != 1:
            return chr(ord(chars[index])+1)
        index += 1

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day14(['a','b','c','d','f'])
'''


Jens_setup = '''
from __main__ import Jens_day14
'''

def Jens_day14(chars):
    index = 0
    while index < len(chars) - 1:
        if(ord(chars[index+1])-ord(chars[index])) != 1:
            return chr(ord(chars[index])+1)
        index += 1

TEST_CODE_Jens = '''
result = Jens_day14(['a','b','c','d','f'])
'''

Yang_setup = '''
from __main__ import Yang_day14
'''


def Yang_day14(chars):
    for i,x in enumerate(chars,ord(chars[0])): 
        if i != ord(x): 
            return (chr(i))

TEST_CODE_Yang = '''
result = Yang_day14(['a','b','c','d','f'])
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day14
'''


def Vanessa_G_day14(chars):
    alf = "abcdefghijklmnopqrstuvwxyz"
    if chars[0].isupper(): alf = alf.upper()
    first = alf.find(chars[0])
    findIn = set(alf[first : first + len(chars)])
    return list(findIn.difference(set(chars)))[0]

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day14(['a','b','c','d','f'])
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day14
'''


def Memo_Hurtado_day14(chars):
    alphabet = ('abcdefghijklmnopqrstuvwxyx', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  [chars[0].isupper()]
    alphaSlice = alphabet[alphabet.find(chars[0]):]
    #print(alphaSlice)
    for i in range(0, len(chars)-1):
        if (chars[i] != alphaSlice[i]):
            return alphaSlice[i]
    return alphaSlice[i+1] 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day14(['a','b','c','d','f'])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day14
'''


def Oleksandra_Chmel_day14(chars):
    s = string.ascii_lowercase + string.ascii_uppercase
    target = s[s.index(chars[0]):s.index(chars[len(chars)-1])]
    for i in target:
        if i not in chars:
            return i


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day14(['a','b','c','d','f'])
'''

sjay_setup = '''
from __main__ import sjay_day14
'''


def sjay_day14(chars):
    abcs = "abcdefghijklmnopqrstuvwxyz"
    comp = abcs[abcs.index(chars[0].lower()):abcs.index(chars[0].lower())+len(chars)]
    for ind,ch in enumerate(chars):
          if ch.lower() != comp[ind].lower():
              if ch.islower():
                  return comp[ind]
              else:
                  return comp[ind].upper()
              break


TEST_CODE_sjay = '''
result = sjay_day14(['a','b','c','d','f'])
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
#print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=100000)) + " seconds")
#print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
#print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=100000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
