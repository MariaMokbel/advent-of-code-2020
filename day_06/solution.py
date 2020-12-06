from functools import reduce
from typing import List


def parse_input(filename: str) -> List[str]:
    file_content = []
    with open(filename) as f:
        for line in f:
            file_content.append(line.replace('\n', ''))
    return file_content


def get_groups(file_content: List[str]) -> List[str]:
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


def count_yes_questions(groups: List[str]) -> int:
    return reduce(lambda a, b: a + b, [len(set(questions.replace(' ', ''))) for questions in groups])


def count_all_yes_questions(groups: List[str]):
    all_yes_questions = 0
    for group in groups:
        questions = []
        people = group.count(' ')
        for q in group:
            if group.replace(' ','').count(q) == people and q not in questions:
                questions.append(q)
        all_yes_questions += len(questions)
    return all_yes_questions


if __name__ == "__main__":
    content = parse_input('input.txt')
    groups = get_groups(content)
    yes_count = count_yes_questions(groups)
    print("Solution 1:", yes_count)
    all_yes_count = count_all_yes_questions(groups)
    print("Solution 2:", all_yes_count)
