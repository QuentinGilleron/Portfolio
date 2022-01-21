import sys
import random


##################

### CONSTANTES #### 

##################

b1='Porte-avions'
b2='Croiseur'
b3='Destroyer'
b4='Torpilleur'

##################

### FONCTIONS ####

##################


def placement(taille_plateau, taille_bateau):
    #fonction de placement aléatoir de bateaux
    
#choix aléatoir (horizontal ou verticale)

    #pour l'horizontal
    if(random.randint(0,1)==0):
        
        orientation2='HOR'

    #pour le verticale
    else:
        
        orientation2='VER'

    #placement aléatoir en fonction de la taille du tableau de façon horizontal
    if(orientation2=='HOR'):
        
        ir2 = random.randint(0,taille_plateau-1)
        jr2 = random.randint(0,taille_plateau-taille_bateau)
        
    else:
        
        #placement aléatoir en fonction de la taille du tableau de façon verticale
        ir2 = random.randint(0,taille_plateau-taille_bateau)
        jr2 = random.randint(0,taille_plateau-1)
        
    return orientation2, (ir2, jr2)

###########################################################################################

def verif_placement(plateau, coordonné, nombre_de_colonne, orientation2):

#cette fonction vérifie que les bateaux soit bien placé de façon horizontal ou horizontale sans etre sur une case deja pleine 
    
    ligne, colonne = coordonné[0], coordonné[1]
    
    #pour les bateaux à l'horizontal
    if orientation2=='HOR':
        
        for j in range(nombre_de_colonne):
            
            if(plateau[ligne][colonne+j]['contenu']!='Eau'):
                
                return False
    
    #pour les bateaux à la verticale
    else:
        
        for i in range(nombre_de_colonne):
            
            if(plateau[ligne+i][colonne]['contenu']!='Eau'):
                
                return False
            
    return True

###########################################################################################

if __name__ == "__main__":
    
#création d'un plateau de jeu avec des case vide
#ces cases vide contiennent de l'eau

    plateau_de_jeu=[]
    
    for i in range(10):
        
        case=[]
        

        for j in range(10):
            
            case.append({'contenu':'Eau', 'numero':0, 'etat':'Neuf'})

        plateau_de_jeu.append(case)

###########################################################################################

#                                      PORTE AVION

    #taille du bateau en nombre de case
    #numéro du bateau    
    taille_bateau=5
    numero_bateau=0
    
    orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)

    #vérification de l'emplacement des bateaux avec la fonction
    #si le placement existe deja, la position est renouvellé
    while(verif_placement(plateau_de_jeu, position3, taille_bateau, orientation3)==False):
        
        print('Impossible. Nouvelle position')
        orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)

    #pour les bateaux placer avec 'HOR'(horizontal)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)
    if(orientation3=='HOR'):
        
        for j in range(taille_bateau):
            
            plateau_de_jeu[position3[0]][position3[1]+j]={'contenu':b1, 'numero':numero_bateau, 'etat':'Neuf'}

    #pour les bateaux placer avec 'VER'(verticale)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)
    else:

        for i in range(taille_bateau):
            
            plateau_de_jeu[position3[0]+i][position3[1]]={'contenu':b1, 'numero':numero_bateau, 'etat':'Neuf'}


###########################################################################################

#                                      CROISEUR

    #taille du bateau en nombre de case
    #numéro du bateau
    taille_bateau=4
    numero_bateau=0
    
    orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)
    
    #vérification de l'emplacement des bateaux avec la fonction
    #si le placement existe deja, la position est renouvellé
    while(verif_placement(plateau_de_jeu, position3, taille_bateau, orientation3)==False):
        
        print('Impossible. Nouvelle position')
        orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)
    
    #pour les bateaux placer avec 'HOR'(horizontal)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)
    if(orientation3=='HOR'):
        
        for j in range(taille_bateau):
            
            plateau_de_jeu[position3[0]][position3[1]+j]={'contenu':b2, 'numero':numero_bateau, 'etat':'Neuf'}

    #pour les bateaux placer avec 'VER'(verticale)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)        
    else:
    
        #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)
        for i in range(taille_bateau):
            
            plateau_de_jeu[position3[0]+i][position3[1]]={'contenu':b2, 'numero':numero_bateau, 'etat':'Neuf'}


