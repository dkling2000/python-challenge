import os
import csv
csvpath = os.path.join ("resources","election_data.csv")
tvote = 0
kvote = 0
cvote = 0
lvote = 0
ovote = 0
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) 
# Looping through data to get vote totals
    for row in csvreader:
        tvote = tvote + 1
        if row[2] == "Khan":
            kvote = kvote +1
        elif row[2] == "Correy":
            cvote = cvote + 1
        elif row[2] == "Li":
            lvote = lvote + 1
        elif row[2] == "O'Tooley":
            ovote = ovote + 1
# Calcs to determine totals and percentages
kpct = "{:.3%}".format(kvote/tvote)
cpct = "{:.3%}".format(cvote/tvote)
lpct = "{:.3%}".format(lvote/tvote)
opct = "{:.3%}".format(ovote/tvote)
#determining the winner
if kvote > cvote and kvote > lvote and kvote > ovote:
    winner = "Khan"
elif cvote > kvote and cvote > lvote and cvote > ovote:
        winner = "Correy"
elif lvote > kvote and lvote > cvote and lvote > ovote:
    winner = "Li"
elif ovote > kvote and ovote > cvote and ovote > lvote:
    winner = "O'Tooley"
    
#printing results
print('Election Results')
print('--------------------------')
print('Total Votes: ' + str(tvote))
print('--------------------------')
print('Khan: ' + str(kpct) + ' ' + '(' + str(kvote)+")")
print('Correy: ' + str(cpct) + ' ' + '(' + str(cvote)+")")
print('Li: ' + str(lpct) + ' ' + '(' + str(lvote)+")")
print("O'Tooley: " + str(opct) + ' ' + '(' + str(ovote)+")")
print('--------------------------')
print ("Winner: " + winner)
#writing results out
output_path = os.path.join("resources", "results.csv")
with open(output_path, 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile, delimiter=',')   
    csvwriter.writerow(['Candidate', 'Percentage of Vote', 'Candidate Vote Total'])
    csvwriter.writerow(['Total Votes', str(tvote),''])
    csvwriter.writerow(['Khan', str(kpct), str(kvote)])
    csvwriter.writerow(['Correy', str(cpct), str(cvote)])
    csvwriter.writerow(['Li', str(lpct), str(lvote)])
    csvwriter.writerow(["O'Tooley", str(opct), str(ovote)])
    csvwriter.writerow(['Winner', winner, ""])