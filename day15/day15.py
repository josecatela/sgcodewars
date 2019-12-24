import timeit
from functools import reduce
import string
import itertools

kilian_setup = '''
from __main__ import kilian_day15
'''

def kilian_day15(arr):
    i = 1
    while i < len(arr):
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
        elif i == len(arr) - 1:
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
result = kilian_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

akash_karan_setup = '''
from __main__ import akash_karan_day15
'''

def akash_karan_day15(arr):
    pos,peaks=[],[]
    l=len(arr)-1
    s,m=1,1
    fl=0
    maxx=-999
    di={}
    while(s<=l):
        if(arr[s]>arr[m]):
            m=s
        elif(arr[m]>arr[s] and arr[m]>maxx):
            if(arr[m]<=arr[m-1] and fl==0):
                m=s
            else:
                #print(m,arr[m])
                pos.append(m)
                peaks.append(arr[m])
                m=s
                maxx=arr[m]
        elif(arr[m]<=maxx and arr[m]>arr[s]):
            m=s
            maxx=arr[m]
            fl=1
        s+=1
    return {"pos":pos,"peaks":peaks}

TEST_CODE_akash_karan = '''
result = akash_karan_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day15
'''

def akash_agarwal_day15(arr):
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
result = akash_agarwal_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

ccquiel_setup = '''
from __main__ import ccquiel_day15
'''

def ccquiel_day15(arr):
    findex = 0
    pos, peaks = [], []
    for i in range(1, len(arr)-1):
        # prev curr next
        p, c, n = arr[i-1:i+2]
        if c == p and i > 1:
            if p > arr[i-2]:
                findex = i-1
        if c > n:
            if c > p:
                peaks.append(c)
                pos.append(i)
            elif c == p and findex:
                peaks.append(c)
                pos.append(findex)
                findex = 0
    return {'pos': pos, 'peaks': peaks}

TEST_CODE_ccquiel = '''
result = ccquiel_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day15
'''

def diana_henninger_day15(arr):
    pos = []
    peaks = []
    result = {'pos': pos, 'peaks': peaks}
    len_arr = len(arr)
    if(len_arr==0): return result # empty arr
    prev = arr[0]
    peaky = False
    for i in range(len_arr):
        a = arr[i]
        if not peaky:
            if prev < a: # might be a peak?
                peaky = True
                temp_peak = a
                temp_pos = i
        else: # might have a peak
            if prev > a: # yay, it's a peak!
                pos.append(temp_pos)
                peaks.append(temp_peak)
                peaky = False
            elif prev < a: # hmm not yet...
                temp_peak = a
                temp_pos = i
        prev = a
    return result


TEST_CODE_diana_henninger = '''
result = diana_henninger_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

ggebre_setup = '''
from __main__ import ggebre_day15
'''

def ggebre_day15(arr):
    n_to_string = [digit for digit in str(arr)]
    loop_count = 0
    while len(n_to_string) > 1:
        multiplication = 1
        for digit in n_to_string:
            multiplication *= int(digit)
        n_to_string = str(multiplication)
        loop_count += 1
    return loop_count

TEST_CODE_ggebre = '''
result = ggebre_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day15
'''

def recursion(arr):    
        
    return loopCount
def vijaya_lakshmi_day15(arr):
    firstLetter = ord(chars[0])
    loopCount = 0
    for everyChar in chars:
        if ord(everyChar) is not firstLetter + loopCount:
            return chr(firstLetter + loopCount)
        else:
            loopCount += 1

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day15
'''

def Prashanth_Kadimisetty_day15(arr):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day15
'''

def Krzysztof_Blach_day15(arr):
    count = 0
    while len(str(arr)) > 1:
        count += 1
        mult = 1
        digits = [int(el) for el in str(arr)]
        for digit in digits:
            mult = mult * digit
        n = mult
    return count

TEST_CODE_Krzysztof_Blach = '''
result = Krzysztof_Blach_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day15
'''


def Kurt_Hinderer_day15(arr):
    #nope not pick peak, pick local maximums
    pos = []
    for i in range(1, len(arr)-1):
        #peak or start of plateau
        if arr[i] > arr[i - 1]:
            #definitly a peak
            if arr[i] > arr[i + 1]:
                pos.append(i)
            elif arr[i] == arr[i+1]:
                j = i+1
                while j < len(arr) - 1 and arr[i] == arr[j]:
                    j += 1
                if arr[i] > arr[j]:
                    pos.append(i)
    peaks = [arr[pos[i]] for i in range(len(pos))]
    dictionary = {"pos":pos, "peaks":peaks}
    return dictionary


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day15
'''

