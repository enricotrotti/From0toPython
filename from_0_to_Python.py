##########################################################################################
#####################                From 0 to Python                #####################
##########################################################################################
#####################              Author: Enrico Trotti             #####################
##########################################################################################

# THIS IS A BEGINNER COURSE WITH EXAMPLES.
# EACH SECTION IS AN EXAMPLE ITSELF. WHEN TRYING ONE, LEAVE THE OTHER COMMENTED:
# NOT GUARANTEED THAT THE SAME VARIABLE IS NOT DEFINED IN MULTIPLE SECTIONS!!

# When starting with Python, always remember the importance of the indentation.


# Exercise: calculate the bmi with the data inserted in the terminal

"""
name = input('Name:  ')
height = input('Height: ')
weigth = input('Weigth: ')
age = input('How old are you? ')
print(type(height)) 
bmi = float(weigth) / float(height)**2
print(F'Your bmi, {name.title()}, is {round(bmi, 2)} and your age is {age}.')
"""
# Same exercise in a single line:

"""print('your bmi', input('Name:  '), 'is', (float(input('Weigth: '))/ float(input('Height: '))**2))"""


#--------------IF

"""
year = float(input('Your age: '))
if 100 > year >= 18:
    print('Now you can drive')
elif year >= 100:
    print('Maybe too old to drive still')
else:
    print('Too young to drive')
"""

# Exercise (EX) of bmi using the command IF

"""
name = input('Name:  ')
height = input('Height (m): ')
weigth = input('Weigth (Kg): ')
bmi = float(weigth) / float(height)**2
if bmi < 19:
    print('You should eat more.')
elif 19 <= bmi < 25:
    print('OK')
elif bmi >= 25:
    print('A bit of sport is a good starting point.')
"""

# Nested IF: instead of several conditions at the same level, we can use another IF inside the ELSE 

"""
bmi= 25
if bmi < 19:
    print('underweight')
else:
    if bmi > 25:
        print('overweight')
    else:
        print('normal')
"""

# We can also add more conditions to test different intervals

"""
bmi = 36
if bmi < 19:
    print('Go to eat!')
elif 19 <= bmi < 25:
    print('OK')
elif bmi >= 25:
    print('Careful')
elif bmi >= 35: #considers only > 25 and not also 35
    print('Roll back to a normal weight.')
else:
    print('')
"""

#-------------WHILE

"""
import random # To call in the code a library (a database of functions)
number = random.randint(0,5) # Any time I run, number is a random integer number between 0 and 5 included
while number < 9:  # As long as this condition is true, continue the loop
    print(number)
    number = number + 1 # redefine number as n+1 and continue the while cycle
"""

# EX: if someone lies saying they're taller than 3 m, ask again.

"""
tall = input ('How tall r u? ')
while float(tall) >= 3:  
    tall = input ('I do not trust you, tell the truth: ')
"""

# EX: Ask the data: name cannot be accepted empty, height must be between 1 and 3 m,
# weight should not be more than 200 Kg (over 200 Kg ask confirmation and with positive answer accept).
# ACHTUNG: name=None means the value 'None'

"""
name = input('name: ') 
while name == '':  # work also the command 'while not name' 
    name = input('Not empty name: ')
height = input('height in m: ') 
while float(height) < 1 or float(height) > 3:  
    height = input('not valid value of height: ') 
weight = float(input('weight: '))
sure = "not"   # I have to initialize: I put anything different from yes
while weight > 200 and sure != "yes":
    weight = float(input('reinsert weight value: '))
    if weight > 200:
        sure = input('Are you sure? (yes/not)')
"""


# In the previous case, with a huge weight, first I am asked to insert again, and then
# I am asked if I am sure. In the next case, it will ask directly if I am sure, before
# asking me to reinsert (weight starts directly in the loop).

