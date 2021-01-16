import os
import csv

# Path to collect data from the Resources folder
poll_data_csv = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

# Read in the CSV file
with open(poll_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Create a dictionary to hold our candidates & associated vote totals
    candidate_votes = {}

    for row in csvreader:

        voted_for = row[2]

        # Determine if this candidate already exists in the dictionary, and if so, add a vote
        if voted_for in candidate_votes:
            candidate_votes[voted_for] += 1

        # Otherwise, add the candidate to the dictionary with a starting total of one vote
        else:
            candidate_votes.update({voted_for: 1})


# Begin calculating and printing results to the terminal
print()
print("Election Results")
print("-------------------------")


# Calculate the total number of votes cast
total_votes = 0

for candidate in candidate_votes:

    total_votes += candidate_votes[candidate]

print(f"Total Votes: {total_votes}")
print("-------------------------")

# Create a list to store strings with the candidate information to print
candidate_strings = []

# Create variables to determine the winner
election_winner = ""
winner_votes = 0


# For loop that goes through candidates and creates strings with information
# Also, compares vote totals to determine who won
for candidate in candidate_votes:

    # Check to see if they are the winner
    if candidate_votes[candidate] > winner_votes:
        election_winner = candidate
        winner_votes = candidate_votes[candidate]

    # Calculate the percentage of votes the candidate won
    vote_percentage = round((int(candidate_votes[candidate]) / total_votes) * 100, 3)

    # Compile all candidate info into one string and append to the list for storage
    candidate_info = f"{candidate}: {vote_percentage}% ({candidate_votes[candidate]})"
    candidate_strings.append(candidate_info)

    # While in this for loop, print each candidate's info from their string
    print(candidate_info)


# Print the winning candidate
print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")
print()


# Path to write data to the Analysis folder
output_path = os.path.join("Analysis", "analysis.txt")


# Write the results to a new file, using our stored list of strings for each candidate
with open(output_path,'w') as txtfile:

    txtfile.write("Election Results")
    txtfile.write("\n-------------------------")
    txtfile.write(f"\nTotal Votes: {total_votes}")
    txtfile.write("\n-------------------------")

    for string_index in range(len(candidate_strings)):
        txtfile.write(f"\n{candidate_strings[string_index]}")
    
    txtfile.write("\n-------------------------")
    txtfile.write(f"\nWinner: {election_winner}")
    txtfile.write("\n-------------------------")