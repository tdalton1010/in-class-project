import csv
import os

title = []
price = []
subscribers = []
reviews = []
length = []

csvpath = os.path.join('Resources', 'WebDevelopment.csv')

with open(csvpath newline = "", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        #add title
        title.append(row[1])
        #add price
        price.append(row[4])
        #add number of subscibers
        subscribers.append(row[5])
        #add amount of reviews
        reviews.append(row[6])
        #determin percent of review left to 2 decimal places
        percent = round(int(row[6])/int(row[5]), 2)

        #Get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(new_length[0])

WholeTuple = zip(title, price, subscribers, reviews,length)
out_path = os.path.join('Resources', 'UdemyOutPut.csv')

with open(out_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    #write header row
    csvwriter.writerow(["Title"])
    csvwriter.writerows(WholeTuple)









