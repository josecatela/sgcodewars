import timeit
from functools import reduce
import string
import itertools

kilian_setup = '''
from __main__ import kilian_day16
'''

def kilian_day16(reinforces, airstrikes):
    if len(airstrikes) == 0:
        return reinforces[0]
    battlefield = list(reinforces[0])
    pos_on_battlefield = [0] * len(battlefield)
    change_battlefield = [0] * len(battlefield)
    for k, word in enumerate(reinforces):
        reinforces[k] = list(word)
    for strike in airstrikes:
        for i, bomb in enumerate(strike):
            if len(battlefield) < i:
                continue
            if bomb == '*':
                if 0 < i < len(battlefield) - 1:
                    for j in range(i - 1, i + 2):
                        battlefield[j] = '_' if pos_on_battlefield[j] >= len(reinforces) - 1 else \
                        reinforces[pos_on_battlefield[j] + 1][j]
                        change_battlefield[j] = 1
                elif i == 0 and i < len(battlefield) - 1:
                    for j in range(i, i + 2):
                        battlefield[j] = '_' if pos_on_battlefield[j] >= len(reinforces) - 1 else \
                        reinforces[pos_on_battlefield[j] + 1][j]
                        change_battlefield[j] = 1
                elif i > 0 and i == len(battlefield) - 1:
                    for j in range(i - 1, i + 1):
                        battlefield[j] = '_' if pos_on_battlefield[j] >= len(reinforces) - 1 else \
                        reinforces[pos_on_battlefield[j] + 1][j]
                        change_battlefield[j] = 1
                else:
                    battlefield[i] = '_' if pos_on_battlefield[i] >= len(reinforces) - 1 else \
                    reinforces[pos_on_battlefield[i] + 1][i]
                    change_battlefield[i] = 1
        for l in range(len(change_battlefield)):
            pos_on_battlefield[l] += change_battlefield[l]
            change_battlefield[l] = 0
    return ''.join(battlefield)

TEST_CODE_kilian = '''
result = kilian_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

akash_karan_setup = '''
from __main__ import akash_karan_day16
'''

def akash_karan_day16(reinforces, airstrikes):
    l=len(reinforces[0])
    ct=[0]*l
    al=len(airstrikes)
    k,result=0,""
    while(k<al):
        resultant=[False]*l
        for i,x in enumerate(airstrikes[k]):
            if(x=="*"):
                if(i==0):
                    resultant[i+1]=True
                elif(i==(l-1)):
                    resultant[i-1]=True
                elif(x=="*"):
                    resultant[i-1]=True
                    resultant[i+1]=True
                resultant[i]=True
        for i,x in enumerate(resultant):
            if(x):
                ct[i]+=1
        k+=1
    for i,x in enumerate(ct):
        if(x>=len(reinforces)):
            result+="_"
        else:
            result+=reinforces[x][i]
    return result

TEST_CODE_akash_karan = '''
result = akash_karan_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''



akash_agarwal_setup = '''
from __main__ import akash_agarwal_day16
'''

def akash_agarwal_day16(reinforces, airstrikes):
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
result = akash_agarwal_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

ccquiel_setup = '''
from __main__ import ccquiel_day16
'''

def ccquiel_day16(reinforces, airstrikes):
    reinforces = [list(r) for r in reinforces]
    maxi = len(reinforces[0]) - 1
    mini = 0
    field = reinforces.pop(0)
    for strike in airstrikes:
        # Get indices
        indices = set()
        for i, x in enumerate(strike):
            if x == "*":
                indices.add(i)
                if i < maxi:
                    indices.add(i+1)
                if i > mini:
                    indices.add(i-1)
        # Set reinforcements
        for i in list(indices):
            for r in reinforces:
                if r[i] != '_':
                    field[i] = r[i]
                    r[i] = '_'
                    break
            else:
                field[i] = '_'
    return ''.join(field)

TEST_CODE_ccquiel = '''
result = ccquiel_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day16
'''

def diana_henninger_day16(reinforces, airstrikes):
    bfield = reinforces[0]
    index = [0 for x in bfield]
    for airstrike in airstrikes:
        bombed_places = [False for x in bfield]
        for i in range(len(airstrike)):
            if airstrike[i]=='*':
                if i > 0: bombed_places[i-1] = True
                if i < len(index): bombed_places[i] = True
                if i < len(index)-1: bombed_places[i+1] = True
        for i in range(len(index)):
            if bombed_places[i]: index[i]+=1
        bombed_places = [False for x in bfield]
    result = ""
    j = 0
    for i in index:
        if i >= len(reinforces): result += '_'
        else: result += reinforces[i][j]
        j+=1
    return result


