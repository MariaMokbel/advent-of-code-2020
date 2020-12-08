from functools import reduce
from typing import List, Tuple


def parse_input(filename: str) -> List[Tuple]:
    file_content = []
    with open(filename) as f:
        for line in f:
            cleaned_line = line.replace('\n', '')
            file_content.append((cleaned_line.split()[0], int(cleaned_line.split()[1])))
    return file_content


def find_accumulator_before_loop(instructions: List[Tuple]) -> int:
    acc = 0
    rerun = False
    index = 0
    visited = []
    while not rerun:
        if index in visited:
            return acc
        else:
            visited.append(index)
        if instructions[index][0] == 'acc':
            acc += instructions[index][1]
            index += 1
        elif instructions[index][0] == 'nop':
            index += 1
        else:
            index += instructions[index][1]


def find_acc_with_changed_instruction(instructions: List[Tuple]) -> int or None:
    acc = 0
    rerun = False
    index = 0
    visited = []
    while not rerun:
        if index == len(instructions):
            return acc
        if index in visited:
            return None
        else:
            visited.append(index)

        if instructions[index][0] == 'acc':
            acc += instructions[index][1]
            index += 1
        elif instructions[index][0] == 'nop':
            index += 1
        else:
            index += instructions[index][1]


def change_jmp_instruction(instructions, current_index, index_of_changed_instruction, changed_instruction):
    if index_of_changed_instruction:
        instructions[index_of_changed_instruction] = changed_instruction
    if instructions[current_index][0] == 'jmp':
        changed_instruction = instructions[current_index]
        instructions[current_index] = ('nop', 0)
        index_of_changed_instruction = current_index
    return index_of_changed_instruction, changed_instruction


def fix_loop(instructions: List[Tuple]) -> int:
    index_of_changed_instruction = None
    changed_instruction = None
    for i in range(len(instructions)):
        index_of_changed_instruction, changed_instruction = change_jmp_instruction(instructions, i,
                                                                                   index_of_changed_instruction,
                                                                                   changed_instruction)
        acc = find_acc_with_changed_instruction(instructions)
        if acc:
            return acc


if __name__ == "__main__":
    content = parse_input('input.txt')
    print("Solution 1:", find_accumulator_before_loop(content))
    print("Solution 2:", fix_loop(content))
