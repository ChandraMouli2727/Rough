a = '''
Two roads diverged in a yellow wood,

And sorry I could not travel both

And be one traveler, long I stood

And looked down one as far as I could

To where it bent in the undergrowth;



Then took the other, as just as fair,

And having perhaps the better claim,

Because it was grassy and wanted wear;

Though as for that the passing there

Had worn them really about the same,



And both that morning equally lay

In leaves no step had trodden black.

Oh, I kept the first for another day!

Yet knowing how way leads on to way,

I doubted if I should ever come back.



I shall be telling this with a sigh

Somewhere ages and ages hence:

Two roads diverged in a wood, and Iâ€”

I took the one less traveled by,

And that has made all the difference.
'''

words = {}
for line in a.splitlines():   # ✅ split into lines
    tokens = line.split(' ')
    for token in tokens:
        token = token.strip()   # removes spaces/newlines
        if token:               # skip empty strings
            if token in words:
                words[token] += 1
            else:
                words[token] = 1

print(words)

'''
arr = []

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature.Ignore the row")
'''



arr = []
with open("C:\\Users\\Chandra Mouli\\Desktop\\Ai_Eng\\rough\\nyc_weather.csv","r") as f :
    for line in f:
         tokens = line.split(',')
         try:
             temperature = int(tokens[1])
             arr.append(temperature)
         except:
             print("Invalid temperature.Ignore the row")

print(arr)
'''
Exercise: Hash Table: New York City Weather Analysis
(1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

  (a) What was the average temperature in first week of Jan

  (b) What was the maximum temperature in first 10 days of Jan

  Figure out data structure that is best for this problem
'''

avg = sum(arr[0:7])/len(arr[0:7])
print(avg)

max_m = max(arr[0:10])

print(max_m)

''' The best data structure to use here was a list because all we wanted was access of temperature elements '''

'''
(2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

  (a) What was the temperature on Jan 9?

  (b) What was the temperature on Jan 4?

  Figure out data structure that is best for this problem
  
  
The best data structure to use here was a dictionary (internally a hash table) because we wanted to know temperature for specific day, 
requiring key, value pair access where you can look up an element by day using O(1) complexity
'''

weather_dict = {}

with open("C:\\Users\\Chandra Mouli\\Desktop\\Ai_Eng\\rough\\nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")

print(weather_dict)
print(weather_dict['Jan 9'])
print(weather_dict['Jan 4'])

with open("C:\\Users\\Chandra Mouli\\Desktop\\Ai_Eng\\rough\\poem.txt","r") as f:
    for line in f:
        print(line)


word_count = {}
with open("C:\\Users\\Chandra Mouli\\Desktop\\Ai_Eng\\rough\\poem.txt","r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token=token.replace('\n','')
            if token in word_count:
                word_count[token]+=1
            else:
                word_count[token]=1

print(word_count)