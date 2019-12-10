import timeit

MORSE_CODE ={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

killian_setup = '''
from __main__ import killian_day9
'''

def killian_day9(morse_code):
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
result = killian_day9('.... . -.--   .--- ..- -.. .')
'''

akash_karan_setup = '''
from __main__ import akash_karan_day9
'''

def akash_karan_day9(morse_code):
    return "".join([ MORSE_CODE.get(i," ") for i in morse_code.strip().replace("   ","  ").split(" ")])

TEST_CODE_akash_karan = '''
result = akash_karan_day9('.... . -.--   .--- ..- -.. .')
'''

ccquiel_setup = '''
from __main__ import ccquiel_day9
'''

def ccquiel_day9(morse_code):
    MORSE_CODE[''] = ' '    
    decoded = str()
    morse_words = morse_code.strip().split('  ')
    for w in morse_words:
        chars = w.split(' ')
        for c in chars:
            decoded += MORSE_CODE[c]
    return decoded

TEST_CODE_ccquiel = '''
result = ccquiel_day9('.... . -.--   .--- ..- -.. .')
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day9
'''

def diana_henninger_day9(morse_code):
    message = ""
    morse_code_sentence = morse_code.split("   ") # split into words
    for word in morse_code_sentence:
        morse_cord_word = word.split(" ") # split into letters
        morse = False # to check for trailing ''
        for letter in morse_cord_word:
            if(letter!=''):
                message+= MORSE_CODE[letter] # decode letter
                morse = True
        if morse: message += ' ' # space after word
    return message[:-1]

TEST_CODE_diana_henninger = '''
result = diana_henninger_day9('.... . -.--   .--- ..- -.. .')
'''

ggebre_setup = '''
from __main__ import ggebre_day9
'''

def ggebre_day9(morse_code):
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
result = ggebre_day9('.... . -.--   .--- ..- -.. .')
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day9
'''

def vijaya_lakshmi_day9(morse_code):
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
result = vijaya_lakshmi_day9('.... . -.--   .--- ..- -.. .')
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day9
'''

def Prashanth_Kadimisetty_day9(morse_code):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day9('.... . -.--   .--- ..- -.. .')
'''

David_Nugent_setup = '''
from __main__ import David_Nugent_day9
'''

def David_Nugent_day9(morse_code):
    return min(available.get(k, 0) // recipe[k] for k in recipe)

TEST_CODE_David_Nugent = '''
result = David_Nugent_day9('.... . -.--   .--- ..- -.. .')
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day9
'''


def Kurt_Hinderer_day9(morse_code):
    # I'm going to return this string and initializing here so I can add to it.
    decode = ""
    # No remove white space at beginning and end
    morse_code.strip()
    # Break the code into words
    word_breaks = morse_code.split("   ")
    # Break the words into characters
    word_characters = []
    for word in word_breaks:
        characters = word.split(" ")
        # I'm not sure why but we got some '' words in there
        if characters !=['']:
            word_characters.append(characters)
    i = 0
    # now changing the characters into letters/codes
    for word in word_characters:
        for character in word:
            if MORSE_CODE.get(character):
                decode += MORSE_CODE.get(character)
        if i < len(word_characters) - 1:
            decode += " "
        i += 1
    return(decode)


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day9('.... . -.--   .--- ..- -.. .')
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day9
'''

def Jose_Catela_day9(morse_code):
    morse_code = morse_code.strip()
    result = ''
    words_in = morse_code.split('   ')
    words_out = []
    for word_in in words_in:
        letters = word_in.split(' ')
        word_out = ''
        for letter in letters:
            word_out += MORSE_CODE[letter]
        words_out.append(word_out)
    return ' '.join(words_out)

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day9('.... . -.--   .--- ..- -.. .')
'''

Yang_setup = '''
from __main__ import Yang_day9
'''


def Yang_day9(morse_code):
    dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    val = dict[roman[0]]
    if len(morse_code) == 1: return val
    for i, x in enumerate(roman[1:], 1):
        val += dict[x]
        if dict[roman[i - 1]] < dict[roman[i]]:
            val -= dict[roman[i - 1]] * 2
    return val

TEST_CODE_Yang = '''
result = Yang_day9('.... . -.--   .--- ..- -.. .')
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day9
'''


def Vanessa_G_day9(morse_code):
    MORSE_CODE[''] = ' '
    result = ""
    for c in morse_code.split('   '):
        result += ''.join(MORSE_CODE[a] for a in c.split(' ')) + ' '
    return result.strip()

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day9('.... . -.--   .--- ..- -.. .')
'''

Memo_Hurtado_setup = '''
from __main__ import Memo_Hurtado_day9
'''


def Memo_Hurtado_day9(morse_code):
    words_list = list(morse_code.split('   ')) 
    readable_list = []
    for word in words_list:
        letter_list = list(word.split(' '))
        for letter in letter_list:
            if letter != '':
                readable_list.append(MORSE_CODE[letter])
        readable_list.append(' ')
    return ''.join( readable_list).strip()

TEST_CODE_Memo_Hurtado = '''
result = Memo_Hurtado_day9('.... . -.--   .--- ..- -.. .')
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day9
'''


def Oleksandra_Chmel_day9(morse_code):
     # ToDo: Accept dots, dashes and spaces, return human-readable message
    words_morse = morse_code.split('   ')
    message = []
    for word in words_morse:
        letters = word.split()
        word_eng = ''.join(MORSE_CODE[symbol] for symbol in letters)
        message.append(word_eng)
    return ' '.join(message).strip()


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day9('.... . -.--   .--- ..- -.. .')
'''

sjay_setup = '''
from __main__ import sjay_day9
'''


def sjay_day9(morse_code):
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
result = sjay_day9('.... . -.--   .--- ..- -.. .')
'''

print("Time for akash_karan test code: " + str(timeit.timeit(stmt=TEST_CODE_akash_karan, setup=akash_karan_setup, number=100000)) + " seconds")
print("Time for killian test code: " + str(timeit.timeit(stmt=TEST_CODE_killian, setup=killian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
#print("Time for David_Nugent test code: " + str(timeit.timeit(stmt=TEST_CODE_David_Nugent, setup=David_Nugent_setup, number=100000)) + " seconds")
#print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
#print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Memo_Hurtado test code: " + str(timeit.timeit(stmt=TEST_CODE_Memo_Hurtado, setup=Memo_Hurtado_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
print("Time for sjay test code: " + str(timeit.timeit(stmt=TEST_CODE_sjay, setup=sjay_setup, number=100000)) + " seconds")
