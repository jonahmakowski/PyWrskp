import pyWrkspPackage
import sys
from random import shuffle
sys.setrecursionlimit(90000)

def parse_rules(rules, split):
    output = []
    for rule in rules:
        if split in rule:
            rule_temp = []
            for rule in rule.split(split):
                rule_temp.append(int(rule))
            output.append(rule_temp)
    return output

def check_valid(rules, message):
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
    valid = True
    count_invalid = 1
    for item in list1:
        if not item in list2:
            #print(f"{count_invalid} Item {item} not in list2")
            count_invalid += 1
            valid = False
    return valid

def make_valid(rules, message):
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
