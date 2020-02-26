import timeit


ccquiel_setup = '''
from __main__ import ccquiel_day32
'''

def ccquiel_day32(year):
    while True:
        year += 1
        ys = str(year)
        if len(set(ys)) == len(ys):
            return year

TEST_CODE_ccquiel = '''
result = ccquiel_day32(1987)
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day32
'''

def charlie_ang_day32(year):
    check = set()
    while len(check) != 4:
        year += 1
        check.clear()
        check.update(str(year))
    return year

TEST_CODE_charlie_ang = '''
result = charlie_ang_day32(1987)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day32
'''

def diana_henninger_day32(year):
    happy_year = False
    while not happy_year:
        year += 1
        if len(set(str(year))) == 4: return year

TEST_CODE_diana_henninger = '''
result = diana_henninger_day32(1987)
'''

Jens_setup = '''
from __main__ import Jens_day32
'''

def Jens_day32(year):
    while True:
        year += 1
        if (str(year)[0] not in str(year)[1:] and 
            str(year)[1] not in str(year)[2:] and 
            str(year)[2] != str(year)[3]):
            return year

TEST_CODE_Jens = '''
result = Jens_day32(1987)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day32
'''

def Kurt_Hinderer_day32(year):
    unhappy = True
    while unhappy:
        year += 1
        year_str = str(year)
        unhappy = False
        for i in range(len(year_str) - 1):
            for j in range(i+1, len(year_str)):
                unhappy = unhappy or year_str[i] == year_str[j]
    return year

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day32(1987)
'''

Navneet_Kumar_setup = '''
from __main__ import Navneet_Kumar_day32
'''

def check_unique(year):
    unique_array= [False]*10
    while (year):
        if (unique_array[year%10] == True):
            return False
        unique_array[year%10] = True
        year = year//10
    return True

def Navneet_Kumar_day32(year):
    year+=1
    while not check_unique(year) :
        year+=1
    return year 

TEST_CODE_Navneet_Kumar = '''
result = Navneet_Kumar_day32(1987)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day32
'''

def Oleksandra_Chmel_day32(year):
    for i in range(year+1,10000):
        if len(set(str(i))) == 4:
            return i

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day32(1987)
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day32
'''

def Tushar_Jain_day32(year):
    for i in range(year + 1, 9013):
        if len(set(str(i))) == 4:
            return i

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day32(1987)
'''

Viji_setup = '''
from __main__ import Viji_day32
'''

def Viji_day32(year):
    #your code here
    return_year = ''
    while True:
        year_found = False
        year = year + 1
        str_year =  str(year)
        for index, y in enumerate(str_year):
            occurences = str_year.count(y)
            # print(y)
            if occurences > 1:      
                break      
            if index == 3 and occurences == 1:
                year_found = True
        if year_found == True:
            return_year = str_year
            break
    return int(return_year)

TEST_CODE_Viji = '''
result = Viji_day32(1987)
'''

Yang_setup = '''
from __main__ import Yang_day32
'''

def Yang_day32(year): 
    year +=1 
    while len(set(str(year)))!=4: 
        year+=1 
    return year 

TEST_CODE_Yang = '''
result = Yang_day32(1987)
'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Navneet_Kumar test code: " + str(timeit.timeit(stmt=TEST_CODE_Navneet_Kumar, setup=Navneet_Kumar_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Viji test code: " + str(timeit.timeit(stmt=TEST_CODE_Viji, setup=Viji_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
