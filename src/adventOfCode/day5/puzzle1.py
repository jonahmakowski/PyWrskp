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
    Checks if a message is valid based on a set of rules.

    Each rule is a tuple containing two characters. A message is considered valid if,
    for each rule, the first character appears before the second character in the message.

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

def main():
    """
    Main function to process input data, parse rules and messages, check for valid messages, 
    and compute a sum based on valid messages.
    The function performs the following steps:
    1. Loads data from "input.txt" and splits it into lines.
    2. Parses the first 1177 lines as rules using '|' as the delimiter.
    3. Parses the remaining lines as messages using ',' as the delimiter.
    4. Checks each message against the parsed rules to determine validity.
    5. Collects all valid messages.
    6. Computes the sum of the middle character (as an integer) of each valid message.
    7. Prints the computed sum.
    """
    data = pyWrkspPackage.load_from_file("input.txt").split("\n")
    rules = parse_rules(data[:1177], '|')
    messages = parse_rules(data[1178:], ',')
    valid_rules = []
    for message in messages:
        if check_valid(rules, message):
            valid_rules.append(message)
    
    su = 0
    for rule in valid_rules:
        su += rule[int(len(rule) / 2)]
    print(su)

if __name__ == "__main__":
    main()
