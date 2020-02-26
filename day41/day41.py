import timeit
from itertools import chain


abdiwoli_setup = '''
from __main__ import abdiwoli_day41
'''

def abdiwoli_day41(n):
	n = [i for i in n if i != [0,0] and i != [] ]
	for i in range(len(n)):
		if 0 in n[i]:
			c = i+1
			try:
				for h in n[i+1:]:
					if 0 in h:
						a = [n[i],h]
						n[i] = list(i for i in (chain.from_iterable(a)) if i != 0)
						n.remove(h)
						n.append(['x'])
						break
			except IndexError:    print(h,2)
	n = [i for i in n if i != ['x'] and 0 not in i]
	return n

TEST_CODE_abdiwoli = '''
result = abdiwoli_day41([[0, 0], [3, 7], [0, 5]])
'''

akash_karan_setup = '''
from __main__ import akash_karan_day41
'''

def akash_karan_day41(apples):
    l=[0, 0]
    li=[]
    ct=0
    for i in apples:
        if l == i :
            continue
        elif 0 in i:
            i.remove(0)
            ct+=1
            if(ct%2!=0):
                temp=i
            if(ct%2==0):
                temp.append(i[0])
                continue
        li.append(i)
    return [x for x in li if len(x)==2 ]

TEST_CODE_akash_karan = '''
result = akash_karan_day41([[0, 0], [3, 7], [0, 5]])
'''

ccquiel_setup = '''
from __main__ import ccquiel_day41
'''

def ccquiel_day41(apples):
    temp = None
    good_apples = list()
    for apple in apples:
        if 0 not in apple:
            good_apples.append(apple)
        else:
            if apple == [0, 0]: continue
            if temp:
                tapple = temp
                tapple.pop(tapple.index(0))
                tapple.append(apple[not apple.index(0)])
                temp = None
            else:
                temp = apple
                good_apples.append(apple)
                temp_index = good_apples.index(apple)
    if temp:
        del good_apples[temp_index]
    return good_apples

TEST_CODE_ccquiel = '''
result = ccquiel_day41([[0, 0], [3, 7], [0, 5]])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day41
'''

def diana_henninger_day41(apples):
    bad_package = None
    i = 0
    while i < len(apples):
        apples[i] = [x for x in apples[i] if x!=0] # remove bad apples
        if len(apples[i])==0: # if package is empty..
            del apples[i] # ..remove package
            i -=1
        elif len(apples[i])==1: # if there is only one good apple..
            if bad_package != None: # ..add to another package
                apples[bad_package].append(apples[i][0])
                del apples[i]
                i -= 1
                bad_package = None
            else: bad_package = i # ..else remember bad package
        i += 1
    if bad_package!=None: del apples[bad_package] # remove leftover bad package
    return apples

TEST_CODE_diana_henninger = '''
result = diana_henninger_day41([[0, 0], [3, 7], [0, 5]])
'''

Jens_setup = '''
from __main__ import Jens_day41
'''

def Jens_day41(apples):
    selected_apples = []
    for i in range(len(apples)):
        if apples[i] == [0, 0]:
            continue
        elif apples[i].count(0) == 1:
            if i < len(apples)-1:
                for n in range(i+1, len(apples)):
                    if apples[n].count(0) == 1:
                        if apples[i][0] == 0:
                            apples[i][0] = apples[i][1]
                        apples[i][1] = apples[n][0] if apples[n][1] == 0 else apples[n][1]
                        apples[n] = [0, 0]
                        selected_apples.append(apples[i])
                        break
        else:    
            selected_apples.append(apples[i])
    return selected_apples     

TEST_CODE_Jens = '''
result = Jens_day41([[0, 0], [3, 7], [0, 5]])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day41
'''

def Oleksandra_Chmel_day41(apples):
    good_apples, one_two, count, index = [], 0, 0, 0
    for apple in apples:
        if apple == [0,0]: continue
        elif 0 not in apple: good_apples.append(apple); index += 1
        else:
            apple.remove(0)
            if one_two == 0:
                good_apples.append(apple)
                one_two = 1
                index += 1
                count = index
            else:
                good_apples[count-1].append(apple[0])
                one_two = 0
    return [i for i in good_apples if len(i) == 2]    

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day41([[0, 0], [3, 7], [0, 5]])
'''

Omar_B_setup = '''
from __main__ import Omar_B_day41
'''

def Omar_B_day41(apples):
    repack=[]
    output=[]
    index_bad_apple=-1
    for i,elt in enumerate(apples):
        if (0 in elt) and (elt !=[0,0]) and (i != index_bad_apple) : 
            if elt[0] != 0 :
                repack.append(elt[0])
            else :
                repack.append(elt[1])
            i+=1
            while i<len(apples): 
                if (0 in apples[i]) and apples[i]!=[0,0] : 
                    index_bad_apple=i 
                    if apples[i][0]!=0 : 
                        repack.append(apples[i][0])
                    else : 
                        repack.append(apples[i][1])
                    output.append(repack)
                    repack=[]
                    break
                i+=1
        elif 0 not in elt :
            output.append(elt)
    return output

TEST_CODE_Omar_B = '''
result = Omar_B_day41([[0, 0], [3, 7], [0, 5]])
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day41
'''

def Tushar_Jain_day41(apples):
    indices = [sum(pack) for pack in apples
               if sum(pack) != 0 and (pack[0] == 0 or pack[1] == 0)]
    result = []
    lose = False
    for apple in apples:
        if apple[0] != 0 and apple[1] != 0:
            result.append(apple)
        elif (len(indices) > 1 and
              (apple[0] != 0 or apple[1] != 0)):
            if not lose:
                result.append([indices.pop(0), indices.pop(0)])
            lose = not lose
    return result

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day41([[0, 0], [3, 7], [0, 5]])
'''

Yang_setup = '''
from __main__ import Yang_day41
'''

def Yang_day41(apples): 
    idx,salv,good = [],[],[] 
    for i,box in enumerate(apples): 
        if box.count(0)==1: 
            idx.append(i) 
            salv.append(box[1] if box[0]==0 else box[0]) 
            good.append(None) 
        elif box.count(0)==0: 
            good.append(box)
        else: 
            good.append(None)
    while len(salv)>1: 
        good[idx[0]] = [salv[0],salv[1]] 
        idx = idx[2:]
        salv = salv[2:]
    return [x for x in good if x]

TEST_CODE_Yang = '''
result = Yang_day41([[0, 0], [3, 7], [0, 5]])
'''

print("Time for abdiwoli test code: " + str(timeit.timeit(stmt=TEST_CODE_abdiwoli, setup=abdiwoli_setup, number=100000)) + " seconds")
print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Omar_B test code: " + str(timeit.timeit(stmt=TEST_CODE_Omar_B, setup=Omar_B_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
