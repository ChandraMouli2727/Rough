'''
exceptions are errors detected at the time of program executation
Road clear = Executing program without any exception
Accident = Exception
Detour = Handling Exception

'''
x = input("Enter Number 1 :  ")
y = input("Enter Number 2 :  ")

try:
   z = int(x)/int(y)
except ZeroDivisionError as e:
    print("Division by Zero Exception")
    z = None

print("Division is :  ",z)

'''
try:
   while road_is_clear():
       drive()
except Accident as e:
        take_detour()
'''

try:
   z = x/int(y)
except TypeError  as e:
   # print("Exception",type(e).__name__)
    print("Type Error Exception  Convert str to int")
    z = None

print("Division is :  ",z)


#Python Day 19 - Raise Exception 
try: 
    raise MemoryError('Memory Error')
except MemoryError as e:
    print(e)
    
try: 
    raise Exception('Memory Error')
except Exception as f:
    print(f)

#You need to define Exception by own using instance/obj of a class
class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("User Defined Exception ",self.msg)
    def handle(self):
        print("Accident Occured Take Detour")
        
try: 
    raise Accident('Crash of 2 cars')
except Accident as f:
   f.print_exception()
   f.handle()
   
def process_file():
    try:
        f = open("C:\\Code\\data.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("Inside Exception")
    finally:
        f.close() # It will close necessary files
        print("Finally")


