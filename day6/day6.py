import timeit

killian_setup = '''
from __main__ import killian_day5
'''

def killian_day5(customers, n):
    checkout = [0] * n
    for customer in customers:
        checkout[checkout.index(min(checkout))] += customer
    return max(checkout)

TEST_CODE_killian = '''
result = killian_day5([2,3,10], 2)
'''

ccquiel_setup = '''
from __main__ import ccquiel_day5
'''

def ccquiel_day5(customers, n):
    # Special cases
    if not customers:
        return 0
    if len(customers) <= n:
        return max(customers)
    # General case
    tills = [0] * n
    for customer in customers:
        tills[tills.index(min(tills))] += customer
    return max(tills)

TEST_CODE_ccquiel = '''
result = ccquiel_day5([2,3,10], 2)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day5
'''

def diana_henninger_day5(customers, n):
    # if only one till, then it's just the sum
    if n == 1: return sum(customers)
    # if there are more tills than customers, it's the max checkout time
    if n > len(customers): return max(customers)
    time = 0
    # serve the first n (# of tills) customers
    served = customers[0:n]
    customers = customers[n:]
    while len(served) > 0:
        # the customer with the shortest check out
        # ...time finishes first
        shortest = min(served)
        time += shortest
        # subtract time from the others at the tills
        served = [x - shortest for x in served]
        # remove customers that are finished
        served.remove(0)
        # fill up tills with new customers
        while len(served) < n and len(customers) > 0:
            served.append(customers.pop(0))
    return time

TEST_CODE_diana_henninger = '''
result = diana_henninger_day5([2,3,10], 2)
'''

ggebre_setup = '''
from __main__ import ggebre_day5
'''

def ggebre_day5(customers, n):
    total_time = 0
    tills = [0 for index in range(n)]
    if len(customers) <= n and len(customers) != 0:
        total_time = max(customers)
    elif n == 1:
        total_time = sum(customers)
    else:
        # checks for the next till to be taken by evaluating the minimum
        # time at the tills
        count = 0
        while count < len(customers):
            min_index = tills.index(min(tills))
            tills[min_index] += customers[count]
            count += 1
        total_time = max(tills)
    return total_time

TEST_CODE_ggebre = '''
result = ggebre_day5([2,3,10], 2)
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day5
'''

def vijaya_lakshmi_day5(customers, n):
    return min(available[key] // recipe[key] if key in available else 0 for key in recipe)

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day5([2,3,10], 2)
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day5
'''

def Prashanth_Kadimisetty_day5(customers, n):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day5([2,3,10], 2)
'''

David_Nugent_setup = '''
from __main__ import David_Nugent_day5
'''

def David_Nugent_day5(customers, n):
    return min(available.get(k, 0) // recipe[k] for k in recipe)

TEST_CODE_David_Nugent = '''
result = David_Nugent_day5([2,3,10], 2)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day5
'''


def Kurt_Hinderer_day5(customers, n):
    ##get a list for the time of each time
    checkout_tills = [0] * n
    #go through the customer list and add it to the till w/ minimum time
    #then add that time to that till
    for customer in customers:
        checkout_tills[checkout_tills.index(min(checkout_tills))] += customer
    #return the till with the largest time.
    return max(checkout_tills)


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day5([2,3,10], 2)
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day5
'''


def Jose_Catela_day5(customers, n):
    time_elapsed = 0  # initialize time
    tills = []
    for till in range(0, n):  # initialize tills
        tills.append(0)
    while customers:
        for i, till in enumerate(tills):  # assign customers to empty tills
            if customers and till == 0:
                customer = customers.pop(0)
                tills[i] = customer
        time_elapsed += 1  # time passes
        for i, till in enumerate(tills):
            tills[i] -= 1
    return time_elapsed + max(tills)  # when there are no more customers, we need to wait for the slower one

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day5([2,3,10], 2)
'''

Yang_setup = '''
from __main__ import Yang_day5
'''


def Yang_day5(customers, n):
    if len(customers) <= n: return max(customers, default=0)  # without this line it would still work
    qq = [0] * (n)
    for x in customers: qq[qq.index(min(qq))] += x
    return max(qq)

TEST_CODE_Yang = '''
result = Yang_day5([2,3,10], 2)
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day5
'''


def Vanessa_G_day5(customers, n):
    q = [0] * n
    for c in customers: q[q.index(min(q))] += c
    return max(q)

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day5([2,3,10], 2)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day5
'''


def Oleksandra_Chmel_day5(customers, n):
    people = len(customers)
    tills = [0] * n
    if people == 0:
        return 0
    elif n == 1:
        return sum(customers)
    elif people <= n:
        return max(customers)
    else:
        for i in customers:
            tills[0] += i
            tills.sort()
        return max(tills)


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day5([2,3,10], 2)
'''

sjay_setup = '''
from __main__ import sjay_day5
'''


def sjay_day5(customers, n):
    if (len(customers) > 0):
        till = []
        valnow = customers[0]
        toadd = 0
        maxval = 0
        for ind in range(len(customers)):
            #print(ind % 3, customers[ind])
            if (ind < n):
                till.insert(ind, [customers[ind]])
            else:
                for num in range(n):
                    valnow = sum(till[toadd])
                    if sum(till[num]) < valnow:
                        #print("current value is " + str(sum(till[num])))
                        valnow = sum(till[num])
                        toadd = num
                #print("min is " + str(till[toadd]))
                # till[ind%3].append(customers[ind])
                till[toadd].append(customers[ind])
        #print(till)
        for line in till:
            if sum(line) > maxval:
                maxval = sum(line)
        #print(str(maxval))
        return maxval
    else:
        #print(str(0))
        return 0


TEST_CODE_sjay = '''
result = sjay_day5([2,3,10], 2)
'''

print("Time for killian test code: " + str(timeit.timeit(stmt=TEST_CODE_killian, setup=killian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
#print("Time for David_Nugent test code: " + str(timeit.timeit(stmt=TEST_CODE_David_Nugent, setup=David_Nugent_setup, number=100000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