"""
init_weight = 200
weight = init_weight + 1
sure = "not"   # to initialize I put anything different from yes
while weight > 200 and sure != "yes":
    weight = float(input('Insert weight value: '))
    if weight > 200:
        sure = input('Are you sure? (yes/not) ')
"""

    
#--------------FOR

"""
for n in range(-10,10,3): # Show all the numbers from - 10 to 10 with steps of 3
    print(n)

for m in range(10):
    print(m, end="")
"""

# Ask n numbers and calculate the average

"""
tot = 0
avg = 0
count = int(input('How many numbers will you insert? '))
for i in range(count):
    tot += int(input('Give me an integer number: '))
avg = tot/count
print(avg)
"""

# Average of 50 random numbers

"""
tot = 0
avg = 0
import random
i = random.randint(0,1000)
for i in range(50):
     tot += random.randint(0,1000)
avg = tot/50
print(avg)
"""

#########################################################################################################################
#####                                         The structure of data                                                 #####
#########################################################################################################################

#-------------LISTS

"""
days = ['mon', 'tue', 'wed', 'thu', 'fri']
print(days, '\n', days[-4:2])   
# days[x:y] valid from -5 to +4. 'mon'=days[0]. If x = -1, then it starts showing the last element in the list. It will thus show 1 element only 
# (since it cannot restart from the first element after the last one). Usually are used the elements -1 (the last element) or the positive indices.

print(days[-1:6]) # [-2:4] is equiv to [3:4], so it gives me the element 3. With [-2:1] and [3:1] I get an empty list.

days.append('sat')  # I add 1 element to the list days
print(days)

days.extend(['sun','mon']) 
# If I want to add 2+ elements, I use extend (I add another list to the previous list, not an element like with append)
print(days)
"""


#EX: build a shopping list (with alreasy apples inside) until the user says 'stop', I finish the list.

"""
shopping_bag =['apples']
print('Starting list: ', shopping_bag)
new = []
while new != 'stop':
    new = input('What I should buy? ')
    shopping_bag.append(new)
    print('List: ', shopping_bag)  # This is printed every loop.

# Now, if you add cucumber, remove from the list (I do not like it)

if 'cucumber' in shopping_bag:
    shopping_bag.remove('cucumber') 
# problem if the element in 'remove' is not in the list. I solve with the command 'if cucumber in shopping_bag:' above the command remove.

# I have to take out the element 'stop'. I can do in 2 ways: 
# .pop(), so that I remove the element 'stop' from the list
# print(shopping_bag[:-1]), the element 'stop' is still a part of the list, but it is not shown

shopping_bag.pop(-1)
print('The final list: ', shopping_bag)

print('The final list: ', shopping_bag[:-1]) 
"""

#----- Ordered lists
"""
days = ['mon', 'tue', 'wed', 'thu', 'fri']
print(sorted(days)) 
# Here the list is printed in ordered way, but the list does not change (the elements of days are strings: alphabetical order)
days.reverse() # I modify the list: I reverse it without ordering.
print(list(reversed(days))) # I print the re-reversed list
days.sort(reverse=True) # This modify the list: put the elements in the reversed order
print(days)
print(days.sort(reverse=True)) # This doesn't work, since sort returns only True or False
"""


# Manipulation of the elements in the lists
"""
letters = ['a', 'b ', 'c', 'd', 'e','f','g']
letters[-1] = 'G' # I substitute the last element
del letters[2] # I can also delete a whole part of the list with [:2]
print(letters)
letters.remove('f') # it eliminates only the first 'f' found
print(letters)
letters.pop(1) #pop() delete the last element pop has output the deleted element: print(list.pop()) returns the last element of the list
print(letters)
"""

# EX: repeat the exercise of the shopping bag, with a blacklist of elements to be removed in case of input

