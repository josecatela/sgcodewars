import timeit

killian_setup = '''
from __main__ import killian_day8
'''

def killian_day8(roman):
    checkout = [0] * n
    for customer in customers:
        checkout[checkout.index(min(checkout))] += customer
    return max(checkout)

TEST_CODE_killian = '''
result = killian_day8('MCMXIV')
'''

akash_karan_setup = '''
from __main__ import akash_karan_day8
'''

def akash_karan_day8(roman):
    di = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    c = 1001
    for i in roman:
        if (di[i] <= c):
            s += di[i]
        else:
            s = s + di[i] - 2 * c
        c = di[i]
    return s

TEST_CODE_akash_karan = '''
result = akash_karan_day8('MCMXIV')
'''

ccquiel_setup = '''
from __main__ import ccquiel_day8
'''

rom_num = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
def ccquiel_day8(roman):
    num = 0
    prev = 1000
    for s in roman:
        num += rom_num[s]
        if prev < rom_num[s]:
            num -= 2*prev
        prev = rom_num[s]
    return num

TEST_CODE_ccquiel = '''
result = ccquiel_day8('MCMXIV')
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day8
'''

def diana_henninger_day8(roman):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    length = len(roman)
    for i in range(length):
        curr = romans[roman[i]]
        if (i + 1 < length and romans[roman[i + 1]] > curr):
            sum -= curr
        else:
            sum += curr
    return sum

TEST_CODE_diana_henninger = '''
result = diana_henninger_day8('MCMXIV')
'''

ggebre_setup = '''
from __main__ import ggebre_day8
'''

def ggebre_day8(roman):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M': 1000, 'D': 500}
    roman_specials = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    roman_specials_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    number = 0
    # the roman special case values are filtered from the input roman numeral
    filtered_input = [roman_special for roman_special in roman_specials if roman_special in roman]
    # input is copied
    input_less_specials = roman
    # checks if there are any special cases in the input and if there is, then the
    # for loop goes through and calculate their sum
    if len(filtered_input) != 0:
        for x in filtered_input:
            input_less_specials = input_less_specials.replace(x, '')
            number += roman_specials_dict[x]
    for x in input_less_specials:
        number += dict[x]
    return number

TEST_CODE_ggebre = '''
result = ggebre_day8('MCMXIV')
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day8
'''

def vijaya_lakshmi_day8(roman):
    return min(available[key] // recipe[key] if key in available else 0 for key in recipe)

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day8('MCMXIV')
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day8
'''

def Prashanth_Kadimisetty_day8(roman):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day8('MCMXIV')
'''

David_Nugent_setup = '''
from __main__ import David_Nugent_day8
'''

def David_Nugent_day8(roman):
    return min(available.get(k, 0) // recipe[k] for k in recipe)

TEST_CODE_David_Nugent = '''
result = David_Nugent_day8('MCMXIV')
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day8
'''


def Kurt_Hinderer_day8(roman):
    ##get a list for the time of each time
    checkout_tills = [0] * n
    #go through the customer list and add it to the till w/ minimum time
    #then add that time to that till
    for customer in customers:
        checkout_tills[checkout_tills.index(min(checkout_tills))] += customer
    #return the till with the largest time.
    return max(checkout_tills)


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day8('MCMXIV')
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day8
'''

def get_value(char):
    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    return values.get(char, 0)

def Jose_Catela_day8(roman):
  """complete the solution by transforming the roman numeral into an integer"""
  result = 0
  idx = 0
  last = len(roman) - 1
  while idx < len(roman):
      if idx < last and ((roman[idx]=='I' and roman[idx+1]=='V') or (roman[idx]=='I' and roman[idx+1]=='X') or (roman[idx]=='X' and roman[idx+1]=='C') or (roman[idx]=='X' and roman[idx+1]=='L') or (roman[idx]=='C' and roman[idx+1]=='M') or (roman[idx]=='C' and roman[idx+1]=='D')):
          result += get_value(roman[idx+1]) - get_value(roman[idx])
          idx += 2
      else :
          result += get_value(roman[idx])
          idx += 1
  return result

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day8('MCMXIV')
'''

Yang_setup = '''
from __main__ import Yang_day8
'''


def Yang_day8(roman):
    dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    val = dict[roman[0]]
    if len(roman) == 1: return val
    for i, x in enumerate(roman[1:], 1):
        val += dict[x]
        if dict[roman[i - 1]] < dict[roman[i]]:
            val -= dict[roman[i - 1]] * 2
    return val

TEST_CODE_Yang = '''
result = Yang_day8('MCMXIV')
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day8
'''


def Vanessa_G_day8(roman):
    r = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    return sum(-r[roman[i]] if i + 1 < len(roman) and r[roman[i + 1]] > r[roman[i]]
               else r[roman[i]] for i in range(len(roman)))

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day8('MCMXIV')
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day8
'''


def Memo_Hurtado_day8(roman):
    r = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    return sum(-r[roman[i]] if i + 1 < len(roman) and r[roman[i + 1]] > r[roman[i]]
               else r[roman[i]] for i in range(len(roman)))

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day8('MCMXIV')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day8
'''


def Oleksandra_Chmel_day8(roman):
    numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    r = [numerals[num] for num in roman]
    y = [0] + [j - i for i, j in zip(r[: -1], r[1:])]
    for i, n in enumerate(y):
        if n > 0:
            r[i - 1] = n
            r[i] = 0
    return sum(r)


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day8('MCMXIV')
'''

sjay_setup = '''
from __main__ import sjay_day8
'''


def sjay_day8(roman):
    reference = {
        'I': {'index': 0, 'value': 1},
        'V': {'index': 1, 'value': 5},
        'X': {'index': 2, 'value': 10},
        'L': {'index': 3, 'value': 50},
        'C': {'index': 4, 'value': 100},
        'D': {'index': 5, 'value': 500},
        'M': {'index': 6, 'value': 1000}
    }
    total = reference.get(roman[0])['value']
    flag = True
    i = 1
    while i <= len(roman) - 1:
        ind = reference.get(roman[i - 1])['index']
        nxt = reference.get(roman[i])['index']
        if (ind >= nxt):
            total = total + reference.get(roman[i])['value']
            i = i + 1
        else:
            total = total + reference.get(roman[i])['value'] - 2 * reference.get(roman[i - 1])['value']
            i = i + 1
    return total


TEST_CODE_sjay = '''
result = sjay_day8('MCMXIV')
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
#print("Time for killian test code: " + str(timeit.timeit(stmt=TEST_CODE_killian, setup=killian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
#print("Time for David_Nugent test code: " + str(timeit.timeit(stmt=TEST_CODE_David_Nugent, setup=David_Nugent_setup, number=100000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
#print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
