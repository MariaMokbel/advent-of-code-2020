from functools import reduce
from typing import List, Dict, Set


def parse_input(filename: str):
    f = open(filename, "r")
    lines = f.readlines()
    actual = 'rules'
    rules = {}
    my_ticket = None
    tickets = []
    for line in lines:
        line = line.replace('\n', '')
        if actual == 'rules':
            rule_parts = line.split(': ')
            first_numbers = rule_parts[1].split(' or ')[0]
            rules[rule_parts[0]] = [list(range(int(first_numbers.split('-')[0]), int(first_numbers.split('-')[1]) + 1)),
                                    list(range(int(rule_parts[1].split(' or ')[1].split('-')[0])
                                               , int(rule_parts[1].split(' or ')[1].split('-')[1]) + 1))
                                    ]
            if rule_parts[0] == 'zone':
                actual = ''
        if line == 'your ticket:':
            actual = 'my ticket'
            continue
        if actual == 'my ticket':
            my_ticket = [int(number) for number in line.split(',')]
            actual = ''
            continue
        if line == 'nearby tickets:':
            actual = 'tickets'
            continue
        if actual == 'tickets':
            tickets.append([int(number) for number in line.split(',')])
    return rules, my_ticket, tickets


def get_invalid_numbers(possible_numbers: Set, tickets: List):
    invalid_numbers = []
    for ticket in tickets:
        intersection = set(ticket).intersection(possible_numbers)
        difference = list(set(ticket).difference(intersection))
        if len(difference) > 0:
            invalid_numbers.extend(difference)
    return invalid_numbers


def get_valid_tickets(possible_numbers: Set, tickets: List):
    valid_tickets = []
    for ticket in tickets:
        intersection = set(ticket).intersection(possible_numbers)
        difference = list(set(ticket).difference(intersection))
        if len(difference) == 0:
            valid_tickets.append(ticket)
    return valid_tickets


def get_all_possible_numbers(rules: Dict):
    all_numbers = []
    for rule, value in rules.items():
        all_numbers.extend(list(set(value[0]).union(set(value[1]))))
    return set(all_numbers)


def get_rules_per_column(rules: Dict, valid_tickets: List):
    class_per_column = {i: [] for i in range(len(valid_tickets[0]))}
    for i in range(len(valid_tickets[0])):
        for field, value in rules.items():
            incorrect = False
            for ticket in valid_tickets:

                if ticket[i] not in value[0] and ticket[i] not in value[1]:
                    incorrect = True
                    break
            if not incorrect:
                class_per_column[i].append(field)
    return class_per_column


def get_correct_rule(rules_per_column: Dict):
    repeat = [len(v) == 0 for k, v in rules_per_column.items()]
    correct_rule = {}
    while sum(repeat) < len(rules_per_column):
        for key, rules in rules_per_column.items():
            if len(rules) == 1:
                rule_found = rules[0]
                correct_rule[key] = rule_found
                updated_rules_per_column = {}
                for key, rules in rules_per_column.items():
                    if rule_found in rules:
                        rules.remove(rule_found)
                    updated_rules_per_column[key] = rules
                rules_per_column = updated_rules_per_column
                repeat = [len(v) == 0 for k, v in rules_per_column.items()]
                break
    return correct_rule


def get_product_stations_values(my_ticket: List, correct_rule: Dict):
    return reduce(lambda a, b: a * b,
                  [my_ticket[i] for i in list(correct_rule.keys()) if 'departure' in correct_rule[i]])


if __name__ == "__main__":
    rules, my_ticket, tickets = parse_input('input.txt')
    all_possible_numbers = get_all_possible_numbers(rules)
    invalid_numbers = get_invalid_numbers(all_possible_numbers, tickets)
    print("Solution 1: ", sum(invalid_numbers))
    valid_tickets = get_valid_tickets(all_possible_numbers, tickets)
    possible_rules_per_column = get_rules_per_column(rules, valid_tickets)
    correct_rule = get_correct_rule(possible_rules_per_column)
    print("Solution 2: ", get_product_stations_values(my_ticket, correct_rule))
