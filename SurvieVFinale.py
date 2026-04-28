#Voici le projet python de Barilly Arthur, NumEt :  22405057
#Le but du Jeu Vidéo de survie est de prendre du bois ainsi que du papier pour aller sur le port pour fuir
#globalement des fonctions vues en cours sauf Dessin.after et les barres de progression
#si ce n'est pas autorisé la version précédente bien moins complète
#pour prendre papier il faut sur la gauche de la hitbox et certains bug résolus/non résolus sont commentés
#Amusez vous bien, ce jeu est très aléatoire.
#############################################################

import tkinter as tk
from random import randint
from math import *

(Hauteur,Largeur) = (800,800) #laisser en format carré pour éviter problème
root = tk.Tk()
root.title("Survie... ")
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg='white')
Dessin.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

taille_case=Hauteur//16
case=(taille_case,taille_case)
bord_sup=(Largeur-taille_case,Hauteur-taille_case)
bord_inf=(Largeur-taille_case,Hauteur-taille_case)
x_nuage = 500
x_nuage2 = 700
random_papier = randint(50,200)

#############################################################

def disque(x,y,rayon, couleur):
    X=(x+1)*taille_case
    Y=(y+1)*taille_case
    p = (X-rayon,Y-rayon)
    q = (X+rayon,Y+rayon)
    Dessin.create_oval(p ,q ,width=0, fill=couleur)

def ile():
    Dessin.create_rectangle(case,bord_sup, fill='#20B2AA')
    disque(7,7,300,'#EDC9AF')
    disque(6,6,200,'#b9f8aa')
    disque(6,7,200,'#b9f8aa')
    disque(7,6,200,'#b9f8aa')
    disque(6,6,180,'#98ee84')
    disque(10,10,30,'#20B2AA')
    Dessin.create_rectangle((680,380),(730,410), fill='#774634', width=0)
    
def ligne():
    for i in range(16):
        debut_trait=((i)*taille_case,taille_case)
        fin_trait=((i)*taille_case,Hauteur-taille_case)
        Dessin.create_line(debut_trait,fin_trait)
    for k in range(16):
        debut_trait=(taille_case,(k)*taille_case)
        fin_trait=(Largeur-taille_case,(k)*taille_case)
        Dessin.create_line(debut_trait,fin_trait)

def personnage(x,y):
    Dessin.create_oval((x+20,y+20),(x-20,y-20),width=1,fill='#f8dcaa', outline="")
    Dessin.create_oval((x+10,y+10),(x-10,y-10),width=1,fill='#c9a35f', outline="")
    Dessin.create_oval((x+8,y+8),(x-8,y-8),width=1,fill='#ffe7bd', outline="")

def personnage_de_victoire(x,y):
    #tete
    Dessin.create_oval((x+573,y+246),(x+655,y+328), width=0, fill='#ffefd2')
    Dessin.create_rectangle((x+602,y+320),(x+627,y+350),width=0, fill='#ffefd2')
    #chapeau ^^
    Dessin.create_oval((x+560,y+251),(x+676,y+277), width=0, fill='#f8dcaa')
    Dessin.create_oval((x+582,y+219),(x+646,y+275), width=0, fill='#c9a35f')
    Dessin.create_oval((x+582,y+215),(x+646,y+270), width=0, fill='#ffe7bd')
    #corps
    Dessin.create_rectangle((x+577,y+333),(x+659,y+436),width=0, fill='#1e00ff')
    Dessin.create_rectangle((x+611,y+358),(x+700,y+378),width=0, fill='#2b15d0')
    
def bateau(x,y):
    Dessin.create_oval((x+285,y+132),(x+467,y+400), width=0, fill='#dedede')
    Dessin.create_rectangle((x+366,y+132),(x+386,y+453),width=0, fill='#ffe7bd')    
    Dessin.create_rectangle((x+142,y+415),(x+704,y+509),width=0, fill='#f7d18e')
    Dessin.create_rectangle((x+181,y+42),(x+366,y+415),width=0, fill='#aff5fb')#pour cacher la voile
    
