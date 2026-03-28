
import multiprocessing
def calc_sq(numbers,q):
    for i in numbers:
        q.put(i*i)


if __name__ == "__main__":
    arr = [1,2,3,4]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target = calc_sq,args =(arr,q))
    p1.start()
    p1.join()

    while q.empty() is  False:
        print(q.get())

'''
multiprocessing Queue   Queue Module

shared                                      lives in-process
between processes             share data between threads
'''