TEST_CODE_diana_henninger = '''
result = diana_henninger_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

ggebre_setup = '''
from __main__ import ggebre_day16
'''

def ggebre_day16(reinforces, airstrikes):
    n_to_string = [digit for digit in str(reinforces, airstrikes)]
    loop_count = 0
    while len(n_to_string) > 1:
        multiplication = 1
        for digit in n_to_string:
            multiplication *= int(digit)
        n_to_string = str(multiplication)
        loop_count += 1
    return loop_count

TEST_CODE_ggebre = '''
result = ggebre_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day16
'''

def recursion(reinforces, airstrikes):    
        
    return loopCount
def vijaya_lakshmi_day16(reinforces, airstrikes):
    firstLetter = ord(chars[0])
    loopCount = 0
    for everyChar in chars:
        if ord(everyChar) is not firstLetter + loopCount:
            return chr(firstLetter + loopCount)
        else:
            loopCount += 1

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day16
'''

def Prashanth_Kadimisetty_day16(reinforces, airstrikes):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day16
'''

def Krzysztof_Blach_day16(reinforces, airstrikes):
    count = 0
    while len(str(reinforces, airstrikes)) > 1:
        count += 1
        mult = 1
        digits = [int(el) for el in str(reinforces, airstrikes)]
        for digit in digits:
            mult = mult * digit
        n = mult
    return count

TEST_CODE_Krzysztof_Blach = '''
result = Krzysztof_Blach_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day16
'''


def Kurt_Hinderer_day16(reinforces, airstrikes):
    for i in range(len(airstrikes)):
        strike_zone = []
        for j in range(len(airstrikes[i])):
            if airstrikes[i][j] == '*':
                if j-1 not in strike_zone and j-1 >= 0:
                    strike_zone.append(j-1)
                if j not in strike_zone:
                    strike_zone.append(j)
                if j+1 not in strike_zone and j+1 < len(reinforces[0]):
                    strike_zone.append(j+1)
        forward_march = ['_'] * len(strike_zone)
        for j in range(len(reinforces)-1, -1, -1):
            for k in range(len(strike_zone)):
                ordered_up = reinforces[j][strike_zone[k]]
                reinforces[j] = reinforces[j][:strike_zone[k]] + forward_march[k] + reinforces[j][strike_zone[k]+1:]
                forward_march[k] = ordered_up
    return reinforces[0]


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day16
'''

def Jose_Catela_day16(reinforces, airstrikes):
    battlefield = list(reinforces[0])
    blim = len(battlefield)-1
    bsize = len(battlefield)
    rsuper = ''
    for pos in range(1,len(reinforces)):
        rsuper += reinforces[pos]
    arsuper = list(rsuper)
    arsupersize = len(rsuper)
    #print(arsuper)
    for index, airstrike in enumerate(airstrikes):
        #print(''.join(battlefield))
        #print(airstrike)
        for pos, bomb in enumerate(airstrike):
            if bomb == '*':
                battlefield[pos] = '_'
                if pos != 0:
                    battlefield[pos-1] = '_'
                if pos != blim:
                    battlefield[pos+1] = '_'
        for pos, soldier in enumerate(battlefield):
            if soldier == '_':
                for posreinf in range(pos, arsupersize, bsize):
                    if arsuper[posreinf] != '_':
                        battlefield[pos] = arsuper[posreinf]
                        arsuper[posreinf] = '_'
                        break
        #print(arsuper)
        #print('///////////////////////////////////////////////')
    return ''.join(battlefield)

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''


Jens_setup = '''
from __main__ import Jens_day16
'''

def Jens_day16(reinforces, airstrikes):
    destruction_count = [0 for i in range(len(reinforces[0]))]
    for strike in airstrikes:
        if len(strike) == 1:
            if strike == '*':
                destruction_count[0] +=1
                destruction_count[1] +=1
        else:
            for i in range(len(strike)):
                if i == 0:
                    if strike[i] == '*' or strike[i+1] == '*':
                        destruction_count[i] +=1
                elif i == len(strike)-1:
                    if strike[i] == '*' or strike[i-1] == '*':
                        destruction_count[i] +=1
                        if len(strike) < len(destruction_count) and strike[i] == '*':
                            destruction_count[i+1] +=1
                else:
                    if strike[i] == '*' or strike[i+1] == '*' or strike[i-1] == '*':
                        destruction_count[i] +=1
    return_string = ''
    for i in range(len(reinforces[0])):
        if destruction_count[i] >= len(reinforces):
            return_string += '_'
        else:
            return_string += reinforces[destruction_count[i]][i]
    return return_string

