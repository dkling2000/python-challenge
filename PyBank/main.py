import os
import csv
csvpath = os.path.join ("resources","budget_data.csv")
rowcount = 0
total = 0
totalpnl_change = 0
pnl_change = 0
pnl = 0
max = 0
min = 0
maxmonth = ""
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) 
# The total number of months included in the dataset
    for row in csvreader:
        rowcount = rowcount + 1
        if rowcount == 1:
            pnl = int(row[1])
        total = total + int(row[1])
        pnl_change = int(row[1]) - pnl
        pnl = int(row[1])
        if max < pnl_change:
            max = pnl_change
            maxmonth = row[0]
        if min > pnl_change:
            min = pnl_change
            minmonth = row[0]
        totalpnl_change += pnl_change
    avgchange = totalpnl_change / (rowcount - 1)
    avg = round(avgchange,2)
    print ('Financial Analysis')
    print('-----------------------------')
    print ('Total months: ' + str(rowcount))
    print ('Total: $' + str(total)) 
    print ('Average Change: $' +str(avg))
    print('Greatest increase in profits: ' + maxmonth + ' '+ '($' + str(max) + ")")
    print('Greatest decrease in profits: ' + minmonth + ' '+ '($' + str(min) +')')
    
output_path = os.path.join("resources", "results.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Category','result'])
    csvwriter.writerow(['Total Months', str(rowcount)])
    csvwriter.writerow(['Average Change', str(avg)])
    csvwriter.writerow(['Greatest increase in profts', maxmonth + ' ' +str(max)])
    csvwriter.writerow(['Greatest decrease in profts', minmonth + ' ' +str(min)])
