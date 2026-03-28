import time
import multiprocessing

#from MultiThreading_26_Ex import calc_sq,calc_cu

sq_res = []
def calc_sq(numbers):
    global sq_res
    for i in numbers:
        print("Sq of  numbers " + " "+str(i*i))
        sq_res.append(i*i)
    print("Within result  works   " + str(sq_res))


def calc_cu(numbers):
    for i in numbers:
        time.sleep(5)
        print("Cube of  numbers" + str(i*i*i))
if __name__ == "__main__":
    arr = [1,2,3,4]
    p1 = multiprocessing.Process(target = calc_sq,args =(arr,))
    #p2 = multiprocessing.Process(target = calc_cu,args =(arr,))

    p1.start()
    #p2.start()

    p1.join()
   # p2.join()
    print("The result is " + str(sq_res))
    '''
    Every Process has it's own addr space (virtual memory).Thus Program variables are not shared between process
    you need to use interprocess communication (IPC) Techniques if you  want to share data between two process   '''
    print("Done")
