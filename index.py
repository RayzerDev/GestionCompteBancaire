#!/usr/bin/env python3
# coding: utf-8
"""
Usage: Application bancaire
======
    python index.py 

__authors__ = ("Louis KARAMUCKI")
__version__ = "1.0.0"
__copyright__ = "copyleft"
__date__ = "02/10/2021"

"""

# Importation des fichiers banque et interface
from banque import *
from interface import *
from tkinter.messagebox import *

# Déclaration Variables
creation_compte(20, CompteBancaire.L_CLIENTS)

# Creation Fenetre
def creation_fen_accueil(fenetre_close = None):
    """
    Fonction qui créé une fenêtre d'accueil grâce à la class Fenetre.
    Possibilité d'accéder à:
        - La création de compte
        - La gestion des comptes
    
    """
    if fenetre_close != None:
        fenetre_close.close()
        
    bouton_accueil = []
    fen_accueil = Fenetre('Accueil')
    message_accueil = Label(fen_accueil, text = "Vous êtes dans l'accueil, appuyez sur un bouton pour vous rendre à l'endroit souhaité.", font = ("Helvetica", 20), bg = fen_accueil.bg_gris)
    message_accueil.pack()
    
    bouton_creation_compte = Button(fen_accueil, text = 'Ouvrir un Compte Bancaire', command = lambda: creation_fen_creation_compte(fen_accueil))
    bouton_creation_compte.pack()
    
    bouton_compte = Button(fen_accueil, text = 'Comptes Existants', command = lambda: creation_fen_compte(fen_accueil))
    bouton_compte.pack()
    
    fen_accueil.mainloop()

def creation_fen_creation_compte(fenetre_close):
    """
    Fonction qui permet la création d'une fenêtre pour créer un compte bancaire.
    2 choix sont possibles: Soit créer son compte avec la saisie des données, soit la création de compte avec les noms indiens et le solde aléatoire.
    """
    fenetre_close.close()
    fen_creation_compte = Fenetre('Ouverture de compte')
    
    # Texte
    message_creation_compte = Label(fen_creation_compte, text = "Vous êtes dans l'onglet création de compte.", font = ("Helvetica", 15), bg = fen_creation_compte.bg_gris)
    message_creation_compte.pack()
    
    # Bouton Accueil
    bouton_creation_compte_accueil = Button(fen_creation_compte, text = 'Accueil', command = lambda: creation_fen_accueil(fen_creation_compte))
    bouton_creation_compte_accueil.place(x = 5, y = 5)
    
    # Création de Compte à saisies
        # Zone de saisie
            # Liste des saisies
    l_saisie_creation = [[],[],[]]
    l_element_saisie = ['Prénom', 'Nom', 'Solde']
            # Boucle création des zones 
    for i in range(len(l_saisie_creation)):
        l_saisie_creation[i] = [Label(fen_creation_compte, text = l_element_saisie[i], font = ("Helvetica", 12), bg = fen_creation_compte.bg_gris), Entry(fen_creation_compte, width = 35, bg = fen_creation_compte.bg_gris)]
        l_saisie_creation[i][0].place(x = fen_creation_compte.dim[0]/2-270, y = fen_creation_compte.dim[0]/6-4 + 40*i)
        l_saisie_creation[i][1].place(x = fen_creation_compte.dim[0]/2-500, y = fen_creation_compte.dim[0]/6 + 40*i)
        
            # Bouton création
            # Fonction création
    def creation_compte_saisie():
        prenom = l_saisie_creation[0][1].get()
        nom = l_saisie_creation[1][1].get()
        solde = l_saisie_creation[2][1].get()
        if prenom == '' or nom == '': return showwarning('Saisie Incorect','Vous devez saisir un prénom et/ou un nom\nVeuillez recommencer !')
        try:
            solde = int(solde)
            nouveau_compte = CompteBancaire(prenom, nom, solde)
            
        except ValueError:
            nouveau_compte = CompteBancaire(prenom, nom)
            
        CompteBancaire.L_CLIENTS.append(nouveau_compte)
        return showinfo(title = "Bienvenue chez nous !", message = "Vous venez de créer un nouveau compte à {} {} avec un solde de {}€ !".format(prenom, nom, nouveau_compte.get_solde()))
            # Placement du bouton
    bouton_validation = Button(fen_creation_compte, text = "Créer un compte", bg = fen_creation_compte.bg_gris, command = creation_compte_saisie)
    bouton_validation.place(x = fen_creation_compte.dim[0]/2-450, y = fen_creation_compte.dim[0]/3-100)
    
    # Création de comptes aléatoires
    texte_titre = Label(fen_creation_compte, text = 'Création de compte aléatoires\n Choisissez le nombre de compte que vous voulez créer', font = ("Helvetica", 12), bg = fen_creation_compte.bg_gris)
    texte_titre.place(x = fen_creation_compte.dim[0]/2+180, y = fen_creation_compte.dim[0]/6)
    
    saisie_nombre = Entry(fen_creation_compte, width = 10, bg = fen_creation_compte.bg_gris)
    saisie_nombre.place(x = fen_creation_compte.dim[0]/2+335, y = fen_creation_compte.dim[0]/6 + 60)
        # Fonction bouton
    def creation_compte_alea():
        nombre_de_compte = saisie_nombre.get()
        try:
            nombre_de_compte = int(nombre_de_compte)
            creation_compte(nombre_de_compte, CompteBancaire.L_CLIENTS)
        except ValueError:
            return showwarning('Saisie Incorect','Vous devez saisir un nombre.\n Veuillez recommencer !')
        return showinfo(title = "Création effectué avec succès !", message = "Vous venez de créer {} comptes !".format(nombre_de_compte))
    
        # Placement du bouton
    bouton_validation_alea = Button(fen_creation_compte, text = "Création compte aléatoire", bg = fen_creation_compte.bg_gris, command = creation_compte_alea)
    bouton_validation_alea.place(x = fen_creation_compte.dim[0]/2+295, y = fen_creation_compte.dim[0]/6+100)

    fen_creation_compte.mainloop()
    