def Jose_Catela_day15(arr):
    #your code here
    results = {"pos": [], "peaks": []}
    if len(arr) == 0:
        return results
    for index in range(len(arr)-2):
        left = arr[index]
        peak = arr[index+1]
        right = arr[index+2]
        plateau = 3
        while index+plateau < len(arr) and peak == right:
            right = arr[index+plateau]
            plateau += 1
        if left < peak and peak > right:
            results["pos"].append(index+1)
            results["peaks"].append(arr[index+1])
    return(results)

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''


Jens_setup = '''
from __main__ import Jens_day15
'''

def Jens_day15(arr):
    index = 0
    while index < len(arr) - 1:
        if(ord(chars[index+1])-ord(chars[index])) != 1:
            return chr(ord(chars[index])+1)
        index += 1

TEST_CODE_Jens = '''
result = Jens_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

Yang_setup = '''
from __main__ import Yang_day15
'''


def Yang_day15(arr):
    if not arr: return {"pos":[],"peaks":[]} 
    ll,index = [],[]
    for v,g in itertools.groupby(enumerate(arr), key = lambda k:k[1]): 
         ll.append(v) 
         index.append(next(g)[0])     
    ll[:0] = [arr[0]]
    ll.append(arr[-1]) 
    idx = 0 
    val,pos = [],[]
    for i,x in enumerate(ll[1:-1],1): 
        if ll[i-1] < x and x > ll[i+1]: 
            val.append(x)
            pos.append(index[i-1])
    return {"pos":pos,"peaks":val} 

TEST_CODE_Yang = '''
result = Yang_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day15
'''


def Vanessa_G_day15(arr):
    alf = "abcdefghijklmnopqrstuvwxyz"
    if chars[0].isupper(): alf = alf.upper()
    first = alf.find(chars[0])
    findIn = set(alf[first : first + len(arr)])
    return list(findIn.difference(set(arr)))[0]

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day15
'''


def Memo_Hurtado_day15(arr):
    alphabet = ('abcdefghijklmnopqrstuvwxyx', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  [chars[0].isupper()]
    alphaSlice = alphabet[alphabet.find(chars[0]):]
    #print(alphaSlice)
    for i in range(0, len(arr)-1):
        if (chars[i] != alphaSlice[i]):
            return alphaSlice[i]
    return alphaSlice[i+1] 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day15
'''


def Oleksandra_Chmel_day15(arr):
    if arr == []:
        return {"pos":[],"peaks":[]}
    pos = []
    peaks = []
    en = list(enumerate(arr))
    len_arr = len(arr)
    en = [tuple(en[0])] + [en[i] for i in range(1,len_arr) if i>0 and en[i][1]!=en[i-1][1]]
    len_en = len(en)-1
    for i,e in enumerate(en):
        if 0<i<len_en and en[i+1][1]<e[1]>en[i-1][1]:
            pos.append(e[0])
            peaks.append(e[1])
    return {'pos': pos, 'peaks': peaks}


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

sjay_setup = '''
from __main__ import sjay_day15
'''


def sjay_day15(arr):
    peaks=[]
    pos=[]
    #print(arr)
    for ind,elem in enumerate(arr):       
         if(ind > 0 and ind<len(arr)-1):
             flag = False
             if arr[ind-1] < elem and elem > arr[ind+1]:
                      flag=True
             elif arr[ind+1] == elem:
                 if(arr[ind-1] < elem and arr[ind+1:].count(elem)!= len(arr[ind+1:]) and arr[ind+1] >= arr[ind+2]):
                    flag=True
             if flag:
                 #print(arr[ind-1],elem,arr[ind+1])
                 pos.append(ind)
                 peaks.append(elem)
    return {"pos":pos, "peaks" :peaks}


TEST_CODE_sjay = '''
result = sjay_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''


charlie_ang_setup = '''
from __main__ import charlie_ang_day15
'''

def charlie_ang_day15(arr):
    peaks=[]
    pos=[]
    #print(arr)
    for ind,elem in enumerate(arr):       
         if(ind > 0 and ind<len(arr)-1):
             flag = False
             if arr[ind-1] < elem and elem > arr[ind+1]:
                      flag=True
             elif arr[ind+1] == elem:
                 if(arr[ind-1] < elem and arr[ind+1:].count(elem)!= len(arr[ind+1:]) and arr[ind+1] >= arr[ind+2]):
                    flag=True
             if flag:
                 #print(arr[ind-1],elem,arr[ind+1])
                 pos.append(ind)
                 peaks.append(elem)
    return {"pos":pos, "peaks" :peaks}


TEST_CODE_charlie_ang = '''
result = charlie_ang_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
#print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=100000)) + " seconds")
#print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
#print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=100000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
#print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
#print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
