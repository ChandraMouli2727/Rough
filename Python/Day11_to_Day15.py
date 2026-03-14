# Python --> Day 11 Dictionaries & Tuples Key Value pairs
# It is also Known as Maps,HashTables,Associate Arrays
d={"Tom":1234,"rob":23456,"Joe":34567}
print(d["Tom"])
d["Sam"] =5678
print(d)

del d["Sam"]

print(d)

for key in d:
    print("key",key,"Value :",d[key])

print("*****************")
for k,v in d.items():
    print("KEY",k,"VALUE :",v)

print("sam" in d)

d.clear()
print(d)

#Tuple
#It is a list of Values Grouped together

point = (5,9)
print(point[0])

'''
List: All Values have similar Meaning(Homogeneous) 
Tuple: All Values have different meaning(heterogeneous)

List Examples :
exp_lst = [2300,2500,29000,6700] #every item is an exp
list_of_names = ["Bob","Tom","partha"] # every item is a name of the person

Tuple Examples:

point(4,5) #4 is X coordinate , 5 is Y coordinate
addr = ("1 purple street","new york",1001)
tuple is immutable if u change get err
'''

#Python Day 12 --> Modules

'''
import matplotlib

python package index , pip installs python

pip install matplotlib

pip uninstall matplotlib
'''
# python Day 13 --> Modules in python

'''
The Whole idea of "Reuse" Applies to programming as well
Modules is a way to reuse a code written by someone else

'''

import math

print(math.sqrt(16))

print(dir(math))

print(math.pi)
print(math.log10(100))
print(math.log10(1000))
print(math.floor(10.88))
print(math.ceil(10.88))

import calendar

cal = calendar.month(2026,2)
print(cal)

print(calendar.isleap(2026))
print(dir(calendar))

# functions.py & Myprogram.py

# Python Day -->13 JSON Obj
'''
JSON = Java Script Object Notation 
JSon is a data exchange format similar to XML

{"name" : "tom",
"address" : "1 green",
"ph" : 1234
}
xml
<name>tom</name>
<addr>1 green </addr>
<ph>12123</phone>

Json is More lightweight Compared to xml

1)To Create Addr Book and write Some records into it
2)Read this addr book
'''

book = {}
book ['Chandra']= {
    "Name" : "Chandra",
    "Ph":1234}
book ['Mouli']= {
    "Name" : "Mouli",
    "Ph":9876}
print(book)

import  json

s = json.dumps(book) #Converts String obj
print(s)

with open("C:\\Users\\Chandra Mouli\\Desktop\\json","w") as f:
    f.write(s)

'''
you can read this json data using any language that supports json such js,Hence this is called data exchange format(python to JS)
'''
with open("C:\\Users\\Chandra Mouli\\Desktop\\json","r") as f:
      a = f.read()
      print(a)


import json
book = json.loads(a)
type(book)
print(book)
print(book['Chandra'])

for p in book:
    print(book[p])

#python 14 Reading / Writing  Files