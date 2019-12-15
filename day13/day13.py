import timeit
from functools import reduce

kilian_setup = '''
from __main__ import kilian_day13
'''

def kilian_day13(arr):
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
result = kilian_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

akash_karan_setup = '''
from __main__ import akash_karan_day13
'''

def akash_karan_day13(arr):
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

TEST_CODE_akash_karan = '''
result = akash_karan_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day13
'''

def akash_agarwal_day13(arr):
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
result = akash_agarwal_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

ccquiel_setup = '''
from __main__ import ccquiel_day13
'''

def ccquiel_day13(arr):
    dirnum = {"NORTH": 1, "SOUTH": -1,
            "EAST":  2,  "WEST": -2}
    index = 0
    while index < (len(arr) - 1):
        if dirnum[arr[index]] + dirnum[arr[index+1]] == 0:
            arr = arr[:index] + arr[index+2:]
            index = 0
        else:
            index += 1
    return arr

TEST_CODE_ccquiel = '''
result = ccquiel_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day13
'''

def opposite(x,y):
    return (x=="NORTH" and y=="SOUTH") or (x=="SOUTH" and y=="NORTH") or (x=="WEST" and y=="EAST") or (x=="EAST" and y=="WEST")
def diana_henninger_day13(arr):
    i = 0
    while (i<len(arr)-1):
        x = arr[i]
        y = arr[i+1]
        if opposite(x,y):
            del arr[i]
            del arr[i]
            i = 0
        else: i+=1
    return arr


TEST_CODE_diana_henninger = '''
result = diana_henninger_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

ggebre_setup = '''
from __main__ import ggebre_day13
'''

def ggebre_day13(arr):
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
result = ggebre_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day13
'''

def recursion(arr):    
    res = [int(x) for x in str(arr)]   
    total = reduce((lambda x, y: x * y), res)
    loopCount = 1
    while total >= 10:    
        tot = [int(x) for x in str(total)]   
        total = reduce((lambda x, y: x * y), tot)
        loopCount += 1
        
    return loopCount
def vijaya_lakshmi_day13(arr):
    # your code
    if(len(str(arr)) < 2):
        return 0
    else:
        return recursion(arr)

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day13
'''

def Prashanth_Kadimisetty_day13(arr):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day13
'''

def Krzysztof_Blach_day13(arr):
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
result = Krzysztof_Blach_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day13
'''


def Kurt_Hinderer_day13(directions):
    #damn, no vectors, have to fudge it
    dir_dict = {"NORTH": -1, "SOUTH": 1, "EAST": -2, "WEST": 2}
    done = False
    while not done:
        i = 0
        deleted = False
        while i < len(directions)-1 and not deleted:
            if dir_dict[directions[i]] + dir_dict[directions[i+1]] == 0:
                del directions[i: i+2]
                deleted = True
            i += 1
        done = not deleted
    return directions


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day13
'''

def Jose_Catela_day13(arr):
    cases = ['NORTHSOUTH', 'SOUTHNORTH', 'EASTWEST', 'WESTEAST']
    position = 0
    while len(arr) != 0 and position != len(arr) - 1:
        to_test = arr[position] + arr[position+1]
        if to_test in cases:
            arr.pop(position)
            arr.pop(position)
            position = 0
        else:
            position += 1
    return arr

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Yang_setup = '''
from __main__ import Yang_day13
'''


def Yang_day13(arr):
    count = 0 
    while n>9: 
        n = reduce(lambda x,y:int(x)*int(y), str(arr))
        count +=1 
    return count

TEST_CODE_Yang = '''
result = Yang_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day13
'''


def Vanessa_G_day13(arr):
    count = 0
    while n >= 10:
        n = reduce(lambda x, y: x * y, [int(x) for x in str(arr)])
        count += 1
    return count

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day13
'''


def Memo_Hurtado_day13(arr):
    if (n<10):
      return 0;
    string = str(arr)
    a = 1
    p = 0
    while True:
        string = (str(a), string)  [p == 0]
        a = 1
        for s in string:
            b = int(s) 
            a = a * b
        p += 1
        if (a<9):
            break
    return p 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day13
'''


def Oleksandra_Chmel_day13(arr):
    check = {'WEST':'EAST','EAST':'WEST','NORTH':'SOUTH','SOUTH':'NORTH'}
    count = len(arr)+1
    def smaller(arr):
        for ind,dir in enumerate(arr):
            if dir and check[dir]==arr[ind-1]:
                del arr[ind-1:ind+1]
        return arr
    while len(arr)!=count:
        arr = smaller(arr)
        count -= 1
    return arr


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

sjay_setup = '''
from __main__ import sjay_day13
'''


def sjay_day13(arr):
    index=0
    while index <= len(arr)-2:
        if (str(arr[index]).upper() == "NORTH" and str(arr[index+1]).upper()=="SOUTH") or (str(arr[index].upper()) == "SOUTH" and str(arr[index+1]).upper()=="NORTH"):
            del arr[index:index+2]
            index =0
        elif (str(arr[index]).upper() == "EAST" and str(arr[index+1]).upper()=="WEST") or (str(arr[index]).upper() == "WEST" and str(arr[index+1]).upper()=="EAST"):
            del arr[index:index+2]
            index=0
        else:
            index = index + 1
    return arr


TEST_CODE_sjay = '''
result = sjay_day13(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=100000)) + " seconds")
print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
#print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=100000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
#print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
#print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
