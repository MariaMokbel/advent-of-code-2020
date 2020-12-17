from functools import lru_cache
from typing import List


class Point:
    def __init__(self, x: int, y: int, z: int, state: str):
        self.x = x
        self.y = y
        self.z = z
        self.state = state

    def __str__(self) -> str:
        return f'Point({self.x},{self.y},{self.z},{self.state})'

    def get_coordinates(self):
        return self.x, self.y, self.z

    @property
    @lru_cache()
    def get_neighbors(self):
        neighbors = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    if x != 0 or y != 0 or z != 0:
                        neighbors.append(Point(self.x + x, self.y + y, self.z + z, '.'))

        return neighbors

    def __eq__(self, o: 'Point') -> bool:
        return o.x == self.x and o.y == self.y and o.z == self.z

    def __hash__(self) -> int:
        return self.x + self.y + self.z


class Point2:
    def __init__(self, x: int, y: int, z: int, w: int, state: str):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.state = state

    def __str__(self) -> str:
        return f'Point2({self.x},{self.y},{self.z},{self.w},{self.state})'

    def get_coordinates(self):
        return self.x, self.y, self.z, self.w

    @property
    @lru_cache()
    def get_neighbors(self):
        neighbors = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    for w in [-1, 0, 1]:
                        if x != 0 or y != 0 or z != 0 or w != 0:
                            neighbors.append(Point2(self.x + x, self.y + y, self.z + z, self.w + w, '.'))

        return neighbors

    def __eq__(self, o: 'Point2') -> bool:
        return o.x == self.x and o.y == self.y and o.z == self.z and o.w == self.w

    def __hash__(self) -> int:
        return self.x + self.y + self.z + self.w


def parse_input(filename: str) -> List[Point]:
    content = []
    y = 0
    z = 0
    with open(filename) as f:
        for line in f:
            cleaned_line = line.replace('\n', '')
            x = 0
            for point in cleaned_line:
                content.append(Point(x, y, z, point))
                x += 1
            y += 1

    return content


def parse_input_2(filename: str) -> List[Point2]:
    content = []
    y = 0
    z = 0
    w = 0
    with open(filename) as f:
        for line in f:
            cleaned_line = line.replace('\n', '')
            x = 0
            for point in cleaned_line:
                content.append(Point2(x, y, z, w, point))
                x += 1
            y += 1

    return content


def compute_cycle(points: List[Point]) -> List[Point]:
    all_points = []
    for point in points:
        count_active_neighbors_1 = 0
        for neighbor in point.get_neighbors:

            if neighbor in points:
                count_active_neighbors_1 += 1
                if len([n for n in neighbor.get_neighbors if n in points]) in [2, 3]:
                    all_points.append(Point(neighbor.x, neighbor.y, neighbor.z, '#'))
            else:
                if len([n for n in neighbor.get_neighbors if n in points]) == 3:
                    all_points.append(Point(neighbor.x, neighbor.y, neighbor.z, '#'))

        if count_active_neighbors_1 in [2, 3]:
            all_points.append(Point(point.x, point.y, point.z, '#'))

    return all_points


def compute_cycle2(points: List[Point2]) -> List[Point2]:
    all_points = []
    for point in points:
        count_active_neighbors_1 = 0
        for neighbor in point.get_neighbors:

            if neighbor in points:
                count_active_neighbors_1 += 1
            else:
                active_neighbors = len([n for n in neighbor.get_neighbors if n in points])
                if active_neighbors == 3:
                    all_points.append(Point2(neighbor.x, neighbor.y, neighbor.z, neighbor.w, '#'))

        if count_active_neighbors_1 in [2, 3]:
            all_points.append(Point2(point.x, point.y, point.z, point.w, '#'))

    return all_points


def get_only_active_points(new_points):
    return [point for point in new_points if point.state == '#']


if __name__ == "__main__":
    points = parse_input('input.txt')
    points2 = parse_input_2('input.txt')

    active_points = get_only_active_points(set(points))

    for i in range(6):
        new_points = compute_cycle(active_points)
        active_points = list(set(get_only_active_points(new_points)))

    print("Solution 1:", len(active_points))

    active_points2 = get_only_active_points(set(points2))

    for i in range(6):
        new_points = compute_cycle2(active_points2)
        active_points2 = list(set(get_only_active_points(new_points)))

    print("Solution 2:", len(active_points2))
