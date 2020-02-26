import timeit
from collections import Counter


abdiwoli_setup = '''
from __main__ import abdiwoli_day35
'''

def abdiwoli_day35(r,n):
	d = {'Wild3':100,'Star3':90,'Bell3':80,'Shell3':70,'Seven3':60,'Cherry3':50,'Bar3':40,'King3':30,'Queen3':20,'Jack3':10,'Wild2':10,'Star2':9,'Bell2':8,'Shell2':7,'Seven2':6,'Cherry2':5,'Bar2':4,'King2':3,'Queen2':2,'Jack2':1,
}
	n[0] = r[0][n[0]]
	n[1] = r[1][n[1]] 
	n[2] = r[2][n[2]]
	n = [i+str(n.count(i)) for i in n]
	s = set(i for i in n)
	c = 0
	for i in s:
		if 'Wild1' in i and len(s)==2:
			t = ','.join(s).split(',')
			z = t.index('Wild1')
			if z==0:    return d[t[1]] *2
			else:    return d[t[0]] *2
		try:    c+= d[i]
		except:    c+=0
	return c

TEST_CODE_abdiwoli = '''
result = abdiwoli_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

akash_karan_setup = '''
from __main__ import akash_karan_day35
'''

def akash_karan_day35(reels, spins):
    one=reels[0][spins[0]]
    two=reels[1][spins[1]]
    three=reels[2][spins[2]]
    #print(one,two,three)
    jack={"Wild":10,"Star":9,"Bell":8,"Shell":7,"Seven":6,"Cherry":5,"Bar":4,"King":3,"Queen":2,"Jack":1}
    if(one==two and one==three):
        return jack[one]*10
    elif(one==two and three=="Wild"): 
        return jack[one]*2
    elif(two==three and one=="Wild"): 
        return jack[two]*2
    elif(one==three and two=="Wild"): 
        return jack[three]*2
    elif(one==two): 
        return jack[one]
    elif(three==two): 
        return jack[two]
    elif(one==three): 
        return jack[one]
    else:
        return 0

TEST_CODE_akash_karan = '''
result = akash_karan_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

ccquiel_setup = '''
from __main__ import ccquiel_day35
'''

def ccquiel_day35(reels, spins):
    scores = {'Wild': 10, 'Star': 9,
              'Bell': 8, 'Shell': 7, 
              'Seven': 6, 'Cherry': 5,
              'Bar': 4, 'King': 3,
              'Queen': 2, 'Jack': 1}
    counts = Counter([reel[index] for reel, index in zip(reels, spins)])
    for s, c in counts.items():
        if c == 3:
            return scores[s]*10
        if c == 2:
            return scores[s] if ('Wild' not in counts or s=='Wild') else scores[s]*2
    else:
        return 0

TEST_CODE_ccquiel = '''
result = ccquiel_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day35
'''

def diana_henninger_day35(reels, spins):
    items = ["Zero", "Jack", "Queen", "King", "Bar", "Cherry", "Seven", "Shell", "Bell", "Star", "Wild"]
    score = 0
    reel1 = reels[0][spins[0]]
    reel2 = reels[1][spins[1]]
    reel3 = reels[2][spins[2]]
    reel1 = items.index(reel1)
    reel2 = items.index(reel2)
    reel3 = items.index(reel3)
    if reel1 != reel2 and reel1 != reel3 and reel2 != reel3: return 0 # no match
    if reel1 == reel2 and reel2 == reel3: return reel1*10 # three of the same        
    if reel1 == reel2: # two of the same
        if reel3 == 10: return reel1*2 # plus wildcard
        else: return reel1
    elif reel2 == reel3:
        if reel1 == 10: return reel2*2 # plus wildcard
        else: return reel2
    elif reel1 == reel3:
        if reel2 == 10: return reel1*2 # plus wildcard
        else: return reel1

