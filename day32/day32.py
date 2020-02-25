import timeit


Akash_Karan_setup = '''
from __main__ import Akash_Karan_day32
'''

def Akash_Karan_day32(n):
    se=[]
    for i in range(1,n+1):
        res=Akash_Karan_chk_day32(i)
        if(res==1):
            se.append(i)
    return se

def Akash_Karan_chk_day32(n):
    li=[]
    x=0
    while(x!=1):
        x=Akash_Karan_sq_day32(n)
        if(x in li):
            return 0
            break
        li.append(x)
        n=x
    return 1

def Akash_Karan_sq_day32(no):
    sum=0
    no=str(no)
    for n in no:
        sum=sum+int(n)**2
    return sum

TEST_CODE_Akash_Karan = '''
result = Akash_Karan_day32(100)
'''

ccquiel_setup = '''
from __main__ import ccquiel_day32
'''

def ccquiel_is_happy_day32(m):
    mseq = list()
    while True:
        msum = sum(int(i)**2 for i in str(m))
        if msum == 1:
            return True
        if msum in mseq:
            return False
        mseq.append(msum)
        m = msum

def ccquiel_day32(n):
    happy = list()
    for m in range(1, n+1):
        if ccquiel_is_happy_day32(m):
            happy.append(m)
    return happy

TEST_CODE_ccquiel = '''
result = ccquiel_day32(100)
'''

charlie_ang_setup = '''
from __main__ import charlie_ang_day32
'''

def charlie_ang_is_happy_number_day32(n):
    current_sum, matched = n, set()
    while current_sum not in matched:
        matched.add(current_sum)
        current_sum = sum(int(i)**2 for i in str(current_sum))
        if current_sum == 1:
            return True
    return False 

def charlie_ang_day32(n):
    return [i for i in range(1, n+1) if charlie_ang_is_happy_number_day32(i)]

TEST_CODE_charlie_ang = '''
result = charlie_ang_day32(100)
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day32
'''

def diana_henninger_is_happy_number_day32(n):
    nums = []
    while True:
        if n==1: return True
        if n in nums: return False
        nums.append(n)
        num = 0
        if n >= 10:
            while n >= 10:
                temp = n%10
                num += temp**2
                n = n//10
        num += n**2
        n = num

def diana_henninger_day32(n):
    return [x for x in range(1,n+1) if diana_henninger_is_happy_number_day32(x)]

TEST_CODE_diana_henninger = '''
result = diana_henninger_day32(100)
'''

Jens_setup = '''
from __main__ import Jens_day32
'''

def Jens_sqare_sum_day32(n):
    s_sum = 0
    for digit in str(n):
        s_sum += int(digit)**2
    return s_sum

def Jens_day32(n):
    happy_list = []
    for i in range(1, n+1):
        number_list = []
        number = Jens_sqare_sum_day32(i)
        while True:
            if number in number_list:
                break
            elif number == 1:
                happy_list.append(i)
                break
            else:
                number_list.append(number)
                number = Jens_sqare_sum_day32(number)    
    return happy_list

TEST_CODE_Jens = '''
result = Jens_day32(100)
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day32
'''

def Kurt_Hinderer_day32(n):
    happy_num = [1]
    unhappy_num = []
    for i in range(2, n+1):
        sequence = [i]
        next_num = i
        done = False
        if i in happy_num + unhappy_num:
            done = True
        while not done:
            num_str = str(next_num)
            next_num = 0
            for j in range(len(num_str)):
                next_num += int(num_str[j])**2
            if next_num in happy_num:
                happy_num += sequence
                done = True
            elif next_num in unhappy_num + sequence:
                unhappy_num += sequence
                unhappy_num.append(next_num)
                done = True
            sequence.append(next_num)
    happy_num.sort()
    i = len(happy_num)-1
    while happy_num[i] > n:
        happy_num.remove(happy_num[i])
        i -= 1
    return happy_num

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day32(100)
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day32
'''

def Oleksandra_Chmel_day32(n):
    if n == 1: return [1]
    happy = [1]
    def check(num):
        b = []
        while num not in b: 
            b.append(num)
            num_str = str(num)
            a = 0
            for val in num_str:
                a += int(val) ** 2
            num = a
        return num       
    for i in range(2,n+1):
        if check(i) == 1:
            happy.append(i)
    return happy

TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day32(100)
'''

Viji_setup = '''
from __main__ import Viji_day32
'''

def Viji_day32(n):
    happy_number_array = []
    for i in range(1, n+1):
        current_array = []
        value = i
        while True:      
            value = sum(int(c) ** 2 for c in str(value))
            current_array.append(value)            
            if value == 1 :
                happy_number_array.append(i)                
                break
            if len(current_array) != len(set(current_array)):
                break
              
    return happy_number_array

TEST_CODE_Viji = '''
result = Viji_day32(100)
'''

Yang_setup = '''
from __main__ import Yang_day32
'''

def Yang_loops_day32(x): 
    ss = []
    while True: 
        k = sum(int(d)**2 for d in str(x))
        ss.append(k) 
        if ss.count(k)>1: 
            return None
        elif k==1: 
            return x
        x = k 
        
def Yang_day32(n):
    return [x for x in range(1,n+1) if Yang_loops_day32(x) ] 

TEST_CODE_Yang = '''
result = Yang_day32(100)
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_Akash_Karan, setup=Akash_Karan_setup, number=1000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=1000)) + " seconds")
print("Time for charlie_ang test code: " + str(timeit.timeit(stmt=TEST_CODE_charlie_ang, setup=charlie_ang_setup, number=1000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=1000)) + " seconds")
print("Time for Jens test code: " + str(timeit.timeit(stmt=TEST_CODE_Jens, setup=Jens_setup, number=1000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=1000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=1000)) + " seconds")
print("Time for Viji test code: " + str(timeit.timeit(stmt=TEST_CODE_Viji, setup=Viji_setup, number=1000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=1000)) + " seconds")
