import pyWrkspPackage

def parse_rules(rules, split):
    """
    Parses a list of rules and splits each rule by a given delimiter.

    Args:
        rules (list of str): A list of rule strings to be parsed.
        split (str): The delimiter to split each rule string.

    Returns:
        list of list of int: A list where each element is a list of integers 
                             obtained by splitting and converting the rule strings.
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
    Checks if a given message is valid based on a set of rules.

    Each rule is a tuple containing two characters. The message is considered valid if for each rule,
    the first character appears in the message before the second character.

    Args:
        rules (list of tuple): A list of tuples where each tuple contains two characters.
        message (str): The message to be checked.

    Returns:
        bool: True if the message is valid according to the rules, False otherwise.
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
    Check if all elements of list1 are present in list2.

    Args:
        list1 (list): The list of elements to check.
        list2 (list): The list in which to check for the presence of elements from list1.

    Returns:
        bool: True if all elements of list1 are present in list2, False otherwise.
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
    Reorders characters in the message according to the given rules until the message is valid.
    Args:
        rules (list of tuples): A list of tuples where each tuple contains two characters. 
                                The first character should appear before the second character in the message.
        message (str): The message to be validated and reordered.
    Returns:
        str: The reordered message that satisfies all the given rules.
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
    Main function to process input data, parse rules and messages, validate messages, 
    and calculate a sum based on the valid messages.

    The function performs the following steps:
    1. Loads data from "input.txt" and splits it into lines.
    2. Parses rules and messages from the data.
    3. Checks each message against the rules and makes invalid messages valid.
    4. Prints the number of made valid rules.
    5. Checks the validity of the made valid rules and prints invalid messages.
    6. Calculates and returns the sum of the middle characters of the valid messages.

    Returns:
        int: The sum of the middle characters of the valid messages.
    """
    data = pyWrkspPackage.load_from_file("input.txt").split("\n")
    rules = parse_rules(data, '|')
    messages = parse_rules(data, ',')
    valid_rules = []
    for message in messages:
        if not check_valid(rules, message):
            valid_rules.append(make_valid(rules, message))

    print(f"Made Valid rules: {len(valid_rules)}")

    invalid_rules = 1
    for message in valid_rules:
        if not check_valid(rules, message):
            print(f"{invalid_rules} Invalid message")
            invalid_rules += 1

    su = 0
    for message in valid_rules:
        print(message[len(message) // 2])
        su += message[len(message) // 2]
    return su

if __name__ == "__main__":
    print(main())
