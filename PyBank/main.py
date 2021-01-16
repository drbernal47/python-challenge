import os
import csv

# Path to collect data from the Resources folder
bank_data_csv = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

# Read in the CSV file
with open(bank_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Create a variable to help us count the total number of months
    total_months = 0

    # Create a variable to help us keep track of the net loss/profit
    net_profit = 0

    # Create variables to calculate average change over the period
    # This can be mathematically calculated only using the first profit/loss,
    # the last profit/loss, since the values in between form a telescoping sequence.
    first_month_profit = 0
    last_month_profit = 0

    # Create variables to helps us track the greatest increase and decrease
    greatest_profit_month = ""
    greatest_loss_month = ""
    greatest_profit = 0
    greatest_loss = 0

    for row in csvreader:

        row_month = row[0]
        row_profit = int(row[1])

        total_months += 1
        net_profit += row_profit

        if total_months == 1:
            first_month_profit = row_profit
        else:
            last_month_profit = row_profit

        if row_profit > greatest_profit:
            greatest_profit = row_profit
            greatest_profit_month = row_month

        if row_profit < greatest_loss:
            greatest_loss = row_profit
            greatest_loss_month = row_month
        

# Calculate average change over the period (using the mathematical formula)
average_change = round((last_month_profit - first_month_profit) / (total_months - 1),2)

def neg_format(amount):
    if amount < 0:
        return f"-${(-1 * amount)}"
    else:
        return f"${amount}"


# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {neg_format(net_profit)}")
print(f"Average Change: {neg_format(average_change)}")
print(f"Greatest Increase in Profits: {greatest_profit_month} {neg_format(greatest_profit)}")
print(f"Greatest Decrease in Profits: {greatest_loss_month} {neg_format(greatest_loss)}")


# Path to write data to the Analysis folder
output_path = os.path.join("Analysis", "analysis.txt")


# Write the results to a new file
with open(output_path,'w') as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write("\n----------------------------")
    txtfile.write(f"\nTotal Months: {total_months}")
    txtfile.write(f"\nTotal: {neg_format(net_profit)}")
    txtfile.write(f"\nAverage Change: {neg_format(average_change)}")
    txtfile.write(f"\nGreatest Increase in Profits: {greatest_profit_month} {neg_format(greatest_profit)}")
    txtfile.write(f"\nGreatest Decrease in Profits: {greatest_loss_month} {neg_format(greatest_loss)}")