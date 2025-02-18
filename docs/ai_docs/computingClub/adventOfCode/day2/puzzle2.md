# Documentation for src/computingClub/adventOfCode/day2/puzzle2.py

**Script Documentation**

**Summary**
------------

This Python script checks a list of numbers represented as strings, following the "SAFE" challenge rules. It determines how many valid sequences ( SAFE ) can be found in the input and identifies all invalid indices where unsafe sequences are detected.

**Functions and Classes**
-------------------------

### Functions:

#### `report_check(reports)`

*   **Description:** Checks a list of numbers represented as strings for valid "SAFE" sequences.
*   **Parameters:**

    *   `reports`: A list of lists containing integers, each representing a string with two or more consecutive digits.
*   **Return Value:** Tuples (safe_count, invalid_indices), where:

    *   `safe_count`: The number of valid SAFE sequences found in the input.
    *   `invalid_indices`: A list of indices of invalid sequences detected in the input.

#### `is_safe(report)`

*   **Description:** Checks if a single string representation of numbers follows the "SAFE" challenge rules.
*   **Parameters:**

    *   `report`: A string containing consecutive digits (0-9).
*   **Return Value:** Boolean indicating whether the sequence is SAFE or not.

#### `check_report(report)`

*   **Description:** Checks if a single string representation of numbers follows the "SAFE" challenge rules, considering possible splits.
*   **Parameters:**

    *   `report`: A string containing consecutive digits (0-9).
*   **Return Value:** Boolean indicating whether the sequence is SAFE or not.

#### `do_challenge()`

*   **Description:** Reads input from a file named 'input.txt', processes it, and returns the count of valid SAFE sequences.
*   **Parameters:** None
*   **Return Value:** An integer representing the number of SAFE sequences found in the input.

**Dependencies**
--------------

This script depends on the following external packages/modules:

*   `os`: for file operations

**Code with Comments**
---------------------

```python
import os  # Importing necessary module for file operations

def report_check(reports):  # Checking if all reports follow SAFE rules
    """
    Checks a list of numbers represented as strings for valid "SAFE" sequences.
    
    Args:
        reports (list): A list of lists containing integers, each representing a string with two or more consecutive digits.
        
    Returns:
        tuple: Tuples (safe_count, invalid_indices), where safe_count is the number of valid SAFE sequences found in the input,
               and invalid_indices is a list of indices of invalid sequences detected in the input.
    """
    # Initialize counters
    safe = 0  
    nots = []  

    for ind, report in enumerate(reports):  # Iterate over each sequence of numbers
        if is_safe(report):  # Check if the current sequence follows SAFE rules
            safe += 1  
        else:
            nots.append(ind)  # Mark invalid sequences
        
    return safe, nots  # Return counts and indices

def is_safe(report):  # Checks a single string representation of numbers for SAFE rule compliance
    """
    Checks if a single string representation of numbers follows the "SAFE" challenge rules.
    
    Args:
        report (str): A string containing consecutive digits (0-9).
        
    Returns:
        bool: Boolean indicating whether the sequence is SAFE or not.
    """
    if check_report(report):  # Use helper function for validation
        return True  
    for i in range(len(report)):  # Check all possible splits of the string
        temp = report[:i] + report[i+1:]  
        if check_report(temp):  # Validate split version of string
            return True 
    return False  # String does not follow SAFE rules

def check_report(report):  # Checks a single string representation of numbers for SAFE rule compliance
    """
    Checks if a single string representation of numbers follows the "SAFE" challenge rules, considering possible splits.
    
    Args:
        report (str): A string containing consecutive digits (0-9).
        
    Returns:
        bool: Boolean indicating whether the sequence is SAFE or not.
    """
    # Check initial conditions
    if len(report) < 2:
        return False  
    status = False  
    
    if report[0] < report[1]:
        typ = 1  
    elif report[0] > report[1]:
        typ = -1  
    else:
        return False  
    
    prev_num = None  
    for num in report:  # Iterate over each number
        if prev_num is not None:  # Compare with previous number
            if 1 <= abs(num-prev_num) <= 3:
                if num < prev_num and typ == -1:
                    status = True  
                elif num > prev_num and typ == 1:
                    status = True  
                else:
                    return False 
            else:
                return False  
        prev_num = num  
    
    return status  

def do_challenge():  # Reads input from a file named 'input.txt' and returns SAFE sequence count
    """
    Reads input from a file named 'input.txt', processes it, and returns the count of valid SAFE sequences.
    
    Returns:
        int: An integer representing the number of SAFE sequences found in the input.
    """
    with open('input.txt') as f:  # Open the file for reading
        lines = f.readlines()  
    
    reports = []  
    for line in lines:  # Process each line of input
        report = []  
        for num in line.strip().split():  # Parse numbers from string
            report.append(int(num))  
        reports.append(report)  

    safe, nots = report_check(reports)  # Count SAFE sequences and mark invalid indices

    return safe  # Return the count of valid sequences

# Call the challenge function and print the result
print(do_challenge())
```