import pygame
from random import *
import math


#Initialise la fenetre et la taille
pygame.init()
pygame.font.init()
fenetre = pygame.display.set_mode((800,600))

#Titre fenetre
pygame.display.set_caption('Space Invaders')

#Image à charger : les deux vaisseaux, le fond et laser
vaiss1 = pygame.image.load('image/spp.png')
vaiss2 = pygame.image.load('image/spp2.png')
back = pygame.image.load('image/background.jpg')
laser = pygame.image.load('image/las.png')


#Etapes de jeux et variable de tir actif
run = True
menu = True
diff = False
vaisseau = False
game = False
go = False
tir = False



#Definition des polices et des tailles pour les différents messages
font = pygame.font.Font('freesansbold.ttf',32)
msg_font = pygame.font.Font('freesansbold.ttf',64)
button_font = pygame.font.Font('freesansbold.ttf',18)


#Defini une liste pour chaque informations des asteroides
#Crée le nombre d'astéroide défini et ajoute chaque info à la liste

nbr_aste = 4

astes = []
astesX = []
astesY = []
astesMouvX = []
astesMouvY = []

for i in range(nbr_aste):
    astes.append(pygame.image.load('image/aste.png'))
    astesX.append(randint(20,780))
    astesY.append(0)
    astesMouvY.append(40)


#coordonnées de départ et variable de mouvement du vaisseau
vaissX = 370
vaissY = 530
vaissMouv = 0


#coordonnées de départ et vitesse du laser
laserX = vaissX
laserY = 550
laserMouvY = -12





def boutton(msg_principal,msg_gauche,msg_droit):
    """
    argument --> a : message principale
                 b : message bouton gauche
                 c : message bouton droit
    
    """
    
    #texte à afficher
    texte = msg_font.render(msg_principal, True, (255,255,255))
    fenetre.blit(texte, (200,300))

    #affichage rectangle blanc
    pygame.draw.rect(fenetre, (255,255,255),(550,450,100,50))
    pygame.draw.rect(fenetre, (255,255,255),(200,450,100,50))

    #affichage msg bouton
    but1 = button_font.render(msg_gauche, True, (0,0,0))
    but2 = button_font.render(msg_droit, True, (0,0,0))
    fenetre.blit(but1,(210,460))
    fenetre.blit(but2,(560,460))



def joueur(x,y):
    """
    fonction pour afficher le vaisseau
    prend comme argument les coordonnées x et y du vaisseau sur la fenetre
    """
    fenetre.blit(vaiss,(x,y))

def asteroide(x,y,i):
    """
    fonction pour afficher l'asteroide
    prend comme argument les coordonnées x et y de l'asteroide sur la fenetre
    l'argument i permet de définir de quel asteroide est concerné
    """
    fenetre.blit(astes[i],(x,y))

def tirer(x,y):
    """
    defini le tir comme étant en cours et affiche la balle
    prend comme argument les coordonnées x et y de la balle sur la fenetre
    """
    global tir
    tir = True
    fenetre.blit(laser, (x,y))

def collision(asteX,asteY,laserX,laserY):
    """
    Fonction qui détecte s'il y a collison entre le laser et l'astéroide
    prend en argument les coordonnées de l'astéroide et du laser
    retourne un booléen 
    """
    distance = math.sqrt(math.pow(asteX - laserX, 2) + math.pow(asteY - laserY, 2))
    if distance < 25:
        return True
    else:
        return False

def afficherScore():
    """
    affiche le score en haut à gauche
    """
    score = font.render('Score : '+ str(score_value), True, (255,255,255))
    fenetre.blit(score, (20,20))


    
