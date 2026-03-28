from multiprocessing import Pool


def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f,[1,2,3,4,5]) # func,arr
    #p.close(),p.join()
    for n in result:
        print(n)

'''
utilising all cores /power in the computer parallel processing 
map : process of Dividing work multiple inputs between all cores
reduce : Process of aggregating a results back
array = [1,2.3,4,5]
result = []
for n in array:
result.append(f(n))
print(result)
'''