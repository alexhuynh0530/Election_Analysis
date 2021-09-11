# An Analysis of an Election Audit Using Python

## Overview of Project

### Purpose

This is an anlayis of an election audit of the results for the US Congressional precinct in Colorado. Using python to automate the task, we reported the total amount of votes, total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote. In addition, we report the voter turnout for each county, percentage of votes from each county, and the county with the highest turnout. 

## Results

### How many votes were cast in this congressional election?

The total number of votes were 369,711 votes.

#### Python Script to Find Total Votes
Add a variable to load the file from a path
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```

Create a total vote counter variable and initialize to zero.
```
# Initialize a total vote counter.
total_votes = 0
```

Open election_results.csv file
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
```

Create a for loop to loop through each row of the CSV file
```
    # For each row in the CSV file.
    for row in reader:
```

Add the to the total vote counter each time it loops through each row
```
        # Add to the total vote count
        total_votes = total_votes + 1
```

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

County Votes:

Jefferson:
- 38,855 votes
- 10.5% of total votes

Denver: 
- 306,055 votes
- 82.8% of total votes

Arapahoe: 
- 24,801 votes
- 6.7% of total votes

#### Python Script to Find County Votes
Add a variable to load the file from a path
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```

Create a county list and a dictionary for county votes
```
# 1: Create a county list and county votes dictionary.
county_list = []
county_dict = {}
```

Open election_results.csv file
```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
```

Create a for loop to loop through each row of the CSV file
```
# For each row in the CSV file.
    for row in reader:
```

Get the county name from each row
```
        # 3: Extract the county name from each row.
        county_name = row[1]
```

Create a nested if statement to find the unique county names and to count the county's vote count
```
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_dict[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_dict[county_name] += 1
```        

Create a for loop to get the county name from the county dictionary
```
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_dict:
```

Get the county votes from the dictionary, calculate the percentage, and print the results
```
        # 6b: Retrieve the county vote count.
        county_votes = county_dict.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_vote_percentage:.1f}% ({county_votes:,})\n")

         # 6d: Print the county results to the terminal.
        print(county_results)
```

### Which county had the largest number of votes?

Denver had the largest number of votes.

#### Python Script to Find the County with the Largest Number of Votes

Create variables to track the largest county and county voter turnout
```
# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_county_votes = 0
```

Create a for loop to get the county name from the county dictionary
```
 # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_dict:
```

Using the script to find the county votes data, create an if statement to determine the winning county and print
```
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_votes > largest_county_votes):
            largest_county_votes = county_votes
            largest_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_summary)
```

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

Candidate Votes:

Charles Casper Stockham: 
- 85,213 votes
- 23.0% of total votes

Diana DeGette: 
- 272,892 votes
- 73.8% of total votes

Raymon Anthony Doane: 
- 11,606 votes
- 3.1% of total votes

#### Python Script to Find Candidate Votes
Add a variable to load the file from a path
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```

Create a candidate list and a dictionary for candidate votes
```
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
```

Open election_results.csv file
```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
```

Create a for loop to loop through each row of the CSV file
```
# For each row in the CSV file.
    for row in reader:
```

Get the candidate name from each row
```
        # Get the candidate name from each row.
        candidate_name = row[2]
```

Create a nested if statement to find the unique county names and to count the county's vote count
```
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
```        

Create a for loop to get the county name from the county dictionary
```
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
```

Get the county votes from the dictionary, calculate the percentage, and print the results
```
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
```
            

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Diana DeGette won the election with 272,892 votes which was 73.8% of the total votes.

#### Python Script to Find Which Candidate Won the Election

Create variables to track the winning candidate, vote count and percentage
```
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
```

Create a for loop to get the candidate name from the candidate dictionary
```
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
```

Using the script to find the candidate votes data, create an if statement to determine the winning county and print
```
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
```

*PLEASE NOTE: FULL PYTHON SCRIPT CAN BE FOUND AT PyPollChallenge.py*
![PyPoll.py](https://github.com/alexhuynh0530/Election_Analysis/blob/main/PyPoll.py)

#### Original Script



## Summary

Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.


