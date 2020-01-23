import os
import csv

# Path to collect data from the resources folder
budget_path=os.path.join('..','Pybank/Resources','budget_data.csv')

# open the csv file
with open(budget_path,'r') as budget_csv:
    budget_file=csv.reader(budget_csv,delimiter=',')
# skip the header row
    next(budget_file)

# Create a list of month data and profit/loss data 
    month=[]
    profit=[]
    for row in budget_file:   
        month.append(row[0])
        profit.append(row[1])
# Count the total number of months included in the dataset
# Calculate The net total amount of "Profit/Losses" over the entire period
        monthcount=0
        nettotal=0
        monthcount = len(month)
        nettotal = sum(int(p) for p in profit)
        
# To start the iteration again
    budget_csv.seek(0)
# skip the header row again
    next(budget_file)
    def averagechange(profit):
        # The average of the changes in "Profit/Losses" over the entire period
        # Total change equals to (2nd value-1st value)+(3rd value-2nd value)+...+(last value-second last value)) equals to (last value-first value)
        # Total times of change equals to (month count -1), e.g. with in 2 months, there is 1 change
        lastvalue=float(profit[-1])
        firstvalue=float(profit[0])
        average=round((float(lastvalue-firstvalue))/(float(monthcount)-1),2)
        return average

# To start the iteration again
    budget_csv.seek(0)
# skip the header row again
    next(budget_file)
# Creat a list to record increase/decrease in profit/loss
    listOfChanges = []
#Calculate each period's change and add it to the list    
    for p in range(len(profit)-1):
        def changes(profit):
            diff = int(profit[p+1])-int(profit[p])
            return diff
        listOfChanges.append(changes(profit)) 

# The greatest increase in profits (date and amount) over the entire period
    max_profit = max(listOfChanges)
    max_index=listOfChanges.index(max_profit)
    max_month=month[max_index+1]
   
# The greatest decrease in losses (date and amount) over the entire period
    min_loss = min(listOfChanges)
    min_index=listOfChanges.index(min_loss)
    min_month=month[min_index+1]

# Print out the results
    print ("Financial Analysis")
    print ("----------------------------")
    print (f'Total months: {monthcount}')     
    print (f'Total: ${nettotal}')
    print (f'Average change: ${averagechange(profit)}')  
    print (f'Greatest Increase in Profits: {max_month} (${max_profit})')
    print (f'Greatest Decrease in Profits: {min_month} (${min_loss})')
    
    
# Specify the file to write to
output_path = os.path.join("AnalysisResult.txt")
with open(output_path, 'w') as AnalysisResult:
    
    # Write contents
    print ("Financial Analysis", file=AnalysisResult)
    print ("----------------------------",file=AnalysisResult)
    print (f'Total months: {monthcount}',file=AnalysisResult)     
    print (f'Total: ${nettotal}',file=AnalysisResult)
    print (f'Average change: {averagechange(profit)}',file=AnalysisResult)  
    print (f'Greatest Increase in Profits: {max_month} (${max_profit})',file=AnalysisResult)
    print (f'Greatest Decrease in Profits: {min_month} (${min_loss})',file=AnalysisResult)

    