TEST_CODE_diana_henninger = '''
result = diana_henninger_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

Jens_setup = '''
from __main__ import Jens_day35
'''

def Jens_day35(reels, spins):
    values = {"Wild": 10, "Star": 9, "Bell": 8, "Shell": 7 ,"Seven": 6,
              "Cherry": 5, "Bar": 4, "King": 3, "Queen": 2, "Jack": 1}
    results = [reel[spin] for reel, spin in zip(reels, spins)]
    for key, value in values.items():
        if results.count(key) == 3:
            return 10*value
        elif results.count(key) == 2:
            win = value
            if key != "Wild" and "Wild" in results:
                win *= 2
            return win
    return 0

TEST_CODE_Jens = '''
result = Jens_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day35
'''

def Kurt_Hinderer_day35(reels, spins):
    values = {"Wild": 10, "Star": 9, "Bell": 8, "Shell": 7, "Seven": 6, "Cherry": 5, "Bar": 4, "King": 3, "Queen": 2, "Jack": 1, "Bust": 0}
    result = [reels[0][spins[0]], reels[1][spins[1]], reels[2][spins[2]]]
    pair_card = "Bust"
    extra_wild = False
    tripple = False
    if result[0] == result[1]:
        pair_card = result[0]
        if result[2] == result[0]:
            tripple = True
        elif result[2] == "Wild":
            extra_wild = True
    elif result[0] == result[2] or result[1] == result[2]:
        pair_card = result[2]
        if result[2] != "Wild" and (result[0] == "Wild" or result[1] == "Wild"):
            extra_wild = True
    return values[pair_card] * (1 + extra_wild + tripple*9)

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

Navneet_Kumar_setup = '''
from __main__ import Navneet_Kumar_day35
'''

def Navneet_Kumar_day35(reels, spins):
    # Code here
        item = {'Jack':1, 'Queen':2, 'King':3, 'Bar':4, 'Cherry':5, 'Seven':6, 'Shell':7, 'Bell':8, 'Star':9, 'Wild':10}
        s1 = reels[0][spins[0]]
        s2 = reels[1][spins[1]]
        s3 = reels[2][spins[2]]
        if s1==s2==s3:
            return item[s1]*10
        elif s1==s2 and s3=='Wild':
            return item[s1]*2
        elif s1==s3 and s2=='Wild':
            return item[s1]*2
        elif s2==s3 and s1=='Wild':
            return item[s2]*2
        elif s1==s2:
            return item[s1]
        elif s1==s3 :
            return item[s1]
        elif s2==s3 :
            return item[s2]
        else:
            return 0

TEST_CODE_Navneet_Kumar = '''
result = Navneet_Kumar_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day35
'''

def Oleksandra_Chmel_day35(reels, spins):
    # print(reels, spins)
    d = {'Wild': 10, 'Star': 9, 'Bell': 8, 'Shell': 7, 'Seven': 6, 'Cherry': 5,
        'Bar': 4, 'King': 3, 'Queen': 2, 'Jack': 1}
    r1, r2, r3 = reels[0][spins[0]], reels[1][spins[1]], reels[2][spins[2]]
    s = set((r1,r2,r3))
    if len(s) == 1: return d[r1] * 10
    elif len(s) == 2:
        l = [r1,r2,r3]
        if l.count('Wild') == 1:
            l.remove('Wild')
            return d[l[0]] * 2
        else:
            if l.count(l[0]) == 2: return d[l[0]]
            else: return d[l[1]]
    return 0

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

Tushar_Jain_setup = '''
from __main__ import Tushar_Jain_day35
'''

def Tushar_Jain_day35(reels, spins):
    result = sorted([reels[i][spins[i]] for i in range(len(spins))])
    values = {'Wild': 10,
              'Star': 9,
              'Bell': 8,
              'Shell': 7,
              'Seven': 6,
              'Cherry': 5,
              'Bar': 4,
              'King': 3,
              'Queen': 2,
              'Jack': 1}    
    if result[0] != result[1] and result[1] != result[2]:
        return 0
    else:
        multiple = 1
        if result.count('Wild') == 2:
            return 10
        if 'Wild' in result:
            multiple = 2
        if result[0] == result[1] and result[1] == result[2]:
            multiple = 10
        return multiple * values[result[1]]

TEST_CODE_Tushar_Jain = '''
result = Tushar_Jain_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

Yang_setup = '''
from __main__ import Yang_day35
'''

def Yang_day35(reels, spins):
    dict = {"Wild":10,"Star":9,"Bell":8,"Shell":7,"Seven":6,"Cherry":5,"Bar":4,"King":3,"Queen":2,"Jack":1}
    a,b,c = reels
    p1,p2,p3 = spins 
    spin = [a[p1],b[p2],c[p3]]
    if len(set(spin))==1: return dict[spin[0]]*10 
    elif len(set(spin))==2: 
        k = list(set(x for x in spin if spin.count(x)>1))[0]
        wild = True if "Wild" in spin and k!="Wild" else False 
        return dict[k]*2 if wild else dict[k] 
    return 0  

TEST_CODE_Yang = '''
result = Yang_day35([["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"],["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]],[0,0,0])
'''

print("Time for abdiwoli test code: " + str(timeit.timeit(stmt=TEST_CODE_abdiwoli, setup=abdiwoli_setup, number=100000)) + " seconds")
print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Navneet_Kumar test code: " + str(timeit.timeit(stmt=TEST_CODE_Navneet_Kumar, setup=Navneet_Kumar_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for Tushar_Jain test code: " + str(timeit.timeit(stmt=TEST_CODE_Tushar_Jain, setup=Tushar_Jain_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
