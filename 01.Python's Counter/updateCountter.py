# how to update Counter value with  .update() function

from collections import Counter

letter = Counter({"i":3, "n":5, "d":2, "a":6, "h":1})

# update counter
letter.update("cahaya")

print("update value the counter")
print(letter)
print()

# sort base on count

most_letter = letter.most_common(3)
print("sort the most 3 appears ")
print(most_letter)

# reverse sort

rev_letter = letter.most_common()[::-1]
print()
print("reverse all for most sequences")
print(rev_letter)