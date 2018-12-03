from collections import Counter
import csv

biters = []
def read_csv(file):
    global biters

    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            biters.append(row[2])


read_csv('animal-bites-1.csv')
read_csv('animal-bites-2.csv')
c = Counter(biters)
top_5_biters = c.most_common(5)

print(top_5_biters)