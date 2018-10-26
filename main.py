#import os and csv tools
import os
import csv


#set data file path
tradeCSV = os.path.join('budget_data.csv')
#open data file in location below, read it, store data as csvfile

with open(tradeCSV, "r") as csvfile:
    # make a list to store values
    c1 = []
    total = 0
    months = 0
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header
    header = next(csvreader)
    #loop through rows
    for row in csv.reader(csvfile):
        c1.append(row[1])
        total = total + (int(row[1]))
        months = months + 1
        
        
print("Financial Analysis")
print("------------------------")
print("Total months: " + str(months))
print("Total volume: " + str(total))
        
with open(tradeCSV, "r") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    c2 = []
    for x, y in zip(c1, c1[1:]):

        c2.append(int(x) - int(y))

        totalchange = sum(c2)
        average = totalchange / months
print("Average monthly change: "+ str(average))

greatestincrease = max(c2)
greatestdecrease = min(c2)
print("Greatest increase: " + str(greatestincrease))
print("Greatest decrease: " + str(greatestdecrease))


text_file = open("PYBankFinancials.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------\n")
text_file.write("Total months: " + str(months) + "\n")
text_file.write("Total volume: " + str(total) + "\n")
text_file.write("Average monthly change: " + str(average) + "\n")
text_file.write("Greatest increase: " + str(greatestincrease) + "\n")
text_file.write("Greatest decrease: " + str(greatestdecrease) + "\n")
text_file.close()
     
