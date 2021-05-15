#QUESTION 1
#PIYUSH GOEL


import csv

filename = 'input.csv'

data=[]
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)  #reading the CSV file
    for row in datareader:
        data.append(row[0])    #reading the rows and putting strings into a single column

for i in range(0,len(data[0])):
    for j in range(0,len(data[1])):
        for k in range(0,len(data[2])):
            print(data[0][i]+data[1][j]+data[2][k], end=' ')