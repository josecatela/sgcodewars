import timeit


akash_karan_setup = '''
from __main__ import akash_karan_day26
'''

def akash_karan_day26(chars, n):
    ct=0
    le=len(chars)
    pat=""
    for i in range(n+1):
        pa=" "*(n-i)
        pat+=pa
        for k in range(i):
            pat+=chars[ct%le]+" "
            ct+=1
        pat=pat[:-1]+"\n"
    p=" "*(n-1)+"|"+"\n"
    p=p*(n//3)
    pat+=p    
    return pat[n:-1]

TEST_CODE_akash_karan = '''
result = akash_karan_day26("1234",6)
'''

ccquiel_setup = '''
from __main__ import ccquiel_day26
'''

def ccquiel_day26(chars, n):
    tree = str()
    chars_len = len(chars)
    lcount = 0
    for i in range(1, n+1):
        leaves = ' '.join([chars[(lcount + j) % chars_len] for j in range(i)])
        tree += ' '*(n - i) + leaves + '\n'
        lcount += i
    trunk = (' '*(n-1) + '|\n')*(n // 3)
    tree += trunk[:-1]
    return tree

TEST_CODE_ccquiel = '''
result = ccquiel_day26("1234",6)
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day26
'''

def charlie_ang_day26(chars, n):
    # first define width as being width = (n*2-1)
    result = [ " ".join(chars[(column + sum(range(rownum+1))) % len(chars)] for column in range(rownum+1)) for rownum in range(n) ]
    result += [ '|' for i in range(n//3)]
    return "\n".join(row.center(n*2-1).rstrip()  for row in result)

TEST_CODE_charlie_ang = '''
result = charlie_ang_day26("1234",6)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day26
'''

def diana_henninger_day26(chars, n):
    tree = ""
    index = 0
    for i in range(n): # each line
        tree += (n-i-1) * ' ' #space
        for j in range(i+1):  #each char
            tree += chars[index%len(chars)] + ' '
            index += 1
        tree = tree[:-1] +'\n'
    for k in range(n//3): # trunk
        tree += (n-1) * ' ' + '|' + '\n'
    return tree[:-1]

TEST_CODE_diana_henninger = '''
result = diana_henninger_day26("1234",6)
'''

Jens_setup = '''
from __main__ import Jens_day26
'''

def Jens_day26(chars, n):
    tree_string, count = '', 0        
    for i in range(n):           # create leaves
        tree_string += (n-1-i)*' ' + (i)*'* ' + '*\n'
    for i in range(0, len(tree_string)-1): # decorate
        if tree_string[i] == '*':                  
            tree_string = tree_string[:i] + chars[count%len(chars)] + tree_string[i+1:]
            count += 1
    for i in range(n//3):         # create trunk
        tree_string += (n-1)*' ' + '|\n' 
    return(tree_string[:-1])

TEST_CODE_Jens = '''
result = Jens_day26("1234",6)
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day26
'''

def Jose_Catela_day26(chars, n):
    spaces = n - 1
    tree = ''
    pos = 0
    npos = len(chars)
    for k in range(n):
        tree += ' ' * spaces
        spaces -= 1
        for j in range(k+1):
            tree += chars[pos]
            pos += 1
            if pos == npos:
                pos = 0
            if j != k:
                tree += ' '
        tree += '\n'
    base_size = n // 3
    for k in range(base_size):
        tree += ' ' * ( n - 1)
        tree += '|'
        if k != base_size - 1:
            tree += '\n'
    return(tree)

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day26("1234",6)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day26
'''

def Kurt_Hinderer_day26(chars, n):
    character = 0
    tree = ""
    if len(chars) == 0:
        return tree
    for i in range(n):
        tree += " " * (n - i - 1)
        for j in range(i + 1):
            tree += chars[character % len(chars)]
            character += 1
            if j < i:
                tree += " "
        tree += "\n"
    for i in range(n//3):
        tree += " " * (n - 1) + "|"
        if i < n//3 -1:
            tree += "\n"
    return tree

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day26("1234",6)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day26
'''


def Oleksandra_Chmel_day26(chars, n):
    length = sum([x for x in range(1,n+1)])
    new_chars = chars * (length // len(chars)) + chars[:length%len(chars)]
    tree = ''
    for t in range(1,n+1):
        tree += ' ' * (n-t) + new_chars[0:t].replace('',' ').strip() + '\n'
        new_chars = new_chars[t:]
    return (tree + n//3 * (' ' * (n - 1) + '|' + '\n'))[:-1]

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day26("1234",6)
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