"""
shopping_bag =[]
new_bag = []
blacklist = ['beer','cucumber', 'wine', 'vodka', 'frogs']
while new_bag != 'stop':
    new_bag = input('What I should buy? ')
    shopping_bag.append(new_bag)

for food in blacklist:
    while food in shopping_bag: 
    # Instead of the command WHILE, I could use IF, but in the case the user cheats by inserting 
    # several times a forbidden food, the IF command will delete only one of the equivalent inputs
        shopping_bag.remove(food)
        if food in blacklist[0:2]:
            print(F'I removed {food}. You saved some money!!!')
        if food in blacklist[2:5]:
            print(F'I removed {food}. You saved a lot of money!!!')

# Additionally, since nutella is not too healthy, 
# I decide to substitute with carrots, in the case nutella is an input (IF).
# If nutella is inserted several times, the WHILE does its role.

if 'nutella' in shopping_bag:
    nmr = shopping_bag.index('nutella')
    shopping_bag[nmr] = 'carrots'
    print('I substituted nutella with carrots :)')
while 'nutella' in shopping_bag:
    nmr = shopping_bag.index('nutella')
    shopping_bag[nmr] = 'carrots'
    print('I substituted nutella with carrots, again. STOP CHEATING!!!')

# shopping_bag.pop(-1)     # I pop the element 'stop'
# shopping_bag.sort()      # I order the shopping list
# print('The final list is made of ', int(len(shopping_bag)) ,' elements: ', shopping_bag)
# print(blacklist[0:2])
"""

#EX: Find the lenght of the longest name in a list of stings.
"""
max_name = 0
names = ['Marco Polo', 'Antonio Vivaldi', 'Gioacchino Rossini']
for i in names:
    print(i, len(i))
    if len(i) > max_name:
        max_name = len(i)
print('max length: ', max_name)
"""

#-------------TUPLE (couples)
# Given 2 lists of values (widths and lengths), find the area of the room (room[n]=widths[n]*lenghts[n])
"""
widths = [300, 450, 350, 280]
lengths = [380, 690, 370, 410]
for (a,b) in zip(widths,lengths):
    print("Room: ", a, " x ",b,"area m^2", a*b/10000)
"""

# Now I want to use enumerate: I want to switch an element by associating an index to it.
"""
food = ['beer','cucumber', 'wine', 'vodka', 'frogs']
for i in food:
    if i=='beer':

#       i = 'carrots' #This does not work. It reinitialize every time 'i'

       position = food.index(i)
       food[position] ='carrots' # This works, but not the best way to do it

for (n,i) in enumerate(food):
    if i == 'beer':
        food[n] ='carrots'
"""


#--------List comprehension

# Divide a list of marks into two sublists of sufficient and not sufficient marks.

"""
marks=[20, 18, 25, 30, 11, 14, 18, 19, 21, 27, 28, 13, 16]
passed = []
not_passed = []
for mark in marks:
    if mark >=18:
        passed.append(mark)
    else:
        not_passed.append(mark)

passed = [x for x in marks if x>=18]
# I do not need to initialize passed and not_passed as empty
not_passed = [x for x in marks if x<18]

# As a gift, I increase now all marks by 1
increased =[min(mark+1,30) for mark in marks] 
# 'min' is needed in the case of 30 as initial mark (the highest): I want the min between (30+1=)31 and 30.
print(increased)
# The firsts at the oral will be the even elements of the ordered list
print([ i for (n,i) in enumerate(sorted(increased)) if n % 2 == 0])
"""

#EX:

"""
Temp = [26, 28, 30, 25, 24, 28, 26, 27, 28,35,31,27,22]  
days = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13]
# I want the discrepancy with the Temperature = 27
discr = [t-27 for t in Temp]
print(discr)

hot_cold = ['hot' if i>0 else 'cold' if i<0 else 'normal' for i in discr]
print(hot_cold)

# Now I plot days vs temperature
import matplotlib.pyplot as plt
plt.scatter(days, Temp)
plt.show()

# How many days was it hot or normal?
hot_normal_days = ['hot or normal' for x in hot_cold if x=='hot' or x == 'normal']
print(hot_normal_days, len(hot_normal_days))
"""

