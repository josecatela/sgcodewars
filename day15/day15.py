import timeit
import itertools


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

charlie_ang_setup = '''
from __main__ import charlie_ang_day15
'''

def charlie_ang_day15(arr):
    pos = []
    peaks = []
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i]:
            # possible peak, check if there are any downward movements
            next_value = next(filter(lambda x: x != arr[i], [q for q in arr[i+1:]]), None)
            if next_value is not None and arr[i] > next_value:
                pos.append(i)
                peaks.append(arr[i])
    return {"pos": pos, "peaks": peaks}

TEST_CODE_charlie_ang = '''
result = charlie_ang_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
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

Jens_setup = '''
from __main__ import Jens_day15
'''

def Jens_day15(arr):
    peaks = {"pos": [], "peaks": []}
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]: #regular peaks
            peaks["pos"].append(i)
            peaks["peaks"].append(arr[i])
        if arr[i-1] < arr[i] and arr[i] == arr[i+1]: #plateau peaks
            for n in range(i+1, len(arr)):
                if arr[i] > arr[n]:
                    peaks["pos"].append(i)
                    peaks["peaks"].append(arr[i])
                    break
                elif arr[i] < arr[n]:
                    break
    return peaks

TEST_CODE_Jens = '''
result = Jens_day15([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
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

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
