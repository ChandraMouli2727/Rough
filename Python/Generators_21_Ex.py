'''
Generator is a simple way of creating iterator
yield is same as like return but return it will clean up func where yield hold last executation
generators are better no need  to create a iter() & next() methods & don't need to raise exception
'''

def remote_ctrl():
    yield "cnn"
    yield "abc" #
    
r = remote_ctrl()
print(r)
for a in r:
    print(a)
    
def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

for f in fib():
    if f > 13:
        break
    print(f)
    
def sq():
    a = 0
    while True:
        yield a*a
        a += 1

for i in sq():
    if i > 50:
        break
    print(i)