# EX:
# Calculate the average (avg) of the heights of some people (in cm). 
# I want to exclude the 0s (reflecting those who did not answered their size).

"""
heights = [165,187,155,0,156,178,149,0,186,158,178] 
avg = sum([i for i in heights])/len([i for i in heights if i>0])
print(avg)
"""

#--------DICTIONARIES (couples key - value)

# In Python I can use equivalently the single quote ' and the double quote "
# In general it is better the double quote, since this is valid also in JSON
# ACHTUNG: LIST have square brackets [], while DICTIONARY has curly brackets {}
"""
person = {"name" : "Vlad",   
        "surname" : "Dracula",
        "years" : 593 
        }
print(person)
print(person['surname']) # Note, to select an element I use [] as for the lists, but calling the corresponding key

person['surname'] = "the Impaler"  # I sustitute the value associated to [surname] in the dictionary: "person"
print(person)

# I add now a new value: differently from the lists, here I do not use append:
person["favourite food"] = "blood"  
# The commands to modify a value and to add a value are written in the same way
print(person)

# To reorder the elements is not simple and is also useless
del person["years"]

# 3 functions of the dictionary
print(list(person.keys()))  # KEYS
print(list(person.values())) # VALUES
print(list(person.items()))  # ITEMS (I get the tuples)

for i in person:  
    print(i)  # Here I get the keys
    print(person[i])  # here I get the values
"""


# EX:
"""
person = {"name" : "",   
         "surname" : ""
         }        # I do not need to initialize the dictionary, if I create it inside the WHILE
people = []
while person['name'] != 'stop':
    person = {}    # I reset the dictionary, since each loop it restarts as not empty and, before appending, it substitute it.
    person['name'] = input("nome ")  
    person['surname'] = input("surname ")
    people.append(person)
    print(people)
people.pop()
print(people)
# The previous example can be also done as follows

people = []
while person['name'] != 'stop': 
    name = input("nome ")  
    cognome = input("surname ")
    person = {"name" :name, "surname":cognome} 
    people.append(person)
    print(people)
people.pop()
print(people)
"""

# I create a dictionary, whith the short version of the months as key
"""
months = ["January", "February", "March", "April"]
d = {nome[:3].upper() :nome for nome in months}
print(d)
"""

#--------------SET
# Like a dictionary, but without a couple. In sets there cannot be double elements that are equals.
"""
shop_list = ["apple", "banana", "ananas", "carrots","apple", "cherries", "ananas", "kiwi"] # I create a SET from a LIST
print(shop_list)
shop_list_set = set(shop_list) # It will remove one of the doubled randomly (the first, the second...) 
# Also the function pop() could eliminate the last element, but remind that the set is randomly ordered
print(shop_list_set)

shop_list_set.add("melon") # If the added element is already in the set, it will not be considered
shop_list_set.remove("apple") # Returns an error if the element is not in the set
print(shop_list_set)
shop_list_set.discard("ananas") # Ok even if the element is not in the set. Thus, for this case, DISCARD is better than REMOVE
print(shop_list_set)

shop_list_set2 = {'cherries', 'strawberries', 'pear', 'mango'}
print(shop_list_set | shop_list_set2) # Union
print(shop_list_set & shop_list_set2) # Intersection
"""

# EX: build a set of random numbers (0 to 9). make it run until the set will not be formed by less than 3 distinct randomly generated numbers
"""
import random
randomset = {random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)}
while len(randomset) > 3:
    print(randomset, len(randomset))
    randomset = {random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)}
print(randomset, len(randomset))
#    Analogously
while True:
    randomset = {random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)}
    print(randomset, len(randomset))
    if len(randomset) < 3:
        break
"""

