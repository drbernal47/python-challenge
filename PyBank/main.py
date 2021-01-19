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
    greatest_increase_month = ""
    greatest_decrease_month = ""
    greatest_increase = 0
    greatest_decrease = 0
    current_change = 0
    previous_profit = 0

    for row in csvreader:

        row_month = row[0]
        row_profit = int(row[1])

        total_months += 1
        net_profit += row_profit

        # These conditionals help us track the first and last month to calculate average change
        if total_months == 1:
            first_month_profit = row_profit
        else:
            last_month_profit = row_profit

        # These conditionals compare change to see which months have greatest increase/decrease
        if total_months > 1:
            current_change = row_profit - previous_profit
            if current_change > greatest_increase:
                greatest_increase = current_change
                greatest_increase_month = row_month
            if current_change < greatest_decrease:
                greatest_decrease = current_change
                greatest_decrease_month = row_month
        previous_profit = row_profit
        

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
print(f"Greatest Increase in Profits: {greatest_increase_month} ({neg_format(greatest_increase)})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ({neg_format(greatest_decrease)})")


# Path to write data to the Analysis folder
output_path = os.path.join("Analysis", "analysis.txt")


# Write the results to a new file
with open(output_path,'w') as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write("\n----------------------------")
    txtfile.write(f"\nTotal Months: {total_months}")
    txtfile.write(f"\nTotal: {neg_format(net_profit)}")
    txtfile.write(f"\nAverage Change: {neg_format(average_change)}")
    txtfile.write(f"\nGreatest Increase in Profits: {greatest_increase_month} ({neg_format(greatest_increase)})")
    txtfile.write(f"\nGreatest Decrease in Profits: {greatest_decrease_month} ({neg_format(greatest_decrease)})")