def afficher_papier(x,y):
    Dessin.create_rectangle((x+235,y+480),(x+300,y+520),fill="white")
    Dessin.create_oval((x+226,y+460),(x+243,y+520),width=0,fill='#EDC9AF', outline="")
    Dessin.create_oval((x+234,y+515),(x+319,y+523),width=0,fill='#EDC9AF', outline="")
    Dessin.create_oval((x+238,y+479),(x+301,y+483),width=0,fill='#EDC9AF', outline="")
    Dessin.create_oval((x+295,y+479),(x+305,y+535),width=0,fill='#EDC9AF', outline="")
    
#############################################################
    
class Etat():
    def __init__(self):
        (L,H) = (Largeur,Hauteur)
        tc=4*taille_case
        self.palmiers = [(randint(tc,L-tc),randint(tc,H-tc)) for e in range(30)]
        self.position=(L/2,H/2)
        self.faim=100
        self.soif=100
        self.score=0
        self.bois=0
        self.papier=0
        self.x_nuage = 600
        
        self.var_faim = tk.StringVar()
        self.var_soif = tk.StringVar()
        self.var_score = tk.StringVar()
        self.var_bois = tk.StringVar()
        self.var_papier = tk.StringVar()
        
        self.var_faim.set(f"Faim : {self.faim}")
        self.var_soif.set(f"Soif : {self.soif}")
        self.var_score.set(f"Score : {self.score}")
        self.var_bois.set(f"Bois : {self.bois}/25")
        self.var_papier.set(f"Papier : {self.papier}/1")
               
        
        self.ecriture_faim = tk.Label(root, text=f"Faim : {self.faim}")
        self.ecriture_soif = tk.Label(root, text=f"Soif : {self.soif}")
        self.barre_de_nourriture = tk.Canvas(root, width=200, height=20, bg="white", highlightthickness=1, highlightbackground="black")
        self.barre_de_soif = tk.Canvas(root, width=200, height=20, bg="white", highlightthickness=1, highlightbackground="black")
        
        self.ecriture_faim.pack()
        self.barre_de_nourriture.pack()
        self.ecriture_soif.pack()
        self.barre_de_soif.pack()
        
        self.verifier_etat() 
        self.mettre_a_jour_barres()
        self.affichage()
    
#############################################################

    def affichage(self):
        Dessin.delete('all')
        ile()
        (x_pers, y_pers) = self.position
        global random_papier
        if self.papier == 0:
            afficher_papier(random_papier,150)
        ligne()
        personnage(x_pers,y_pers)
        for (x,y) in self.palmiers: 
            Dessin.create_rectangle((x-10,y-10),(x+10,y+10),fill='brown')
            Dessin.create_oval((x+14,y+14),(x,y),width=4,fill='green', outline="")
            Dessin.create_oval((x-14,y+14),(x,y),width=4,fill='green', outline="")
            Dessin.create_oval((x+14,y-14),(x,y),width=4,fill='green', outline="")
            Dessin.create_oval((x-14,y-14),(x,y),width=4,fill='green', outline="") #spawn dans l'eau sadge
            
#############################################################
            
    def mettre_a_jour_barres(self):
        self.barre_de_nourriture.delete("progression")
        self.barre_de_soif.delete("progression")
        self.barre_de_nourriture.create_rectangle((0, 0), (2 * self.faim, 20), fill="red", tags="progression")
        self.barre_de_soif.create_rectangle((0, 0), (2 * self.soif, 20), fill="blue", tags="progression")
        self.ecriture_faim.config(text=f"Faim : {self.faim}")
        self.ecriture_soif.config(text=f"Soif : {self.soif}")
        
