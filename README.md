# An Analysis of an Election Audit Using Python

## Overview of Project

### Purpose

This is an anlayis of an election audit of the results for the US Congressional precinct in Colorado. Using python to automate the task, we reported the total amount of votes, total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote. In addition, we report the voter turnout for each county, percentage of votes from each county, and the county with the highest turnout. 

## Results

### How many votes were cast in this congressional election?

The total number of votes were 369,711 votes.

#### Python Script to Find Total Votes
- Add a variable to load the file from a path
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```

- Create a total vote counter variable and initialize to zero.
```
# Initialize a total vote counter.
total_votes = 0
```

- Open election_results.csv file
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
```

- Create a for loop to loop through each row of the CSV file
```
    # For each row in the CSV file.
    for row in reader:
```

- Add the to the total vote counter each time it loops through each row
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
- Add a variable to load the file from a path
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```

- Create a county list and a dictionary for county votes
```
# 1: Create a county list and county votes dictionary.
county_list = []
county_dict = {}
```

- Open election_results.csv file
```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
```

- Create a for loop to loop through each row of the CSV file
```
# For each row in the CSV file.
    for row in reader:
```

- Create a nested if statement to find the unique county names and to count the county's vote count
```
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_dict[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_dict[county_name] += 1
```        

- Create a for loop to get the county name from the county dictionary
```
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_dict:
```

- Get the county votes from the dictionary, calculate the percentage, and print the results
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

- Create varabiliest to track the largest county and county voter turnout
```
# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_county_votes = 0
```

- Create a for loop to get the county name from the county dictionary
```
 # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_dict:
```

- 
```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
```

- Create a for loop to loop through each row of the CSV file
```
# For each row in the CSV file.
    for row in reader:
```

- Create a nested if statement to find the unique county names and to count the county's vote count
```
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_dict[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_dict[county_name] += 1
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


### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Diana DeGette won the election with 272,892 votes which was 73.8% of the total votes.




![VBA_Challenge_2017_results.png](https://github.com/alexhuynh0530/stock-analysis/blob/main/Resources/VBA_Challenge_2017_results.png)

#### Original Script



## Summary

Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.


