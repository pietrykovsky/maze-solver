import numpy as np
from numpy.random import shuffle

class MazeGenerator:
    def __init__(self, h, w):
        """Initialize maze dimensions and create an empty grid."""
        assert w >= 3 and h >= 3, "Mazes cannot be smaller than 3x3."
        self.h, self.w = h, w
        self.H, self.W = (2 * h) + 1, (2 * w) + 1
        self.grid = np.empty((self.H, self.W), dtype=np.int8)
        self.grid.fill(1)

    def _create_forest_and_edges(self):
        """Populate forest with cells and edges with potential wall positions."""
        forest = [[(row, col)] for row in range(1, self.H - 1, 2) for col in range(1, self.W - 1, 2)]
        edges = [(row, col) for row in range(2, self.H - 1, 2) for col in range(1, self.W - 1, 2)] + \
                 [(row, col) for row in range(1, self.H - 1, 2) for col in range(2, self.W - 1, 2)]

        shuffle(edges)

        for cell in forest:
            self.grid[cell[0]] = 0

        return forest, edges

    def _find_trees(self, forest, row, col):
        """Find the indices of the trees to which two cells belong."""
        tree1 = self._find_tree(forest, row - 1, col) if row % 2 == 0 else self._find_tree(forest, row, col - 1)
        tree2 = self._find_tree(forest, row + 1, col) if row % 2 == 0 else self._find_tree(forest, row, col + 1)
        return tree1, tree2

    @staticmethod
    def _find_tree(forest, row, col):
        """Find the index of the tree to which a cell belongs."""
        for i, tree in enumerate(forest):
            if (row, col) in tree:
                return i
        return -1  # return -1 if no tree is found

    def generate(self):
        """Generate the maze using a modified version of Kruskal's algorithm."""
        forest, edges = self._create_forest_and_edges()

        while len(forest) > 1 and edges:
            current_edge = edges.pop(0)
            tree1, tree2 = self._find_trees(forest, *current_edge)

            if tree1 != -1 and tree2 != -1 and tree1 != tree2:
                self._merge_trees(forest, tree1, tree2)
                self.grid[current_edge] = 0

        return self.grid

    @staticmethod
    def _merge_trees(forest, tree1, tree2):
        """Merge two trees in the forest."""
        forest.append(forest.pop(tree1) + forest.pop(tree2 - 1 if tree2 > tree1 else tree2))
