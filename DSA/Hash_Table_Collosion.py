'''
when you store values in a list while retriving a element you need to do n computations for for that we can use Dictionary 

stock_prices = []
stock_prices_dict = {}
with open("stock_prices) as f:
  for line in f:
      tokens = line.split(',')
      day = tokens[0]
      price = float(tokens[1])
      stock_prices.append([day,price])
      stock_prices_dict[day] = price
      
for element in stock_prices:# 0(n)
  if element[0] =='march 9';
     print(element[1])

stock_prices_dict['march'] # 0(1)
'''

'''
For Dictionary backend it will create a hash func to store a data
for list it is normal int index whereas dict it is string index in hash table

hash func will create using ascii code 
'''

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char) # it will give ascii value
    return h % 100 # mod(h,10)
    
print(ord('m'))
print(ord('a'))

a = get_hash('march 6') #609 --> 9
print(a)


class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = ['' for i in range(self.Max)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char) # it will give ascii value
        return h % self.Max # mod(h,10)
        
    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def get(self,key):
        h = self.get_hash(key) 
        return self.arr[h]
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __getitem__(self,key):
        h = self.get_hash(key) 
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        

t = HashTable()
b = t.get_hash('march 6')
print(b)
c = t.add('march 6',120)
print(c)
d = t.get('march 6')
print(d)

t['march 5'] = 236 # familiar way to add elements in dict & retrival
f = t['march 5']
t['march 1'] = 123
t['dec 1'] = 100
print(f)
del t['march 5']
g = t.arr
print(g)
