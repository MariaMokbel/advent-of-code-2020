from typing import List


def parse_input(filename: str) -> List[int]:
    file_content = []
    with open(filename) as f:
        for line in f:
            file_content.append(int(line.replace('\n', '')))
    return file_content


def find_first_invalid_number(numbers: List[int]) -> int:
    i = 0
    while (25 + i) < len(numbers):
        found = False
        current_number = numbers[25 + i]
        for num in numbers[i:25 + i]:
            if (current_number - num) in numbers[i:25 + i]:
                found = True
                break
        if not found:
            return current_number
        i += 1


def find_contiguous_set(numbers: List[int], invalid_number: int) -> List[int]:
    i = 0
    index = numbers.index(invalid_number)
    while i < index:
        j = i
        contiguous_set = [numbers[j]]
        while sum(contiguous_set) < invalid_number and j < index:
            j += 1
            contiguous_set.append(numbers[j])
        if sum(contiguous_set) == invalid_number:
            return contiguous_set
        i += 1


if __name__ == "__main__":
    content = parse_input('input.txt')
    invalid_number = find_first_invalid_number(content)
    print("Solution 1:", invalid_number)
    contiguous_set = find_contiguous_set(content, invalid_number)
    print("Solution 2:", max(contiguous_set) + min(contiguous_set))
