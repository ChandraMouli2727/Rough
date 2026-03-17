'''
Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable,
one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
'''

a = 'Kammapalyam'
b = 'Atp'
c = 'India'

addr = f'Street is {a} , City is {b} , Country {c}'
print(addr)

'''
Create a variable to store the string "Earth revolves around the sun"
Print "revolves" using slice operator
Print "sun" using negative index
'''
ab = 'Earth revolves around the sun'

print(ab[6:15])
print(ab[-3:])
