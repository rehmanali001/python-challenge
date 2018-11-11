import os
import csv


csvpath = os.path.join("election_data.csv")

with open(csvpath, newline='') as PyPoll:
    csv_reader = csv.reader(PyPoll, delimiter=',')
    csv_header = next(PyPoll)

    Vote1 = 0
    Vote2 = 0
    Vote3 = 0
    Vote4 = 0
    total_votes = 0

    for i, row in enumerate(csv_reader):
        if i == 0:
            header = row
        else:
            total_votes = total_votes + 1
            if row[2] == "Khan":
                Vote1 += 1
                Vote1_percent = (Vote1/total_votes) * 100
            if row[2] == "Correy":
                Vote2 += 1
                Vote2_percent = (Vote2/total_votes) * 100
            if row[2] == "Li":
                Vote3 += 1
                Vote3_percent = (Vote3/total_votes) * 100
            if row[2] == "O'Tooley":
                Vote4 += 1
                Vote4_percent = (Vote4/total_votes) * 100  
            if Vote1 > Vote2 and Vote3 and Vote4:
                winner = "Khan"
            if Vote2 > Vote1 and Vote3 and Vote4:
                winner = "Correy"
            if Vote3 > Vote2 and Vote1 and Vote4:
                winner = "Li"
            if Vote4 > Vote2 and Vote3 and Vote1:
                winner = "O'Tooley"    
            
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {round(Vote1_percent)}% ({Vote1})")
print(f"Correy: {round(Vote2_percent)}% ({Vote2})")
print(f"Li: {round(Vote3_percent)}% ({Vote3})")
print(f"O'Tooley: {round(Vote4_percent)}% ({Vote4})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

output = os.path.join("PyPoll.txt")
with open(output, "w", newline='') as election_results:
    csvwriter = csv.writer(election_results)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Khan: {round(Vote1_percent)}% ({Vote1})"])
    csvwriter.writerow([f"Correy: {round(Vote2_percent)}% ({Vote2})"])
    csvwriter.writerow([f"Li: {round(Vote3_percent)}% ({Vote3})"])
    csvwriter.writerow([f"O'Tooley: {round(Vote4_percent)}% ({Vote4})"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["----------------------------"])
