# An Analysis of an Election Audit Using Python

## Overview of Project

### Purpose

This is an anlayis of an election audit of the results for the US Congressional precinct in Colorado. Using python to automate the task, we reported the total amount of votes, total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote. In addition, we report the voter turnout for each county, percentage of votes from each county, and the county with the highest turnout. 

## Results

### How many votes were cast in this congressional election?

The total number of votes were 369,711 votes.

#### Pseudocode
- Add a variable to load the file from a path
- Create a total vote counter variable and initialize to zero.
- Open election_results.csv file
- Create a for loop to loop through each row of the CSV file
- Add the to the total vote counter each time it loops through each row

#### Python Code

```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
```
```
# Initialize a total vote counter.
total_votes = 0
```
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
```
```
    # Read the header
    header = next(reader)
```
```
    # For each row in the CSV file.
    for row in reader:
```
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

#### Pseudocode
- Create a total vote counter variable and initialize to zero.
- Open election_results.csv file
- Create a for loop to loop through each row of the CSV file
- Add the to the total vote counter each time it loops through each row

#### Python Code

```
# Initialize a total vote counter.
total_votes = 0
```

```# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
```        

### Which county had the largest number of votes?

Denver had the largest number of votes.

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