###########################################################################################

#                                       DESTROYER

    #taille du bateau en nombre de case
    #numéro du bateau
    taille_bateau=3
    numero_bateau=0
    
    orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)
    
    #vérification de l'emplacement des bateaux avec la fonction
    #si le placement existe deja, la position est renouvellé
    while(verif_placement(plateau_de_jeu, position3, taille_bateau, orientation3)==False):
        
        print('Impossible. Nouvelle position')
        
        orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)

    #pour les bateaux placer avec 'HOR'(horizontal)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)    
    if(orientation3=='HOR'):
        
        for j in range(taille_bateau):
            
            plateau_de_jeu[position3[0]][position3[1]+j]={'contenu':b3, 'numero':numero_bateau, 'etat':'Neuf'}

    #pour les bateaux placer avec 'VER'(verticale)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)        
    else:
        
        for i in range(taille_bateau):
            
            plateau_de_jeu[position3[0]+i][position3[1]]={'contenu':b3, 'numero':numero_bateau, 'etat':'Neuf'}


###########################################################################################

#                                      DESTROYER

    #taille du bateau en nombre de case
    #numéro du bateau
    taille_bateau=3
    numero_bateau=1
    
    #vérification de l'emplacement des bateaux avec la fonction
    #si le placement existe deja, la position est renouvellé
    orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)
    
    while(verif_placement(plateau_de_jeu, position3, taille_bateau, orientation3)==False):
        
        print('Impossible. Nouvelle position')
        orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)

    #pour les bateaux placer avec 'HOR'(horizontal)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)    
    if(orientation3=='HOR'):
        
        for j in range(taille_bateau):
            
            plateau_de_jeu[position3[0]][position3[1]+j]={'contenu':b3, 'numero':numero_bateau, 'etat':'Neuf'}

    #pour les bateaux placer avec 'VER'(verticale)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)        
    else:
        
        for i in range(taille_bateau):
            
            plateau_de_jeu[position3[0]+i][position3[1]]={'contenu':b3, 'numero':numero_bateau, 'etat':'Neuf'}




###########################################################################################

#                                      TORPILLEUR

    #taille du bateau en nombre de case
    #numéro du bateau
    taille_bateau=2
    numero_bateau=0
    
    #vérification de l'emplacement des bateaux avec la fonction
    #si le placement existe deja, la position est renouvellé
    orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)
    
    while(verif_placement(plateau_de_jeu, position3, taille_bateau, orientation3)==False):
        
        print('Impossible. Nouvelle position')
        
        orientation3, position3 = placement(len(plateau_de_jeu), taille_bateau)

    #pour les bateaux placer avec 'HOR'(horizontal)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)    
    if(orientation3=='HOR'):
        
        for j in range(taille_bateau):
            
            plateau_de_jeu[position3[0]][position3[1]+j]={'contenu':b4, 'numero':numero_bateau, 'etat':'Neuf'}

    #pour les bateaux placer avec 'VER'(verticale)
    #identifier le bateau sur le plateau avec, son nom, son noméro et son état de base(neuf)        
    else:
        
        for i in range(taille_bateau):
            
            plateau_de_jeu[position3[0]+i][position3[1]]={'contenu':b4, 'numero':numero_bateau, 'etat':'Neuf'}
            
###########################################################################################

                        
    # affichage du tableau |_|
    print('-'*(len(plateau_de_jeu)+2))
    
    for l7 in plateau_de_jeu:
        
        a_afficher='|'
        
        for c7 in l7:
            
            if(c7['etat']=='Neuf'):
                
                # afficher une case vide la ou il ne s'est rien passé 
                
                a_afficher=a_afficher+' '
                
            else:
                
                if(c7['contenu']=='Eau'):
                    
                    #afficher une croix pour les endroits touché vide

                    a_afficher=a_afficher+'X'
                    
                else:

                    #afficher la lettre du bateau pour les bateaux touchés
                    
                    a_afficher=a_afficher+'{}'.format(c7['contenu'][0].lower())
                    
        #séparation des cases
        a_afficher=a_afficher+'|'
        
        print(a_afficher)
        
    print('-'*(len(plateau_de_jeu)+2))
    
    tous_coulés=False
    
