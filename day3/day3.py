import timeit

ccquiel_setup = '''
from __main__ import ccquiel_diamond
'''

def ccquiel_diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    diamond = [""]*n
    center = int((n + 1)/2) - 1
    for i in range(center):
        spaces = center - i
        line = " "*spaces + '*'*(n - 2*spaces)
        diamond[i] = line
        diamond[(n-1)-i] = line
    diamond[center] = '*'*n
    return "\n".join(diamond) + "\n"

TEST_CODE_ccquiel = '''
example=11
result = ccquiel_diamond(example)'''

diana_henninger_setup = '''
from __main__ import diana_henninger_diamond
'''

def diana_henninger_diamond(n):
    # Make some diamonds!
    if n%2 == 0 or n < 0: return None
    diamond_string = ""
    i = 1
    while i <= n:
        diamond_string += " "*int((n-i)/2) + "*"*i + "\n"
        i+=2
    i-=4
    while i > 0:
        diamond_string += " "*int((n-i)/2) + "*"*i + "\n"
        i-=2
    return diamond_string

TEST_CODE_diana_henninger = '''
example=11
result = diana_henninger_diamond(example)'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_diamond
'''

def Prashanth_Kadimisetty_diamond(n):
    if (n > 1 and n % 2 != 0):
        ls = [((n // 2 + 1) - i) * ' ' + (2 * i - 1) * '*' + '\n' for i in range(1, (n // 2) + 1)]
        ls.append('*' * n + '\n')
        ls = ls + ls[len(ls) - 2::-1]
        finals = ''.join(ls)
        return finals
    elif n == 1:
        return '*\n'
    else:
        return None

TEST_CODE_Prashanth_Kadimisetty = '''
example=11
result = Prashanth_Kadimisetty_diamond(example)'''


jorge_setup = '''
from __main__ import jorge_diamond
'''


def jorge_diamond(number):
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
result = jorge_diamond(example)'''


Ahmed_El_Midany_setup = '''
from __main__ import Ahmed_El_Midany_diamond
'''


def Ahmed_El_Midany_diamond(number):
    text = ""
    if number <= 0 or ((number % 2) == 0):
        print("No diamond for you baby!")
    else:
        for i in range(1, number + 1):
            i = i - (number // 2 + 1)
            if i < 0:
                i = -i
            text = text + (" " * i + "*" * (number - i * 2) + " " * i) + "\n"
    return text


TEST_CODE_Ahmed_El_Midany = '''
example=11
result = Ahmed_El_Midany_diamond(example)'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_diamond
'''


def Kurt_Hinderer_diamond(n):
    #defining the diamond output, first odd natural number
    if(n % 2 == 1 and n > 0):
        diamond_output = ""
        for row in range(0, n):
            diamond_output += " " * abs((n-1)//2 - row)
            diamond_output += "*" * (-abs(2*row - (n-1)) + n)
            diamond_output += "\n"
    #now for the bad input case
    else:
        diamond_output = None
    return diamond_output


TEST_CODE_Kurt_Hinderer = '''
example=11
result = Kurt_Hinderer_diamond(example)'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_diamond
'''


def Jose_Catela_diamond(n):
    # Make some diamonds!
    if n < 0 or n % 2 == 0:
        return None
    count_spaces = int(n/2)
    count_asterisks = 1
    result = ''
    for x in range(0, n):
        result = result + ' ' * count_spaces
        result = result + '*' * count_asterisks
        result = result + '\n'
        if x < int(n/2):
            count_spaces = count_spaces - 1
            count_asterisks = count_asterisks + 2
        else:
            count_spaces = count_spaces + 1
            count_asterisks = count_asterisks - 2
    return result

TEST_CODE_Jose_Catela = '''
example=11
result = Jose_Catela_diamond(example)'''

Yang_setup = '''
from __main__ import Yang_diamond
'''


def Yang_diamond(n):
    if n>0 and n%2==1:
        ll = list(list(range(1,n,2))+list(range(n,-1,-2)))
        return (('\n').join ( ' '*int((n-i)/2) + '*'*i for i in ll) + '\n')


TEST_CODE_Yang = '''
example=11
result = Yang_diamond(example)'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_diamond
'''


def Vanessa_G_diamond(n):
    s = ""
    for i in range(n):
        s += " " * abs((n//2) - i)
        s += "*" * (n - abs((n-1) - 2 * i))
        s += "\n"
    return s if s and n % 2 != 0 else None

TEST_CODE_Vanessa_G = '''
example=11
result = Vanessa_G_diamond(example)'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_diamond
'''


def Oleksandra_Chmel_diamond(n):
    if n < 1 or n % 2 == 0:
        return None
    else:
        ranges = ['*' * t for t in range(1, n - 1, 2) if n > 0] + ['*' * f for f in range(n, 0, -2) if n > 0]
        spaces = [' ' * t for t in range(n // 2, 0, -1)] + [' ' * f for f in range(0, n // 2 + 1)]
        diam = ''.join(''.join(x) for x in zip(spaces, ranges, '\n' * n))
        return diam


TEST_CODE_Oleksandra_Chmel = '''
example=11
result = Oleksandra_Chmel_diamond(example)'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for jorge test code: " + str(timeit.timeit(stmt=TEST_CODE_jorge, setup=jorge_setup, number=100000)) + " seconds")
print("Time for Ahmed_El_Midany test code: " + str(timeit.timeit(stmt=TEST_CODE_Ahmed_El_Midany, setup=Ahmed_El_Midany_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
