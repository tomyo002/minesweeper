# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse
from random import randrange

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


def getContenuGrilleDemineur(grille: list, coordonnee: tuple) -> int:
    return getContenuCellule(getCelluleGrilleDemineur(grille, coordonnee))

def setContenuGrilleDemineur(grille: list, coordonnee: tuple, contient: int) -> None:
    setContenuCellule(getCelluleGrilleDemineur(grille, coordonnee), contient)
    return  None

def isVisibleGrilleDemineur(grille: list, coordonnee: tuple) -> bool:
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coordonnee))

def setVisibleGrilleDemineur(grille: list, coordonnee: tuple, visible: tuple) -> None:
    setVisibleCellule(getCelluleGrilleDemineur(grille, coordonnee), visible)
    return None

def contientMineGrilleDemineur(grille: list, coordonnee:tuple) -> bool:
    return contientMineCellule(getCelluleGrilleDemineur(grille, coordonnee))


def getCoordonneeVoisinsGrilleDemineur(grille: list, coordonnee : tuple) -> list:
    if type(coordonnee) != tuple or type(grille) != list:
        raise TypeError(f"getCoordonneeVoisinsGrilleDemineur: un des paramètres n'est pas du bon type")
    elif not isCoordonneeCorrecte(grille, coordonnee):
        raise IndexError(f"getCoordonneeVoisinsGrilleDemineur: coordonnée n'est pas dans la grille")
    lVoisin = []
    for i in range(coordonnee[0]-1,  coordonnee[0]+2):
        for j in range(coordonnee[1]-1,  coordonnee[1]+2):
            val = (i, j)
            if i >= 0 and j >= 0 and val != coordonnee:
                if isCoordonneeCorrecte(grille, val):
                        lVoisin.append(val)

    return lVoisin


def placerMinesGrilleDemineur(grille: list, nb: int, coordonnee: tuple) -> None:
    if nb < 0 or nb > len(grille) * len(grille[0]):
        raise ValueError(f"placerMinesGrilleDemineur: nombre de bombes à placer incorrect")
    elif not isCoordonneeCorrecte(grille, coordonnee):
        raise IndexError(f"placerMinesGrilleDemineur: la coordonnée n'est pas dans la fonctions précédentes")

    lPossible = []
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if (i, j) != coordonnee:
                lPossible.append((i, j))

    while nb > 0:
        coorMine = randrange(len(lPossible))
        setContenuGrilleDemineur(grille, lPossible[coorMine], const.ID_MINE)
        del lPossible[coorMine]
        nb -= 1

    return None

def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    l=[]
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if getContenuGrilleDemineur(grille, (i,j)) == const.ID_MINE:
                l += (getCoordonneeVoisinsGrilleDemineur(grille, (i,j)))
    for i in l:
        val = 0
        for j in l:
            if i == j:
                val += 1
        setContenuGrilleDemineur(grille, i, val)
    return None

