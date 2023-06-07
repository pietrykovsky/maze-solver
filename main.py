import random

from maze_solver.generation import MazeGenerator
from maze_solver.solver import MazeSolver
from maze_solver.visualizer import MazeVisualizer


def generate_plots(plots_number: int = 5):
    for i in range(1, plots_number+1):
        maze_generator = MazeGenerator(random.randint(5, 40), random.randint(5, 40))
        maze = maze_generator.generate()

        maze_solver = MazeSolver(maze)
        path = maze_solver.solve()

        print(maze_solver.position_handler.start, maze_solver.position_handler.end)

        MazeVisualizer.generate_plot(maze, path, maze_solver.position_handler.start, maze_solver.position_handler.end, f'plot_{i}.jpg')


if __name__ == '__main__':
    generate_plots()
