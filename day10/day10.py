import timeit
from itertools import groupby

MORSE_CODE ={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

killian_setup = '''
from __main__ import killian_day10
'''

def killian_day10(morse_code):
    while morse_code[0] == ' ':
        morse_code = morse_code[1:]
    while morse_code[len(morse_code)-1] == ' ':
        morse_code = morse_code[:-1]
    words = morse_code.split('   ')
    readable = ""
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            readable += MORSE_CODE[letter]
        readable += ' '
    return readable[: -1]

TEST_CODE_killian = '''
result = killian_day10('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
'''

akash_karan_setup = '''
from __main__ import akash_karan_day10
from __main__ import akash_karan_day10_decode
'''

def akash_karan_day10_decode(bits):
    di={'1':'.','111':'-','0':'','000':' ','0000000':'   '}
    mini=min([len(list(value)) for key,value in groupby(bits.strip("0"))])
    return "".join([di.get(seq,"") for seq in ([key*(len(list(value))/mini) for key,value in groupby(bits)])])
def akash_karan_day10(morseCode):
    return ''.join([MORSE_CODE.get(i, ' ') for i in morseCode.strip().replace('  ', ' ').split(' ')])

TEST_CODE_akash_karan = '''
result = akash_karan_day10(akash_karan_day10_decode('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
'''

ccquiel_setup = '''
from __main__ import ccquiel_day10
from __main__ import ccquiel_day10_decode
'''

def ccquiel_day10_decode(bits):
    bits = bits.strip('0')   
    rates = list()
    rate0 = 0
    rate1 = 0
    for c in bits:
        if c == '0':
            rate0 += 1
        elif rate0:
            if rate0 not in rates:
                rates.append(rate0)
            rate0 = 0
        if c == '1':
            rate1 += 1
        elif rate1:
            if rate1 not in rates:
                rates.append(rate1)
            rate1 = 0
    if rate1 not in rates:
        rates.append(rate1)
    rate = min(rates)
    code = bits.replace('0000000'*rate, '   ').replace('111'*rate, '-').replace('000'*rate, ' ').replace('1'*rate, '.').replace('0'*rate, '')
    return code
def ccquiel_day10(morse_code): 
    MORSE_CODE[''] = ' '    
    decoded = str()
    morse_words = morse_code.strip().split('  ')
    for w in morse_words:
        chars = w.split(' ')
        for c in chars:
            decoded += MORSE_CODE[c]
    return decoded


TEST_CODE_ccquiel = '''
result = ccquiel_day10(ccquiel_day10_decode('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day10
from __main__ import diana_henninger_decodeBits
'''

def diana_henninger_decodeBits(bits):
    # Accept 0's and 1's, return dots, dashes and spaces
    if(len(bits)==0): return '' # empty message
    if(len(bits)==1): return '.' # dot message
    bits_1 = []
    bits_0 = []
    prev = None
    sum = 0
    for bit in bits:
        if prev != bit: # if there is a change
            if prev == '1': 
            # add the new amount of 1s to bits_1
                if sum not in bits_1: bits_1.append(sum)
            elif prev == '0':
            # add the new amount of 0s to bits_0, except for trailing 0s in the beginning
                if sum not in bits_0 and len(bits_1)!=0: bits_0.append(sum)
            sum = 0
        prev = bit
        sum +=1
        if len(bits_0)==3 and len(bits_1)==2: # abort, if we've already found everything
            prev = None
            break
    if prev == '1': # if the message ended in 1s
        if sum not in bits_1: bits_1.append(sum) # add final amount to bits_1
    dot, dash, pause_char, pause_letter, pause_words = None,None,None,None,None
    len_b1 = len(bits_1)
    len_b0 = len(bits_0)
    if len_b1 == 2: # if we have found both dot and dash
        dot = min(bits_1) * '1'
        dash = max(bits_1) * '1'
    elif len_b1 == 1: # if we only found either dot or dash
        b = bits_1[0]
        if len_b0 == 1: # if we also found only one type of pause
            pause = bits_0[0]
            if b <= pause: 
                dot = b * '1' # pause is longer -> dot
                if b < pause:
                    pause_letter = pause * '0' # longer pause
                else: pause_char = pause * '0' # short pause
            else : 
                dash = b *'1' # pause is shorter -> dash
                pause_char = pause *'0' # short pause
        else: dot = b *'1'
    if(len_b0==3): # if we found all types of pauses
        bits_0.sort() 
        pause_char = bits_0[0] *'0' # pause between dots/dashes
        pause_letter = bits_0[1] *'0' 
        pause_words = bits_0[2] *'0' 
    elif(len_b0==2): # if we only found two different pauses
        bits_0.sort()
        pause_char = bits_0[0] *'0'
        pause_letter = bits_0[1] *'0'
    else: pause_char = '0' # to get rid of trailing 0s
    if dash: bits = bits.replace(dash, '-')
    if pause_words: bits = bits.replace(pause_words, '   ')
    if dot: bits = bits.replace(dot, '.')
    if pause_letter: bits = bits.replace(pause_letter, ' ')
    if pause_char: bits = bits.replace(pause_char, '')
    return bits
def diana_henninger_day10(morse_code):
    message = ""
    morse_code_sentence = morse_code.strip().split("   ") # split into words
    for word in morse_code_sentence:
        morse_cord_word = word.split(" ") # split into letters
        for letter in morse_cord_word:
            message+= MORSE_CODE[letter] # decode letter
        message+= ' ' # space after word
    return message[:-1]

TEST_CODE_diana_henninger = '''
result = diana_henninger_day10(diana_henninger_decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
'''

ggebre_setup = '''
from __main__ import ggebre_day10
'''

def ggebre_day10(morse_code):
    words = morse_code.strip().split("   ")
    decoded_words = []
    for word in words:
        decoded_word = ""
        letter = word.split()
        for lett in letter:
            decoded_word += MORSE_CODE[lett]
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)

