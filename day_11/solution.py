from typing import List, Tuple, Optional


def parse_input(filename: str) -> List[str]:
    file_content = []
    with open(filename) as f:
        for line in f:
            file_content.append(line.replace('\n', ''))
    return file_content


def convert(string: str) -> List[str]:
    list1 = []
    list1[:0] = string
    return list1


def is_empty_or_floor(seat: str) -> bool:
    return seat == 'L' or seat == '.'


def create_seat_map(seats: List[str]):
    new_seat_map = seats.copy()

    new_row = convert(new_seat_map[0])
    new_row[0] = '#'
    new_row[len(seats[0]) - 1] = '#'
    new_seat_map[0] = ''.join(new_row)
    new_row = convert(new_seat_map[len(seats) - 1])
    new_row[0] = '#'
    new_seat_map[len(seats) - 1] = ''.join(new_row)

    for row_index in range(len(seats)):
        for seat_index in range(len(seats[row_index])):
            if (row_index == 0 and (seat_index == 0 or seat_index == len(seats[row_index]) - 1)) \
                    or (row_index == len(seats) - 1 and (seat_index == 0 or seat_index == len(seats[row_index]) - 1)):
                continue
            elif row_index == 0:
                if seats[0][seat_index] == 'L' and all_seats_empty(seats, 0, seat_index):
                    update_seats_map(new_seat_map, 0, seat_index, '#')
                if seats[0][seat_index] == '#' and more_than_four_seats_occupied(seats, 0, seat_index):
                    update_seats_map(new_seat_map, 0, seat_index, 'L')

            elif row_index == len(seats) - 1:
                if seats[len(seats) - 1][seat_index] == 'L' and all_seats_empty(seats, len(seats) - 1,
                                                                                seat_index):
                    update_seats_map(new_seat_map, len(seats) - 1, seat_index, '#')
                if seats[len(seats) - 1][seat_index] == '#' and more_than_four_seats_occupied(seats, len(seats) - 1,
                                                                                              seat_index):
                    update_seats_map(new_seat_map, len(seats) - 1, seat_index, 'L')

            elif seat_index == 0:
                if seats[row_index][0] == 'L' and all_seats_empty(seats, row_index, 0):
                    update_seats_map(new_seat_map, row_index, 0, '#')
                if seats[row_index][0] == '#' and more_than_four_seats_occupied(seats, row_index, 0):
                    update_seats_map(new_seat_map, row_index, 0, 'L')

            elif seat_index == len(seats[0]) - 1:
                if seats[row_index][len(seats[0]) - 1] == 'L' and all_seats_empty(seats, row_index, len(seats[0]) - 1):
                    update_seats_map(new_seat_map, row_index, len(seats[0]) - 1, '#')
                if seats[row_index][len(seats[0]) - 1] == '#' and more_than_four_seats_occupied(seats, row_index,
                                                                                                len(seats[0]) - 1):
                    update_seats_map(new_seat_map, row_index, len(seats[0]) - 1, 'L')

            else:
                if seats[row_index][seat_index] == 'L' and all_seats_empty(seats, row_index, seat_index):
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
                if seats[row_index][seat_index] == '#' and more_than_four_seats_occupied(seats, row_index, seat_index):
                    update_seats_map(new_seat_map, row_index, seat_index, 'L')

    return new_seat_map


