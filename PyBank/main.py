import os
import csv

# initializing the variables
total_months=0
net_total_amount=0
average_profit_loss=0
total_profit=0
total_loss=0
prev_pl_val=0
change_pl=0
change_pl_list=[]
greatest_increase=0
greatest_decrease=0
greatest_increase_dt_stmt=''
greatest_decrease_dt_stmt=''
average_change=0

# defining the path of the input csv file
pybank_csv_path=os.path.join('Resources','budget_data.csv')


with open(pybank_csv_path) as pybank_csv_file:
    csv_reader=csv.reader(pybank_csv_file)
    # removing the header from the dataset
    header=next(csv_reader)
    # print(header)
    # looping through the rows in csv_reader
    for row in csv_reader:
        # calculating the total number of months
        total_months=total_months+1
        # calculating the net total amount
        net_total_amount+=int(row[1])
        # calculating the changes in profit and loss value with the previous month's profit and loss value
        if total_months>1:#this if loop is to avoid the first row
            change_pl=(float(row[1])-prev_pl_val)
            change_pl_list=change_pl_list+[change_pl]
        
        prev_pl_val=float(row[1])#assigning the current row pl value to the variable
        # checking the greatest increase in profits
        if change_pl>greatest_increase:
            greatest_increase=change_pl
            greatest_increase_dt_stmt="Greatest Increase in Profits: "+row[0] +" ($"+str(int(greatest_increase))+")"
       
       # checking the greatest decrease in profits
        
        if change_pl<greatest_decrease:
            greatest_decrease=change_pl
            greatest_decrease_dt_stmt="Greatest Decrease in Profits: "+row[0] +" ($"+str(int(greatest_decrease))+")"
        
# calculating the average change in profits
average_change=sum(change_pl_list)/len(change_pl_list)        
    
print(f"Financial Analysis\n")
print(f"--------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_total_amount}\n")
print(f"Average Change: ${round(average_change,2)}\n")
print(f"{greatest_increase_dt_stmt}\n")
print(f"{greatest_decrease_dt_stmt}\n")

# defining the output file path
output_path=os.path.join('analysis','output_budget_data.txt')
# writing the files
# opening the file in write mode
with open(output_path,'w') as writefile:
    writefile.write("Financial Analysis\n")
    writefile.write("--------------------------\n")
    writefile.write(f"Total Months: {total_months}\n")
    writefile.write(f"Total: ${net_total_amount}\n")
    writefile.write(f"Average Change: ${round(average_change,2)}\n")
    writefile.write(f"{greatest_increase_dt_stmt}\n")
    writefile.write(f"{greatest_decrease_dt_stmt}\n")