def creation_fen_compte(fenetre_close):
    """
    Création de la fenêtre où nous pouvons accéder à la liste des comptes actifs avec leurs informations
    Possibilité de supprimer ce compte, dépot et retrait d'argent, échange entre compte, voir l'historique des opérations.
    """
    fenetre_close.close()
    fen_compte = Fenetre('Compte Existant')
    
    # Texte
    texte_compte = Label(fen_compte, text = "Vous êtes dans l'onglet des gestions des comptes existants.\n Appuyez sur le le bouton 'Rechercher un compte' pour retrouver un compte par son nom, prénom.", font = ("Helvetica", 15), bg = fen_compte.bg_gris)
    texte_compte.pack()
    texte_nombre_actif_inactif = Label(fen_compte, text = str(get_nombre_actif_inactif()[0]) + " comptes actifs et " + str(get_nombre_actif_inactif()[1]) + " comptes inactifs", font = ("Helvetica", 12), bg = fen_compte.bg_gris)
    texte_nombre_actif_inactif.pack()
    
    # Bouton Accueil
    bouton_compte_accueil = Button(fen_compte, text = 'Accueil', command = lambda: creation_fen_accueil(fen_compte))
    bouton_compte_accueil.place(x = 5, y = 5)
    
    # Contenu Box
    l_compte_check = []
    for i in CompteBancaire.L_CLIENTS:
        l_compte_check.append(i.prenom + '   ' + i.nom)  
    l_contenu_box_compte = StringVar(value = l_compte_check)
    
    # Box compte
    box_compte = Listbox(fen_compte,font = ("Helvetica", 10), bg = fen_compte.bg_gris, width = 30, justify = CENTER, listvar = l_contenu_box_compte )
    box_compte.place(x = 60, y = fen_compte.dim[1]/1.4)

    # Event Selection
    def select(event):
        selection = box_compte.curselection()[0]
        for i in CompteBancaire.L_CLIENTS:
            if i.prenom + '   ' + i.nom == box_compte.get(selection):
                client_selection = i
        return information_compte_selection(fen_compte, 20, 160, fen_compte.bg_gris, liste_information_bancaire(client_selection), client_selection)
    box_compte.bind('<<ListboxSelect>>', select)
        
    # Recherche compte par prenom nom
    # Zone de saisie
    zone_recherche = Entry(fen_compte, width = 35, bg = fen_compte.bg_gris, text = "Rechercher par le prénom/nom un compte existants")
    zone_recherche.place(x = 60, y = fen_compte.dim[1]/1.4-30)
    # Fonction Recherche
    def recherche_compte(evt = None):
        l_compte_recherche = []
        recherche = zone_recherche.get()
        for i in CompteBancaire.L_CLIENTS:
            if recherche.lower() == i.prenom.lower()[0:len(recherche)]:
                l_compte_recherche.append(i.prenom + '   ' + i.nom)
            elif recherche.lower() == i.nom.lower()[1:len(recherche)+1]:
                l_compte_recherche.append(i.prenom + '   ' + i.nom)
        l_contenu_box_compte.set(l_compte_recherche)
    # Bind touche Enter
    zone_recherche.bind('<Return>', recherche_compte)
    # Bouton Recherche
    loupe_recherche = PhotoImage(file = "image/loupe.png")
    bouton_recherche = Button(fen_compte, image = loupe_recherche, bg = fen_compte.bg_gris, command = recherche_compte)
    bouton_recherche.place(x = 30, y = fen_compte.dim[1]/1.4-30)
    
    # Fin de la fenêtre
    fen_compte.mainloop()
    