############################################################

    def haut(self, event=None):
        (x,y)=etat.position
        if y != 2*taille_case:    
            etat.position=(x,y-taille_case)
            etat.faim -= randint(5,10)
            etat.soif -= randint(10,15)
            etat.score += 5
            self.var_faim.set(f"Faim : {self.faim}")
            self.var_soif.set(f"Soif : {self.soif}")
            self.var_score.set(f"Score : {self.score}")
            self.verifier_palmier()
            self.verifier_etat()
            self.mettre_a_jour_barres()
            self.verifier_papier()
        etat.affichage()
        self.verif_construire()
        
    def bas(self, event=None):
        (x,y)=etat.position
        if y != Hauteur-2*taille_case:
            etat.position=(x,y+taille_case)
            etat.faim -= randint(5,10)
            etat.soif -= randint(10,15)
            etat.score += 5
            self.var_faim.set(f"Faim : {self.faim}")
            self.var_soif.set(f"Soif : {self.soif}")
            self.var_score.set(f"Score : {self.score}")
            self.verifier_palmier()
            self.verifier_etat()
            self.mettre_a_jour_barres()
            self.verifier_papier()
        etat.affichage()
        self.verif_construire()
        
    def gauche(self, event=None):
        (x,y)=etat.position
        if x != 2*taille_case:
            etat.position=(x-taille_case,y)
            etat.faim -= randint(5,10)
            etat.soif -= randint(10,15)
            etat.score += 5
            self.var_faim.set(f"Faim : {self.faim}")
            self.var_soif.set(f"Soif : {self.soif}")
            self.var_score.set(f"Score : {self.score}")
            self.verifier_palmier()
            self.verifier_etat()
            self.mettre_a_jour_barres()
            self.verifier_papier()
        etat.affichage()
        self.verif_construire()
        
    def droite(self, event=None):
        (x,y)=etat.position
        if x != Largeur-2*taille_case:
            etat.position=(x+taille_case,y)
            etat.faim -= randint(5,10)
            etat.soif -= randint(10,15)
            etat.score += 5
            self.var_faim.set(f"Faim : {self.faim}")
            self.var_soif.set(f"Soif : {self.soif}")
            self.var_score.set(f"Score : {self.score}")
            self.verifier_palmier()
            self.verifier_etat()
            self.mettre_a_jour_barres()
            self.verifier_papier()
        etat.affichage()
        self.verif_construire()
  
#############################################################  
  
    def verifier_palmier(self):
        (pers_x, pers_y) = self.position
        for (x_palm_rnd, y_palm_rnd) in self.palmiers:
            if abs(pers_x - x_palm_rnd) < 20 and abs(pers_y - y_palm_rnd) < 30:
                self.faim = min(100, self.faim + randint(5, 15))
                self.soif = min(100, self.soif + randint(15, 25))
                self.score += 10
                self.bois += randint(3,5)
                self.var_faim.set(f"Faim : {self.faim}")
                self.var_soif.set(f"Soif : {self.soif}")
                self.var_score.set(f"Score : {self.score}")
                self.var_bois.set(f"Bois : {self.bois} /25")
                self.palmiers.remove((x_palm_rnd, y_palm_rnd)) #enleve pas tt les palmiers, meme en passant pluss dessus
                
    def verifier_papier(self):
        (x,y)=etat.position
        global random_papier
        #print(x,y, random_papier)
        if abs(x-random_papier-235)<40 and abs(y-650) <20: #decalage de coo dans random papier donc -235 pour remttre en coo basique
            self.papier = min(1,self.papier+1)
            self.var_papier.set(f"Papier : {self.papier} /1")
        
    def verifier_etat(self):
        if self.faim <= 0 or self.soif <= 0:
            self.perdu() #arreter à 0 et pas en negatif
    
    def verif_construire(self):
        if etat.bois >= 25 and etat.papier == 1:
            (x,y) =  self.position
            if (x == 700.0) and (y == 400.0):
                construire = tk.Button(root, text="build", command=self.construction)
                construire.pack()               

