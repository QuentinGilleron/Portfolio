# Implémentation des dates et calendriers
# Implémentation des tests (voir main en fin de fichier)

from types import MethodDescriptorType
from typing import Dict, List, Tuple, NoReturn



# =============================================================================
def est_bissextile(annee: int): 

    ###############
    #     TEST    #
    ###############

    """
    retourne vrai si l'année est bissextile

    >>> est_bissextile(2020)
    True
    >>> est_bissextile(2021)
    False
    >>> est_bissextile(2022)
    False
    >>> est_bissextile(1900)
    False
    >>> est_bissextile(2000)
    True
    """ 

    #####################
    #    EXPLICATION    #
    #####################

    """
    Calcule mathématique trouvé sur internet, permetant de verifier si une année est bissextile ou non.
    """
    ################################
    #      CORPS DE FONCTION       #
    ################################

    if annee%4 ==0 and annee%100 != 0 or annee%400 == 0:
        return True
    else:
        return False
    
    
# =============================================================================
def cree_date(j: int, m: int, a: int) -> Dict :

    ###############
    #     TEST    #
    ###############

    """
    Crée une date à partir des entiers la décrivant.
    Si l'un des paramètres n'est pas un entier, la fonction retournera None

    >>> cree_date(15,12,2020)
    {'jour': 15, 'mois': 12, 'annee': 2020}
    >>> cree_date(1.5,12,2020)
    
    """

    #####################
    #    EXPLICATION    #
    #####################

    """
    Création de la bibliotéque 'dic' qui va stocker les dates créé lors de l'execution du programme.
    Verifi que le jour, le mois et l'année soit bien de type entier.
    Retourne donc la date sous forme ' jour;j , mois:m , année:a '.
    Sinon ne retourne rien (None).
    """

    ################################
    #      CORPS DE FONCTION       #
    ################################

    dic={}
    if type(j) == int and type(m) == int and type(a):
        if j % 1 == 0 and m % 1 == 0 and  a % 1 == 0:
            dic={"jour":j,"mois":m,"annee":a}
        return(dic)

    
    
# =============================================================================
def copie_date(date: Dict) -> Dict :

    ###############
    #     TEST    #
    ###############

    """
    copie la date passée en paramètre
    
    >>> copie_date({'jour': 15, 'mois': 12, 'annee': 2020})
    {'jour': 15, 'mois': 12, 'annee': 2020}
    >>> copie_date({'jour': 10, 'mois': 9, 'annee': 2000})
    {'jour': 10, 'mois': 9, 'annee': 2000}

    """

    #####################
    #    EXPLICATION    #
    #####################

    """
    récupere la date et la colle dans une copie, dans le même format que la date initial
    """
    

    ################################
    #      CORPS DE FONCTION       #
    ################################

    copie = {'jour': date['jour'],'mois': date['mois'],'annee': date['annee']}
    
    return copie

    
# =============================================================================
def compare(d1: Dict, d2: Dict) -> int :

    ###############
    #     TEST    #
    ###############

    """
    Permet de classer deux dates.
    Retourne
    -1 si la date d1 < d2
    +1 si la date d1 > d2
    0 si les dates sont identiques
    on considère que les dates sont croissantes 
    dans l'ordre chronologique

    >>> date1 = cree_date(15,11,2021)
    >>> date2 = cree_date(10,12,2021)
    >>> compare(date1,date2)
    -1
    >>> compare(date2,date1)
    1
    >>> compare(date1,date1)
    0
    """

    #####################
    #    EXPLICATION    #
    #####################

    """
    Déclaration d'un compteur (parce que j'aime bien les compteurs xD).
    Derification de la date en passant de la valeur la plus forte à la plus faible (année>mois>jour).
    Vérification en 3 forme :
        - si année1 < année2 = -1
        - si année1 > année2 = 1
        - si année1 = année2 = 0, dans ce cas il faut donc passer à la valeur suivante

    si le resultat est différent de 0 la fonction s'arréte et renvoie le resultat 
    

    """

    ################################
    #      CORPS DE FONCTION       #
    ################################
    
    
    compteur:int

    #vérification de la différence entre les années
    if d1['annee'] < d2['annee'] :
        compteur =-1
    elif d1['annee'] > d2['annee'] :
        compteur =1
    else:
        compteur =0 
    
    #vérification de la différence entre les mois
    if compteur == 0 :
        if d1['mois'] < d2['mois'] :
            compteur =-1
        elif d1['mois'] > d2['mois'] :
            compteur =1 
        else:
            compteur =0
    
    #vérification de la différence entre les jours
    if compteur == 0 :
        if d1['jour'] < d2['jour'] :
            compteur =-1
        elif d1['jour'] > d2['jour'] :
            compteur =1
        else:
            compteur =0

    return compteur
    
        
    


