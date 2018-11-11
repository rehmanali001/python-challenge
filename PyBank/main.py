import csv
import os 

csvpath = os.path.join("budget_data.csv")

with open(csvpath, "r") as pybank:
    csvreader = csv.reader(pybank, delimiter=",") 
    csv_header = next(csvreader)

    agr_months = 0
    avg_months = 0
    decrease = 0
    increase = 0
    months = 0
    total_profit_loss = 0
    prev_value = 0 
    agg_check = 0
    
    for row in csvreader:
        months += 1
        profits_losses = int(row[1])
        total_profit_loss += profits_losses

        now_month = row[1]
        dif_months = int(now_month) - int(prev_value)
        avg_months = (dif_months)/2

        agr_months += avg_months
        prev_value = now_month


        if decrease > dif_months:
            decrease = dif_months
            decrease_date = row[0]
        elif increase < dif_months:
            increase = dif_months
            increase_date = row[0]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${agr_months}")
print(f"Greatest Increase in Profits: {increase_date} (${increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

output = os.path.join("PyBank.txt")
with open(output, "w", newline='') as financial_analysis:
    csvwriter = csv.writer(financial_analysis)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {months}"])
    csvwriter.writerow([f"Total Net Profits/Losses: ${total_profit_loss}"])
    csvwriter.writerow([f"Average Change Between Months: ${agr_months}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {increase_date} (${increase})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {decrease_date} (${decrease})"])