############################################################# 
                
    def initialisation(self):
        Dessin.create_rectangle((0,0),(800,500),fill="#aff5fb")
        Dessin.create_rectangle((0,500),(800,800),fill="blue")
        self.enlever_overlay() 
        personnage_de_victoire(0,0)
        bateau(0,0)
        
    def nuage(self, x_nuage,y,couleur):
        Dessin.create_oval((x_nuage,y),(x_nuage+50,y+50), width=0, fill=couleur)
        Dessin.create_oval((x_nuage+25,y-25),(x_nuage+75,y+25), width=0, fill=couleur)
        Dessin.create_oval((x_nuage+25,y+20),(x_nuage+75,y+70), width=0, fill=couleur)
        Dessin.create_oval((x_nuage+50,y),(x_nuage+100,y+50), width=0, fill=couleur)
        Dessin.create_oval((x_nuage+75,y-25),(x_nuage+125,y+25), width=0, fill=couleur)
        Dessin.create_oval((x_nuage+75,y+20),(x_nuage+125,y+70), width=0, fill=couleur)
        Dessin.create_oval((x_nuage+100,y),(x_nuage+150,y+50), width=0, fill=couleur)
        Dessin.create_oval((x_nuage+50,y-40),(x_nuage+100,y+10), width=0, fill=couleur)
        Dessin.create_oval((x_nuage+50,y+20),(x_nuage+100,y+70), width=0, fill=couleur)
                                    
    def mouvement_nuage(self):
        Dessin.delete('all')
        self.initialisation()
        global x_nuage
        x_nuage -= 10
        self.nuage(x_nuage,50,"white")
        if x_nuage >-200:
            Dessin.after(50, self.mouvement_nuage)
        global x_nuage2
        x_nuage2 -= 10
        self.nuage(x_nuage2,150,"white")
        if x_nuage2 >-200:
            Dessin.after(50, self.mouvement_nuage)
 
    def construction(self, event=None):
        self.nuage
        self.mouvement_nuage()
        Score_final = tk.Label(root, text=f"Score final : {self.score}")
        Score_final.pack()
        texte_de_victoire = tk.Label(root, text="Victoire", font=("Arial", 40), fg="#90EE90")
        texte_de_victoire.pack() 
 
#############################################################  
 
    def enlever_overlay(self):
        bouton_haut.pack_forget()
        bouton_bas.pack_forget()
        bouton_gauche.pack_forget()
        bouton_droite.pack_forget()
        faim.pack_forget()
        soif.pack_forget()
        score.pack_forget()
        Ressources.pack_forget()
        bois.pack_forget()
        papier.pack_forget()
        root.unbind("<KeyPress-z>")
        root.unbind("<KeyPress-s>")
        root.unbind("<KeyPress-q>")
        root.unbind("<KeyPress-d>") #pour éviter de bouger apres fin du jeu
        
    def perdu(self):
        self.enlever_overlay()
        texte_de_défaite = tk.Label(root, text="GAME OVER", font=("Arial", 24), fg="red")
        texte_de_défaite.pack()
        Score_final = tk.Label(root, text=f"Score final : {self.score}")
        Score_final.pack()
          
##################################
etat=Etat()

faim= tk.Label(root,textvariable=etat.var_faim)
soif= tk.Label(root,textvariable=etat.var_soif)
score = tk.Label(root, textvariable=etat.var_score)
Ressources = tk.Label(root, text='Ressources collectées', font=("Arial", 16))
bois = tk.Label(root, textvariable=etat.var_bois)
papier = tk.Label(root, textvariable=etat.var_papier)

bouton_haut = tk.Button(root, text="haut", command=etat.haut, width=10)
bouton_bas = tk.Button(root, text="bas", command=etat.bas, width=10)
bouton_gauche = tk.Button(root, text="gauche", command=etat.gauche, width=10)
bouton_droite = tk.Button(root, text="droite", command=etat.droite, width=10)

bouton_haut.pack()
bouton_bas.pack()
bouton_gauche.pack()
bouton_droite.pack()
score.pack()
Ressources.pack()
bois.pack()
papier.pack()

root.bind("<KeyPress-z>", etat.haut)
root.bind("<KeyPress-s>", etat.bas)
root.bind("<KeyPress-q>", etat.gauche)
root.bind("<KeyPress-d>", etat.droite)

root.mainloop()