def more_than_four_seats_occupied(seats, row_index, seat_index):
    adjacent_seats = []
    if row_index == 0:
        adjacent_seats.append(seats[0][seat_index - 1])
        adjacent_seats.append(seats[0][seat_index + 1])
        adjacent_seats.append(seats[1][seat_index - 1])
        adjacent_seats.append(seats[1][seat_index])
        adjacent_seats.append(seats[1][seat_index + 1])
        return adjacent_seats.count('#') > 3

    if row_index == len(seats) - 1:
        adjacent_seats.append(seats[len(seats) - 1][seat_index - 1])
        adjacent_seats.append(seats[len(seats) - 1][seat_index + 1])
        adjacent_seats.append(seats[len(seats) - 2][seat_index - 1])
        adjacent_seats.append(seats[len(seats) - 2][seat_index])
        adjacent_seats.append(seats[len(seats) - 2][seat_index + 1])
        return adjacent_seats.count('#') > 3

    if seat_index == 0:
        adjacent_seats.append(seats[row_index - 1][0])
        adjacent_seats.append(seats[row_index - 1][1])
        adjacent_seats.append(seats[row_index][1])
        adjacent_seats.append(seats[row_index + 1][0])
        adjacent_seats.append(seats[row_index + 1][1])
        return adjacent_seats.count('#') > 3

    if seat_index == len(seats[0]) - 1:
        adjacent_seats.append(seats[row_index - 1][len(seats[0]) - 1])
        adjacent_seats.append(seats[row_index - 1][len(seats[0]) - 2])
        adjacent_seats.append(seats[row_index][len(seats[0]) - 2])
        adjacent_seats.append(seats[row_index + 1][len(seats[0]) - 1])
        adjacent_seats.append(seats[row_index + 1][len(seats[0]) - 2])
        return adjacent_seats.count('#') > 3

    adjacent_seats.append(seats[row_index - 1][seat_index - 1])
    adjacent_seats.append(seats[row_index - 1][seat_index])
    adjacent_seats.append(seats[row_index - 1][seat_index + 1])
    adjacent_seats.append(seats[row_index][seat_index - 1])
    adjacent_seats.append(seats[row_index][seat_index + 1])
    adjacent_seats.append(seats[row_index + 1][seat_index - 1])
    adjacent_seats.append(seats[row_index + 1][seat_index])
    adjacent_seats.append(seats[row_index + 1][seat_index + 1])
    return adjacent_seats.count('#') > 3


def all_seats_empty(seats, row_index, seat_index):
    adjacent_seats = []
    if row_index == 0:
        adjacent_seats.append(is_empty_or_floor(seats[0][seat_index - 1]))
        adjacent_seats.append(is_empty_or_floor(seats[0][seat_index + 1]))
        adjacent_seats.append(is_empty_or_floor(seats[1][seat_index - 1]))
        adjacent_seats.append(is_empty_or_floor(seats[1][seat_index]))
        adjacent_seats.append(is_empty_or_floor(seats[1][seat_index + 1]))
        return sum(adjacent_seats) == len(adjacent_seats)

    if row_index == len(seats) - 1:
        adjacent_seats.append(is_empty_or_floor(seats[len(seats) - 1][seat_index - 1]))
        adjacent_seats.append(is_empty_or_floor(seats[len(seats) - 1][seat_index + 1]))
        adjacent_seats.append(is_empty_or_floor(seats[len(seats) - 2][seat_index - 1]))
        adjacent_seats.append(is_empty_or_floor(seats[len(seats) - 2][seat_index]))
        adjacent_seats.append(is_empty_or_floor(seats[len(seats) - 2][seat_index + 1]))
        return sum(adjacent_seats) == len(adjacent_seats)

    if seat_index == 0:
        adjacent_seats.append(is_empty_or_floor(seats[row_index - 1][0]))
        adjacent_seats.append(is_empty_or_floor(seats[row_index - 1][1]))
        adjacent_seats.append(is_empty_or_floor(seats[row_index][1]))
        adjacent_seats.append(is_empty_or_floor(seats[row_index + 1][0]))
        adjacent_seats.append(is_empty_or_floor(seats[row_index + 1][1]))
        return sum(adjacent_seats) == len(adjacent_seats)

    if seat_index == len(seats[0]) - 1:
        adjacent_seats.append(is_empty_or_floor(seats[row_index - 1][len(seats[0]) - 1]))
        adjacent_seats.append(is_empty_or_floor(seats[row_index - 1][len(seats[0]) - 2]))
        adjacent_seats.append(is_empty_or_floor(seats[row_index][len(seats[0]) - 2]))
        adjacent_seats.append(is_empty_or_floor(seats[row_index + 1][len(seats[0]) - 1]))
        adjacent_seats.append(is_empty_or_floor(seats[row_index + 1][len(seats[0]) - 2]))
        return sum(adjacent_seats) == len(adjacent_seats)

    adjacent_seats.append(is_empty_or_floor(seats[row_index - 1][seat_index - 1]))
    adjacent_seats.append(is_empty_or_floor(seats[row_index - 1][seat_index]))
    adjacent_seats.append(is_empty_or_floor(seats[row_index - 1][seat_index + 1]))
    adjacent_seats.append(is_empty_or_floor(seats[row_index][seat_index - 1]))
    adjacent_seats.append(is_empty_or_floor(seats[row_index][seat_index + 1]))
    adjacent_seats.append(is_empty_or_floor(seats[row_index + 1][seat_index - 1]))
    adjacent_seats.append(is_empty_or_floor(seats[row_index + 1][seat_index]))
    adjacent_seats.append(is_empty_or_floor(seats[row_index + 1][seat_index + 1]))
    return sum(adjacent_seats) == len(adjacent_seats)


