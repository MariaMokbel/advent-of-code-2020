from typing import List, Tuple


def parse_input(filename: str) -> List[Tuple]:
    file_content = []
    with open(filename) as f:
        for line in f:
            cleaned_line = line.replace('\n', '')
            file_content.append((cleaned_line[0], int(cleaned_line[1:])))
    return file_content


def update_east_direction(east: int, north: int, steps: int) -> Tuple:
    east += steps
    return east, north


def update_west_direction(east: int, north: int, steps: int) -> Tuple:
    east -= steps
    return east, north


def update_north_direction(east: int, north: int, steps: int) -> Tuple:
    north += steps
    return east, north


def update_south_direction(east: int, north: int, steps: int) -> Tuple:
    north -= steps
    return east, north


UPDATE_DIRECTIONS = {
    'E': update_east_direction,
    'W': update_west_direction,
    'N': update_north_direction,
    'S': update_south_direction
}


def turn_right(current_direction: str, degrees: int):
    right_direction = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
    for i in range(degrees // 90):
        current_direction = right_direction[current_direction]
    return current_direction


def turn_left(current_direction: str, degrees: int):
    left_direction = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }
    for i in range(degrees // 90):
        current_direction = left_direction[current_direction]
    return current_direction


def try_exchange_directions(instruction, waypoint):
    opposite_directions = {
        'S': 'N',
        'N': 'S',
        'W': 'E',
        'E': 'W'
    }
    waypoint[opposite_directions[instruction[0]]] -= instruction[1]
    if waypoint[opposite_directions[instruction[0]]] < 0:
        waypoint[instruction[0]] = -waypoint[opposite_directions[instruction[0]]]
        waypoint.pop(opposite_directions[instruction[0]])


def calculate_manhattan_distance(instructions: List[Tuple]) -> int:
    east = 0
    north = 0
    current_direction = 'E'
    for instruction in instructions:
        if instruction[0] == 'F':
            east, north = UPDATE_DIRECTIONS[current_direction](east, north, instruction[1])
        elif instruction[0] == 'R':
            current_direction = turn_right(current_direction, instruction[1])
        elif instruction[0] == 'L':
            current_direction = turn_left(current_direction, instruction[1])
        else:
            east, north = UPDATE_DIRECTIONS[instruction[0]](east, north, instruction[1])

    return abs(east) + abs(north)


def calculate_manhattan_distance_with_waypoint(instructions: List[Tuple]) -> int:
    waypoint = {
        'E': 10,
        'N': 1
    }
    current_position = {
        'E': 0,
        'N': 0,
        'W': 0,
        'S': 0
    }

    for instruction in instructions:
        if instruction[0] == 'F':
            for direction, value in waypoint.items():
                current_position[direction] = current_position[direction] + value * instruction[1]

        elif instruction[0] == 'R':
            new_waypoint = {}
            for direction, value in waypoint.items():
                new_waypoint[turn_right(direction, instruction[1])] = value
            waypoint = new_waypoint

        elif instruction[0] == 'L':
            new_waypoint = {}
            for direction, value in waypoint.items():
                new_waypoint[turn_left(direction, instruction[1])] = value
            waypoint = new_waypoint

        else:
            try:
                waypoint[instruction[0]] += instruction[1]
            except:
                try_exchange_directions(instruction, waypoint)

    return abs(current_position['E'] - current_position['W']) + abs(current_position['N'] - current_position['S'])


if __name__ == "__main__":
    content = parse_input('input.txt')
    print("Solution 1:", calculate_manhattan_distance(content))
    print("Solution 2:", calculate_manhattan_distance_with_waypoint(content))
