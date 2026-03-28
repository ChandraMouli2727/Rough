import time
import multiprocessing

#Sharing Data Between Processes Using Array and value

def calc_sq(numbers,sq_res,v):
    v.value = 9.63
    for idx, i in enumerate(numbers):
        sq_res[idx] = i*i
    print("Inside  Process   " + str(sq_res[:]))

if __name__ == "__main__":
    arr = [1,2,3,4]
    sq_res = multiprocessing.Array('i',4)
    v = multiprocessing.Value('d',0.0)
    p1 = multiprocessing.Process(target = calc_sq,args =(arr,sq_res,v))
    p1.start()
    p1.join()
    print("Outside process   " + str(sq_res[:]))
    print("Value    " + str(v.value))

#Sharing Data Between Processes Using Queue