# =============================================================================
def valide_simple(d: Dict) -> bool :

    ###############
    #     TEST    #
    ###############

    """   
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - si le premier (le jour) est un entier compris entre 1 et 31
    - si le second (le mois) est un entier compris entre 1 et 12

    >>> date = cree_date(1, 2, 0)
    >>> valide_simple(date)
    True
    >>> date = cree_date(1.5, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(0, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(20, 8, 2021)
    >>> valide_simple(date)
    True
    """

    #####################
    #    EXPLICATION    #
    #####################

    """
    Vérifie si la création de ma date est valide pour pouvoir avancer dans le progamme.

    Vérifie que le nombre de jours est bien comprit entre 1 et 31 et que le nombre de mois soit comprit entre 1 et 12
    retourne un booleen 
    """

    ################################
    #      CORPS DE FONCTION       #
    ################################

    #déclaration de ma vérif sous forme de booleen
    verif:bool

    #Vérifiction de la validité de la date 
    if d == None:
        verif = False
    else:
        verif= True

        #vérification de la validité du nombre de jour
        if verif == True:
            if d['jour'] < 31 and d['jour'] > 0:
                verif = True 
            else:
                verif = False

        #vérification de la validité du nombre de mois
        if verif == True:
            if d['mois'] < 13 and d['mois'] > 0:
                verif = True
            else:
                verif = False


    return verif 

# =============================================================================
def valide_complet(d: Dict) -> bool :

    ###############
    #     TEST    #
    ###############

    """ 
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - la validation simple est vraie
    - si la date représente une date réelle 

    >>> date = cree_date(15, 1, 2022)
    >>> valide_complet(date)
    True
    >>> date = cree_date(32, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(-1, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(31, 6, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(29, 2, 2020)
    >>> valide_complet(date)
    True
    >>> date = cree_date(29, 2, 2022) 
    >>> valide_complet(date)
    False
    """

    #####################
    #    EXPLICATION    #
    #####################

    """
    Vérifie si valid_simple est Vrai

    Annalyse en détaille cette fois-ci
    (suivre les commentaires dans le coprs de la fonction pour plus d'explication)
    """

    ################################
    #      CORPS DE FONCTION       #
    ################################

    #déclaration de ma vérification sous forme de booleen
    verif:bool  

    #vérification de la validité de valide_simple
    if valide_simple(d) == True:
        verif = True
    else:
        verif = False
    
    #si valide_simple vrai 
    if verif == True:

        #pour les mois comportant 31 jours
        if d['mois'] == 1 or d['mois'] == 3 or d['mois'] == 5 or d['mois'] == 7 or d['mois'] == 8 or d['mois'] == 10 or d['mois'] == 12:

            #vérifier si le jour de ce est bien comprit entre 1 et 31
            if d['jour'] > 31 or d['jour'] < 1 :
                verif = False
            else :
                verif = True

        #pour les mois comportant 30 jours
        elif d['mois'] == 4 or d['mois'] == 6 or d['mois'] == 9 or d['mois'] == 11 :

            #vérifier si le jour de ce est bien comprit entre 1 et 30
            if d['jour'] > 30 or d['jour'] < 1 :
                verif = False
            else:
                verif = True

        #pour le mois de février
        elif d['mois'] == 2:
            #utilisation de la fonction 'est_bissextille' pour savoir si l'année comporte 28 ou 29 jours en février
            if est_bissextile(d['annee']) == True :
                
                #vérifier si le jour de ce est bien comprit entre 1 et 29
                if d['jour'] > 29 or d['jour'] < 1:
                    verif = False
                else:
                    verif = True

            else:

                #vérifier si le jour de ce est bien comprit entre 1 et 28
                if d['jour'] > 28 or d['jour'] < 1:
                    verif = False
                else:
                    verif = True
        else:
            verif = False
    
    return verif
        
calendrier = []

# =============================================================================
def ajoute_calendrier(calendrier: List, date: Dict, description: str ) -> NoReturn :

    ###############
    #     TEST    #
    ###############

    """
    ajoute un élément à la liste du calendrier.
    """
    #####################
    #    EXPLICATION    #
    #####################

    """
    #vérification et ajout de donnée dans la liste
    """

    ################################
    #      CORPS DE FONCTION       #
    ################################

    #vérifier si la date est valide avec le 'valide_complet'
    if valide_complet(date) == True:

        #permission d'ajout de descripation que l'on ajoute à notre bibliothéque
        #ajout de la date + description dans la liste calendrier 
        
        description = {'description':description}
        date.update(description)
        calendrier.append(date)
    
    #si la vérif est mauvaise il faut recommencer 
    else:
        print("la date n'est pas correcte, recommencez ! ")
        

    
