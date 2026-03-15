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