def find_right_seat(seats: List, row_index: int, seat_index: int) -> Optional[Tuple[int, int]]:
    i = seat_index + 1
    while i < len(seats[0]) and seats[row_index][i] == '.':
        i += 1
    if i == len(seats[0]):
        return None
    return row_index, i


def find_left_seat(seats: List, row_index: int, seat_index: int) -> Optional[Tuple[int, int]]:
    i = seat_index - 1
    while seats[row_index][i] == '.' and i >= 0:
        i -= 1
    if i == -1:
        return None
    return row_index, i


def find_bottom_seat(seats: List, row_index: int, seat_index: int) -> Optional[Tuple[int, int]]:
    i = row_index + 1
    while i < len(seats) and seats[i][seat_index] == '.':
        i += 1
    if i == len(seats):
        return None
    return i, seat_index


def find_up_seat(seats: List, row_index: int, seat_index: int) -> Optional[Tuple[int, int]]:
    i = row_index - 1
    while seats[i][seat_index] == '.' and i >= 0:
        i -= 1
    if i == -1:
        return None
    return i, seat_index


def find_bottom_right_seat(seats: List, row_index: int, seat_index: int) -> Optional[Tuple[int, int]]:
    row_i = row_index + 1
    seat_i = seat_index + 1
    while row_i < len(seats) and seat_i < len(seats[0]) and seats[row_i][seat_i] == '.':
        row_i += 1
        seat_i += 1
    if row_i == len(seats) or seat_i == len(seats[0]):
        return None
    return row_i, seat_i


def find_up_right_seat(seats: List, row_index: int, seat_index: int) -> Optional[Tuple[int, int]]:
    row_i = row_index - 1
    seat_i = seat_index + 1
    while row_i >= 0 and seat_i < len(seats[0]) and seats[row_i][seat_i] == '.':
        row_i -= 1
        seat_i += 1
    if row_i == -1 or seat_i == len(seats[0]):
        return None
    return row_i, seat_i


def find_bottom_left_seat(seats: List, row_index: int, seat_index: int) -> Optional[Tuple[int, int]]:
    row_i = row_index + 1
    seat_i = seat_index - 1
    while row_i < len(seats) and seat_i >= 0 and seats[row_i][seat_i] == '.':
        row_i += 1
        seat_i -= 1
    if row_i == len(seats) or seat_i == -1:
        return None
    return row_i, seat_i


