from typing import List, Dict


class BagData:
    def __init__(self, bag_type: str, number: int):
        self.bag_type = bag_type
        self.number = number

    def __str__(self):
        return str(self.number) + ' ' + self.bag_type


def parse_input(filename: str) -> Dict:
    file_content = {}
    with open(filename) as f:
        for line in f:
            container = line.split('bags contain ')[0][:-1]
            if line.split('bags contain ')[1][:-1] == 'no other bags.':
                continue
            content = [BagData(bag_type, number) for number, bag_type in
                       [(int(el[0]), el[2:].replace(' bags', '').replace(' bag', '')) for el in
                        line.split('bags contain ')[1][:-2].split(', ')]]
            file_content[container] = content
    return file_content


def find_bag_colors(bags_data: Dict, colors: List):
    possible_colors = []
    if len(colors) == 0:
        return []
    for color in colors:
        for key, values in bags_data.items():
            if color in [value.bag_type for value in values]:
                possible_colors.append(key)
    return colors + find_bag_colors(bags_data, possible_colors)


class Node():
    def __init__(self, data: BagData):
        self.data = data
        self.children = []

    def add_node(self, node: 'Node'):
        self.children.append(node)


class Tree:
    def __init__(self, root: BagData):
        self.data = root
        self.children = []

    def add_node(self, node: Node):
        self.children.append(node)


def construct_tree(bags_data: Dict, node: Node or Tree) -> Node or Tree:
    for bag_color, bags in bags_data.items():
        if bag_color == node.data.bag_type:
            for bag in bags:
                new_bag_data = BagData(bag.bag_type, bag.number)
                node.add_node(construct_tree(bags_data, Node(new_bag_data)))
    return node


def dfs(node: Tree or Node, visited: List, multiplier: int, count: List):
    if node not in visited:
        visited.append(node)
        count.append(multiplier * node.data.number)
        if len(node.children) == 0:
            multiplier = 1
        else:
            multiplier = multiplier * node.data.number
        for child in node.children:
            dfs(child, visited, multiplier, count)


if __name__ == "__main__":
    content = parse_input('input.txt')
    colors = find_bag_colors(content, ['shiny gold'])
    print("Solution 1:", len(set(colors)) - 1)
    root = Tree(BagData('shiny gold', 1))
    tree = construct_tree(content, root)
    count = []
    dfs(tree, [], 1, count)
    print("Solution 2:", sum(count) - 1)
