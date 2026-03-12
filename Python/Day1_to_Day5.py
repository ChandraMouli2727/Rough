#Python Intro
'''
1.Very Easy to Learn
  with open(filename) as f:
       for line in f:
           print(line)
2.Code Development Speed
3.Compact easy to Remember code Syntax
4.No Compilation it is intepreter Language it speeds up
5.Library (or Module) for everything PIP is used to install a module
6.Rich Set of Libraries (modules)
7.Open Source
8.Used Heavily in
  i) Data Science
  ii) Machine Learning
  iii)Scientific Computing
9.Plenty of Jobs Numpy in Photon it is Speed..
'''
#Python Day 1 --> Installation
#Python Day 2 --> Variable in Python
# P : Find Out Total Monthly expense given individual expense items
rent = 1220
gas = 202.5
groceries = 305.6

total = rent+gas+groceries
print(total)
print(rent)

item1 = "rent"
item2 = "gas"
item3 = "groceries"

print("Expense Items : ",item1,item2,item3)

#Don't use Keywords in python

import keyword
print(dir(keyword.kwlist))

#Python day 3 --> Numbers
print(12+34,3-4,3/4,4*5,11%2,3**2,2**4)

#P : You are driving from NYC to BM and then going to PS.You want to know how much total distance you will be travelling.
nyc = 188
BM_PS = 247

total_distance = nyc + BM_PS
print(total_distance)
mph = 65
speed = total_distance/mph
print(speed)
print(round(speed,2))
print(10+2*3)
print((10+2)*3)

print(6-5.7)
print(round(6-5.7,2))


#Python day 4 --> Strings
text ="ice cream"
print(text)
print(text[0])
print(text[1])
#text [0] = 'A' It is Immutable
print(text[0:3])
print(text[4:9])
print(text[4:])
print(text[:3])
text = 'Hello'
text = "Hello"
text = 'Hello "World"'
print(text)
addr = '''
Chandra Mouli
HYD
TG
'''
print(addr)

s1 = "Hello"
s2 = "World"

s= s1 + " "+ s2
print(s)

s = "Total States in a USA # "
num = 25
f = s+str(num) #can only concatenate str (not "int") to str
print(f)


#Python day 5 --> Lists
item1 = 'bread'
item2 = 'pasta'
item3 = 'fruits'

items = ['bread','pasta','fruits','veggies']
print(items)
print(items[1])
items[1] = 'Jamun' #we can change list elements
print(items)
print(items [1:2])
print(items [-1])
items.append("Butter")
print(items)
items.insert(2,"PASTA")
print(items)

#Join 2 Lists

food = ['bread','pasta','fruits']
washroom = ['shampoo','soap']
items = food + washroom

# food + 'soda' Can only Concatenate list (not "str") to list
print(items)

print(len(items))

print('bread' in items)
print('Soda' in items)


