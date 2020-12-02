from typing import List, Tuple


def parse_input(filename: str) -> List[int]:
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


def find_pair_numbers_sum_2020(numbers: List[int]) -> Tuple[int, int]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) == 2020:
                return numbers[i], numbers[j]


def find_triplet_numbers_sum_2020(numbers: List[int]) -> Tuple[int, int, int]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if (numbers[i] + numbers[j] + numbers[k]) == 2020:
                    return numbers[i], numbers[j], numbers[k]


if __name__ == "__main__":
    numbers = parse_input('input.txt')
    num_1, num_2 = find_pair_numbers_sum_2020(numbers)
    print("Solution 1:", num_1 * num_2)
    num_1, num_2, num_3 = find_triplet_numbers_sum_2020(numbers)
    print("Solution 1:", num_1 * num_2 * num_3)