#--------------FUNCTIONS
"""
import math
def square(number):
    result = number*number
    return result
print(square(5.2))
print(math.sqrt(square(12)+square(5)))

def sum(number):
    result = number + number
    return result
print(sum(35.2))

def vowels(word):
    vocals = {"a","e","i","o","u"}
    message =""
    for i in word:
        if i in vocals:
           message += i
    return word, message  # If I return two or more elements, I get a tuple from the function
print(vowels("aaabbbcccdddeeefff"))

def info(name, surname, country="Italy"):
    print(f'I am {name} {surname} and I live in {country}')
info("Alla", "Dalla")
info("Alia", "Pallia", "Congo")
"""

# EX
"""
def welcome(name, gender="M"): # I set Male gender by default
    if gender=="F":
        print(f'Welcome Ms. {name}')
    else:
        print(f'Welcome Mr. {name}')
welcome("Gianni")
"""
"""
def welcome(name, gender="M"):
    if gender=="F":
        print(f'Welcome Ms. {name}')
    elif gender=="M" or gender=="":
        print(f'Welcome Mr. {name}')
    else:
        print(f'Welcome {gender} {name}')
welcome("Marlo")
welcome("Carla","F")
welcome("Darlo","M")
welcome("Parlo","Other")
"""

# EX:
# Generator of the first part of the Italian Fiscal Code 
# cf(first name, last name, birth, gender), where birth = [ day, month, year ]
# Return:
# - Three characters for last name (first, second, third consonant).
# Extras: Special cases: "Mari" → "MRA," "Bo" → "BOX"
# - Three characters for first name (first, third and fourth consonants).
# Extras: "Marina" → "MRN," "Mario" → "MRA," "Ji" → "JIX"
# - Date of birth encoded with:
# - Year without century (example: 95, 03).
# - Month from a list: (Jan, Feb, Mar, Apr...) = (A, B, C, D, E, H, L, M, P, R, S, T)
# - Day of birth (+ 40 if sex is "F"), two characters (5→05)

"""
def filter_string(s,mode="mode_surname"):
    s=s.upper()  # Local variable
    vowels ="AEIOU"
    s_consonants = ""
    s_vowels =""
    for letter in s:
        if letter in vowels:
            s_vowels += letter
        else:
            s_consonants += letter
    #In mode_name, with at least 4 consonants, I eliminate the second
    if mode == "mode_name" and len(s_consonants) >= 4:
        s_consonants = s_consonants[0] + s_consonants[2:]    # The string is immutable
    reordered = (s_consonants + s_vowels +"XXX")
    return reordered[:3]
    pass

def filter_surname(surname):
    return filter_string(surname)

def filter_name(name):
    return filter_string(name, "mode_name")

def filter_data(birth, sex):
    code_months = "ABCDEHLMPRST"
    result = ""
    result += str(birth[2])[-2:]
    result += code_months[birth[1]-1]
    day_considering_gender = birth[0] + (40 if sex == 'F' else 0)
    if day_considering_gender <= 9:
        result += '0'
    result += str(day_considering_gender)
    return result

def cf(name, surname, birth, sex):
    return filter_surname(surname) + filter_name(name) + filter_data(birth, sex)

print(cf("Niccolò", "Paganini", [27,10,1782], "F"))
"""

# Additional info
"""
def average(*values):   # with '*' I have to know before the number of arguments  
    # *values is an iterable (I can use it in for, if , len...)
    tot = 0
    for x in values:
        tot += x
    return tot/len(values)

print(average (25,50,75,100,125))
"""
"""
def stamp(nome, cognome):
    print(nome.title(), cognome.upper())
stamp("AnnA","KaReninA")
stamp(nome="aNNa",cognome="KaREnInA")
stamp(cognome="karenina",nome="ANnA")
"""
"""
def print_all(**kwargs):
    for i in kwargs.keys():
        print(i,kwargs[i])
    
print_all(brand="Audi", color="red")
print_all(street="Kirchegasse", name="Fischer")
"""

# From another file (example: exercise_fiscal_code) I can import a function (example: cf)
"""
from exercise_fiscal_code import cf
cf
"""

# This is a useful library
"""
import qrcode
img = qrcode.make('https://python.org')
img.save("my_qrcode.png")
"""




