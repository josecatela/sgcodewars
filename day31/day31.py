import timeit


ccquiel_setup = '''
from __main__ import ccquiel_day31
'''

def ccquiel_day31(num):
    nums = str(round(num, 3)).split('.')
    dec = '.' + nums[1] if len(nums) == 2 and len(nums[1]) > 1 else ''
    return "{:,}{}".format(int(nums[0]), dec)

TEST_CODE_ccquiel = '''
result = ccquiel_day31(-1000000.123)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day31
'''

def diana_henninger_day31(num):
    num = round(num,3)
    if type(num)==type(0.3) and num.is_integer():
       num = int(num) 
    return '{:,}'.format(num)

TEST_CODE_diana_henninger = '''
result = diana_henninger_day31(-1000000.123)
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day31
'''

def Vanessa_G_day31(num):
    snum = "{:,}".format(round(num,3))
    return snum[0:-2] if snum.endswith('.0') else snum

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day31(-1000000.123)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day31
'''

def Kurt_Hinderer_day31(num):
    if isinstance(num, float):
        num = round(num, 3)
        if num.is_integer():
            num = int(num)
    num_str = str(num)
    negative = num < 0
    dec_loc = num_str.find('.')
    if dec_loc == -1:
        dec_loc = len(num_str)
    dec_loc -= 3
    while dec_loc > 0:
        if dec_loc == 1 and negative:
            dec_loc -= 1
        else:
            num_str = num_str[:dec_loc] + ',' + num_str[dec_loc:]
            dec_loc -= 3
    return num_str

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day31(-1000000.123)
'''

Jens_setup = '''
from __main__ import Jens_day31
'''

def Jens_day31(num):
    num_str = '' if num >= 0 else '-'
    num = round(num, 3)
    num_parts = str(abs(num)).split('.')
    if len(num_parts[0])%3 != 0:
      num_str += num_parts[0][:len(num_parts[0])%3] + ','  
    rest_num = num_parts[0][len(num_parts[0])%3:]
    while len(rest_num) > 0:
        num_str += rest_num[:3] + ','
        rest_num = rest_num[3:]
    if len(num_parts) == 1 or num_parts[1] == '0':
        return num_str[:-1]
    return num_str[:-1] + '.' + num_parts[1]

TEST_CODE_Jens = '''
result = Jens_day31(-1000000.123)
'''

Yang_setup = '''
from __main__ import Yang_day31
'''

def Yang_day31(num): 
    n = format(round(num,3), ",").split('.') 
    return n[0] + '.' + n[1] if len(n)>1 and n[1]!='0' else n[0] 

TEST_CODE_Yang = '''
result = Yang_day31(-1000000.123)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day31
'''

def Oleksandra_Chmel_day31(num):
    return "{:,.3f}".format(num).strip('0').strip('.') if '.' in str(num) else "{:,}".format(num)

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day31(-1000000.123)
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day31
'''

def charlie_ang_day31(num):
    number = float(num)
    return f'{number:,.0f}' if number.is_integer() else f'{number:,.3f}'.rstrip('0').rstrip('.')

TEST_CODE_charlie_ang = '''
result = charlie_ang_day31(-1000000.123)
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
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=10000)) + " seconds")
#print("Time for Daniel_Ruiz test code: " + str(timeit.timeit(stmt=TEST_CODE_Daniel_Ruiz, setup=Daniel_Ruiz_setup, number=10000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
#print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=10000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
