import timeit
import random
from collections import Counter

def one_two():
    return random.randrange(1,3)

# Basic Test
'''
length = 60000
treshold = 0.05
count = Counter(one_two_three() for _ in range(length)) # past here student's function

print(1 in count, '1 is present')
print(2 in count, '2 is present')
print(3 in count, '3 is present')
print(abs(count[1] / length - 1 / 3) < treshold, '1 count is nearly equal 1/3')
print(abs(count[2] / length - 1 / 3) < treshold, '2 count is nearly equal 1/3')
print(abs(count[3] / length - 1 / 3) < treshold, '3 count is nearly equal 1/3')
'''

ccquiel_setup = '''
from __main__ import ccquiel_day30
'''

def ccquiel_day30():
    t = one_two() + one_two()
    if t == 2: return 1
    if t == 4: return 2
    if t == 3:
        if one_two() == 1: return 3
        else: return ccquiel_day30()

TEST_CODE_ccquiel = '''
result = ccquiel_day30()
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day30
'''

def diana_henninger_day30():
    if one_two()==1:
        if one_two()==1: return 1
        else: return 2
    else:
        if one_two()== 1: return 3
        else: return diana_henninger_day30()

TEST_CODE_diana_henninger = '''
result = diana_henninger_day30()
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day30
'''

def Kurt_Hinderer_day30():
    repeat = False
    while not repeat:
        if one_two() == 1:
            if one_two() == 1:
                return 1
            else:
                return 2
        else:
            if one_two() == 1:
                return 3

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day30()
'''

Jens_setup = '''
from __main__ import Jens_day30
'''

def Jens_day30():
    while True:
        r_list = [i for i in range(1, 4) if one_two() == 1]
        if len(r_list) == 1:
            return r_list[0]
        elif len(r_list) == 2:
            return r_list[0] if one_two() == 1 else r_list[1]

TEST_CODE_Jens = '''
result = Jens_day30()
'''

Yang_setup = '''
from __main__ import Yang_day30
'''

def Yang_day30(): 
    a,b = one_two(),one_two()+1
    if a*b==4: 
        return 1 
    elif a*b<4: 
        return a*b
    else: 
        return Yang_day30() 

TEST_CODE_Yang = '''
result = Yang_day30()
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day30
'''

def Oleksandra_Chmel_day30():
    one = one_two()
    two = one_two()
    if one == 1 and two == 1:
        return 1
    if one == 2 and two == 2:
        return 2
    if one == 2 and two == 1:
        return 3
    return Oleksandra_Chmel_day30()

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day30()
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day30
'''

def charlie_ang_day30():
    while True:
        if one_two() == 1:
            return one_two()
        elif one_two() == 1:
            return 3

TEST_CODE_charlie_ang = '''
result = charlie_ang_day30()
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day30
'''

def Tushar_Jain_day30():
    while True:
        if one_two() == 1:
            return one_two()
        elif one_two() == 1:
            return 3

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day30()
'''

#print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=10000)) + " seconds")
#print("Time for akash_agarwal test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_agarwal, setup=akash_agarwal_setup, number=10000)) + " seconds")
#print("Time for Samrat_Mukherjee test code: " + str(timeit.timeit(stmt=TEST_CODE_Samrat_Mukherjee, setup=Samrat_Mukherjee_setup, number=10000)) + " seconds")
#print("Time for kilian test code: " + str(timeit.timeit(stmt=TEST_CODE_kilian, setup=kilian_setup, number=10000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=10000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=10000)) + " seconds")
#print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=10000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
#print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=10000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
#print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=10000)) + " seconds")
#print("Time for Daniel_Ruiz test code: " + str(timeit.timeit(stmt=TEST_CODE_Daniel_Ruiz, setup=Daniel_Ruiz_setup, number=10000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
#print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=10000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
