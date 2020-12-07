import unittest

from day_07.solution import BagData, Tree, construct_tree, dfs


class MyTestCase(unittest.TestCase):
    def test_count_bags(self):
        # Given
        bags = {'shiny gold': [BagData('dark red', 2)],
                'dark red': [BagData('dark orange', 2)],
                'dark orange': [BagData('dark yellow', 2)],
                'dark yellow': [BagData('dark green', 2)],
                'dark green': [BagData('dark blue', 2)],
                'dark blue': [BagData('dark violet', 2)]}

        # When Then
        root = Tree(BagData('shiny gold', 1))
        tree = construct_tree(bags, root)
        count = []
        dfs(tree, [], 1, count)
        self.assertEqual(sum(count) - 1, 126)

    def test_count_bags_2(self):
        # Given
        bags = {'shiny gold': [BagData('dark olive', 1), BagData('vibrant plum', 2)],
                'dark olive': [BagData('faded blue', 3), BagData('dotted black', 4)],
                'vibrant plum': [BagData('faded blue', 5), BagData('dotted black', 6)]}

        # When Then
        root = Tree(BagData('shiny gold', 1))
        tree = construct_tree(bags, root)
        count = []
        dfs(tree, [], 1, count)
        self.assertEqual(sum(count) - 1, 32)


if __name__ == '__main__':
    unittest.main()
