import random
import numpy as np
from typing import Optional, Tuple


class MazePositionHandler:
    """Handle maze position related operations."""

    def __init__(self, maze: np.ndarray, start: Optional[Tuple[int, int]] = None,
                 end: Optional[Tuple[int, int]] = None):
        self.maze = maze
        self.start = start
        self.end = end
        self._generate_random_positions()

    def _generate_random_positions(self):
        """Generate random start and end positions."""
        free_cells = np.argwhere(self.maze == 0)
        if not self.start:
            self.start = tuple(free_cells[random.randint(0, len(free_cells) - 1)])
        if not self.end:
            self.end = tuple(free_cells[random.randint(0, len(free_cells) - 1)])
