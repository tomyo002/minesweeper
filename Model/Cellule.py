# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(contient: int) -> bool:
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    isCorrect = False
    try:
        if contient in l or contient == const.ID_MINE:
            isCorrect = True
    except TypeError:
        isCorrect = False
    return isCorrect

def construireCellule(contient: int =0, visible : bool = False) -> dict:
    if isContenuCorrect(contient) == False:
        raise ValueError(f"construireCellule : le contenu {contient} n'est pas correct")
    elif type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visible)} n'est pas un booléen")
    dico = {}
    dico[const.CONTENU] = contient
    dico[const.VISIBLE] = visible
    return  dico

def getContenuCellule(dico: dict) -> int:
    if not type_cellule(dico):
        raise TypeError(f"getContenuCellule : Le paramètre n’est pas une cellule")
    return dico[const.CONTENU]

def isVisibleCellule(dico: dict) -> bool:
    if not type_cellule(dico):
        raise TypeError(f"getContenuCellule : Le paramètre n’est pas une cellule")
    return dico[const.VISIBLE]

def setContenuCellule(dico: dict, contient: int) -> None:
    if not type_cellule(dico):
        raise TypeError(f"getContenuCellule : Le  premier paramètre n’est pas une cellule")
    elif type(contient) != int:
        raise TypeError(f" setContenuCellule : Le second paramètre n’est pas un entier.")
    elif isContenuCorrect(contient) == False:
        raise ValueError(f"setContenuCellule : la valeur du contenu {contient} n’est pas correcte")

    dico[const.CONTENU] = contient
    return None

def setVisibleCellule(dico: dict, visible: bool) -> None:
    if not type_cellule(dico):
        raise TypeError(f"getContenuCellule : Le premier paramètre n’est pas une cellule")
    elif type(visible) != bool:
        raise TypeError(f" setContenuCellule : Le second paramètre n’est pas un booléen.")

    dico[const.VISIBLE] = visible
    return None

def contientMineCellule(dico: dict) -> bool:
    if not type_cellule(dico):
        raise TypeError(f"getContenuCellule : Le paramètre n’est pas une cellule")
    isMine = False
    if dico[const.CONTENU] == const.ID_MINE:
        isMine = True
    return isMine
