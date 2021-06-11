from collections import Counter
import matplotlib.pyplot as plt

sales = Counter(banana=15, tomato=14, apple=30,orange=33).most_common()
x, y = zip(*sales)

print(x)
print(y)

plt.bar(x.y)

plt.show()