from typing import List

from numpy import prod


def parse_input(filename: str) -> List:
    file_content = []
    with open(filename) as f:
        for line in f:
            file_content.append(line.replace('\n', '').replace(' ', ''))
    return file_content


def evaluate_expression(operation: str, precedence: bool) -> int:
    if '(' in operation:
        parenthesis_pairs = find_parenthesis_pairs(operation)

        origin = []
        dest = []
        for start, end in parenthesis_pairs:
            origin.append(operation[start:end + 1])
            dest.append(evaluate_expression(operation[start + 1:end], precedence))

        for o, d in zip(origin, dest):
            operation = operation.replace(o, str(d))

    operation_list = to_list(operation)

    if precedence:
        return compute_with_precedence_level(operation_list)
    else:
        return compute_without_precedence_level(operation_list)


def find_parenthesis_pairs(operation):
    parenthesis_pairs = []
    start_index = 0
    i = 0
    for index, char in enumerate(operation):
        if char == '(':
            if i == 0:
                start_index = index
            i += 1
        if char == ')':
            if i == 1:
                end_index = index
                parenthesis_pairs.append((start_index, end_index))
            i -= 1
    return parenthesis_pairs


def compute_without_precedence_level(operation_list):
    acc = int(operation_list[0])
    i = 1
    while i < len(operation_list) - 1:
        if operation_list[i] == '*':
            acc *= int(operation_list[i + 1])
            i += 2
        elif operation_list[i] == '+':
            acc += int(operation_list[i + 1])
            i += 2
        else:
            i += 1
    return acc


def compute_with_precedence_level(operation_list):
    i = 0
    while i < len(operation_list) - 1:
        if operation_list[i] == '+':
            operation_list[i - 1] = operation_list[i - 1] + operation_list[i + 1]
            operation_list = [op for j, op in enumerate(operation_list) if j not in [i, i + 1]]
            i = 0
            continue
        i += 1

    return int(prod([num for num in operation_list if num != '*']))


def to_list(operation):
    operation_list = []
    current_num = ''
    for char in operation:
        if char in ['+', '*']:
            operation_list.append(int(current_num))
            operation_list.append(char)
            current_num = ''
        else:
            current_num += char
    operation_list.append(int(current_num))
    return operation_list


if __name__ == "__main__":
    operations = parse_input('input.txt')
    print("Solution 1:", sum([evaluate_expression(operation, False) for operation in operations]))
    print("Solution 2:", sum([evaluate_expression(operation, True) for operation in operations]))
