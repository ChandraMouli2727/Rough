import time
import threading
def calc_sq(n):
    print("Calculalte Sq no's")
    
    for a in n:
        time.sleep(0.2)
        print('square',a*a)

def calc_cu(n):
    print("Calculalte cube no's")
    
    for a in n:
        time.sleep(0.2)
        print('Cube',a*a*a)

arr = [2,3,8,9]

t = time.time()
calc_sq(arr)
calc_cu(arr)

print("Done in ",time.time() - t)

print("****Using Threading time reduces*****")
print("Here it will run simultaneously like sq,cb")
t1 = threading.Thread(target = calc_sq,args = (arr,)) # here args passing in tuple so added , at last
t2 = threading.Thread(target = calc_cu,args = (arr,))

tm = time.time()
t1.start()
t2.start()

t1.join() # it will wait until firts t1 needs to done for entire process need to complete
t2.join()

print("Done in ",time.time() - tm)

'''
for i in range(10):
    th = Thread(target=func_name, args=(i, ))
    
print total active threads in multithreaded code using threading.active_count()
'''
import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())
