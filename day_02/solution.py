from typing import List, Tuple


def parse_input(filename: str) -> List[Tuple]:
    file_content = []
    with open(filename) as f:
        for line in f:
            group = line.split()
            num1 = int(group[0].split('-')[0])
            num2 = int(group[0].split('-')[1])
            letter = group[1].split(':')[0]
            word = group[2]
            file_content.append((num1, num2, letter, word))
    return file_content


def find_number_valid_password_count(content: List[Tuple]) -> int:
    count = 0
    for info in content:
        mini, maxi, letter, word = info
        if mini <= word.count(letter) <= maxi:
            count = count + 1
    return count


def find_number_valid_password_position(content: List[Tuple]) -> int:
    count = 0
    for info in content:
        pos1, pos2, letter, word = info
        positions = [pos + 1 for pos, char in enumerate(word) if char == letter]
        if (pos1 in positions) ^ (pos2 in positions):
            count = count + 1
    return count


if __name__ == "__main__":
    content = parse_input('input.txt')
    count_valid_passwords = find_number_valid_password_count(content)
    print("Solution 1:", count_valid_passwords)
    count_valid_passwords_pos = find_number_valid_password_position(content)
    print("Solution 2:", count_valid_passwords_pos)