while run:
    
     
    
    while menu:

        #evenement de click et de déplacement de la souris
        posi = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Initialisation de la fenetre et du fond
        
        fenetre = pygame.display.set_mode((800,600))
        fenetre.fill((0,0,0))
        fenetre.blit(back,(0,0))
        
        
        
             
        #affichage bouton      
        boutton('Bienvenue','JOUER','QUITTER')
        
        #Click sur les boutons
        if posi[0] > 200 and posi[0] < 300 and posi[1] > 450 and posi[1] < 500 and click[0] == 1 :
            menu = False
            diff = True  
        elif posi[0] > 550 and posi[0] < 650 and posi[1] > 450 and posi[1] < 500 and click[0] == 1 :
            menu,game,diff,vaisseau,run = False,False,False,False,False
        
        pygame.display.update()
        
    
    
    #Definition du socre au debut de la partie
    score_value = 0

    while diff:
        
        #Position et de la souris et click
        posi = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Fenetre
        fenetre = pygame.display.set_mode((800,600))
        fenetre.fill((0,0,0))
        fenetre.blit(back,(0,0))
        boutton('DIFFICULTE','FACILE','DIFFICILE')

        if posi[0] > 200 and posi[0] < 300 and posi[1] > 450 and posi[1] < 500 and click[0] == 1 :
            diff = False
            vaisseau = True
            v = 3
            for i in range(nbr_aste):
                astesMouvX.append(v)
            
            
        elif posi[0] > 550 and posi[0] < 650 and posi[1] > 450 and posi[1] < 500 and click[0] == 1 :
            diff = False
            vaisseau = True
            v = 7
            for i in range(nbr_aste):
                astesMouvX.append(v)
            
            
        pygame.display.update()

        
        
    while vaisseau:

        #Position et de la souris et click
        posi = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #Fenetre
        fenetre = pygame.display.set_mode((800,600))
        fenetre.fill((0,0,0))
        fenetre.blit(back,(0,0))

        #Affichage pour le choix du vaisseau
        texte = msg_font.render('CHOIX VAISSEAU', True, (255,255,255))
        fenetre.blit(texte, (130,280))
        fenetre.blit(vaiss1,(200,500))
        fenetre.blit(vaiss2,(600,500))

        #Si Click sur l'un des vaisseaux pour choisir
        if posi[0] > 200 and posi[0] < 260 and posi[1] > 500 and posi[1] < 560 and click[0] == 1 :
            vaiss = pygame.image.load('image/spp.png')
            vaisseau = False
            game = True
        elif posi[0] > 600 and posi[0] < 660 and posi[1] > 500 and posi[1] < 560 and click[0] == 1 :
            vaiss = pygame.image.load('image/spp2.png')
            vaisseau = False
            game = True
            

        

        pygame.display.update()

        
    
    
        
    while game:

        
        

        #Fenetre
        
        fenetre.fill((0,0,0))
        fenetre.blit(back,(0,0))
        
        
                 
            
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game = False
                run = False
                
            #Si touche clavier gauche ou droite
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #déplacemenent vers la gauche
                    vaissMouv = -6
                    
                        
                if event.key == pygame.K_RIGHT:
                    #déplacemenent vers la droite
                    vaissMouv = 6
                    
                        
                if event.key == pygame.K_SPACE:
                    if tir is False: #Tir uniquement si on ne tir pas déjà
                        #Recupère position à laquelle on tire 
                        laserX = vaissX+20
                        tirer(laserX,laserY)

                        
            if event.type == pygame.KEYUP:
                    #Lorsqu'on relache la touche le vaisseau arrete de se déplacer
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        vaissMouv = 0
            
            
        
                 
            
        #On ajoute la valeur du déplacement à la coordonnée x   
        vaissX += vaissMouv
        
        

        #Bloque le vaisseau si les coordonnées dépassent la fenetre
        if vaissX < 0:
            vaissX = 0
        elif vaissX > 740:
            vaissX = 740

        #Boucle pour changer le sens de chaque astéroide lorsqu'il atteint le bord de la fenetre
        #Descend les asteroid a chaque fois qu'ils touchent un bord
        #Vérifie les collisions
        for i in range(nbr_aste):

            #Si un ennemie atteint la dernière ligne
            #Il est sorti de l'écran et on sort de la boucle d'affichage des asteroides
            if astesY[i] >= 470:
                for j in range(nbr_aste):
                    astesY[j] = 0
                go = True
                game = False
                
            #Mouvement des asteroides et changement de sens quand ils arrivent au bout
            astesX[i] += astesMouvX[i]
            if astesX[i] < 0:
                astesMouvX[i] = v
                astesY[i] += astesMouvY[i]
            elif astesX[i] > 740:
                astesMouvX[i] = -v
                astesY[i] += astesMouvY[i]

            #S'il y collision on reinitialise le tir et la positon du laser et on augmente le score
            coll = collision(astesX[i],astesY[i],laserX,laserY)
            if coll is True:
                tir = False
                laserY = 500
                score_value += 1
                astesX[i] = randint(40,760)
                astesY[i] = 50

            

        #Affichage et mouvementdu laser
        if tir is True:
            tirer(laserX,laserY)
            laserY += laserMouvY
        if laserY < 0:
            tir = False
            laserY = 500
        
        #Affichage du vaisseau du score et des asteroides
        joueur(vaissX, vaissY)
        afficherScore()
        for i in range(nbr_aste):
            asteroide(astesX[i],astesY[i], i)
            
        pygame.display.update()
        
    while go:



        #Position et de la souris et click
        posi = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Fenetre
        fenetre = pygame.display.set_mode((800,600))
        fenetre.fill((0,0,0))
        fenetre.blit(back,(0,0))
            
        #Affichage des boutons
        boutton('GAME OVER', 'REJOUER', 'QUITTER')
            
        #Detection des clicks sur les boutons
        if posi[0] > 200 and posi[0] < 300 and posi[1] > 450 and posi[1] < 500 and click[0] == 1 :
            go = False
            menu = True
            #game = True
                
        elif posi[0] > 550 and posi[0] < 650 and posi[1] > 450 and posi[1] < 500 and click[0] == 1 :
            go = False
            run = False
        
            
        pygame.display.update()
            
            
                      
pygame.quit()

