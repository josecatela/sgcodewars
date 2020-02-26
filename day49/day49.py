import timeit
import re


abdiwoli_setup = '''
from __main__ import abdiwoli_day49
'''

def abdiwoli_day49(x):
    x = x.split(' ')
    x = [list(i) for i in x]
    t = ''
    for i in x:
        if len(i) > 4:
            i.reverse()
            t += ''.join(i) + ' '
        else:
            t+= ''.join(i) + ' '
    return t[:-1]

TEST_CODE_abdiwoli = '''
result = abdiwoli_day49('CodeWars')
'''

akash_karan_setup = '''
from __main__ import akash_karan_day49
'''

def akash_karan_day49(sentence):
    return " ".join([x[::-1] if len(x)>4 else x for x in sentence.split()])

TEST_CODE_akash_karan = '''
result = akash_karan_day49('CodeWars')
'''

ccquiel_setup = '''
from __main__ import ccquiel_day49
'''

def ccquiel_day49(sentence):
    spinned = ''
    for w in sentence.split():
        if len(w) > 4: spinned += w[::-1] + ' '
        else: spinned += w + ' '
    return spinned[:-1]

TEST_CODE_ccquiel = '''
result = ccquiel_day49('CodeWars')
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day49
'''

def diana_henninger_day49(sentence):
    return re.sub(r'[a-z]{5,}', lambda w: w.group(0)[::-1], sentence, flags=re.IGNORECASE)

TEST_CODE_diana_henninger = '''
result = diana_henninger_day49('CodeWars')
'''

Jens_setup = '''
from __main__ import Jens_day49
'''

def Jens_day49(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = ''.join(reversed(words[i]))
    return ' '.join(words)   

TEST_CODE_Jens = '''
result = Jens_day49('CodeWars')
'''

kheireddine_Douli_setup = '''
from __main__ import kheireddine_Douli_day49
'''

def kheireddine_Douli_day49(sentence):
    return ' '.join([x[::-1] if len(x) >= 5 else x for x in sentence.split() ])   

TEST_CODE_kheireddine_Douli = '''
result = kheireddine_Douli_day49('CodeWars')
'''

Matthias_setup = '''
from __main__ import Matthias_day49
'''

def Matthias_day49(sentence):
    result = ""
    for word in sentence.split():
        if len(word) >= 5:
            word = "".join(reversed(word))
        result += word + " "
    return result.rstrip()   

TEST_CODE_Matthias = '''
result = Matthias_day49('CodeWars')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day49
'''

def Oleksandra_Chmel_day49(sentence):
    sentence = sentence.split()
    sentence = [word[::-1] if len(word) >= 5 else word for word in sentence]
    return ' '.join(sentence)

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day49('CodeWars')
'''

SJay_setup = '''
from __main__ import SJay_day49
'''

def SJay_day49(sentence):
    retval=""
    listwords= sentence.split(' ')
    # print(listwords)
    for ind,word in enumerate(listwords):
        # print (word)
        if len(word) >= 5:
            temp=list(word)
            temp.reverse()
            word=''.join(temp)
        if ind==0:  
            retval+=word
        else:
            retval+=' '+word
    return retval

TEST_CODE_SJay = '''
result = SJay_day49('CodeWars')
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day49
'''

def Tushar_Jain_day49(sentence):
    return ' '.join((x if len(x) < 5 else x[-1::-1]
                    for x in sentence.split(' ')))

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day49('CodeWars')
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day49
'''

def Vanessa_G_day49(sentence):
    return ' '.join(word[::-1] if len(word) > 4 else word for word in sentence.split(' '))

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day49('CodeWars')
'''

Yang_setup = '''
from __main__ import Yang_day49
'''

def Yang_day49(sentence):
    for x in set(sentence.split()): 
        if len(x)>=5: 
            sentence = sentence.replace(x,x[::-1]) 
    return sentence

TEST_CODE_Yang = '''
result = Yang_day49('CodeWars')
'''

print("Time for abdiwoli test code: " + str(timeit.timeit(stmt=TEST_CODE_abdiwoli, setup=abdiwoli_setup, number=100000)) + " seconds")
print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for kheireddine_Douli test code: " + str(timeit.timeit(stmt=TEST_CODE_kheireddine_Douli, setup=kheireddine_Douli_setup, number=100000)) + " seconds")
print("Time for Matthias test code: " + str(timeit.timeit(stmt=TEST_CODE_Matthias, setup=Matthias_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for SJay test code: " + str(timeit.timeit(stmt=TEST_CODE_SJay, setup=SJay_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
