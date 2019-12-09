import timeit

killian_setup = '''
from __main__ import killian_day4
'''

def killian_day4(value):
    digist = len(str(value))
    exp_value = 0
    value_copy = value
    while value_copy != 0:
        exp_value += (value_copy % 10) ** digist
        value_copy //= 10
    return value == exp_value

TEST_CODE_killian = '''
example=11
result = killian_day4(example)'''

ccquiel_setup = '''
from __main__ import ccquiel_day4
'''

def ccquiel_day4(value):
    valstr = str(value)
    powers = [int(n) ** len(valstr) for n in valstr]
    return sum(powers) == value

TEST_CODE_ccquiel = '''
example=11
result = ccquiel_day4(example)'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day4
'''

def diana_henninger_day4(value):
    sum = 0
    len_v = len(str(value))
    for i in str(value):
        sum += pow(int(i), len_v)
        if (sum > value): return False
    return value == sum

TEST_CODE_diana_henninger = '''
example=11
result = diana_henninger_day4(example)'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day4
'''

def vijaya_lakshmi_day4(value):
    sum = 0
    len_v = len(str(value))
    for i in str(value):
        sum += pow(int(i), len_v)
        if (sum > value): return False
    return value == sum

TEST_CODE_vijaya_lakshmi = '''
example=11
result = vijaya_lakshmi_day4(example)'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day4
'''

def Prashanth_Kadimisetty_day4(value):
    strval = str(value)
    return value == sum([int(i) ** (len(strval)) for i in strval])

TEST_CODE_Prashanth_Kadimisetty = '''
example=11
result = Prashanth_Kadimisetty_day4(example)'''

David_Nugent_setup = '''
from __main__ import David_Nugent_day4
'''

def David_Nugent_day4(value):
    sval = str(value)
    lval = len(sval)
    values = [int(x) ** lval for x in sval]
    return sum(values) == value

TEST_CODE_David_Nugent = '''
example=11
result = David_Nugent_day4(example)'''


jorge_setup = '''
from __main__ import jorge_day4
'''


def jorge_day4(number):
    if (number % 2 == 0) | (number <= 0):
        return 'null/nil/None/...'
    #number = number -1
    l = ["*"*num for num in range(number+1) if num % 2 !=0]
    l2 = l.copy()
    l2.reverse()
    l1 = [(i*' ')+item for i, item in enumerate(l2) if len(item)<number]
    l3 = l1.copy()
    l3.reverse()
    l3.append(l[-1])
    l4 = [item+'\n' for item in l3]
    l1 = [item+'\n' for item in l1]
    fl = l4 + l1
    return ''.join(fl)

TEST_CODE_jorge = '''
example=11
result = jorge_day4(example)'''


Ahmed_El_Midany_setup = '''
from __main__ import Ahmed_El_Midany_day4
'''


def Ahmed_El_Midany_day4(number):
    text = ""
    if number <= 0 or ((number % 2) == 0):
        print("No day4 for you baby!")
    else:
        for i in range(1, number + 1):
            i = i - (number // 2 + 1)
            if i < 0:
                i = -i
            text = text + (" " * i + "*" * (number - i * 2) + " " * i) + "\n"
    return text


TEST_CODE_Ahmed_El_Midany = '''
example=11
result = Ahmed_El_Midany_day4(example)'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day4
'''


def Kurt_Hinderer_day4(value):
    num_digits = len(str(value))
    # initializing the total
    narc_total = 0
    # looping through the digits
    for counter in range(num_digits):
        digit = value % 10 ** (counter + 1) // 10 ** (counter)
        narc_total += digit ** num_digits
        # print(narc_total)
    return (narc_total == value)


TEST_CODE_Kurt_Hinderer = '''
example=11
result = Kurt_Hinderer_day4(example)'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day4
'''


def Jose_Catela_day4(value):
    strvalue = str(value)
    lenvalue = len(strvalue)
    result = 0
    for position in strvalue:
        result += int(position) ** lenvalue
    return result == value

TEST_CODE_Jose_Catela = '''
example=11
result = Jose_Catela_day4(example)'''

Yang_setup = '''
from __main__ import Yang_day4
'''


def Yang_day4(value):
    vv = str(value)
    val = sum(list(map(lambda x: int(x) ** len(vv), vv)))
    return (val == value)


TEST_CODE_Yang = '''
example=11
result = Yang_day4(example)'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day4
'''


def Vanessa_G_day4(value):
    return value == sum(int(i) ** len(str(value)) for i in str(value))

TEST_CODE_Vanessa_G = '''
example=11
result = Vanessa_G_day4(example)'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day4
'''


def Oleksandra_Chmel_day4(value):
    value_str = str(value)
    value_len = len(value_str)
    a = 0
    for val in value_str:
        a += int(val) ** value_len
    if value == a:
        return True
    else:
        return False


TEST_CODE_Oleksandra_Chmel = '''
example=11
result = Oleksandra_Chmel_day4(example)'''

print("Time for killian test code: " + str(timeit.timeit(stmt=TEST_CODE_killian, setup=killian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for David_Nugent test code: " + str(timeit.timeit(stmt=TEST_CODE_David_Nugent, setup=David_Nugent_setup, number=100000)) + " seconds")
print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
