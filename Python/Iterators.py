'''
Iterators 
1)What are iterators?
2) Iterator Implementation Using class
'''
a = ["Hey","Bro","you'r","Awesome"]

#processing of one by one in a loop is a Iteration
for i in a:
    print(i)
    
b = dir(a)
print(b)

itr = iter(a)
print(itr)

print(next(itr)) # Remote Control Class next next channel
print(next(itr))
print(next(itr))
print(next(itr))

itr = reversed(a)
print(itr)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

#Example of remote
class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","CN","ABC","ESPN"]
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
