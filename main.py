from patterns import StillLife, Oscilliators, Spaceships, Guns, random_grid
from dataclasses import dataclass
from typing import ClassVar
from random import choice
import pyxel
import copy


@dataclass
class GameOfLife:
    grid: ClassVar[int] = Guns.simkin_glider

    title: str = "Conway's Game of Life"
    cell_size: int = 5
    fps: int = 15

    def __post_init__(self) -> None:
        self.height = len(self.grid) * self.cell_size
        self.width = len(self.grid[0]) * self.cell_size
        self.colors = {"bg": 7, "cells": 0, "grid": 11}

    def get_cell(self, j:int, i:int) -> int:
        """Returns the value (0 or 1) of a specified cell.

        Args:
            j (int): Indice of the list (row)
            i (int): Indice of the element in the list (line)

        Returns:
            int: value of the cell (or 0 if it doesn't exists)
        """
        if (0 <= j <= len(self.grid) - 1) and (0 <= i <= len(self.grid[j]) - 1):
            return self.grid[j][i]
        return 0

    def get_new_cell(self, j:int, i:int) -> int:
        """Returns the next value (0 or 1) of a specified cell :
            - check the total value of the cells' neighbours
            - returns the correct value according to the rules of the Game Of Life

        Args:
            j (int): Indice of the list (row)
            i (int): Indice of the element in the list (line)

        Returns:
            int: next value of the cell
        """
        neigh = 0
        for j_ in [j - 1, j, j + 1]:
            for i_ in [i - 1, i, i + 1]:
                neigh += self.get_cell(j_, i_)
        cell = self.get_cell(j, i)
        neigh -= cell
        if cell == 0 and neigh == 3:
            return 1
        elif cell == 1 and (2 <= neigh <= 3):
            return 1
        else:
            return 0

    def update_grid(self) -> None:
        """Updates the values of the grid"""
        new_grid = copy.deepcopy(self.grid)
        for j in range(len(new_grid)):
            for i in range(len(new_grid[j])):
                new_grid[j][i] = self.get_new_cell(j, i)
        self.grid = new_grid

    def generate_random_colors(self) -> None:
        """Generate a random set of colors for the background, the lines and the cells"""
        colors_list = list(range(16))
        for color in self.colors.keys():
            self.colors[color] = choice(colors_list)
            colors_list.remove(self.colors[color])

    def update(self):
        self.update_grid()

    def draw(self):
        # Draws cells
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                color = (
                    self.colors["bg"] if self.grid[j][i] == 0 else self.colors["cells"]
                )
                pyxel.rect(
                    i * self.cell_size,
                    j * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    color,
                )
        # Draws horizontal lines
        for a in range(0, self.width, self.cell_size):
            pyxel.rect(
                a,
                0,
                1,
                self.width,
                self.colors["grid"]
            )
        # Draws vertical lines
        for b in range(0, self.height, self.cell_size):
            pyxel.rect(
                0,
                b,
                self.height,
                1,
                self.colors["grid"],
            )

    def run_UI(self):
        pyxel.init(width=self.width, height=self.height, title=self.title, fps=self.fps)
        pyxel.run(self.update, self.draw)


if __name__ == "__main__":
    game_of_life = GameOfLife(cell_size=20, fps=15)
    # game_of_life.generate_random_colors()
    game_of_life.run_UI()
