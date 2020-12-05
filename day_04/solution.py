import re
from typing import List


def check_byr_correct(potential_byr: str) -> bool:
    try:
        date = int(potential_byr)
        return 1920 <= date <= 2002
    except:
        return False


def check_iyr_correct(potential_iyr: str) -> bool:
    try:
        date = int(potential_iyr)
        return 2010 <= date <= 2020
    except:
        return False


def check_eyr_correct(potential_eyr: str) -> bool:
    try:
        date = int(potential_eyr)
        return 2020 <= date <= 2030
    except:
        return False


def check_hgt_correct(potential_hgt: str) -> bool:
    try:
        unit = potential_hgt[-2:]
        height = int(potential_hgt[:-2])
        return (unit == 'cm' and 150 <= height <= 193) or (unit == 'in' and 59 <= height <= 76)
    except:
        return False


def check_hcl_correct(potential_hcl: str) -> bool:
    return True if re.search(r'^#[0-9a-f]{6}$', potential_hcl) else False


def check_ecl_correct(potential_ecl: str) -> bool:
    return True if potential_ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False


def check_pid_correct(potential_pid: str) -> bool:
    return True if re.search(r'^[0-9]{9}$', potential_pid) else False


MANDATORY_FIELDS_CHECKS = {'byr': check_byr_correct,
                  'iyr': check_iyr_correct,
                  'eyr': check_eyr_correct,
                  'hgt': check_hgt_correct,
                  'hcl': check_hcl_correct,
                  'ecl': check_ecl_correct,
                  'pid': check_pid_correct}


def parse_input(filename: str) -> List[str]:
    file_content = []
    with open(filename) as f:
        for line in f:
            final_line = line[:-1] if line[len(line) - 1] == '\n' else line
            file_content.append(final_line)
    return file_content


def get_documents(file_content: List[str]) -> List[str]:
    documents = []
    concat = ''
    for el in file_content:
        if el == '':
            documents.append(concat)
            concat = ''
            continue
        concat = concat + el + ' '
    documents.append(concat)
    return documents


def count_passports(documents: List[str]) -> int:
    count = 0
    for doc in documents:
        keys = [el.split(':')[0] for el in doc.split()]
        if set(MANDATORY_FIELDS_CHECKS.keys()).issubset(set(keys)):
            count += 1
    return count


def count_valid_passports(passports: List[str]) -> int:
    count = 0
    for passport in passports:
        keys = [el.split(':')[0] for el in passport.split()]
        values = [el.split(':')[1] for el in passport.split()]

        if set(MANDATORY_FIELDS_CHECKS.keys()).issubset(set(keys)):
            is_valid = True
            for index in range(len(values)):
                if keys[index] == 'cid':
                    continue
                if not MANDATORY_FIELDS_CHECKS[keys[index]](values[index]):
                    is_valid = False
                    break
            if is_valid:
                count += 1
    return count


if __name__ == "__main__":
    content = parse_input('input.txt')
    documents = get_documents(content)
    count = count_passports(documents)
    print("Solution 1:", count)
    count = count_valid_passports(documents)
    print("Solution 2:", count)
