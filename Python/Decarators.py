import  time
from turtledemo.penrose import start
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + "took"+str((end-start)*1000)+"sec")
        return result
    return wrapper

@time_it
def calc_sq(nm):
    #start = time.time()
    result = []
    for number in nm:
        result.append(number*number)
    #end = time.time()
    #print("calc sq "+ str((end-start)*1000)+"mil sec")
    return  result

@time_it
def calc_cu(nm):
   # start = time.time()
    result = []
    for number in nm:
        result.append(number*number*number)
    #end = time.time()
    #print("calc cu " + str((end - start) * 1000) + "mil sec")
    return  result

array = range(1,10)
out_sq = calc_sq(array)
out_cu = calc_cu(array)
print(out_sq)
print(out_cu)