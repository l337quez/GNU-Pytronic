#https://openclassrooms.com/forum/sujet/animer-des-sprite-17872
import os
from tkinter import *
 
 
class Sprite_Abe():
 
    def __init__(self, coord_x, coord_y):
        self.coord_x, self.coord_y = 150, 400
        self.compteur_gauche = 0
        self.compteur_droite = 0
 
        ############ SPRITES ######################################################
 
        self.Abe_repos = PhotoImage(file = os.path.join('Sprite_Abe','Abe_repos.gif'))  #Abe au repos (droite)
        self.Abe_repos_gauche = PhotoImage(file = os.path.join('Sprite_Abe','Abe_repos(G).gif'))  #Abe au repos (gauche)
 
        self.Abe_marche1 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_marche1.gif'))# Images de Marche(droite)
        self.Abe_marche2 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_marche2.gif'))#
        self.Abe_marche3 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_marche3.gif'))#
        self.Abe_marche4 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_marche4.gif'))#
 
        self.Abe_marche1G = PhotoImage(file = os.path.join('Sprite_Abe','Abe_marche1(G).gif'))# Images de Marche(gauche)
        self.Abe_marche2G = PhotoImage(file = os.path.join('Sprite_Abe','Abe_marche2(G).gif'))#
        self.Abe_marche3G = PhotoImage(file = os.path.join('Sprite_Abe','Abe_marche3(G).gif'))#
        self.Abe_marche4G = PhotoImage(file = os.path.join('Sprite_Abe','Abe_marche4(G).gif'))#
 
        self.Abe_retourne_G1 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_retourne1(gauche).gif'))# Images de retournement à gauche
        self.Abe_retourne_G2 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_retourne2(gauche).gif'))#
        self.Abe_retourne_G3 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_retourne3(gauche).gif'))#
        self.Abe_retourne_G4 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_retourne4(gauche).gif'))#
 
        self.Abe_retourne_D1 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_retourne1(droite).gif'))# Images de retournement à droite
        self.Abe_retourne_D2 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_retourne2(droite).gif'))#
        self.Abe_retourne_D3 = PhotoImage(file = os.path.join('Sprite_Abe','Abe_retourne3(droite).gif'))#
        self.Abe_retourne_D4 = PhotoImage(file =os.path.join('Sprite_Abe','Abe_retourne4(droite).gif'))#
         
 
        ############ ITEM DE SUPRETION ############################################
 
        self.Item_Marche = Canvas.create_image(self.coord_x,self.coord_y, image=self.Abe_repos) #Création des item qui permeterons de
        self.Item_Repos = Canvas.create_image(self.coord_x,self.coord_y, image=self.Abe_repos)  #supprimer les image
        self.Item_Retourne = Canvas.create_image(self.coord_x,self.coord_y, image=self.Abe_repos)
         
        Canvas.delete(self.Item_Repos) #Supretion de la première image
 
        ############# LISTE DES IMAGES ##########################################
 
        self.Liste_marche_droite      = [self.Abe_marche1, self.Abe_marche2,  # liste des images de marche(droite)
                                         self.Abe_marche3, self.Abe_marche4]
 
        self.Liste_marche_gauche      = [self.Abe_marche1G, self.Abe_marche2G,  # liste des images de marche(gauche)
                                         self.Abe_marche3G, self.Abe_marche4G]
 
        self.Liste_retourne           = [self.Abe_retourne_G1, self.Abe_retourne_G2,  # liste des images de retournement
                                         self.Abe_retourne_G3, self.Abe_retourne_G4,
                                
                                         self.Abe_retourne_D1, self.Abe_retourne_D2,
                                         self.Abe_retourne_D2, self.Abe_retourne_D4,]
 
    def repos(self):
        Canvas.delete(self.Item_Retourne)
        Canvas.delete(self.Item_Marche)
        Canvas.delete(self.Item_Repos)
 
 
    #----------------------------------# Pour que Abe reste dans la même position après le relachement de la touche
        if(self.compteur_droite == 1):
            self.Item_Repos = Canvas.create_image(self.coord_x,self.coord_y, image= self.Abe_repos)
        if(self.compteur_gauche == 1):
            self.Item_Repos = Canvas.create_image(self.coord_x,self.coord_y, image= self.Abe_repos_gauche)
         
           
    def marche_droite(self):
        Canvas.delete(self.Item_Marche)
        Canvas.delete(self.Item_Repos)
        Canvas.delete(self.Item_Retourne)
        self.Item_Marche = Canvas.create_image(self.coord_x,self.coord_y, image= self.Liste_marche_droite[self.anim_marche])
 
    def marche_gauche(self):
        Canvas.delete(self.Item_Marche)
        Canvas.delete(self.Item_Repos)
        Canvas.delete(self.Item_Retourne)
        self.Item_Marche = Canvas.create_image(self.coord_x,self.coord_y, image= self.Liste_marche_gauche[self.anim_marche])
 
    def retourne(self):
        Canvas.delete(self.Item_Retourne)
        Canvas.delete(self.Item_Marche)
        Canvas.delete(self.Item_Repos)
        self.Item_Retourne = Canvas.create_image(self.coord_x,self.coord_y, image= self.Liste_retourne[self.anim_retourne])
 
 
##############        
fen = Tk()
fen.title("Moddworld")
 
Canvas = Canvas(fen, bg='white', height=450, width=640)
Canvas.pack()
 
ImageDeFond = PhotoImage(file = os.path.join('Sprite_Abe','Fond_Nature.gif')) #Image de fond
Canvas.create_image(150,150, image= ImageDeFond)
