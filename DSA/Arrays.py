# 1. Let us say your Arrense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly Arrenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total Arrense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your Arrense is 1980 dollar. Add this item to our monthly Arrense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly Arrense list
# based on this

Arr = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",Arr[1]-Arr[0]) # 150

# 2. Find out your total Arrense in first quarter (first three months) of the year
print("Arrense for first quarter:",Arr[0]+Arr[1]+Arr[2]) # 7150

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in Arr) # False

# 4. June month just finished and your Arrense is 1980 dollar. Add this item to our monthly Arrense list
Arr.append(1980)
print("Arrenses at the end of June:",Arr) # [2200, 2350, 2600, 2130, 2190, 1980]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly Arrense list
# based on this
Arr[3] = Arr[3] - 200
print("Arrenses after 200$ return in April:",Arr) # [2200, 2350, 2600, 1930, 2190, 1980]


# 2. You have a list of your favourite marvel super marvel_heros
# marvel_heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

marvel_heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(marvel_heros))
# 2. Add 'black panther' at the end of this list
marvel_heros.append('black panther')
print(marvel_heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
marvel_heros.remove('black panther')
marvel_heros.insert(3,'black panther')
print(marvel_heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
marvel_heros[1:3]=['doctor strange']
print(marvel_heros)
# 5. Sort the list in alphabetical order
marvel_heros.sort()
print(marvel_heros)

max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)
