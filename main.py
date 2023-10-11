# from dataclasses import dataclass
# from typing import ClassVar
from patterns import StillLife, Oscilliators, Spaceships, Guns, random_grid
from random import choice
import pyxel
import copy


class GameOfLife:
    grid = Guns.simkin_glider

    def __init__(self, title="Conway's Game of Life", cell_size=5, fps=2) -> None:
        self.title = title
        self.cell_size = cell_size
        self.fps = fps
        self.height = len(self.grid) * cell_size
        self.width = len(self.grid[0]) * cell_size
        self.colors = {"bg": 0, "cells": 7, "grid": 11}

    def get_cell(self, j, i):
        if (0 <= j <= len(self.grid) - 1) and (0 <= i <= len(self.grid[j]) - 1):
            return self.grid[j][i]
        else:
            return 0

    def get_new_cell(self, j, i):
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

    def update_cells(self):
        new_grid = copy.deepcopy(self.grid)
        for j in range(len(new_grid)):
            for i in range(len(new_grid[j])):
                new_grid[j][i] = self.get_new_cell(j, i)
        self.grid = new_grid

    def generate_random_colors(self):
        colors_list = list(range(16))
        for color in self.colors.keys():
            self.colors[color] = choice(colors_list)
            colors_list.remove(self.colors[color])

    def update(self):
        self.update_cells()

    def draw(self):
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                color = (
                    self.colors["cells"] if self.grid[j][i] == 0 else self.colors["bg"]
                )
                pyxel.rect(
                    i * self.cell_size,
                    j * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                    color,
                )
        for a in range(0, self.width, self.cell_size):
            pyxel.rect(
                a,
                0,
                1,
                self.height,
                self.colors["grid"],
            )
        for b in range(0, self.height, self.cell_size):
            pyxel.rect(
                0,
                b,
                self.height,
                1,
                self.colors["grid"],
            )

    def play(self):
        pyxel.init(width=self.width, height=self.height, title=self.title, fps=self.fps)
        pyxel.run(self.update, self.draw)


if __name__ == "__main__":
    game_of_life = GameOfLife(cell_size=20, fps=30)
    game_of_life.generate_random_colors()
    game_of_life.play()