# =============================================================================
def affiche_calendrier(calendrier: List) -> NoReturn :

    ###############
    #     TEST    #
    ###############

    """
    affiche le calendrier sous forme de liste.
    """
    #####################
    #    EXPLICATION    #
    #####################

    """
    selection du mode d'affichage puis affichage dans le mode choisi
    anglais ou français 
    """

    ################################
    #      CORPS DE FONCTION       #
    ################################

    #affichage d'un message d'aide à la selection de l'affichage, puis choix de l'affichage
    print("pour un affichage Français, ecrivez 'fr' ")
    print("pour un affichage Anglais, ecrivez 'gb' ")
    langue = str(input("Quelle affichage voulez vous ? : "))

    #pour le français 
    if langue == "fr":

        #compte la position des données pour pouvoir les afficher à la suite dans les {}
        #chaque i=i+1 permet de passer dans la {} suivante 
        for i in range(len(calendrier)):
            print(" Le {}/{}/{} : {} ".format(calendrier[i]['jour'],calendrier[i]['mois'],calendrier[i]['annee'],calendrier[i]['description']))
            i=i+1

    #pour l'anglais
    elif langue == "gb":
        #effectue la même chose que pour le français, mais le mois et le jour sont donc inversée cette fois-ci
        for i in range(len(calendrier)):
            print(" Le {}/{}/{} : {} ".format(calendrier[i]['mois'],calendrier[i]['jour'],calendrier[i]['annee'],calendrier[i]['description']))
            i=i+1

# =============================================================================    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    #voici mes print test pour chaque fonction jusqu'a valid_complet

    print()
    print("votre année est bissextille",est_bissextile(2020))
    print("Entrez votre date:",cree_date(1.5,12,2020))
    print("La date copié est:",copie_date({'jour': 15, 'mois': 12, 'annee': 2020}))
    print("Entrez les dates une et deux:",compare(cree_date(15,11,2021),cree_date(15,11,2021)))
    print("Entrer la date à verifier: ",valide_simple(cree_date(1,2,0)))
    print("Verif au max",valide_complet(cree_date(29,2,2020)))
    print()
    
    choix=0

    
    print("                           MENU                             ")
    print()
    print("1 - Vérifier que votre année est bissextille")
    print("2 - Pour entrer une date")
    print("3 - Pour savoir si votre date est supérieur à une autre")
    print("4 - Pour faire une vériification simple de votre date")
    print("5 - Pour faire une vérification complete de votre date")
    print("6 - Finir le programme")
    print()

    while choix !=9:
        choix = int(input("Veuillez choisir une option :"))
        if choix == 1:
            annee=int(input("choisir une année: "))
            print("l'année est bissextille",est_bissextile(annee))

        elif choix == 2:
            jour=int(input("entrer le numéro du jour: "))
            mois=int(input("entrer le mois: "))
            annee=int(input("entrer l'année: "))
            print(cree_date(jour,mois,annee))

        elif choix == 3:
            jour1=int(input("entrer le numéro du jour 1: "))
            mois1=int(input("entrer le mois 1: "))
            annee1=int(input("entrer l'année 1: "))
            jour2=int(input("entrer le numéro du jour 2: "))
            mois2=int(input("entrer le mois 2: "))
            annee2=int(input("entrer l'année 2: "))
            print(" -1 = inférieur ")
            print(" 1 = supérieur")
            print(" 0 = égale")
            print("Resultat",compare(cree_date(jour1,mois1,annee1),cree_date(jour2,mois2,annee2)))

        elif choix == 4:
            jour=int(input("entrer le numéro du jour: "))
            mois=int(input("entrer le mois: "))
            annee=int(input("entrer l'année: "))
            print("La date à vérifier est : ",valide_simple(cree_date(1,2,0)))


        elif choix == 5:
            jour=int(input("entrer le numéro du jour: "))
            mois=int(input("entrer le mois: "))
            annee=int(input("entrer l'année: "))
            print("l'année est :",valide_complet(cree_date(jour,mois,annee)))

        
        elif choix == 6:
            print("---------\nFin du programme, à la prochaine !\n---------")



            

# %%
