import argparse

'''
positional
optionall
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1",help ="first number" )
    parser.add_argument("--number2",help ="second  number" )
    parser.add_argument("--operation",help ="operation" ,choices=["add","subtract","mutlipy"])
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)
   # --number is optional
    '''
    Python argparser_commondline.py --number2 5 --number1 4 --operation multiply
    Python argparser_commondline.py --number2 5 --number1 4 
    it will work unsupported
    '''
    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation =="add":
        result = n1 + n2
    elif args.operation == "subtract":
            result = n1 - n2
    elif args.operation == "multiply":
        result = n1 * n2
    else:
        print("Unsupported")
    print("Result : ",result)


'''
Here we are writing a progran that takes 3 inputs

1)First Number
2)Second Number
3)Operation ("add","subtract","multiply")

to  run argparser using pycharm run edit configuration pass values same as in commond prompt
'''