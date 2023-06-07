import random
import numpy as np
from queue import PriorityQueue

class MazeSolver:
    """A* algorithm based maze solver"""
    
    def __init__(self, maze, start=None, end=None):
        """Initialize the solver"""
        self.maze = maze
        self.possible_moves = [(0,1), (0,-1), (1,0), (-1,0)]
        self._generate_random_positions(start, end)

        # Initialize the data structures for cost and path tracking
        self.came_from = [[None for _ in range(maze.shape[1])] for _ in range(maze.shape[0])]
        self.cost_so_far = np.full_like(maze, fill_value=np.inf, dtype=float)
        self.came_from[self.start[0]][self.start[1]] = None
        self.cost_so_far[self.start] = 0

    def _generate_random_positions(self, start, end):
        """Generate random start and end positions"""
        free_cells = np.argwhere(self.maze == 0)
        if not start:
            self.start = tuple(free_cells[random.randint(0, len(free_cells) - 1)])
        else:
            self.start = start

        if not end:
            self.end = tuple(free_cells[random.randint(0, len(free_cells) - 1)])
        else:
            self.end = end

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
        
    def solve(self):
        """Solve the maze"""
        frontier = PriorityQueue()
        frontier.put((0, self.start))

        while not frontier.empty():
            current = frontier.get()[1]
            
            # Break if goal reached
            if current == self.end:
                break

            for next in self._neighbors(current):
                new_cost = self.cost_so_far[current] + 1
                if self.came_from[next[0]][next[1]] is None or new_cost < self.cost_so_far[next]:
                    self.cost_so_far[next] = new_cost
                    priority = new_cost + self._heuristic(self.end, next)
                    frontier.put((priority, next))
                    self.came_from[next[0]][next[1]] = current

        if not frontier.empty():
            # Reconstruct path if a solution exists
            current = self.end
            path = []
            while current != self.start:
                path.append(current)
                current = self.came_from[current[0]][current[1]]
            path.append(self.start)  # optional
            path.reverse()  # optional
            return path
        else:
            print("No path found!")
            return None
