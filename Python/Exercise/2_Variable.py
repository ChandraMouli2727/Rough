
'''
Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.

break=5
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 1
    break=5
         ^
SyntaxError: invalid syntax '''
'''
Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables
'''
birth_year=2001
current_year=2026
age=current_year-birth_year
print(age)

'''
Store your first, middle and last name in three different variables and then print your full name using these variables
'''
first="Perumallagari "
middle="Chandra "
last="Mouli"
print("My full name is: " + first + " " + middle + " " + last)


'''
Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue
1record = a
print(1record)

ERROR!
Traceback (most recent call last):
  File "<main.py>", line 1
    1record = a
    ^
SyntaxError: invalid decimal literal
'''



'''
record-one = b
print(record-one)

ERROR!
Traceback (most recent call last):
  File "<main.py>", line 2
    record-one = b
    ^^^^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
'''



'''
record^one = c
print(record^one)

ERROR!
Traceback (most recent call last):
  File "<main.py>", line 4
    record^one = c
    ^^^^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
'''



'''

continue = d
print(continue)

ERROR!
Traceback (most recent call last):
  File "<main.py>", line 2
    continue = d
             ^
SyntaxError: invalid syntax
'''

