import math
from functools import reduce
from typing import Tuple, List, Dict
import numpy as np


def parse_input(filename: str) -> Tuple:
    f = open(filename, "r")
    lines = f.readlines()
    return (int(lines[0].replace('\n', '')), lines[1])


def get_available_buses(buses: str) -> List[int]:
    return [int(bus) for bus in buses.split(',') if bus != 'x']


def choose_nearest_bus(time: int, buses: List[int]) -> Tuple[int, int]:
    chosen_bus = None
    min_time_diff = math.inf
    for bus in buses:
        if time % bus == 0:
            return bus, 0
        else:
            instant_before = time // bus
            instant_after = bus * (instant_before + 1)
            if (instant_after - time) < min_time_diff:
                min_time_diff = instant_after - time
                chosen_bus = bus
    return chosen_bus, min_time_diff


def parse_buses_and_numbers_of_separating_minutes(bus_list: str) -> Dict:
    return {int(bus): minute for minute, bus in enumerate(bus_list.split(',')) if bus != 'x'}


def find_first_timestamp(buses_minutes: Dict) -> int:
    time = 17000000000 # start with large enough number
    while True:
        modulos = [(bus, (time + minute) % bus) for bus, minute in buses_minutes.items()]
        if sum([modulo[1] for modulo in modulos]) == 0:
            return time
        i = 1
        same_time_buses = []
        for bus, modulo in modulos:
            if modulo == 0:
                same_time_buses.append(bus)
        if len(same_time_buses) > 0:
            i = reduce(np.lcm, same_time_buses)
        time += i


if __name__ == "__main__":
    content = parse_input('input.txt')
    bus_list = get_available_buses(content[1])
    chosen_bus, time_diff = choose_nearest_bus(content[0], bus_list)
    print("Solution 1:", chosen_bus * time_diff)
    buses_minutes = parse_buses_and_numbers_of_separating_minutes(content[1])
    print("Solution 2:", find_first_timestamp(buses_minutes))
