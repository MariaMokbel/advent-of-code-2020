import copy
from typing import Dict


def get_dict_from_input(input: str) -> Dict:
    return {int(number): [(index + 1)] for index, number in enumerate(input.split(','))}


def compute_nth_number_spoken(starting_numbers: Dict, n: int) -> int:
    turn = len(starting_numbers) + 1
    last_number_spoken = list(starting_numbers.keys())[-1]
    numbers_spoken_with_last_occurrence = copy.deepcopy(starting_numbers)
    while turn <= n:
        if len(numbers_spoken_with_last_occurrence[last_number_spoken]) == 1:
            last_number_spoken = 0
            if 0 in numbers_spoken_with_last_occurrence:
                numbers_spoken_with_last_occurrence[last_number_spoken].append(turn)
            else:
                numbers_spoken_with_last_occurrence[last_number_spoken] = [turn]
            turn += 1
        else:
            # Remove useless numbers
            numbers_spoken_with_last_occurrence[last_number_spoken] = numbers_spoken_with_last_occurrence[
                                                                          last_number_spoken][-2:]

            last_number_spoken = numbers_spoken_with_last_occurrence[last_number_spoken][-1] - \
                                 numbers_spoken_with_last_occurrence[last_number_spoken][-2]
            if last_number_spoken in numbers_spoken_with_last_occurrence:
                numbers_spoken_with_last_occurrence[last_number_spoken].append(turn)
            else:
                numbers_spoken_with_last_occurrence[last_number_spoken] = [turn]
            turn += 1

    return last_number_spoken


if __name__ == "__main__":
    input = "0,13,1,16,6,17"
    dict_from_input = get_dict_from_input(input)
    print("Solution 1: ", compute_nth_number_spoken(dict_from_input, 2020))
    print("Solution 2: ", compute_nth_number_spoken(dict_from_input, 30000000))
