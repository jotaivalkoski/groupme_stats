__author__ = 'brent'

import csv

csv_file = "Yardslist.csv"
people = "people at"
houses = ["prospect", "empire", "upgrade", "summit", "palace", "green house", "super 8", "armpit", "dive", "pine", "upper deck", "hunting camp"]
houseCounts = {}
peopleCounts = {}
for house in houses:
    houseCounts[house] = 0

f = open(csv_file, 'rU')
reader = csv.reader(f)

for row in reader:
    person = row[2]
    message = row[3].lower()
    if "people at" in message:
        if person in peopleCounts:
            peopleCounts[person] = peopleCounts[person] + 1
        else:
            peopleCounts[person] = 1
        for house in houses:
            if house in message:
                houseCounts[house] = houseCounts[house] + 1
print houseCounts
print peopleCounts

import matplotlib.pyplot as plt


plt.bar(range(len(peopleCounts)), peopleCounts.values(), align='center')
plt.xticks(range(len(peopleCounts)), peopleCounts.keys())

plt.show()
# for row in reader:
#     if ("people at" in row[2].lower()):
#         print row
