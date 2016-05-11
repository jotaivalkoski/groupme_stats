__author__ = 'brent'

import csv

cities = "cities_crew2.csv"
yoop = "Yardslist5.csv"

csv_file = cities
messageCounts = {}
likeCounts = {}

f = open(csv_file, 'rU')
reader = csv.reader(f)

for row in reader:

    person = row[2]
    uperson = unicode(person, "utf-8")
    if len(person) > 100:
        print person
    message = row[3]
    likeCount = 0
    if len(row) > 4:
        likeCount = float(row[4])
    if person == "Katie":
        person = "Katie Harmala"
    if person == "Tom":
        person = "Tom Halt"
    if person == "Tom Anderson" or person == "James Woods" or person == "Jean Claude van damme" or person == "Chicken Wings' StoBird America" or person == "Thomas America" or person == "Tom but not Tom Halt" or person == "Tommy Two Gloves" or person == "Jake  Junttila" or person == "Jean-Claude Camille Fran\xc3\xa7ois Van Varenberg":
        person = "Stoic"
    if person == "Clark":
        person = "Clark Kangas"
    if person == "Alexa Johnson :)":
        person = "Alexa Johnson"
    if person == "Yard":
        person = "Yard Dog"
    if person == "Boob":
        person = "Bret Frantti"
    if person == "Bruce":
        person = "Bruce Pietila"

    if uperson in messageCounts:
        messageCounts[uperson] = messageCounts[uperson] + 1
    else:
        messageCounts[uperson] = 1

    if uperson in likeCounts:
        likeCounts[uperson] = likeCounts[uperson] + likeCount
    else:
        likeCounts[uperson] = likeCount

filteredMessageCounts = {k:v for k,v in messageCounts.iteritems() if v >= 0}

sortedFreq = sorted(messageCounts.values())
sortedNamesByMessageCount = sorted(messageCounts, key=messageCounts.__getitem__)


sortedLikes = sorted(likeCounts.values())
sortedNamesByLikesCount = sorted(likeCounts, key=likeCounts.__getitem__)


likeToMessageRatio = {}
for person in filteredMessageCounts:
    likeToMessageRatio[person] = likeCounts[person] / messageCounts[person]

sortedLPM = sorted(likeToMessageRatio.values())
sortedNamesByLPM = sorted(likeToMessageRatio, key=likeToMessageRatio.__getitem__)


keep = -25
sortedFreqTrimmed = sortedFreq[keep:]
sortedNamesTrimmed = sortedNamesByMessageCount[keep:]

sortedLikesTrimmed = sortedLikes[keep:]
sortedNamesByLikesCountTrimmed = sortedNamesByLikesCount[keep:]

sortedLPMTrimmed = sortedLPM[keep:]
sortedNamesByLPMTrimmed = sortedNamesByLPM[keep:]

if csv_file == cities:
    title = "Cities"
else:
    title = "Yoop"

totalMessages = "Total Messages"
totalLikes = "Total Likes"
LPM = "Likes Per Message"

mode = LPM

if mode == totalMessages:
    graphedFreq = sortedFreqTrimmed
    graphedNames = sortedNamesTrimmed
    yLabel = "Messages"
elif mode == totalLikes:
    graphedFreq = sortedLikesTrimmed
    graphedNames = sortedNamesByLikesCountTrimmed
    yLabel = "Likes"
elif mode == LPM:
    graphedFreq = sortedLPMTrimmed
    graphedNames = sortedNamesByLPMTrimmed
    yLabel = "Likes Per Message"


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.bar(range(len(graphedFreq)), graphedFreq, align='center')
plt.xticks(range(len(graphedFreq)), graphedNames)
plt.ylabel(unicode(yLabel))

plt.title(title + " GroupMe " + mode)

ax.set_xticklabels(graphedNames)

locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.gcf().subplots_adjust(bottom=0.20)

plt.show()

