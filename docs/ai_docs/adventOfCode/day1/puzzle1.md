# Documentation for src/adventOfCode/day1/puzzle1.py

**Documentation: Distance Sum Calculator**

**Summary**
-----------

This script calculates the total distance between two lists of numbers. The input files contain two lists of integers, each on a separate line, separated by four spaces. The script reads these lines, sorts both lists, and then calculates the absolute difference between corresponding elements in the sorted lists. These differences are summed up to produce the final result.

**Functions and Classes**
------------------------

### do_challange()

*   **Description:** Calculates the total distance between two lists of numbers.
*   **Parameters:**

    *   None (input file is read from 'input.txt')

*   **Returns:** The sum of absolute differences between corresponding elements in the sorted lists.

```python
def do_challange():
    # Open input file and read all lines into a list
    with open('input.txt') as f:
        lines = f.readlines()
    
    # Initialize two empty lists to store numbers from each line
    list_one = []
    list_two = []

    # Iterate over each line in the input file
    for line in lines:
        # Split line into two integers separated by four spaces
        spli = line.strip().split('   ')
        
        # Append the first integer to list_one and the second to list_two
        list_one.append(int(spli[0]))
        list_two.append(int(spli[1]))
    
    # Sort both lists in ascending order
    list_one.sort()
    list_two.sort()
    
    # Initialize an empty list to store the distances between corresponding elements
    distances = []
    
    # Iterate over each element in list_one, calculate its distance from the corresponding element in list_two, and append it to distances
    for index, num in enumerate(list_one):
        distances.append(abs(num - list_two[index]))
    
    # Initialize a variable sum to 0
    sum = 0
    
    # Iterate over each distance in distances, add it to sum, and return the final result
    for num in distances:
        sum += num 
    
    return sum
```

**Dependencies**
----------------

This script depends on the following external packages/modules:

*   None (built-in Python modules are used)

Note: The actual code remains unchanged throughout the documentation.