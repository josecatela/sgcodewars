import timeit
from functools import reduce

MORSE_CODE ={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

killian_setup = '''
from __main__ import killian_day12
'''

def killian_day12(n):
    if n < 0:
        return 0
    i = 0
    while n > 9:
        tmp = 1
        while n > 0:
            tmp *= (n % 10)
            n //= 10
        n = tmp
        i += 1
    return i

TEST_CODE_killian = '''
result = killian_day12(39)
'''

akash_karan_setup = '''
from __main__ import akash_karan_day12
'''

def akash_karan_day12(n):
    ct=0
    while(n%10!=n):
        m=1
        for i in str(n):
            m*=int(i)
        n=m
        ct+=1
    return ct

TEST_CODE_akash_karan = '''
result = akash_karan_day12(39)
'''

ccquiel_setup = '''
from __main__ import ccquiel_day12
'''

def ccquiel_day12(n):
    n = str(n)
    times = 0
    while len(n) > 1:
        m = 1
        for i in n:
            m *= int(i)
        n = str(m)
        times += 1
    return times

TEST_CODE_ccquiel = '''
result = ccquiel_day12(39)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day12
'''

def diana_henninger_day12(n):
    count = 0
    n = str(n)
    while len(n) != 1:
        prod = 1
        for i in range(len(n)):
            prod *= int(n[i])
        n = str(prod)
        count +=1
    return count

TEST_CODE_diana_henninger = '''
result = diana_henninger_day12(39)
'''

ggebre_setup = '''
from __main__ import ggebre_day12
'''

def ggebre_day12(n):
    n_to_string = [digit for digit in str(n)]
    loop_count = 0
    while len(n_to_string) > 1:
        multiplication = 1
        for digit in n_to_string:
            multiplication *= int(digit)
        n_to_string = str(multiplication)
        loop_count += 1
    return loop_count

TEST_CODE_ggebre = '''
result = ggebre_day12(39)
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day12
'''

def recursion(n):    
    res = [int(x) for x in str(n)]   
    total = reduce((lambda x, y: x * y), res)
    loopCount = 1
    while total >= 10:    
        tot = [int(x) for x in str(total)]   
        total = reduce((lambda x, y: x * y), tot)
        loopCount += 1
        
    return loopCount
def vijaya_lakshmi_day12(n):
    # your code
    if(len(str(n)) < 2):
        return 0
    else:
        return recursion(n)

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day12(39)
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day12
'''

def Prashanth_Kadimisetty_day12(n):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day12(39)
'''

Krzysztof_Blach_setup = '''
from __main__ import Krzysztof_Blach_day12
'''

def Krzysztof_Blach_day12(n):
    count = 0
    while len(str(n)) > 1:
        count += 1
        mult = 1
        digits = [int(el) for el in str(n)]
        for digit in digits:
            mult = mult * digit
        n = mult
    return count

TEST_CODE_Krzysztof_Blach = '''
result = Krzysztof_Blach_day12(39)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day12
'''


def Kurt_Hinderer_day12(n):
    #initialize the persistance
    pers = 0
    #while the number is still multidigits
    #find the digits and then multiply them.
    while n >= 10:
        n_string = str(n)
        #like sigma is used in summations, a capitol pi is use for multipliation
        pi = [int(n_string[i]) for i in range(len(n_string))]
        n = 1
        for i in range(len(pi)):
            n *= pi[i]
        pers +=1
    return(pers)


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day12(39)
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day12
'''

def Jose_Catela_day12(n):
    numstr = str(n)
    times = 0
    while len(numstr) > 1:
        newnum = 1
        for letter in numstr:
            newnum *= int(letter)
        numstr = str(newnum)
        times += 1
    return times

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day12(39)
'''

Yang_setup = '''
from __main__ import Yang_day12
'''


def Yang_day12(n):
    count = 0 
    while n>9: 
        n = reduce(lambda x,y:int(x)*int(y), str(n))
        count +=1 
    return count

TEST_CODE_Yang = '''
result = Yang_day12(39)
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day12
'''


def Vanessa_G_day12(n):
    count = 0
    while n >= 10:
        n = reduce(lambda x, y: x * y, [int(x) for x in str(n)])
        count += 1
    return count

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day12(39)
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day12
'''


def Memo_Hurtado_day12(n):
    if (n<10):
      return 0;
    string = str(n)
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
result = Memo_Hurtado_day12(39)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day12
'''


def Oleksandra_Chmel_day12(n):
    def multy(num):
        product = 1
        while num > 0:
            product *= num%10
            num = num//10
        return product
    count = 0
    while n > 9:
        n = multy(n)
        count += 1
    return count


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day12(39)
'''

sjay_setup = '''
from __main__ import sjay_day12
'''


def sjay_day12(n):
    ctr=0
    while len(str(n)) > 1:
        prod=1
        for i in range(len(str(n))):
            prod = prod * int(str(n)[i])
        n = prod
        ctr = ctr + 1
    return ctr


TEST_CODE_sjay = '''
result = sjay_day12(39)
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for killian test code: " + str(timeit.timeit(stmt=TEST_CODE_killian, setup=killian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
print("Time for Krzysztof_Blach test code: " + str(timeit.timeit(stmt=TEST_CODE_Krzysztof_Blach, setup=Krzysztof_Blach_setup, number=100000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
