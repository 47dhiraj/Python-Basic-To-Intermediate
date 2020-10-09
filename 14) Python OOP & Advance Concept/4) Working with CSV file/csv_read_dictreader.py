#csv file ma vako csv file lai dictionary data ma laijane tarika
import csv

with open('test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)         #csv format ma vako file lai dictionary data structure ma lagera read garxa
    for row in csv_reader:           #ek choti ma auta row read garxa
        a = dict(row)
        print(a)

