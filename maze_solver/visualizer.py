import os
import numpy as np
from typing import List, Optional, Tuple
from matplotlib import pyplot as plt


class MazeVisualizer:
    """Visualize the maze."""

    @staticmethod
    def generate_plot(maze: np.ndarray, 
                      path: Optional[List[Tuple[int, int]]] = None, 
                      start: Optional[Tuple[int, int]] = None, 
                      end: Optional[Tuple[int, int]] = None, 
                      filename: str = "maze_plot.jpg"):
        """
        Visualize the maze and the path found (if provided).

        :param maze: Numpy array representing the maze.
        :param path: List of tuples representing the path.
        :param start: Tuple representing the starting point of the path.
        :param end: Tuple representing the ending point of the path.
        :param filename: String representing the filename of the plot image.
        """
        fig, ax = plt.subplots(figsize=(maze.shape[1] / 10, maze.shape[0] / 10))

        # Set marker size relative to maze size
        marker_size = max(maze.shape) // 8

        if start:
            ax.plot(start[1], start[0], 'go', markersize=marker_size, label='Start')  # green start point

        if end:
            ax.plot(end[1], end[0], 'bo', markersize=marker_size, label='End')  # blue end point

        if path:
            path = np.array(path)
            ax.plot(path[:, 1], path[:, 0], 'r-', linewidth=2, label='Path')

        ax.imshow(maze, cmap='binary')

        # Add labels, title, and axis names
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Maze Path')
        ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

        # Save the image to the plots directory
        plots_dir = os.path.join(os.getcwd(), 'plots')
        os.makedirs(plots_dir, exist_ok=True)
        image_path = os.path.join(plots_dir, filename)
        plt.savefig(image_path, bbox_inches='tight')
        plt.close()

    @staticmethod
    def display_plot(maze: np.ndarray, 
                     path: Optional[List[Tuple[int, int]]] = None, 
                     start: Optional[Tuple[int, int]] = None, 
                     end: Optional[Tuple[int, int]] = None):
        """
        Display the maze and the path found (if provided) in an interactive plot.

        :param maze: Numpy array representing the maze.
        :param path: List of tuples representing the path.
        :param start: Tuple representing the starting point of the path.
        :param end: Tuple representing the ending point of the path.
        """
        plt.imshow(maze, cmap='binary')
        
        # Set marker size relative to maze size
        marker_size = max(maze.shape) // 20

        if start:
            plt.plot(start[1], start[0], 'go', markersize=marker_size, label='Start')  # green start point

        if end:
            plt.plot(end[1], end[0], 'bo', markersize=marker_size, label='End')  # blue end point

        if path:
            path = np.array(path)
            plt.plot(path[:, 1], path[:, 0], 'r-', linewidth=2, label='Path')

        # Add labels, title, and axis names
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Maze Path')
        plt.legend(loc='upper right')

        # Display the plot
        plt.show()
