import timeit
import re
from itertools import combinations


abdiwoli_setup = '''
from __main__ import abdiwoli_day43
'''

def abdiwoli_day43(basket,pile):
	txt = 'The basket weighs {} kilograms'
	pile = pile.replace('dust',' ').split(' ')
	pile = [int(i) for i in pile if i.isnumeric() and int(i) <= basket]
	if sum(pile) <= basket:    return txt.format(sum(pile))
	max = 0
	for i in range(len(pile)+1):
		for h in combinations(pile,i):
			if sum(h) == basket:    return txt.format(basket)
			else:
				if sum(h) > max and sum(h) <= basket:
					max = sum(h)
	return txt.format(max)

TEST_CODE_abdiwoli = '''
result = abdiwoli_day43(50,'dust83dust 45 25 22 46')
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day43
'''

def pack(basket, index, solutions, pile):
    if index == len(pile): return 0
    if solutions[index][basket] != '': return solutions[index][basket]
    coal = pile[index]
    a = pack(basket,index+1, solutions, pile) # without this coal
    b = 0
    if (basket-coal >= 0): b = coal + pack(basket-coal, index+1, solutions, pile) # with this coal
    solutions[index][basket] = max(a,b)
    return solutions[index][basket]

def diana_henninger_day43(basket,pile):
    sentence = 'The basket weighs {} kilograms'
    emptyBasket = sentence.format(0)
    if basket == 0: return emptyBasket # useless basket
    pile = re.sub(r'[dust]{1,}', '', pile)
    pile = re.sub(r'\s{2,}', ' ', pile)
    pile = pile.strip().split(' ')
    if(len(pile)==0): return emptyBasket # no coals
    if(len(pile)==1): # only one coal
        if int(pile[0])<=basket: return sentence.format(pile[0])
        else: return emptyBasket # coal won't fit
    pile = [int(x) for x in pile if int(x) <= basket]
    solutions = [['' for y in range(basket+1)] for x in range(len(pile))]
    solution = pack(basket, 0, solutions, pile)
    return sentence.format(solution)

TEST_CODE_diana_henninger = '''
result = diana_henninger_day43(50,'dust83dust 45 25 22 46')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day43
'''

def Oleksandra_Chmel_day43(basket,pile):
    pile = [int(p) for p in pile.replace('dust','').split() if int(p)<= basket]
    def max_sum(pile,basket):
        s = 0
        for i in range(len(pile)+1):
            for seq in combinations(pile, i):
                if sum(seq) == basket: return basket
                elif sum(seq) > s and sum(seq) <= basket: s = sum(seq)
        return s
    maximum = 0
    if sum(pile) <= basket: maximum = sum(pile)
    elif len(pile) > 1: maximum = max_sum(pile,basket)
    return 'The basket weighs {} kilograms'.format(maximum)   

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day43(50,'dust83dust 45 25 22 46')
'''

Omar_B_setup = '''
from __main__ import Omar_B_day43
'''

def max_sum(l,basket):
    s=0
    for ind in range(1,len(l)+1):
        for subset in combinations(l,ind):
            if sum(subset) == basket: return basket
            elif s< sum(subset) and sum(subset)<= basket:
                s=sum(subset)
    return s

def Omar_B_day43(basket,pile):
    l = [ ]
    for d in pile.split():
        a= d.replace('dust','')
        if  (a != '') and (int(a)<= basket) :
            l.append(int(a))
    if l==[]:
        weight=0
    elif len(l)==1:
        weight=l[0]
    else: 
        weight = max_sum(l,basket)
    return 'The basket weighs {} kilograms'.format(weight)

TEST_CODE_Omar_B = '''
result = Omar_B_day43(50,'dust83dust 45 25 22 46')
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day43
'''

def Tushar_Jain_day43(basket,pile):
    contents = sorted([int(x) for x in pile.replace('dust', ' ').split() if x.isdigit() and int(x) <= basket])
    maxsum = 0
    for num in range(len(contents) + 1):
        for possible in combinations(contents, num):
            if not len(possible):
                continue
            newsum = sum(possible)
            if newsum == basket:
                return 'The basket weighs {} kilograms'.format(basket)
            elif newsum > maxsum and newsum < basket:
                maxsum = newsum
    return 'The basket weighs {} kilograms'.format(maxsum)

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day43(50,'dust83dust 45 25 22 46')
'''

print("Time for abdiwoli test code: " + str(timeit.timeit(stmt=TEST_CODE_abdiwoli, setup=abdiwoli_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Omar_B test code: " + str(timeit.timeit(stmt=TEST_CODE_Omar_B, setup=Omar_B_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
