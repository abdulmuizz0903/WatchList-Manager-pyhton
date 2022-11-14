import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
dict = {}

for q in data['Genre']:
    if q in dict:
        dict[q] += 1
    else:
        dict[q] = 1

plt.title("Graph Displaying Your Favoutite Genres")
plt.bar(dict.keys(), dict.values())
plt.show()