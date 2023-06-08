import numpy as np
from queue import PriorityQueue
from typing import Optional, Tuple, List

from maze_solver.position_handler import MazePositionHandler

class MazeSolver:
    """A* algorithm based maze solver."""
    
    def __init__(self, maze: np.ndarray, start: Optional[Tuple[int, int]] = None, end: Optional[Tuple[int, int]] = None):
        """
        Initialize the solver.
        
        :param maze: 2D numpy array representing the maze.
        :param start: Optional tuple (row, column) for the starting position. If not provided, a random start is chosen.
        :param end: Optional tuple (row, column) for the ending position. If not provided, a random end is chosen.
        """
        self.maze = maze
        self.position_handler = MazePositionHandler(self.maze, start, end)
        self.possible_moves = [(0,1), (0,-1), (1,0), (-1,0)]

        # Initialize the data structures for cost and path tracking
        self.came_from = [[None for _ in range(self.maze.shape[1])] for _ in range(self.maze.shape[0])]
        self.cost_so_far = np.full_like(self.maze, fill_value=np.inf, dtype=float)
        self.came_from[self.position_handler.start[0]][self.position_handler.start[1]] = None
        self.cost_so_far[self.position_handler.start] = 0

    def _neighbors(self, cell):
        """Returns valid neighboring cells"""
        neighbors = []
        for move in self.possible_moves:
            new_position = tuple(np.add(cell, move))
            if (new_position[0] < 0 or new_position[1] < 0 or 
                new_position[0] >= self.maze.shape[0] or 
                new_position[1] >= self.maze.shape[1] or 
                self.maze[new_position] == 1):
                continue
            neighbors.append(new_position)
        return neighbors
    
    def _heuristic(self, a, b):
        """Manhattan distance heuristic"""
        return abs(b[0] - a[0]) + abs(b[1] - a[1])
        
    def solve(self) -> Optional[List[Tuple[int, int]]]:
        """Solve the maze using A* algorithm.

        :return: List of tuples representing the path from start to end. If no path is found, return None.
        """
        frontier = PriorityQueue()
        frontier.put((0, self.position_handler.start))

        while not frontier.empty():
            current = frontier.get()[1]

            # Break if goal reached
            if current == self.position_handler.end:
                break

            for next in self._neighbors(current):
                new_cost = self.cost_so_far[current] + 1
                if self.came_from[next[0]][next[1]] is None or new_cost < self.cost_so_far[next]:
                    self.cost_so_far[next] = new_cost
                    priority = new_cost + self._heuristic(self.position_handler.end, next)
                    frontier.put((priority, next))
                    self.came_from[next[0]][next[1]] = current

        if not frontier.empty():
            # Reconstruct path if a solution exists
            current = self.position_handler.end
            path = []
            while current != self.position_handler.start:
                path.append(current)
                current = self.came_from[current[0]][current[1]]
            path.append(self.position_handler.start)  # optional
            path.reverse()  # optional
            return path
        else:
            print("No path found!")
            return None

