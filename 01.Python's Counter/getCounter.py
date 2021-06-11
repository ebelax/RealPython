# this how count a letter using dict.get()

word = "assalamualaikum"
counter = {}

for letter in word:
    counter[letter] = counter.get(letter, 0) + 1

print(counter)