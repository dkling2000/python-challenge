import os
import csv
budgetcsv = os.path.join ("resources","budget_data.csv")
with open(budgetcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# The total number of months included in the dataset
    next(csvreader)
    row_count = sum(1 for row in csvreader)
    print(row_count)


  # The net total amount of "Profit/Losses" over the entire period

  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period
