from collections import defaultdict

# this how to get counter using modul defauldict from collection
word = "assalamualaikum"
counter = defaultdict(int)

for letter in word :
    counter[letter] += 1

print(counter)