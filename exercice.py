import os
import time
import copy
from dataclasses import dataclass
from pprint import pprint
from typing import ClassVar
from patterns import StillLife, Oscilliators

tableau = Oscilliators.beacon

@dataclass
class JeuDeLaVie:
    width: int
    height: int
    grid: int = None

    def __post_init__(self):
        # self.grid = [[0] * self.width for _ in range(self.height)]
        self.grid = tableau

    def run(self, nombre_tours, delai):
        """
        Méthode principale du jeu.

        Fait tourner le jeu de la vie pendant nombre_tours.
        Elle rafraichit l'affichage à chaque tour
        et attend delai entre chaque tour.

        :param nombre_tours: nombre de tours à effectuer
        :param delai: temps d'attente en secondes entre chaque tour
        """
        for _ in range(nombre_tours):
            pprint(self.grid)
            time.sleep(delai)
            os.system('cls')
            self.tour()
        pprint(self.grid)

    def tour(self):
        """
        Met à jour toute les cellules du tableau en respectant les règles
        du jeu de la vie.
        """
        new_grid = copy.deepcopy(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                valeur_case = self.valeur_case(i, j)
                total_voisins = self.total_voisins(i, j)
                new_grid[i][j] = self.resultat(valeur_case, total_voisins)
        self.grid = new_grid

    def valeur_case(self, i, j) -> int:
        """
        Renvoie la valeur de la case [i][j] ou 0 si la case n'existe pas.
        """
        if (0 <= i <= len(self.grid)-1) and (0 <= j <= len(self.grid[i])-1):
            return self.grid[i][j]
        else:
            return 0

    def total_voisins(self, i, j):
        """Renvoie la somme des valeurs des voisins de la case [i][j]."""
        total = 0
        for i_ in [i - 1, i, i + 1]:
            for j_ in [j - 1, j, j + 1]:
                total += self.valeur_case(i_, j_)
        return total - self.valeur_case(i, j)

    def resultat(self, valeur_case, total_voisins):
        """
        Renvoie la valeur suivante d'une la cellule.

        :param valeur_case: la valeur de la cellule (0 ou 1)
        :param total_voisins: la somme des valeurs des voisins
        :return: la valeur de la cellule au tour suivant

        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(0, 4)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 2)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 3)
        1
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 1)
        0
        >>> a = JeuDeLaVie([])
        >>> a.resultat(1, 4)
        0
        """
        if (valeur_case == 0 and total_voisins == 3) or (valeur_case == 1 and 2 <= total_voisins <= 3):
            return 1
        else:
            return 0


jeu = JeuDeLaVie(10, 5)
jeu.run(10, 1)
