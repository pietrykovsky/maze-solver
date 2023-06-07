from matplotlib import pyplot as plt
import numpy as np

from maze_solver.generation import MazeGenerator
from maze_solver.solver import MazeSolver

def plot_maze(maze, path=None):
    """Visualize the maze and the path found (if provided)"""
    plt.imshow(maze, cmap='binary')
    
    if path:
        path = np.array(path)
        plt.plot(path[:, 1], path[:, 0], 'r-')
        
    plt.show()


maze_generator = MazeGenerator(20, 20)
maze = maze_generator.generate()

maze_solver = MazeSolver(maze)
path = maze_solver.solve()

print(maze_solver.start, maze_solver.end)
plot_maze(maze, path)
