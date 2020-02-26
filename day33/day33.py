import timeit


ccquiel_setup = '''
from __main__ import ccquiel_day33
'''

ccquiel_day33 = lambda n: any((all((n % 4 == 0, n % 100)), n % 400==0))

TEST_CODE_ccquiel = '''
result = ccquiel_day33(2000)
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day33
'''

charlie_ang_day33 = lambda n: n % 4 == 0 and (n % 400 == 0 or n % 100 != 0)

TEST_CODE_charlie_ang = '''
result = charlie_ang_day33(2000)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day33
'''

diana_henninger_day33 = lambda n: (n % 4 == 0) and (n % 100 != 0) or (n % 400 == 0)

TEST_CODE_diana_henninger = '''
result = diana_henninger_day33(2000)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day33
'''

Kurt_Hinderer_day33 = lambda n : (n%4 == 0 and n%100 !=0) or n%400==0

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day33(2000)
'''

Navneet_Kumar_setup = '''
from __main__ import Navneet_Kumar_day33
'''

Navneet_Kumar_day33 = lambda n: (n%100!=0 or n%400==0) and n%4==0 

TEST_CODE_Navneet_Kumar = '''
result = Navneet_Kumar_day33(2000)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day33
'''

Oleksandra_Chmel_day33 = lambda n: n % 4 == 0 and not (n % 25 ==0 and n % 200 !=0)

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day33(2000)
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day33
'''

Tushar_Jain_day33 = lambda n: (not n % 100 and not n % 400) or (n % 100 and not n %4)
        
TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day33(2000)
'''

Yang_setup = '''
from __main__ import Yang_day33
'''

Yang_day33 = lambda n: (n%4==0 and n%100==0 and n%400==0) or (n%4==0 and not n%100==0) 
        
TEST_CODE_Yang = '''
result = Yang_day33(2000)
'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Navneet_Kumar test code: " + str(timeit.timeit(stmt=TEST_CODE_Navneet_Kumar, setup=Navneet_Kumar_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
