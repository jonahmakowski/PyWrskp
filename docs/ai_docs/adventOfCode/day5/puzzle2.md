# Documentation for src/adventOfCode/day5/puzzle2.py

# PyWrkspPackage Documentation

## Summary

This Python script is a solution to the Day 5 challenge of the Advent of Code 2020. It takes an input file containing rules and messages, parses the data, checks for valid messages, makes invalid messages valid by swapping characters, and then prints the sum of the middle character of each valid message.

## Functions and Classes

### `parse_rules(rules, split)`

*   Description: This function takes a list of rules and a split character, and returns a new list where each rule is parsed into a list of integers.
*   Parameters:
    *   `rules`: A list of strings representing the rules.
    *   `split`: The character to split the rules by.
*   Returns:
    *   A list of lists containing the parsed rule.

### `check_valid(rules, message)`

*   Description: This function checks if a given message is valid according to the provided rules. A message is valid if all characters in the message that are specified in a rule appear together from left to right.
*   Parameters:
    *   `rules`: A list of rules.
    *   `message`: The message to check.
*   Returns:
    *   True if the message is valid, False otherwise.

### `all_in(list1, list2)`

*   Description: This function checks if all elements in one list are present in another list. It returns False as soon as it finds an element not in the second list.
*   Parameters:
    *   `list1`: The first list to check.
    *   `list2`: The second list to check against.
*   Returns:
    *   True if all elements in list1 are present in list2, False otherwise.

### `make_valid(rules, message)`

*   Description: This function makes an invalid message valid by swapping characters according to the rules. It continues to swap until the message is valid.
*   Parameters:
    *   `rules`: A list of rules.
    *   `message`: The message to make valid.
*   Returns:
    *   The valid message.

### `main()`

*   Description: This function is the main entry point of the script. It loads data from an input file, parses the data, checks for valid messages, makes invalid messages valid, and prints the sum of the middle character of each valid message.
*   Parameters:
    *   None
*   Returns:
    *   The sum of the middle character of each valid message.

## Dependencies

This script depends on the following external packages:

*   `pyWrkspPackage`: A package containing data to solve the Day 5 challenge.
*   `random`: A built-in Python module for generating random numbers. (Not actually used in this script.)

```python
"""
PyWrkspPackage Documentation

This script is a solution to the Day 5 challenge of the Advent of Code 2020.

Author: [Your Name]
Date: [Today's Date]

"""

import pyWrkspPackage
import sys
from random import shuffle
sys.setrecursionlimit(90000)

def parse_rules(rules, split):
    """
    This function takes a list of rules and a split character, 
    and returns a new list where each rule is parsed into a list of integers.

    Args:
        rules (list): A list of strings representing the rules.
        split (str): The character to split the rules by.

    Returns:
        list: A list of lists containing the parsed rule.
    """
    output = []
    for rule in rules:
        if split in rule:
            rule_temp = []
            for rule in rule.split(split):
                rule_temp.append(int(rule))
            output.append(rule_temp)
    return output

def check_valid(rules, message):
    """
    This function checks if a given message is valid according to the provided rules.
    A message is valid if all characters in the message that are specified in a rule 
    appear together from left to right.

    Args:
        rules (list): A list of rules.
        message (str): The message to check.

    Returns:
        bool: True if the message is valid, False otherwise.
    """
    valid = True
    for rule in rules:
        if not (rule[0] in message and rule[1] in message):
            continue

        index1 = message.index(rule[0])
        index2 = message.index(rule[1])

        if index1 > index2:
            valid = False
            break
    return valid

def all_in(list1, list2):
    """
    This function checks if all elements in one list are present in another list.
    It returns False as soon as it finds an element not in the second list.

    Args:
        list1 (list): The first list to check.
        list2 (list): The second list to check against.

    Returns:
        bool: True if all elements in list1 are present in list2, False otherwise.
    """
    valid = True
    count_invalid = 1
    for item in list1:
        if not item in list2:
            #print(f"{count_invalid} Item {item} not in list2")
            count_invalid += 1
            valid = False
    return valid

def make_valid(rules, message):
    """
    This function makes an invalid message valid by swapping characters according to the rules.
    It continues to swap until the message is valid.

    Args:
        rules (list): A list of rules.
        message (str): The message to make valid.

    Returns:
        str: The valid message.
    """
    print(message)
    while not check_valid(rules, message):
        for rule in rules:
            if rule[0] in message and rule[1] in message:
                index1 = message.index(rule[0])
                index2 = message.index(rule[1])
                if index1 > index2:
                    message[index1], message[index2] = message[index2], message[index1]
                    print(message)
    
    return message

def main():
    """
    This function is the main entry point of the script. 
    It loads data from an input file, parses the data, checks for valid messages, 
    makes invalid messages valid, and prints the sum of the middle character of each valid message.
    """
    data = pyWrkspPackage.load_from_file("input.txt").split("\n")
    rules = parse_rules(data, '|')
    messages = parse_rules(data, ',')
    valid_rules = []
    for message in messages:
        if not check_valid(rules, message):
            valid_rules.append(make_valid(rules, message))

    print(f"Made Valid rules: {len(valid_rules)}")

    invalid_message_count = 0
    for message in valid_rules:
        if len(message) > 1:
            middle_char = message[len(message)//2]
            #print(f"{message} {middle_char}")
            invalid_message_count += int(middle_char)

    print(invalid_message_count)

if __name__ == "__main__":
    main()
```