TEST_CODE_ggebre = '''
result = ggebre_day10('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day10
'''

def vijaya_lakshmi_day10(morse_code):
    #your code here
    words = morse_code.split("  ")
    sentence = ""
    for everyWord in words:
        letters = everyWord.split(" ")
        word = ""
        for everyLetter in letters:
            word += MORSE_CODE.get(everyLetter, "")
        sentence += word + " "
    return sentence.strip()

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day10('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day10
'''

def Prashanth_Kadimisetty_day10(morse_code):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day10('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
'''

David_Nugent_setup = '''
from __main__ import David_Nugent_day10
'''

def David_Nugent_day10(morse_code):
    return min(available.get(k, 0) // recipe[k] for k in recipe)

TEST_CODE_David_Nugent = '''
result = David_Nugent_day10('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day10
from __main__ import Kurt_Hinderer_day10_decode
'''

def Kurt_Hinderer_day10_decode(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    #need to determine the speed of the Morse code
    #need to remove leading and trailing zeros
    bits = bits[bits.find('1'): bits.rfind('1')+1]
    #first line the length of all sets of ones.
    length = 1
    #initializing first int to rediculous number
    zero_strings = [9999]
    ones_strings = [9999]
    #as leading zeros removed, the first character is a 1.
    for i in range(1, len(bits)):
        if bits[i] == bits[i-1]:
            length += 1
        else:
            if bits[i-1] == '1':
                ones_strings.append(length)
            else:
                zero_strings.append(length)
            length = 1
    #might be a stragler ones string, so add it in if there is.
    if length > 0:
        ones_strings.append(length)
    #speed will be the shortest string of ones (please don't only have Ts in the message)
    speed = min(min(ones_strings), min(zero_strings))
    return bits.replace('111'*speed, '-').replace('000'*speed, ' ').replace('1'*speed, '.').replace('0'*speed, '')
def Kurt_Hinderer_day10(morseCode):
    #remove white space
    morseCode.strip()
    #split up the code into words
    morse_words = morseCode.split("  ")
    #initialize the decoded word list
    decoded_words = []
    #loop through the words
    for word in morse_words:
        #initialize the decoded word
        decoded_word = ""
        #split up the morse word into characters
        morse_characters = word.split(" ")
        #loop through the charaters
        for character in morse_characters:
            try: 
                decoded_word += MORSE_CODE[character]
            except:
                decoded_word +=''
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)

TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day10(Kurt_Hinderer_day10_decode('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day10
from __main__ import Jose_Catela_day10_decode
'''

def Jose_Catela_day10_decode(bits):
    bits = bits.strip('0')
    time_unit = 0
    pos1zero = 0
    if '0' in bits:
        while pos1zero < len(bits) and bits[pos1zero] != '0':
            pos1zero += 1
        zeros = 0
        while zeros+pos1zero < len(bits) and bits[zeros+pos1zero] != '1':
            zeros += 1
        uns = 0
        while zeros+pos1zero+uns < len(bits) and bits[zeros+pos1zero+uns] != '0':
            uns += 1
        if uns < zeros:
            time_unit = uns
        else:
            time_unit = zeros
    else:
        time_unit = len(bits)
    return bits.replace('1' * time_unit * 3, '-').replace('0' * time_unit * 7, '   ').replace('1'*time_unit, '.').replace('0'*time_unit*3, ' ').replace('0'*time_unit, '')
def Jose_Catela_day10(morse_code):
    result = ''
    words_in = morse_code.split('   ')
    words_out = []
    for word_in in words_in:
        word_in = word_in.split(' ')
        word_out = ''
        for letter in word_in:
            word_out += MORSE_CODE[letter]
        words_out.append(word_out)
    return ' '.join(words_out)

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day10(Jose_Catela_day10_decode('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
'''

Yang_setup = '''
from __main__ import Yang_day10
'''


def Yang_day10(morse_code):
    dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    val = dict[roman[0]]
    if len(morse_code) == 1: return val
    for i, x in enumerate(roman[1:], 1):
        val += dict[x]
        if dict[roman[i - 1]] < dict[roman[i]]:
            val -= dict[roman[i - 1]] * 2
    return val

TEST_CODE_Yang = '''
result = Yang_day10('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day10
'''


def Vanessa_G_day10(morse_code):
    MORSE_CODE[''] = ' '
    result = ""
    for c in morse_code.split('   '):
        result += ''.join(MORSE_CODE[a] for a in c.split(' ')) + ' '
    return result.strip()

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day10('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day10
from __main__ import Oleksandra_Chmel_decodeBits
'''
def Oleksandra_Chmel_decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    separated = list(''.join(group) for key, group in groupby(bits))
    minimum = len(min(separated, key=len))
    morse_message = [{'0'*7*minimum: '   ','000'*minimum: ' ', '0'*minimum: '', 
                      '111'*minimum: '-', '1'*minimum: '.'}.get(item) for item in separated]
    return ''.join(morse_message)
def Oleksandra_Chmel_day10(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    words = morseCode.replace('   ',' space ').split()
    message = ''
    for letter in words:
        try:
            message += MORSE_CODE[letter]
        except KeyError:
            message += letter.replace('space',' ')
    return message.strip()



TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day10(Oleksandra_Chmel_decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
'''

sjay_setup = '''
from __main__ import sjay_day10
'''


def sjay_day10(morse_code):
    morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    initcode=morse_code.strip().split(" ")
    for ind,cd in enumerate(initcode):
        if(MORSE_CODE.get(cd)==None):
            initcode[ind]= " "
        else:
            initcode[ind]=MORSE_CODE.get(cd)
    for ind,cd in enumerate(initcode):
        if(cd == " " and initcode[ind-1] == " "):
            del initcode[ind]
    return "".join(initcode)


TEST_CODE_sjay = '''
result = sjay_day10('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
'''

#print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=10000)) + " seconds")
#print("Time for killian test code: " + str(timeit.timeit(stmt=TEST_CODE_killian, setup=killian_setup, number=10000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=10000)) + " seconds")
#print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=10000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=10000)) + " seconds")
#print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=10000)) + " seconds")
#print("Time for David_Nugent test code: " + str(timeit.timeit(stmt=TEST_CODE_David_Nugent, setup=David_Nugent_setup, number=10000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=10000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=10000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=10000)) + " seconds")
#print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=10000)) + " seconds")
#print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=10000)) + " seconds")
#print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=10000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=10000)) + " seconds")
#print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=10000)) + " seconds")
