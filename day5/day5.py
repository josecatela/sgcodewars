import timeit

killian_setup = '''
from __main__ import killian_day5
'''

def killian_day5(recipe, available):
    cakes = -1
    for ingredient, amount in recipe.items():
        if ingredient in available:
            if cakes == -1:
                cakes = available.get(ingredient, 0) // amount
            else:
                cakes = min(cakes, available.get(ingredient, 0) // amount)
        else:
            return 0
    return cakes

TEST_CODE_killian = '''
result = killian_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

ccquiel_setup = '''
from __main__ import ccquiel_day5
'''

def ccquiel_day5(recipe, available):
    enough = list()
    for ingredient, needed in recipe.items():
        enough.append(available.get(ingredient, 0) // needed)
    return min(enough)

TEST_CODE_ccquiel = '''
result = ccquiel_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

diana_henninger_setup = '''
from __main__ import diana_henninger_day5
'''

def diana_henninger_day5(recipe, available):
    checklist = []
    for item in recipe:
        if item in available:
            checklist.append(available[item] / recipe[item])
        else:
            return 0
    return min(checklist)

TEST_CODE_diana_henninger = '''
result = diana_henninger_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

ggebre_setup = '''
from __main__ import ggebre_day5
'''

def ggebre_day5(recipe, available):
    # list comprehension
    return min([available[key] // recipe[key] if available.get(key) != None else 0 for key in recipe])

TEST_CODE_ggebre = '''
result = ggebre_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

vijaya_lakshmi_setup = '''
from __main__ import vijaya_lakshmi_day5
'''

def vijaya_lakshmi_day5(recipe, available):
    return min(available[key] // recipe[key] if key in available else 0 for key in recipe)

TEST_CODE_vijaya_lakshmi = '''
result = vijaya_lakshmi_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

Prashanth_Kadimisetty_setup = '''
from __main__ import Prashanth_Kadimisetty_day5
'''

def Prashanth_Kadimisetty_day5(recipe, available):
    return min([available[x]//recipe[x] if x in available else 0 for x in recipe])

TEST_CODE_Prashanth_Kadimisetty = '''
result = Prashanth_Kadimisetty_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

David_Nugent_setup = '''
from __main__ import David_Nugent_day5
'''

def David_Nugent_day5(recipe, available):
    return min(available.get(k, 0) // recipe[k] for k in recipe)

TEST_CODE_David_Nugent = '''
result = David_Nugent_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

Kurt_Hinderer_setup = '''
from __main__ import Kurt_Hinderer_day5
'''


def Kurt_Hinderer_day5(recipe, available):
    # setting the max to a rediculous number
    max_cakes = 1000
    # iterate through the ingrediants
    for ingrediant, amount in recipe.items():
        # check to make sure there's enough to make one
        if available.get(ingrediant) >= amount:
            max_cakes = min(max_cakes, available.get(ingrediant) // amount)
        # not enough? can't make the cake and stop looking
        else:
            max_cakes = 0
            break
    return (max_cakes)


TEST_CODE_Kurt_Hinderer = '''
result = Kurt_Hinderer_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

Jose_Catela_setup = '''
from __main__ import Jose_Catela_day5
'''


def Jose_Catela_day5(recipe, available):
    result = 1000000
    for key, value in recipe.items():
        if key in available:
            candidate = available[key] // value
            if result > candidate:
                result = candidate
        else:
            return 0
    return result

TEST_CODE_Jose_Catela = '''
result = Jose_Catela_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

Yang_setup = '''
from __main__ import Yang_day5
'''


def Yang_day5(recipe, available):
    cake = min(available.get(x, 0) // recipe[x] for x in recipe.keys())
    return cake

def David_Nugent_day5(recipe, available):
    return min(available.get(k, 0) // recipe[k] for k in recipe)

def Vanessa_G_day5(recipe, available):
    return min(available[x] // recipe[x] if x in available else 0 for x in recipe)


TEST_CODE_Yang = '''
result = Yang_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

Vanessa_G_setup = '''
from __main__ import Vanessa_G_day5
'''


def Vanessa_G_day5(recipe, available):
    return min(available[x] // recipe[x] if x in available else 0 for x in recipe)

TEST_CODE_Vanessa_G = '''
result = Vanessa_G_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

Oleksandra_Chmel_setup = '''
from __main__ import Oleksandra_Chmel_day5
'''


def Oleksandra_Chmel_day5(recipe, available):
    recipe_keys = set(recipe.keys())
    available_keys = set(available.keys())
    if not recipe_keys.issubset(available_keys):
        return 0
    else:
        return min([available[k] // recipe[k] for k in recipe_keys])


TEST_CODE_Oleksandra_Chmel = '''
result = Oleksandra_Chmel_day5({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
'''

print("Time for killian test code: " + str(timeit.timeit(stmt=TEST_CODE_killian, setup=killian_setup, number=100000)) + " seconds")
print("Time for ccquiel test code: " + str(timeit.timeit(stmt=TEST_CODE_ccquiel, setup=ccquiel_setup, number=100000)) + " seconds")
print("Time for vijaya_lakshmi test code: " + str(timeit.timeit(stmt=TEST_CODE_vijaya_lakshmi, setup=vijaya_lakshmi_setup, number=100000)) + " seconds")
print("Time for diana_henninger test code: " + str(timeit.timeit(stmt=TEST_CODE_diana_henninger, setup=diana_henninger_setup, number=100000)) + " seconds")
print("Time for ggebre test code: " + str(timeit.timeit(stmt=TEST_CODE_ggebre, setup=ggebre_setup, number=100000)) + " seconds")
print("Time for David_Nugent test code: " + str(timeit.timeit(stmt=TEST_CODE_David_Nugent, setup=David_Nugent_setup, number=100000)) + " seconds")
print("Time for Prashanth_Kadimisetty test code: " + str(timeit.timeit(stmt=TEST_CODE_Prashanth_Kadimisetty, setup=Prashanth_Kadimisetty_setup, number=100000)) + " seconds")
print("Time for Kurt_Hinderer test code: " + str(timeit.timeit(stmt=TEST_CODE_Kurt_Hinderer, setup=Kurt_Hinderer_setup, number=100000)) + " seconds")
print("Time for Jose_Catela test code: " + str(timeit.timeit(stmt=TEST_CODE_Jose_Catela, setup=Jose_Catela_setup, number=100000)) + " seconds")
print("Time for Yang test code: " + str(timeit.timeit(stmt=TEST_CODE_Yang, setup=Yang_setup, number=100000)) + " seconds")
print("Time for Vanessa_G test code: " + str(timeit.timeit(stmt=TEST_CODE_Vanessa_G, setup=Vanessa_G_setup, number=100000)) + " seconds")
print("Time for Oleksandra_Chmel test code: " + str(timeit.timeit(stmt=TEST_CODE_Oleksandra_Chmel, setup=Oleksandra_Chmel_setup, number=100000)) + " seconds")