def information_compte_selection(fenetre, pos_x, pos_y, bg_gris, l_info_client, compte_client):
    """
    """
    if Selection.L_CLIENTS_ACTU:
        del(Selection.L_CLIENTS_ACTU[0])
    class_selection = Selection(fenetre, pos_x, pos_y, bg_gris, l_info_client, compte_client)
    Selection.L_CLIENTS_ACTU.append(class_selection)
    
    # Création des boutons de fonctions de compte  
    # Bouton dépôt
    bouton_depot = Button(class_selection.frame_compte, text = "Dépôt", bg = class_selection.bg_gris, command = lambda: sous_fenetre_depot(compte_client, fenetre))
    bouton_depot.place(x = class_selection.pos_x- 10, y = class_selection.pos_y + 20)
    
    # Bouton Retrait
    bouton_retrait = Button(class_selection.frame_compte, text = "Retrait" ,  bg = class_selection.bg_gris, command = lambda: sous_fenetre_retrait(compte_client, fenetre))
    bouton_retrait.place(x = class_selection.pos_x - 10, y = class_selection.pos_y + 20 +30 * 1)
    
#    # Bouton Envoie d'argent
#    bouton_echange_argent = Button(class_selection.frame_compte, text = "Envoie d'argent",  bg = class_selection.bg_gris)
#    bouton_echange_argent.place(x = class_selection.pos_x - 10, y = class_selection.pos_y + 20 + 30 * 2)
#    
#    # Bouton Suppression du compte
#    bouton_suppression = Button(class_selection.frame_compte, text = "Suppression du compte" , bg = class_selection.bg_gris, command = lambda: suppresion_compte(compte_client, fenetre))
#    bouton_suppression.place(x = class_selection.pos_x - 10, y = class_selection.pos_y + 20 + 30 * 3)
    
    # Bouton Rendre inactif / actif le compte
    bouton_changement_statut = Button(class_selection.frame_compte, text = "Rendre inactif / actif le compte", bg = class_selection.bg_gris, command = lambda: changement_statut_compte(compte_client, fenetre))
    bouton_changement_statut.place(x = class_selection.pos_x - 10, y = class_selection.pos_y + 20 + 30 * 2)
    
def sous_fenetre_depot(compte_client, fenetre_principale):
    """
    """
    class_fenetre_depot = SousFenetre('Dépôt')
    fenetre = class_fenetre_depot.fenetre
    
    # Entête
    texte_titre = Label(fenetre, text = 'Entrez dans la zone de saisie le montant que vous voulez déposer \n Appuyez sur "Déposer" pour valider.', font = ("Helvetica", 14), bg = class_fenetre_depot.bg_gris)
    texte_titre.pack()
    
    # Zone de saisie
    saisie_montant = Entry(fenetre, width = 15, bg = class_fenetre_depot.bg_gris)
    saisie_montant.place(x = class_fenetre_depot.dim[0]/5, y = class_fenetre_depot.dim[1]/4 + 60)
    # Texte montant
    texte_montant = Label(fenetre, text = 'Montant', font = ("Helvetica", 10), bg = class_fenetre_depot.bg_gris)
    texte_montant.place(x = class_fenetre_depot.dim[0]/5 - 60, y = class_fenetre_depot.dim[1]/4 + 58)
    # Fonction bouton
    def depot_saisie():
        montant = saisie_montant.get()
        try:
            montant = int(montant)
            compte_client.depot(montant)
            information_compte_selection(fenetre_principale, 20, 160, fenetre_principale.bg_gris, liste_information_bancaire(compte_client), compte_client)
        except ValueError:
            return showwarning('Saisie Incorect','Vous devez saisir un nombre.\n Veuillez recommencer !')
        return showinfo(title = "Dépôt effectué avec succès !", message = "Vous venez de déposer {}€ ! \n Votre solde est de maintenant {}€.".format(montant, compte_client.get_solde()))
    
    # Placement du bouton
    bouton_validation_depot = Button(fenetre, text = "Déposer", bg = class_fenetre_depot.bg_gris, command = depot_saisie)
    bouton_validation_depot.place(x = class_fenetre_depot.dim[0]/5, y = class_fenetre_depot.dim[1]/4+100)
    fenetre.mainloop()
    