TEST_CODE_Jens = '''
result = Jens_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

Yang_setup = '''
from __main__ import Yang_day16
'''


def Yang_day16(reinforces, airstrikes):
    ll=[0]*len(reinforces[0])
    for attack in airstrikes: 
        tt = [0]*len(ll)
        for i,x in enumerate(attack): 
            if x =="*": 
                tt[i]+=1 
                if i != len(tt)-1: tt[i+1]+=1
                if i!=0 : tt[i-1]+=1
        #print(tt)
        for i,t in enumerate(tt): 
            if t!=0: ll[i]+=1
        #print(ll)
    s=""
    for i,x in enumerate(ll): 
        try: 
            s += reinforces[x][i]
        except IndexError: 
            s += "_"
    return s

TEST_CODE_Yang = '''
result = Yang_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day16
'''


def Vanessa_G_day16(reinforces, airstrikes):
    alf = "abcdefghijklmnopqrstuvwxyz"
    if chars[0].isupper(): alf = alf.upper()
    first = alf.find(chars[0])
    findIn = set(alf[first : first + len(reinforces, airstrikes)])
    return list(findIn.difference(set(reinforces, airstrikes)))[0]

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day16
'''


def Memo_Hurtado_day16(reinforces, airstrikes):
    alphabet = ('abcdefghijklmnopqrstuvwxyx', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')  [chars[0].isupper()]
    alphaSlice = alphabet[alphabet.find(chars[0]):]
    #print(alphaSlice)
    for i in range(0, len(reinforces, airstrikes)-1):
        if (chars[i] != alphaSlice[i]):
            return alphaSlice[i]
    return alphaSlice[i+1] 

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day16
'''


def Oleksandra_Chmel_day16(reinforces, airstrikes):
    result = reinforces[0]
    reinforces = reinforces[1:]
    reinforces = list(map(list, zip(*reinforces)))
    length = len(result)
    airstrikes = [a+' '*(length-len(a)) for a in airstrikes]
    airstrikes = [el.replace(' *', '**').replace('* ', '**')
                 .replace(' * ', '***') for el in airstrikes]
    def find_all(string, t):
        result = []
        num = 0
        while num < len(string):
            num = string.find(t, num)
            if num == -1:
                return result
            else:
                result.append(num)
                num += 1
        return result
    indices = [find_all(air,'*') for air in airstrikes]
    n = 0
    for ind,elem in enumerate(indices):
        try:
            for e in elem:
                if len(reinforces)==0:
                    result = ''.join([y if x!=e else '_' for x,y in enumerate(result)])
                else:
                    result = [y if x!=e else (reinforces[e][0] if len(reinforces[e])>0 else '_')
                             for x,y in enumerate(result)]
                    reinforces = [y if x!=e else y[1:] for x,y in enumerate(reinforces)]
            n += 1
            if len(reinforces[0]) < n+2: n = 0
        except IndexError:
            continue
    return ''.join(result)


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

sjay_setup = '''
from __main__ import sjay_day16
'''


def sjay_day16(reinforces, airstrikes):
    peaks=[]
    pos=[]
    #print(reinforces, airstrikes)
    for ind,elem in enumerate(reinforces, airstrikes):       
         if(ind > 0 and ind<len(reinforces, airstrikes)-1):
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
result = sjay_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''


charlie_ang_setup = '''
from __main__ import charlie_ang_day16
'''

def charlie_ang_day16(reinforces, airstrikes):
    done = False
    battlefield = [n for n in reinforces[0]]   # init battlefield to first row
    reinforcement_indices = [1] * len(reinforces[0])  # array the size of each reinforces row, initialized to 1
    #print("The battlefield starts    : '{}'".format(reinforces[0]))
    for strike in airstrikes:
        if done:
            break
        # for each airstrike, find the corresponding battlefield index and change to _
        #print("The next airstrike is     : '{}'".format(strike))
        for i,n in enumerate(strike):
            if n == '*':
                battlefield[i] = '_'
                if i + 1 < len(battlefield):
                    battlefield[i+1] = '_'
                if i - 1 >= 0:
                    battlefield[i-1] = '_'
        #print("After the airstrike       : '{}'".format("".join(battlefield)))
        # reinforcement phase
        for i,n in enumerate(battlefield):
            if n == '_':
                next_index = reinforcement_indices[i]
                if next_index < len(reinforces):
                    battlefield[i] = reinforces[next_index][i]
                    reinforcement_indices[i] = next_index + 1
#                else:               
#                   done = True
#                   break
        #if not done:
            #print("Reinforcements are coming : '{}".format("".join(battlefield)))
    return "".join(battlefield)


TEST_CODE_charlie_ang = '''
result = charlie_ang_day16(["g964xxxxxxxx","myjinxin2015","steffenvogel","smile67xxxxx","giacomosorbi","freywarxxxxx","bkaesxxxxxxx","vadimbxxxxxx","zozofouchtra","colbydauphxx"], ["* *** ** ***"," ** * * * **"," * *** * ***"," **  * * ** ","* ** *   ***","***   ","**","*","*" ])
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=10000)) + " seconds")
#print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=10000)) + " seconds")
print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=10000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=10000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=10000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=10000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=10000)) + " seconds")
#print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=10000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=10000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=10000)) + " seconds")
#print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=10000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=10000)) + " seconds")
#print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=10000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
#print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=10000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=10000)) + " seconds")
