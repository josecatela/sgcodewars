import timeit
import re
from string import punctuation


ccquiel_setup = '''
from __main__ import ccquiel_day49
'''

vowls = 'aeiouy'

def counts(string):
    count = 0
    for word in string.split(' '):
        prev = 'x'
        word = [w for w in word if w.isalpha() or w == ' ']
        for s in word:
            if s in vowls and prev not in vowls:
                count += 1
            prev = s
        if prev == 'e' and len(word) >= 3 and word[-2] not in vowls:
            if len(word) == 3 and word[0] in vowls: count -= 1
            elif len(word) > 3: count -= 1
    return count

def ccquiel_day49(text):
    text = text.split('\n')
    if all(n==counts(t.lower()) for n,t in zip((5,7,5),text)):
        return True
    else:
        return False

TEST_CODE_ccquiel = '''
result = ccquiel_day49("""\
Autumn moonlight -
a worm digs silently
into the chestnut.""")
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day49
'''

def syllable_count(word):
    word = word.strip(punctuation).lower()
    if len(word)==0: return 0
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels: count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels: count += 1
    if len(word)>=2 and word[-1] == 'e' and word[-2] not in vowels: count -= 1
    if count == 0: count += 1
    return count

def diana_henninger_day49(text):
    text = text.split('\n')
    if(len(text)!=3): return False
    lines = []
    for line in text:
        line = line.strip(punctuation).split(" ")
        lines.append(line)
    return ((sum([syllable_count(word) for word in lines[0]])==5) and 
           (sum([syllable_count(word) for word in lines[1]])==7) and
           (sum([syllable_count(word) for word in lines[2]])==5))

TEST_CODE_diana_henninger = '''
result = diana_henninger_day49("""\
Autumn moonlight -
a worm digs silently
into the chestnut.""")
'''

Jens_setup = '''
from __main__ import Jens_day49
'''

def Jens_day49(text):
    vowels, consonants = 'aeiouy', 'bcdfghjklmnpqrstvwxz'
    lines = text.splitlines()
    if len(lines) != 3:
        return False
    for i in range(3):
        words = lines[i].split()
        count = 0
        for word in words:
            syl, prev_vowel, first_syl = '', False, True
            for letter in word:
                if letter.lower() in vowels:
                    if first_syl:
                        first_syl = False
                        prev_vowel = True
                        syl += letter
                    else:
                        if prev_vowel == False and len(syl) > 0:
                            count += 1
                            syl = letter
                        else:
                            syl += letter
                        prev_vowel = True
                elif letter.lower() in consonants:
                    syl += letter
                    prev_vowel = False
            if len(syl) > 0 and (not syl.lower() == 'e' or len(word) == 1):
                count += 1
        if (i in (0, 2) and count != 5) or (i == 1 and count != 7):
            return False
    return True

TEST_CODE_Jens = '''
result = Jens_day49("""\
Autumn moonlight -
a worm digs silently
into the chestnut.""")
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day49
'''

regex = re.compile('[^a-zA-Z]')
v = "aeiouyAEIOUY"

