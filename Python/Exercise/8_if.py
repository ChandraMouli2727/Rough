india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# i.Write a program that asks user to enter a city name and it should tell which country the city belongs to

city_name = input(" Enter a City Name :")
if city_name in india:
    print(f'{city_name} City belongs to India')
elif city_name in pakistan:
    print(f'{city_name} City belongs to pakistan')
elif city_name in bangladesh:
    print(f'{city_name} City belongs to bangladesh')
else:
    print(f'{city_name} City Not found a/c to my knw')

'''Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, 
it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"'''
city_name1 = input("Enter a City Name 1: ")
city_name2 = input("Enter a City Name 2: ")

if city_name1 and city_name2 in india:
    print(f'Cities belongs to India')
elif city_name1 and city_name2 in pakistan:
    print(f'Cities belongs to Pakistan')
elif city_name1 and city_name2 in bangladesh:
    print(f'Cities belongs to Bangladesh')
else:
    print("They don't belong to same country")

# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

sugar_level = int(input("Enter sugar level to check range : "))
sugar_level = float(sugar_level)
if sugar_level < 80:
   print(f'Sugar level {sugar_level} is low')
elif sugar_level > 100:
     print(f'Sugar level {sugar_level} is high')
else:
    print("Your sugar is normal, relax and enjoy your life!")
    
