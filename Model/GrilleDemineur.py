# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(nbLigne: int, nbCol: int) -> list:
    if type(nbLigne) != int or type(nbCol) != int:
        raise TypeError(f"construireGrilleDemineur :le nombre de lignes {type(nbLigne)} ou de colonnes {type(nbCol)} n'est pas un entier")
    elif nbLigne <= 0 or nbCol <= 0:
        raise ValueError(f"construireGrilleDemineur :Le nombre de lignes {nbLigne} ou le nombre de colonnes {nbCol} est négatif ou nul")

    lfin =[]
    for i in range(nbLigne):
        l = []
        for j in range(nbCol):
            l.append(construireCellule())
        lfin.append(l)
    return lfin


def getNbLignesGrilleDemineur(lst: list) -> int:
    if not type_grille_demineur(lst):
        raise TypeError(f"getNbLignesGrilleDemineur : le paramètre n'est pas une grille")
    return len(lst)

def getNbColonnesGrilleDemineur(lst:list) -> int:
    if not type_grille_demineur(lst):
        raise TypeError(f"getNbColonnesGrilleDemineur : le paramètre n'est pas une grille")
    return len(lst[0])

def isCoordonneeCorrecte(lst: list, coordonnee: tuple) -> bool:
    if not type_grille_demineur(lst):
        raise TypeError(f"isCoordonneeCorrecte: le paramètre n'est pas une grille")
    elif type(coordonnee) != tuple or type(lst) != list:
        raise TypeError(f"isCoordonneeCorrecte: un des paramètres n'est pas du bon type")
    isCorrecte = False
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i == coordonnee[0] and j == coordonnee[1]:
                isCorrecte = True
    return isCorrecte

def getCelluleGrilleDemineur(lst: list, coordonnee: tuple) -> dict:
    if not type_grille_demineur(lst):
        raise TypeError(f"getCelluleGrilleDemineur: le paramètre n'est pas une grille")
    elif type(coordonnee) != tuple or type(lst) != list:
        raise TypeError(f"getCelluleGrilleDemineur: un des paramètres n'est pas du bon type")
    elif not isCoordonneeCorrecte(lst, coordonnee):
        raise IndexError(f"getCelluleGrilleDemineur: coordonnée non contenue dans la grille")

    return lst[coordonnee[0]][coordonnee[1]]

