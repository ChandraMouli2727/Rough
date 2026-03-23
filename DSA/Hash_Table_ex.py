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



