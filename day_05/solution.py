from typing import List


def parse_input(filename: str) -> List[str]:
    f = open(filename, 'r')
    return [line.replace('\n', '') for line in f.readlines()]


def find_seat_row(seat: str) -> int:
    row_indication = seat[:7]
    row_indication_binary = row_indication.replace('B', '1').replace('F', '0')
    return int(row_indication_binary, 2)


def find_seat_column(seat: str) -> int:
    row_indication = seat[7:]
    row_indication_binary = row_indication.replace('R', '1').replace('L', '0')
    return int(row_indication_binary, 2)


def get_all_boarding_passes_ids(boarding_passes: List[str]) -> List[int]:
    return [row * 8 + column for row, column in [(find_seat_row(bp), find_seat_column(bp)) for bp in boarding_passes]]


def get_all_possible_ids(ids: List[int]) -> List:
    solutions = []
    for i in range(len(ids)):
        for j in range(i, len(ids)):
            if abs(ids[i] - ids[j]) == 2:
                solutions.append(max(ids[i], ids[j]) - 1)
    return solutions


def get_id_not_in_list(possible_ids: List[int], all_ids: List[int]) -> int:
    return [el for el in possible_ids if el not in all_ids][0]


if __name__ == "__main__":
    content = parse_input('input.txt')
    ids = get_all_boarding_passes_ids(content)
    print("Solution 1: ", max(ids))
    possible_ids = get_all_possible_ids(ids)
    print("Solution 2: ", get_id_not_in_list(possible_ids, ids))