def sous_fenetre_retrait(compte_client, fenetre_principale):
    """
    """
    class_fenetre_retrait = SousFenetre('Retrait')
    fenetre = class_fenetre_retrait.fenetre
    
    # Entête
    texte_titre = Label(fenetre, text = 'Entrez dans la zone de saisie le montant que vous voulez retirer \n Appuyez sur "Retirer" pour valider.', font = ("Helvetica", 14), bg = class_fenetre_retrait.bg_gris)
    texte_titre.pack()
    
    # Zone de saisie
    saisie_montant = Entry(fenetre, width = 15, bg = class_fenetre_retrait.bg_gris)
    saisie_montant.place(x = class_fenetre_retrait.dim[0]/5, y = class_fenetre_retrait.dim[1]/4 + 60)
    # Texte montant
    texte_montant = Label(fenetre, text = 'Montant', font = ("Helvetica", 10), bg = class_fenetre_retrait.bg_gris)
    texte_montant.place(x = class_fenetre_retrait.dim[0]/5 - 60, y = class_fenetre_retrait.dim[1]/4 + 58)
    # Fonction bouton
    def retrait_saisie():
        montant = saisie_montant.get()
        try:
            montant = int(montant)
            compte_client.retrait(montant)
            information_compte_selection(fenetre_principale, 20, 160, fenetre_principale.bg_gris, liste_information_bancaire(compte_client), compte_client)
        except ValueError:
            return showwarning('Saisie Incorect','Vous devez saisir un nombre.\n Veuillez recommencer !')
        return showinfo(title = "Dépôt effectué avec succès !", message = "Vous venez de retirer {}€ ! \n Votre solde est de maintenant {}€.".format(montant, compte_client.get_solde()))
    
    # Placement du bouton
    bouton_validation_retrait = Button(fenetre, text = "Retirer", bg = class_fenetre_retrait.bg_gris, command = retrait_saisie)
    bouton_validation_retrait.place(x = class_fenetre_retrait.dim[0]/5, y = class_fenetre_retrait.dim[1]/4+100)
    fenetre.mainloop()
    
#def sous_fenetre_depot(compte_client, fenetre_principale):
#    """
#    """
#    class_fenetre_transfert = SousFenetre("Transfert d'argent")
#    fenetre = class_fenetre_transfert.fenetre
#    
#    # Entête
#    texte_titre = Label(fenetre, text = 'Entrez dans la zone de saisie le montant que vous voulez déposer \n Appuyez sur "Déposer" pour valider.', font = ("Helvetica", 14), bg = class_fenetre_depot.bg_gris)
#    texte_titre.pack()
#    
#    # Zone de saisie
#    saisie_montant = Entry(fenetre, width = 15, bg = class_fenetre_transfert.bg_gris)
#    saisie_montant.place(x = class_fenetre_transfert.dim[0]/5, y = class_fenetre_transfert.dim[1]/4 + 60)
#    # Texte montant
#    texte_montant = Label(fenetre, text = 'Montant', font = ("Helvetica", 10), bg = class_fenetre_depot.bg_gris)
#    texte_montant.place(x = class_fenetre_transfert.dim[0]/5 - 60, y = class_fenetre_transfert.dim[1]/4 + 58)
#    # Fonction bouton
#    def depot_saisie():
#        montant = saisie_montant.get()
#        try:
#            montant = int(montant)
#            compte_client.depot(montant)
#            information_compte_selection(fenetre_principale, 20, 160, fenetre_principale.bg_gris, liste_information_bancaire(compte_client), compte_client)
#        except ValueError:
#            return showwarning('Saisie Incorect','Vous devez saisir un nombre.\n Veuillez recommencer !')
#        return showinfo(title = "Dépôt effectué avec succès !", message = "Vous venez de déposer {}€ ! \n Votre solde est de maintenant {}€.".format(montant, compte_client.get_solde()))
#    
#    # Placement du bouton
#    bouton_validation_depot = Button(fenetre, text = "Déposer", bg = class_fenetre_depot.bg_gris, command = depot_saisie)
#    bouton_validation_depot.place(x = class_fenetre_depot.dim[0]/5, y = class_fenetre_depot.dim[1]/4+100)
#    fenetre.mainloop()
    
#def suppresion_compte(compte_client, fenetre_principale):
#    """
#    """
#    del(compte_client)
#    showinfo(title = "Merci à vous !", message = "Vous venez de supprimer votre compte.")
#    creation_fen_compte(fenetre_principale)

def changement_statut_compte(compte_client, fenetre_principale):
    """
    """
    compte_client.actif_inactif()
    information_compte_selection(fenetre_principale, 20, 160, fenetre_principale.bg_gris, liste_information_bancaire(compte_client), compte_client)
    return showinfo(title = "Changement de statut !", message = "Vous êtes maintenant un compte {} !".format(compte_client.get_statut_str()))
    
creation_fen_accueil()