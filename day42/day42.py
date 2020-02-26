import timeit


abdiwoli_setup = '''
from __main__ import abdiwoli_day42
'''

def abdiwoli_day42(cost,box):
	box = box.split(' ')
	mn,me = box.count('mon'),box.count('monme')
	t,pme,= (mn*1) + (me*60),min(cost//60,me)
	pmn = min(cost-pme*60,mn)
	mon = [mn,me,t,pmn + pme]
	if pme *60 + pmn != cost:    return 'leaving the market'
	return mon

TEST_CODE_abdiwoli = '''
result = abdiwoli_day42(122,'monme mon mon monme')
'''

akash_karan_setup = '''
from __main__ import akash_karan_day42
'''

def akash_karan_day42(cost, box):
    b=box.split(" ")
    one=b.count("mon")
    two=b.count("monme")
    value=one+two*60
    if(cost<=value):
        if(cost<60 and cost<one):
            return [one,two,value,cost]
        elif(cost>60):
            sec=cost//60
            fir=cost%60
            if sec>two:
                fir=fir+(sec-two)*60
                sec=two
                if fir>one:
                    return'leaving the market'
            return [one,two,value,fir+sec]
    return 'leaving the market'

TEST_CODE_akash_karan = '''
result = akash_karan_day42(122,'monme mon mon monme')
'''

ccquiel_setup = '''
from __main__ import ccquiel_day42
'''

def ccquiel_day42(cost, box):
    mon = 0
    monme = 0
    for c in box.split(' '):
        if c == 'mon': mon += 1
        elif c == 'monme': monme += 1
    due_monme = cost // 60
    pay_monme = due_monme if due_monme < monme else monme
    pay_mon = cost - pay_monme*60
    if pay_mon > mon:
        return 'leaving the market'
    return [mon, monme, (mon + monme*60), pay_monme + pay_mon]

TEST_CODE_ccquiel = '''
result = ccquiel_day42(122,'monme mon mon monme')
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day42
'''

def diana_henninger_day42(cost, box):
    mon_c = box.count('mon')
    monme_c = box.count('monme')
    mon_c -= monme_c
    solution = [mon_c, monme_c, monme_c*60+mon_c]
    count = 0
    while cost > 0:
        if cost >= 60 and monme_c > 0:
            cost -= 60
            monme_c -= 1
            count += 1
        elif mon_c > 0:
            cost -= 1
            mon_c -=1
            count += 1
        else: return "leaving the market"
    solution.append(count)
    return solution

TEST_CODE_diana_henninger = '''
result = diana_henninger_day42(122,'monme mon mon monme')
'''

Jens_setup = '''
from __main__ import Jens_day42
'''

def Jens_day42(cost, box):
    box = box.split()
    mon, monme = box.count('mon'), box.count('monme')
    value = mon + 60*monme
    if cost > value:
        return 'leaving the market'
    else:
        coins = monme if monme <= cost//60 else cost//60
        rest_cost = cost - 60*coins
        if mon < rest_cost:
            return 'leaving the market'
        else:
            return [mon, monme, value, coins+rest_cost]    

TEST_CODE_Jens = '''
result = Jens_day42(122,'monme mon mon monme')
'''

Navneet_Kumar_setup = '''
from __main__ import Navneet_Kumar_day42
'''

def Navneet_Kumar_day42(cost, box):
    box = box.split(" ")
    mon = box.count('mon')
    monme = box.count('monme')
    n1=0
    n2=0
    if (monme*60+mon<cost):
        return "leaving the market"
    else:
        n1 = cost//60
        if (n1<= monme):
            n2 = cost-60*n1
        else:
            n1=monme
            n2 = cost-60*n1
        if (n2>mon):
            return 'leaving the market'    
    return [mon, monme, monme*60+mon, n1+n2]   

TEST_CODE_Navneet_Kumar = '''
result = Navneet_Kumar_day42(122,'monme mon mon monme')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day42
'''

def Oleksandra_Chmel_day42(cost, box):
    monme = box.count('monme')
    box = box.replace('monme','')
    mon = box.count('mon')
    summ = mon + monme*60
    coins = 0
    if monme >= cost//60 and mon >= cost%60: coins = cost//60 + cost%60
    elif mon >= (cost//60 - monme)*60 + cost%60: coins = monme + (cost//60-monme)*60 + cost%60
    return [mon,monme,summ,coins] if coins>0 else 'leaving the market'   

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day42(122,'monme mon mon monme')
'''

Omar_B_setup = '''
from __main__ import Omar_B_day42
'''

def Omar_B_day42(cost, box):
    l = box.split()
    c_mon=0
    c_monme=0
    for elt in l : 
        if elt=='mon':
            c_mon+=1
        if elt =='monme':
            c_monme+=1
    value = c_mon + 60 * c_monme
    if value < cost:
        return 'leaving the market'
    else : 
        n_coins = 0
        c = cost
        a,b = c_mon, c_monme
        while (c > 0) and ((a>0 and c>=1) or (b>0 and c>=60)) : 
            if (b>0) and (c-60>=0):
                c-=60
                n_coins+=1
                b-=1
            elif (a>0) and (c-1>=0):
                c-=1
                n_coins+=1
                a-=1
        if c == 0 : 
            return [c_mon, c_monme, value, n_coins]
        else :
            return 'leaving the market'

TEST_CODE_Omar_B = '''
result = Omar_B_day42(122,'monme mon mon monme')
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day42
'''

def Tushar_Jain_day42(cost, box):
    price = [1, 60]
    result = [box.count('monme')]
    result.insert(0, box.count('mon') - result[0])
    result.append(sum((p*c for (p, c) in zip(price, result))))
    count_monme = result[1] if cost // price[1] > result[1] else cost // price[1]
    cost -= price[1] * count_monme
    if result[0] < cost:
        return 'leaving the market'
    result.append(count_monme + cost)
    return result

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day42(122,'monme mon mon monme')
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day42
'''

def Vanessa_G_day42(cost, box):
    box = box.split(' ')
    mon, monme = box.count('mon'), box.count('monme')
    pay_monme = min(cost // 60, monme)
    pay_mon = min(cost - pay_monme * 60, mon)
    if pay_monme * 60 + pay_mon != cost: return 'leaving the market'
    else: return [mon, monme, monme * 60 + mon, pay_monme + pay_mon]

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day42(122,'monme mon mon monme')
'''

Yang_setup = '''
from __main__ import Yang_day42
'''

def Yang_day42(cost, box):
    mon,monme = 0,0
    for x in box.split(): 
        if x == 'mon': mon+=1 
        elif x == 'monme': monme+=1 
    pay60 = min(cost//60,monme) 
    pay1 = min(cost-pay60*60,mon) 
    if pay60*60+pay1 != cost: 
        return 'leaving the market'
    return [mon,monme,mon+monme*60,pay60+pay1]

TEST_CODE_Yang = '''
result = Yang_day42(122,'monme mon mon monme')
'''

print("Time for abdiwoli test code: " + str(timeit.timeit(stmt=TEST_CODE_abdiwoli, setup=abdiwoli_setup, number=100000)) + " seconds")
print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Navneet_Kumar test code: " + str(timeit.timeit(stmt=TEST_CODE_Navneet_Kumar, setup=Navneet_Kumar_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Omar_B test code: " + str(timeit.timeit(stmt=TEST_CODE_Omar_B, setup=Omar_B_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
