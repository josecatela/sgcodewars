import timeit
import operator

diana_henninger_setup = '''
from __main__ import diana_henninger_eight
from __main__ import diana_henninger_nine
from __main__ import diana_henninger_plus
'''

def diana_henninger_eight(x=None):return 8 if x==None else x(8)
def diana_henninger_nine(x=None): return 9 if x==None else x(9)
def diana_henninger_plus(y): return lambda x: x + y

TEST_CODE_diana_henninger = '''
result = diana_henninger_eight(diana_henninger_plus(diana_henninger_nine()))
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_eight
from __main__ import Vanessa_G_nine
from __main__ import Vanessa_G_plus
'''

def Vanessa_G_eight(f=0):return f(8) if f else 8
def Vanessa_G_nine(f=0): return f(9) if f else 9
def Vanessa_G_plus(x):  return lambda y:  y + x

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_eight(Vanessa_G_plus(Vanessa_G_nine()))
'''

Jose_catela_setup = '''
from __main__ import Jose_catela_eight
from __main__ import Jose_catela_nine
from __main__ import Jose_catela_plus
'''

def Jose_catela_eight(op=''): return 8 if op=='' else eval('8' + op)
def Jose_catela_nine(op=''): return 9 if op=='' else eval('9' + op)
def Jose_catela_plus(num): return ' + ' + str(num)

TEST_CODE_Jose_catela = '''
result = Jose_catela_eight(Jose_catela_plus(Jose_catela_nine()))
'''


ccquiel_setup = '''
from __main__ import ccquiel_eight
from __main__ import ccquiel_nine
from __main__ import ccquiel_plus
'''

def ccquiel_eight(f=None): return 8 if not f else f(8)
def ccquiel_nine(f=None): return 9 if not f else f(9)
def ccquiel_plus(n): return lambda x: x + n

TEST_CODE_ccquiel = '''
result = ccquiel_eight(ccquiel_plus(ccquiel_nine()))
'''


ggebre_setup = '''
from __main__ import ggebre_eight
from __main__ import ggebre_nine
from __main__ import ggebre_plus
'''

def ggebre_eight(f = None): return 8 if not f else f(8)
def ggebre_nine(f = None): return 9 if not f else f(9)
def ggebre_plus(y): return lambda x: x+y

TEST_CODE_ggebre = '''
result = ggebre_eight(ggebre_plus(ggebre_nine()))
'''


Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_eight
from __main__ import Oleksandra_Chmel_nine
from __main__ import Oleksandra_Chmel_plus
'''

def Oleksandra_Chmel_eight(*x): return 8 if not x else int(eval('8' + x[0]))
def Oleksandra_Chmel_nine(*x): return 9 if not x else int(eval('9' + x[0]))
def Oleksandra_Chmel_plus(y): return '+' + str(y)

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_eight(Oleksandra_Chmel_plus(Oleksandra_Chmel_nine()))
'''

Yang_setup = '''
from __main__ import Yang_eight
from __main__ import Yang_nine
from __main__ import Yang_plus
from __main__ import m
'''

def m(x,oy):
    op = {"time":operator.mul,"plus":operator.add,"minus":operator.sub,"div":operator.truediv}
    return int(op[oy[0][0]](x,oy[0][1]))
def Yang_eight(*args): return m(8,args) if args else 8
def Yang_nine(*args): return m(9,args) if args else 9
def Yang_plus(num): return "plus",num

TEST_CODE_Yang = '''
result = Yang_eight(Yang_plus(Yang_nine()))
'''


vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_eight
from __main__ import vijaya_lakshmi_nine
from __main__ import vijaya_lakshmi_plus
'''

def vijaya_lakshmi_eight(func = None): #your code here
    return ("8" if func == None else (eval("8"+func)))
def vijaya_lakshmi_nine(func = None): #your code here
    return ("9" if func == None else (eval("9"+func)))
def vijaya_lakshmi_plus(func): #your code here
    return ("+"+ func)

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_eight(vijaya_lakshmi_plus(vijaya_lakshmi_nine()))
'''


sjay_setup = '''
from __main__ import sjay_eight
from __main__ import sjay_nine
from __main__ import sjay_plus
'''

def sjay_eight(*argeight):
    if len(argeight)>0:
        for i in argeight:
            if(i !=None):
                newval= eval('8' + str(i))
                return int(newval)
    else:
        return 8
def sjay_nine(*argnine):
    if len(argnine)>0:
        for i in argnine:
            if(i !=None):
              newval= eval('9' + str(i))
              return int(newval)
    else:
        return 9
def sjay_plus(numbplus):
    val= numbplus
    return "+" + str(val)

TEST_CODE_sjay = '''
result = sjay_eight(sjay_plus(sjay_nine()))
'''



Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_eight
from __main__ import Kurt_Hinderer_nine
from __main__ import Kurt_Hinderer_plus
from __main__ import calculate
'''
def calculate(num1, operation, num2):
    if operation == '+':
        return(num1 + num2)
    elif operation == '-':
        return(num1 - num2)
    elif operation == '*':
        return(num1 * num2)
    elif operation == '/':
        return(num1 // num2)

def Kurt_Hinderer_eight(operation = ""):
    if operation == "":
        return 8
    else:
        return calculate(8, operation[0], int(operation[1]))
def Kurt_Hinderer_nine(operation = ""):
    if operation == "":
        return 9
    else:
        return calculate(9, operation[0], int(operation[1]))
# returns a string with the operation and the number
def Kurt_Hinderer_plus(num):
    return ('+' + str(num))

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_eight(Kurt_Hinderer_plus(Kurt_Hinderer_nine()))
'''


#print("Time for killian test code: " + str(timeit.timeit(stmt=TEST_CODE_killian, setup=killian_setup, number=1000000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=1000000)) + " seconds")
print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=1000000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=1000000)) + " seconds")
print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=1000000)) + " seconds")
#print("Time for David_Nugent test code: " + str(timeit.timeit(stmt=TEST_CODE_David_Nugent, setup=David_Nugent_setup, number=1000000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=1000000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=1000000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_catela, setup=Jose_catela_setup, number=1000000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=1000000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=1000000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=1000000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=1000000)) + " seconds")
