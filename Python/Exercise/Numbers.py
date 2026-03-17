'''
You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
'''
long_field = 92
wide_field = 48.8
area = long_field*wide_field

print(area)
print("Area of a  Football field ; " , round(area,3))# Ans: 4489.599

'''
You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

'''
chips_count = 9
price = 1.49
have_money = 20

rmn_blc = have_money - (chips_count * price)
print("Returned Amount : ",rmn_blc)# Ans: 6.59

'''
You want to replace tiles in your bathroom which is exactly square and 5.5 feet
#    is its length. If tiles cost 500 rs per square feet, how much will be the total
#    cost to replace all tiles. Calculate and print the cost using python
#    Hint: Use power operator (**) to find area of a square
'''

a = 5.5

b = a**2
cost = b * 500
print("Cost of tiles : ",cost)# Ans: 15125.0

'''
4. Print binary representation of number 17
'''
num=17
print('Binary of number 17 is:',format(num,'b')) # Ans: 10001
