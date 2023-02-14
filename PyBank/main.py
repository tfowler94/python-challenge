#Dependencies
import os
import csv

#Specify folder and csv to read. Specify folder and csv to output analysis.
csvpath = os.path.join('Resources','budget_data.csv')
output_path = os.path.join('analysis','analysis.txt')

#Read CSV file
with open (csvpath) as csv_file:
    csv_reader= csv.reader(csv_file)
    csv_header=next(csv_reader)
    
    #Set variables to blank
    months = []
    netchange = []
    profitloss = []
    
    for row in csv_reader:
        profitloss.append(int(row[1]))
        months.append(row[0])

    #Open file using write mode.Specify the variable to hold the contents. Print title and separator.
    f=open(output_path, "w")
    print("Financial Analysis")
    print("Financial Analysis", file=f)
    print("-----")
    print("-----", file=f)
    
    #Print analysis titles
    print("Total Months:", len(profitloss))
    print("Total Months:", len(profitloss),file=f)
    print("Total Profit: $", sum(profitloss))
    print("Total Profit: $", sum(profitloss),file=f)
    
    #For loop to pull in the needed data
    for x in range(1,len(profitloss)):
        netchange.append(profitloss[x] - profitloss[x-1])   
        avg_change = sum(netchange)/len(netchange)
        max_change = max(netchange)
        min_change = min(netchange)
        max_change_month=str(months[netchange.index(max_change)+1])
        min_change_month=str(months[netchange.index(min_change)+1])
    
    #Print final data analysis
    print("Avereage Revenue Change: $",round(avg_change, 2))
    print("Avereage Revenue Change: $",round(avg_change, 2),file=f)
    print("Greatest Increase in Revenue:",max_change_month,"($", max_change,")")
    print("Greatest Increase in Revenue:",max_change_month,"($", max_change,")",file=f)
    print("Greatest Increase in Revenue:",min_change_month,"($", min_change,")")
    print("Greatest Increase in Revenue:",min_change_month,"($", min_change,")",file=f)