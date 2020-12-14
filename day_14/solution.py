from typing import List, Tuple, Dict


def parse_input(filename: str) -> List:
    file_content = []
    with open(filename) as f:
        for line in f:
            cleaned_line = line.replace('\n', '')
            key = cleaned_line.split(' = ')[0]
            if key == 'mask':
                file_content.append((key, cleaned_line.split(' = ')[1]))
            else:
                file_content.append((int(key[4:-1]), int(cleaned_line.split(' = ')[1])))
    return file_content


def apply_mask(number: int, mask: str):
    binary_number = str(f'{number:036b}')
    list1 = []
    list1[:0] = binary_number
    for i, digit in enumerate(mask):
        if digit == 'X':
            continue
        else:
            list1[i] = digit
    return int(''.join(list1), 2)


def apply_mask_to_address(number: int, mask: str) -> List:
    binary_number = str(f'{number:036b}')
    list1 = []
    list1[:0] = binary_number
    for i, digit in enumerate(mask):
        if digit == '0':
            continue
        else:
            list1[i] = digit
    return list1


def find_all_possible_addresses(address: List, index: int) -> List:
    if index == len(address):
        return [int(''.join(address), 2)]
    elif address[index] != 'X':
        return find_all_possible_addresses(address, index + 1)
    else:
        copy_1 = address.copy()
        copy_1[index] = '0'
        copy_2 = address.copy()
        copy_2[index] = '1'
        return find_all_possible_addresses(copy_1, index + 1) + find_all_possible_addresses(copy_2, index + 1)


def find_all_in_memory_numbers(content: List[Tuple]) -> Dict:
    in_memory = {}
    mask = None
    for line in content:
        if line[0] == 'mask':
            mask = line[1]
        else:
            in_memory[line[0]] = apply_mask(line[1], mask)
    return in_memory


def find_all_in_memory_numbers_with_multiple_addresses(content: List[Tuple]) -> Dict:
    in_memory = {}
    mask = None
    for line in content:
        if line[0] == 'mask':
            mask = line[1]
        else:
            all_addresses = find_all_possible_addresses(apply_mask_to_address(line[0], mask), 0)
            for address in all_addresses:
                in_memory[address] = line[1]
    return in_memory


if __name__ == "__main__":
    content = parse_input('input.txt')
    numbers_in_memory = find_all_in_memory_numbers(content)
    print("Solution 1:", sum(numbers_in_memory.values()))
    numbers_in_memory_2 = find_all_in_memory_numbers_with_multiple_addresses(content)
    print("Solution 2:", sum(numbers_in_memory_2.values()))
