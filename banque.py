#!/usr/bin/env python3
# coding: utf-8
"""
Usage: Application bancaire
======
    python baque.py 

__authors__ = ("Louis KARAMUCKI")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "02/10/2021"

"""


# Modules externes
from random import randint
from dict_indien import *
import datetime

# Déclaration Variables

# Classe
class CompteBancaire():
    """
    """
    L_CLIENTS = []
    L_CLIENTS_INACTIFS = []
    
    def __init__(self, prenom, nom, solde = 0):
        """
        """
        self.prenom = prenom
        self.nom = nom
        self.solde = solde
        self.l_historique_operations = []
        self.date_creation = date_time()
        self.statut = True
        self.l_historique_operations.append({
                'Type':'Création du compte',
                'Date':self.date_creation,
                'Montant':'Null',
                'Ancien Solde':'Null',
                'Nouveau Solde': str(self.solde)+'€'
                })
        
    def decouvert(self):
        """
        Si le compte est à découvert, renvoie True, sinon False.
        """
        if self.solde < 0:
            return True
        else:
            return False
        
    def set_solde(self, new_solde):
        """
        """
        self.solde = new_solde
        
    def get_solde(self):
        """
        """
        return self.solde
    
    def get_solde_str(self):
        """
        """
        return str(self.solde) + '€'
       
    def historique_ope(self, l_temp):
        """
        Ajoute dans la liste des opérations, un dictionnaire avec une nouvelle opération.
        """
        self.l_historique_operations.append({
            'Type':l_temp[0],
            'Date':date_time(),
            'Montant':str(l_temp[1])+ '€',
            'Ancien Solde':str(l_temp[2])+'€',
            'Nouveau Solde':str(l_temp[3])+'€'
            })
    
    def retrait(self, montant):
        """
        Retires le montant en paramètre sauf si le solde est inférieur à 200.
        L'opération est sauvegardé dans la liste de l'historique des opérations.
        """
        new_solde = self.solde - montant
        if new_solde < 200:
            return False
        else:
            self.historique_ope(['Retrait', montant, self.solde, new_solde])
            self.solde = new_solde
            return True
    
    def depot(self, montant):
        """
        Permets le dépôt du montant en paramètre.
        L'opération est sauvegardé dans la liste de l'historique des opérations.
        """
        new_solde = self.solde + montant
        self.historique_ope(['Dépôt', montant, self.solde, new_solde])
        self.solde = new_solde
        return True
         
    def actif_inactif(self):
        """
        """
        if self.statut:
            self.statut = False
            self.l_historique_operations.append({
                'Type':'Changement de statut',
                'Date':date_time(),
                'Montant':'Null',
                'Ancien Solde':'Null',
                'Nouveau Solde':self.get_statut_str()
            })
        else:
            self.statut = True
            self.l_historique_operations.append({
                'Type':'Changement de statut',
                'Date':date_time(),
                'Montant':'Null',
                'Ancien Solde':'Null',
                'Nouveau Solde':self.get_statut_str()
            })
        
        return True
    
    def envoie_argent(self, receveur, montant):
        self.solde -= montant
        receveur.solde += montant
        donneur_ancien_solde = self.solde + montant
        receveur_ancien_solde = self.solde - montant
        
        self.historique_ope(['Echange argent', montant, str(donneur_ancien_solde), str(self.solde)])
        receveur.historique_ope(['Echange argent', montant, str(receveur_ancien_solde), str(receveur.solde)])
        
        return True
    
    def get_statut(self):
        """
        """
        if self.statut:
            return True
        else:
            return False
        
    def get_statut_str(self):
        """
        """
        if self.statut:
            return 'Actif'
        else:
            return 'Inactif'
        
    def __del__(self):
        """
        """
        if self in CompteBancaire.L_CLIENTS:
            CompteBancaire.L_CLIENTS.remove(self)
        if self in CompteBancaire.L_CLIENTS_INACTIFS:
            CompteBancaire.L_CLIENTS_INACTIFS.remove(self)
    
# Fin de la Classe        

def get_nombre_actif_inactif():
    """
    
    :return (tuple): [0] → nombre_actif, [1] → nombre_inactif
    """
    nombre_actif = 0
    for i in CompteBancaire.L_CLIENTS:
        if i.statut:
            nombre_actif += 1
    return nombre_actif, len(CompteBancaire.L_CLIENTS)-nombre_actif

def date_time():
    """
    Fonction qui renvoie la date et l'heure au moment de l'appel de la fonction.
    :return (str): Renvoie une chaîne de caractère sous forme 'J/M/A à H:M:S'
    """
    return datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")

def date_str_int(date):
    """
    Retourne la date de la fonction date_time() sous forme d'entier pour pouvoir manipuler les valeurs
    :return (tuple): Renvoie un de deux listes, la date et l'heure
    """
    return ([int(date[0:2]), int(date[3:5]), int(date[6:8])], [int(date[11:13]), int(date[14:16]), int(date[18:19])])

def creation_compte(n, l_client):
    """
    Fonction qui permet de créer n comptes avec une somme au hasard compris entre
    1000€ et 20 000€ et des noms au hasard depuis la liste de prénom/nom indien, dans la liste mis en paramètre.
    :param (int): n, nombre de compte à créer.
    :param (list): l_client, liste des clients.
    :return (list): l_client; la liste des clients en paramètre
    :Effet de bord: Modifie la lsite mis en paramètre
    :CU: Pour garder la liste en mémoire, mettre une liste déjà déclaré au préalable.
    """
    for i in range(0,n):
        l_client.append(CompteBancaire(dict_prenom(randint(0, 25)), dict_nom(randint(0,25)), randint(1000,20000)))
    return l_client

def affichage_operations(liste, l_tab):
    """
    Retourne une chaine formatée permettant l'affichage en colonne des données de la liste
    :param (list of dict): données à afficher
    :param (int): nombre de caractères par colonne
    :return (list): liste de d'information avec le nombre d'espace et de retour chariot adaptés à l'affichage
    :Cu:
    :Effet de bord (None):     
    
    """
    l_elements = []
    ch = ''
    f = ''.join([' '] * l_tab)
    for i in liste[0].keys():
        ch += (str(i) + f)[0:l_tab]
    ch += '\n'
    l_elements.append(ch)
    
    for enregistrement in liste:
        ch = ''
        for a in enregistrement.items():
            ch += (str(a[1]) + f)[0:l_tab]
        ch += '\n'
        l_elements.append(ch)
    return l_elements

def liste_information_bancaire(compte):
    """
    
    """
    return [compte.get_statut_str(), compte.prenom, compte.nom, compte.get_solde_str(), compte.date_creation]