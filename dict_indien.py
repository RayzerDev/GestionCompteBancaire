#!/usr/bin/env python3
# coding: utf-8
"""
Dictionnaire des noms d'indiens :

Usage:
======
    python dict_indien.py 

__authors__ = ("Louis KARAMUCKI")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "20211008"

"""

DICT_1 = { 'A' : 'Aigle', 
           'B' : 'Buse',
           'C' : 'Chacal',
           'D' : 'Doryphore',
           'E' : 'Ecureuil',
           'F' : 'Fleuve',
           'G' : 'Grenouille',
           'H' : 'Horizon',
           'I' : 'Iris',
           'J' : 'Jaguar',
           'K' : 'Kangourou',
           'L' : 'Loutre',
           'M' : 'Mésange',
           'N' : 'Neige',
           'O' : 'Ours',
           'P' : 'Pluie',
           'Q' : 'Quetzal',
           'R' : 'Renard',
           'S' : 'Sauterelle',
           'T' : 'Tourterelle',
           'U' : 'Ululement',
           'V' : 'Vent',
           'W' : 'Weigélia',
           'X' : 'Xérus',
           'Y' : 'Yak',
           'Z' : 'Zibeline'}

DICT_2 = { 'A' : ' agile',
           'B' : ' de braise',
           'C' : ' qui chante',
           'D' : ' qui danse',
           'E' : ' qui écoute', 
           'F' : ' de feu',
           'G' : ' des glaces',
           'H' : ' humide',
           'I' : ' invincible',
           'J' : ' juvénile',
           'K' : ' kamikaze',
           'L' : ' de lumière',
           'M' : ' du matin',
           'N' : ' nocturne',
           'O' : ' de l\'ombre',
           'P' : ' paisible',
           'Q' : ' sans querelle',
           'R' : ' qui rit',
           'S' : ' du soir',
           'T' : ' taciturne',
           'U' : ' ultime',
           'V' : ' qui voit',
           'W' : ' en week-end',
           'X' : ' xylophoniste',
           'Y' : ' yoyotant',
           'Z' : ' zig-zaguant'}

L_ALPHABETS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Programme principal
if __name__=='__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    pass

def dict_prenom(n):
    """
    Renvoie le dictionnaire du prénom indien à l'indice n
    """
    if n >= 0 and n <= 25:
        return DICT_1[L_ALPHABETS[n]]
    return None

def dict_nom(n):
    """
    Renvoie le dictionnaire du nom indien à l'indice n
    """
    if n >= 0 and n <= 25:
        return DICT_2[L_ALPHABETS[n]]
    return None
