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
        self.Max = 10
        # self.arr = ['' for i in range(self.Max)]
        self.arr = [[] for i in range(self.Max)]  # collision handling
 
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
        # self.arr[h] = value
        found = False
        for idx,element in enumerate (self.arr[h]):
            if len(element) == 2 and element[0] == key:
               self.arr[h][idx] = (key,value) # tuple is immutable so directly removed a element and added
               found = True
               break
        if not found:
           self.arr[h].append((key,value))
    
    def __getitem__(self,key):
        h = self.get_hash(key) 
        #return self.arr[h]
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        # self.arr[h] = None
        for index,element in enumerate (self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
        

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

'''
chaining / collosion means hash code is same for 2 keys we can store it as key value 2.method  is linear probing it will search empty slot and store it
'''
tt = HashTable()
z = tt.get_hash("march 6")
print(z)
y = tt.get_hash("march 17")
print(y)
tt['march 6'] = 420
tt['march 17'] = 520
tt['a@XYZ'] = 320
print(tt.arr)
del tt['a@XYZ']
print(tt.arr)
print(tt['march 17'])