#selection de la case de tire 

    while(not tous_coulés):
        
        print('où voulez vous tirer ? - 0 pour quitter')
        i = (int)(input('Numéro de ligne entre 1 et {} : '.format(10)))

#message de fin si partie est fini avant d'avoir trouvé tout les bateaux
        
        if(i==0):
            
            print('Tu ne vas même pas jusqu\'au bout du jeu ? Tant pis. Bye !')
            sys.exit(0)
            
        j = (int)(input('Numéro de colonne entre 1 et {} : '.format(10)))

#mode triche
#permet d'etre activé si les lignes ou les colonnes sont < à 0
#affiche toutes les cases contenant les bateaux
#ps: c'est pas bien de tricher :c

        if((i<0) or (j<0)):
            
            print('MODE TRICHE :')
            print('-'*(len(plateau_de_jeu)+2))
            
            for l6 in plateau_de_jeu:

                #séparation des cases
                a_afficher='|'
                
                for c6 in l6:
                    
                    if(c6 ['contenu'] == 'Eau'):

                        #afficher un espace sur les cases qui n'ont pas été touché
                        a_afficher=a_afficher+' '
                        
                    else:
                        
                        #afficher le contenu de la case avec la premier lettre du bateau
                        a_afficher=a_afficher+'{}'.format(c6 ['contenu'] [0])
                
                #séparation des cases
                a_afficher=a_afficher+'|'
                
                #print le tableau
                print(a_afficher)
            
            print('-'*(len(plateau_de_jeu)+2))

        else:
            
            #si position est deja touché
            if(plateau_de_jeu [(i-1)] [(j-1)] ['etat'] == 'Touche'):
                
                print('Position déjà touchée')

            #si le bateaux est touché et que tout le bateau est touché     
            else:
                
                plateau_de_jeu [(i-1)] [(j-1)] ['etat'] = 'Touche'

                if(plateau_de_jeu [(i-1)] [(j-1)] ['contenu'] == 'Eau'):
                    
                    print('A l\'eau')
                    
                else:
                    
                    #vérifi si le bateau est coulé ou juste touché 
                    verif_coulé=True
                    for l8 in plateau_de_jeu:

                        for bateau in l8:

                            if bateau ['contenu'] == plateau_de_jeu [(i-1)] [(j-1)] ['contenu'] and bateau ['numero'] == plateau_de_jeu [(i-1)] [(j-1)] ['numero'] and bateau ['etat'] == 'Neuf':

                                verif_coulé=False
                    if(verif_coulé):

                        print(plateau_de_jeu [(i-1)] [(j-1)] ['contenu'], plateau_de_jeu [(i-1)] [(j-1)] ['numero'], 'coulé')

                    else:

                        print(plateau_de_jeu [(i-1)] [(j-1)] ['contenu'], plateau_de_jeu [(i-1)] [(j-1)] ['numero'], 'touché')

            print('-'*(len(plateau_de_jeu)+2))

            for l7 in plateau_de_jeu:
                
                #séparation des cases
                a_afficher='|'

                for c7 in l7:
                    
                    
                    if(c7['etat']=='Neuf'):
                        #afficher un espace sur les cases qui n'ont pas été touché
                        a_afficher=a_afficher+' '

                    else:

                        #si la position contient de l'eau, faire une croix 

                        if(c7['contenu']=='Eau'):

                            a_afficher=a_afficher+'X'

                        else:

                            a_afficher=a_afficher+'{}'.format(c7['contenu'][0].lower())

                #séparation des cases
                a_afficher=a_afficher+'|'

                print(a_afficher)

            print('-'*(len(plateau_de_jeu)+2))
        
        tous_coulés=True

        for l10 in plateau_de_jeu:

            for c10 in l10:

                if((c10['contenu'] != 'Eau') and (c10['etat']=='Neuf')):

                    tous_coulés=False

#message de fin de partie

    print('Tu as coulé tous les bateaux.')
    print('GG')