def Oleksandra_Chmel_day49(text):
    lines = [line for line in text.split('\n')]    
    res = []
    for line in lines:
        line = line.split()
        count = 0
        for word in line:
            word = regex.sub('', word)
            l = len(word)
            if word == '': continue
            elif l <= 3: count += 1
            else:
                if word[0] in v: count += 1
                for i in range(1,l):
                    if word[i-1] not in v and word[i] in v: count += 1
                if word[l-1] == 'e' and word[l-2] not in v: count -= 1
        res.append(count)
    return res == [5, 7, 5]

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day49("""\
Autumn moonlight -
a worm digs silently
into the chestnut.""")
'''

Omar_B_setup = '''
from __main__ import Omar_B_day49
'''

def Omar_B_day49(text):
    vowel = "aeiouyAEIOUY"
    lines = text.split('\n')
    syllabe_count_per_line=[]
    for line in lines : 
        words=line.split()
        count = 0
        for word in words:
            Letters=[d for d in word if ((d>='A') and (d<='Z')) or ((d>='a') and (d<='z'))]
            if len(Letters)==0: continue
            elif len(Letters)<=3 : count+=1
            else:
                syllab=[]
                for i in range(len(Letters)):
                    if Letters[i] in vowel and syllab==[]:
                        syllab.append(Letters[i])
                        count+=1
                    elif Letters[i] not in vowel :
                        syllab.append(Letters[i])
                    elif Letters[i] in vowel and syllab !=[] and syllab[-1] in vowel :
                        syllab.append(Letters[i])
                    elif Letters[i] in vowel and syllab !=[] and syllab[-1] not in vowel :
                        syllab=[Letters[i]]
                        count+=1
                if Letters[-1]=='e' and count>=1 and Letters[-2] not in vowel :
                    count-=1
        syllabe_count_per_line.append(count)
    return syllabe_count_per_line==[5,7,5]

TEST_CODE_Omar_B = '''
result = Omar_B_day49("""\
Autumn moonlight -
a worm digs silently
into the chestnut.""")
'''

SJay_setup = '''
from __main__ import SJay_day49
'''

def SJay_day49(text):
    data=[]
    vowels=['a','e','i','o','u']
    for num,line  in enumerate(text.splitlines()):
              line = line.lower()
              counter=0
              for ind,varcomp in enumerate(list(line)):
                  if ind >0 and varcomp in vowels and list(line)[ind-1] not in vowels:
                      counter += 1
                  if ind ==0 and varcomp in vowels:
                      counter+=1
                  if varcomp=='e' and ind < len(list(line))-1 and (list(line)[ind+1].isalpha()==False )and list(line)[ind-1] in ['l','k','y','m','c','g','d','r','s','p','b','f','n','j','t','v','w','x','z']:
                      counter -=1
                  if varcomp=='e' and ind == len(list(line))-1 and list(line)[ind-1] not in vowels:
                      counter -=1
                  if varcomp=='y' and (ind > 0 and ind <len(list(line)) -1) and (list(line)[ind-1].isalpha()==True or list(line)[ind+1].isalpha()==False) and list(line)[ind-1] not in vowels and list(line)[ind+1] not in vowels:
                      counter +=1
                  if varcomp=="y" and ind==0 and list(line)[ind+1].isalpha()==False:
                      counter+=1
                  if varcomp=='y' and ind < len(list(line))-1 and (list(line)[ind+1] in vowels)and (list(line)[ind-1] in vowels):
                      counter -=1
                  if varcomp=="y" and ind==len(list(line))-1 and list(line)[ind-1].isalpha()==True and list(line)[ind-1] not in vowels:
                      counter+=1
              data.append(counter)
    for i in range(0,len(data),3):
        if data[i:i+3]==[5,7,5]:
            return True
        else:
            return False

TEST_CODE_SJay = '''
result = SJay_day49("""\
Autumn moonlight -
a worm digs silently
into the chestnut.""")
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day49
'''

def Tushar_Jain_day49(text):
    text = text.lower()
    vowels = re.compile(r'''
    [aeiouy]+
    ''', re.VERBOSE)
    specials = re.compile(r'''
    \W+
    ''', re.VERBOSE)
    silent = re.compile('''
    ^.*
    [aeiouy]+
    .*
    [^aeiou]e$
    ''', re.VERBOSE)
    result = []
    for line in text.splitlines():
        line = specials.sub(' ', line.strip()).strip()
        words = [x[:-1] if silent.match(x) else x for x in line.split()]
        vcount = [max(1, len(vowels.findall(x))) for x in words if x]
        result.append(sum(vcount))
    return result == [5,7,5]

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day49("""\
Autumn moonlight -
a worm digs silently
into the chestnut.""")
'''

print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Omar_B test code: " + str(timeit.timeit(stmt=TEST_CODE_Omar_B, setup=Omar_B_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for SJay test code: " + str(timeit.timeit(stmt=TEST_CODE_SJay, setup=SJay_setup, number=100000)) + " seconds")
