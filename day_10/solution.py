from typing import List, Tuple


def parse_input(filename: str) -> List[int]:
    file_content = []
    with open(filename) as f:
        for line in f:
            file_content.append(int(line.replace('\n', '')))
    return file_content


def build_adapters_chain(adapters: List[int]) -> Tuple[List[int], List[int]]:
    current_adapter = 0
    chain = [current_adapter]
    differences = []
    while (len(adapters)) > 0:
        tmp_adapters = []
        for adapter in adapters:
            if adapter - current_adapter < 4:
                tmp_adapters.append(adapter)
        closest_adapter = min(tmp_adapters)
        differences.append(closest_adapter - current_adapter)
        current_adapter = closest_adapter
        chain.append(closest_adapter)
        adapters.remove(closest_adapter)
    return chain, differences


def find_adapter_differences(adapters: List[int]):
    adapters.sort()
    possibilities = {0: 1}
    for adapter in adapters:
        possibilities[adapter] = 0
        if adapter - 1 in possibilities:
            possibilities[adapter] += possibilities[adapter - 1]

        if adapter - 2 in possibilities:
            possibilities[adapter] += possibilities[adapter - 2]

        if adapter - 3 in possibilities:
            possibilities[adapter] += possibilities[adapter - 3]
    return possibilities[max(adapters)]


if __name__ == "__main__":
    content = parse_input('input.txt')
    copy_content = content.copy()
    adapters_chain, differences = build_adapters_chain(content)
    differences.append(3)  # for built-in adapter
    print("Solution 1:", differences.count(1) * differences.count(3))
    value = find_adapter_differences(copy_content)
    print("Solution 2:", value)