def find_up_left_seat(seats: List, row_index: int, seat_index: int) -> Optional[Tuple[int, int]]:
    row_i = row_index - 1
    seat_i = seat_index - 1
    while row_i >= 0 and seat_i >= 0 and seats[row_i][seat_i] == '.':
        row_i -= 1
        seat_i -= 1
    if row_i == -1 or seat_i == -1:
        return None
    return row_i, seat_i


def create_seat_map_2(seats: List[str]):
    new_seat_map = seats.copy()

    for row_index in range(len(seats)):
        for seat_index in range(len(seats[row_index])):
            if seats[row_index][seat_index] == 'L' and row_index == 0 and seat_index == 0:
                right_seat = find_right_seat(seats, row_index, seat_index)
                bottom_seat = find_bottom_seat(seats, row_index, seat_index)
                bottom_right_seat = find_bottom_right_seat(seats, row_index, seat_index)
                if count_nearby_seats_occupied(seats, [right_seat, bottom_seat, bottom_right_seat]) == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
            elif seats[row_index][seat_index] == 'L' and row_index == 0 and seat_index == len(seats[0]) - 1:
                left_seat = find_left_seat(seats, row_index, seat_index)
                bottom_seat = find_bottom_seat(seats, row_index, seat_index)
                bottom_left_seat = find_bottom_left_seat(seats, row_index, seat_index)
                if count_nearby_seats_occupied(seats, [left_seat, bottom_seat, bottom_left_seat]) == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
            elif seats[row_index][seat_index] == 'L' and row_index == len(seats) - 1 and seat_index == 0:
                right_seat = find_right_seat(seats, row_index, seat_index)
                up_seat = find_up_seat(seats, row_index, seat_index)
                up_right_seat = find_up_right_seat(seats, row_index, seat_index)
                if count_nearby_seats_occupied(seats, [right_seat, up_seat, up_right_seat]) == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
            elif seats[row_index][seat_index] == 'L' and row_index == len(seats) - 1 and seat_index == len(seats[0]) - 1:
                left_seat = find_left_seat(seats, row_index, seat_index)
                up_seat = find_up_seat(seats, row_index, seat_index)
                up_left_seat = find_up_left_seat(seats, row_index, seat_index)
                if count_nearby_seats_occupied(seats, [left_seat, up_seat, up_left_seat]) == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')

            elif row_index == 0:
                right_seat = find_right_seat(seats, row_index, seat_index)
                left_seat = find_left_seat(seats, row_index, seat_index)
                bottom_seat = find_bottom_seat(seats, row_index, seat_index)
                bottom_left_seat = find_bottom_left_seat(seats, row_index, seat_index)
                bottom_right_seat = find_bottom_right_seat(seats, row_index, seat_index)
                nearby_seats_occupied = count_nearby_seats_occupied(seats, [right_seat, left_seat, bottom_seat,
                                                                            bottom_left_seat,
                                                                            bottom_right_seat])
                if seats[row_index][seat_index] == 'L' and nearby_seats_occupied == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
                if seats[row_index][seat_index] == '#' and nearby_seats_occupied >= 5:
                    update_seats_map(new_seat_map, row_index, seat_index, 'L')
            elif row_index == len(seats) - 1:
                right_seat = find_right_seat(seats, row_index, seat_index)
                left_seat = find_left_seat(seats, row_index, seat_index)
                up_seat = find_up_seat(seats, row_index, seat_index)
                up_left_seat = find_up_left_seat(seats, row_index, seat_index)
                up_right_seat = find_up_right_seat(seats, row_index, seat_index)
                nearby_seats_occupied = count_nearby_seats_occupied(seats, [right_seat, left_seat, up_seat,
                                                                            up_left_seat,
                                                                            up_right_seat])
                if seats[row_index][seat_index] == 'L' and nearby_seats_occupied == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
                if seats[row_index][seat_index] == '#' and nearby_seats_occupied >= 5:
                    update_seats_map(new_seat_map, row_index, seat_index, 'L')

            elif seat_index == 0:
                right_seat = find_right_seat(seats, row_index, seat_index)
                bottom_seat = find_bottom_seat(seats, row_index, seat_index)
                up_seat = find_up_seat(seats, row_index, seat_index)
                bottom_right_seat = find_bottom_right_seat(seats, row_index, seat_index)
                up_right_seat = find_up_right_seat(seats, row_index, seat_index)
                nearby_seats_occupied = count_nearby_seats_occupied(seats, [right_seat, bottom_seat, up_seat,
                                                                            bottom_right_seat,
                                                                            up_right_seat])
                if seats[row_index][seat_index] == 'L' and nearby_seats_occupied == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
                if seats[row_index][seat_index] == '#' and nearby_seats_occupied >= 5:
                    update_seats_map(new_seat_map, row_index, seat_index, 'L')

            elif seat_index == len(seats[0]) - 1:
                left_seat = find_left_seat(seats, row_index, seat_index)
                bottom_seat = find_bottom_seat(seats, row_index, seat_index)
                up_seat = find_up_seat(seats, row_index, seat_index)
                bottom_left_seat = find_bottom_left_seat(seats, row_index, seat_index)
                up_left_seat = find_up_left_seat(seats, row_index, seat_index)
                nearby_seats_occupied = count_nearby_seats_occupied(seats, [left_seat, bottom_seat, up_seat,
                                                                            bottom_left_seat,
                                                                            up_left_seat])
                if seats[row_index][seat_index] == 'L' and nearby_seats_occupied == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
                if seats[row_index][seat_index] == '#' and nearby_seats_occupied >= 5:
                    update_seats_map(new_seat_map, row_index, seat_index, 'L')

            else:
                left_seat = find_left_seat(seats, row_index, seat_index)
                right_seat = find_right_seat(seats, row_index, seat_index)
                bottom_seat = find_bottom_seat(seats, row_index, seat_index)
                up_seat = find_up_seat(seats, row_index, seat_index)
                bottom_left_seat = find_bottom_left_seat(seats, row_index, seat_index)
                bottom_right_seat = find_bottom_right_seat(seats, row_index, seat_index)
                up_left_seat = find_up_left_seat(seats, row_index, seat_index)
                up_right_seat = find_up_right_seat(seats, row_index, seat_index)
                nearby_seats_occupied = count_nearby_seats_occupied(seats, [left_seat, right_seat, bottom_seat, up_seat,
                                                                            bottom_left_seat, bottom_right_seat,
                                                                            up_right_seat,
                                                                            up_left_seat])
                if seats[row_index][seat_index] == 'L' and nearby_seats_occupied == 0:
                    update_seats_map(new_seat_map, row_index, seat_index, '#')
                if seats[row_index][seat_index] == '#' and nearby_seats_occupied >= 5:
                    update_seats_map(new_seat_map, row_index, seat_index, 'L')

    return new_seat_map


def count_nearby_seats_occupied(seats: List, nearby_seats: List):
    count = 0
    for seat in nearby_seats:
        if seat:
            row = int(seat[0])
            column = int(seat[1])
            if seats[row][column] == '#':
                count += 1
    return count


def update_seats_map(new_seat_map, row_index, seat_index, value):
    new_row = convert(new_seat_map[row_index])
    new_row[seat_index] = value
    new_seat_map[row_index] = ''.join(new_row)


if __name__ == "__main__":
    map = parse_input('input.txt')
    map_copy = map.copy()
    new_map = create_seat_map(map)
    while map != new_map:
        map = new_map
        new_map = create_seat_map(map)

    print("Solution 1:", sum([row.count('#') for row in new_map]))
    map_copy = parse_input('input.txt')
    new_map_2 = create_seat_map_2(map_copy)
    while map_copy != new_map_2:
        map_copy = new_map_2
        new_map_2 = create_seat_map_2(map_copy)

    print("Solution 2:", sum([row.count('#') for row in new_map_2]))
