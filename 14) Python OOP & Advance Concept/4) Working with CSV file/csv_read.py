import csv  #csv module open gareko

with open('test.csv') as csv_file:            #test.csv file lai csv_file format ma kholeko
    csv_reader = csv.reader(csv_file, delimiter=',')    #csv.reader chai python le diyeko inbuilt class ho     #delimiter vaneko test.csv file read garda, tesko data lai comma(,) le seperate garera read garxa
    for row in csv_reader:
        print(row)            #row means tyo test.csv file ma vako harek line print garxa
