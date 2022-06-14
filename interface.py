#!/usr/bin/env python3
# coding: utf-8
"""
Usage: Application bancaire
======
    python interface.py 

__authors__ = ("Louis KARAMUCKI")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "02/10/2021"

"""

# Modules externes
from tkinter import *
from tkinter.messagebox import *
from banque import *

# Déclaration Class
class Fenetre(Tk):
    """
    """
    # Variables de Classe
    ICO_LOGO_BANQUE = 'image/logo_banque.ico'
    LOGO_BANQUE = 'image/logo_banque.png'
    
    def __init__(self, titre, dim = (1280,720), bg_gris = '#E8E8E8'):
        """
        :param (str): titre, Titre de la fenêtre
        :param (tuple): dim, Tuple avec les dimensions x et y
        """
        # Initialisation des variables
        self.dim = dim
        self.titre = titre
        self.bg_gris = bg_gris
        
        Tk.__init__(self)
        self.title(self.titre)
        dimension_fenetre = "%dx%d" % (self.dim[0], self.dim[1])
        self.geometry(dimension_fenetre)
        self['bg'] = self.bg_gris
        # Icone fenêtre
        self.iconbitmap(Fenetre.ICO_LOGO_BANQUE)
        # Logo BG
        self.logo_back = PhotoImage(file=Fenetre.LOGO_BANQUE)
        self.x_logo = self.logo_back.width()
        self.y_logo = self.logo_back.height()
        self.can_back = Canvas(self, width= self.x_logo, height= self.y_logo, bg = self.bg_gris, highlightthickness=0)
        self.can_back.place(x = self.dim[0] / 2 - self.x_logo / 2, y = self.dim[1] / 2 - self.y_logo / 2)
        self.can_back.create_image(self.x_logo/2, self.y_logo/2, image = self.logo_back)
    
    def close(self):
        self.destroy()
        
class Selection():
    """
    """
    # Variables de Classe
    L_CLIENTS_ACTU = []
    L_INFO_CLE = ['Statut: ', 'Prénom: ', 'Nom: ', 'Solde: ', 'Date création du compte: ', 'Historique des opérations: ']
    L_NOM_BOUTON = ['Dépôt', 'Retrait', "Envoie argent", 'Suppression du compte', 'Rendre inactif / actif le compte']

    def __init__(self, fenetre, pos_x, pos_y, bg_gris, l_info_client, compte_client):
        """
        :param (obj): fenetre, fenêtre concerné par le text
        :param (int): pos_x, coordonnée en x pour le placement du texte
        :param (int): pos_y, coordonnée en y pour le placement du texte
        :param (list): l_info_client, 0(str): prénom, 1(str): nom, 2(str): solde, 3(str): date/heure création de compte, 4(list): historique_opérations
        """
            
        self.fenetre = fenetre
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.l_info_client = l_info_client
        self.compte_client = compte_client
        self.bg_gris = bg_gris
        self.l_info_graph = []
        self.l_bouton = []
                    
        # Popup Découvert    
        if self.compte_client.decouvert() == True:
            showerror('Nous ne faisons pas crédit !', 'Veuillez alimenter ce compte au plus vite !\n Ce compte est en dessous du seuil permis.')
        
        # Frame du compte
        self.frame_compte = Frame(self.fenetre, borderwidth = 5, width = 450, height = 350)
        self.frame_compte.place(x= self.pos_x - 5 , y= self.pos_y - 60)
        
        # Statut du compte
        if not self.compte_client.get_statut():
            self.text_inactif = Label(self.frame_compte, text =  "Compte Inactif", font = ("Helvetica", 15), bg = self.bg_gris)
            self.text_inactif.place(x = self.pos_x + 20 , y = self.pos_y + 34 * 4)
            
        # Informations de comptes
        for i in range(len(self.l_info_client)):
            self.l_info_graph.append(Label(self.frame_compte, text = Selection.L_INFO_CLE[i] + self.l_info_client[i] , font = ("Helvetica", 15), bg = bg_gris))
            self.l_info_graph[i].place(x = self.pos_x - 10, y = self.pos_y-150 + i*34)
        
        # Historique opérations    
        self.frame_historique = Frame(self.fenetre, borderwidth = 5, relief  = 'ridge', bg = self.bg_gris, width = 600, height = 600)
        self.frame_historique.place(x=self.pos_x * 30 ,y= self.pos_y - 60)
        self.l_texte_operations = []
        self.l_historique = affichage_operations(self.compte_client.l_historique_operations, 25)
        
        for i in self.l_historique:
            self.l_texte_operations.append(Label(self.frame_historique, text = i, font = ("Helvetica", 9), bg = self.bg_gris).pack())
    
    def __del__(self):
        """
        """
        try:
            self.frame_historique.destroy()
            self.frame_compte.destroy()
            
        except:
            return None
        
class SousFenetre(Tk):
    """
    """
    # Variables de Classe
    ICO_LOGO_BANQUE = 'image/logo_banque.ico'
    LOGO_BANQUE = 'image/logo_banque.png'
    L_SS_FENETRE = []
    
    def __init__(self, titre, dim = (720,500)):
        """
        :param (str): titre, Titre de la fenêtre
        :param (tuple): dim, Tuple avec les dimensions x et y
        """
        # Initialisation des variables
        self.titre = titre
        self.dim = dim
        self.bg_gris = '#E8E8E8'
        
        self.fenetre = Toplevel()        
        self.fenetre.title(self.titre)
        dimension_fenetre = "%dx%d" % (self.dim[0], self.dim[1])
        self.fenetre.geometry(dimension_fenetre)
        self.fenetre['bg'] = self.bg_gris
        # Icone fenêtre
        self.fenetre.iconbitmap(SousFenetre.ICO_LOGO_BANQUE)
        # Logo BG
        self.logo_back = PhotoImage(file=SousFenetre.LOGO_BANQUE)
        self.x_logo = self.logo_back.width()
        self.y_logo = self.logo_back.height()
        self.can_back = Canvas(self.fenetre, width= self.x_logo, height= self.y_logo, bg = self.bg_gris, highlightthickness=0)
        self.can_back.place(x = self.dim[0] / 2 - self.x_logo / 2, y = self.dim[1] / 2 - self.y_logo / 2)
        self.can_back.create_image(self.x_logo/2, self.y_logo/2, image = self.logo_back)