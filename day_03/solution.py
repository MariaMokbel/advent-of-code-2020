from typing import List, Tuple


def parse_input(filename: str) -> List[str]:
    file_content = []
    with open(filename) as f:
        for line in f:
            file_content.append(line[:-1])
    return file_content


def count_trees_till_bottom(content: List[str], right_step: int, down_step: int) -> int:
    trees = 0
    down = 0
    right = 0
    line_length = len(content[0])
    while down < len(content) - 1:
        right = (right + right_step) % line_length
        down += down_step
        if is_tree(content[down][right]):
            trees = trees + 1
    return trees


def is_tree(element):
    return element == '#'


if __name__ == "__main__":
    content = parse_input('input.txt')
    trees = count_trees_till_bottom(content, 3, 1)
    print("Solution 1: ", trees)
    trees_1_1 = count_trees_till_bottom(content, 1, 1)
    trees_3_1 = count_trees_till_bottom(content, 3, 1)
    trees_5_1 = count_trees_till_bottom(content, 5, 1)
    trees_7_1 = count_trees_till_bottom(content, 7, 1)
    trees_1_2 = count_trees_till_bottom(content, 1, 2)
    print("Solution 2: ", trees_1_1 * trees_3_1 * trees_5_1 * trees_7_1 * trees_1_2)
