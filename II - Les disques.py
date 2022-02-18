##########################
#Déclaration de constante#
##########################

const Max_artistes=10
max_morceau=30
max_disque=500

#######################
#Déclaration des types#
#######################
type
    un_disque=enregistrement
    titre:cc
    interprétes:artiste,NB_interprétes:entier
    interpréte:c
    nb_morceaux:entier
    durée:tableau[1..max_morceau]de type reel
    année:entier
    finenrgistrement

une_etagere=tableau[1..max_disque]de type un_disque

#############################
#Déclaration de la procédure#
#############################


procédure disque(D1:disque,var D2:disque)
#copie du disque
var i:entier
debut 
    D2.titre:=D1.titre
    D2.NB_interprétes:=D1.NB_interprétes
    pour i allant de 1 à Max_artistes faire
        D2.interpréte[i]:=D1.interpréte[i]
    fpour
    D2.nb_morceaux:=D1.nb_morceaux
    D2.durée:=D1.durée
    D2.année:=D2.année
fin


###########################
#Déclaration des variables#
###########################

var musique:un_disque

Var mon_disque:un_disque


######################
#Programme princiaple#
######################

(musique.titre:="album blanc")
(musique.interpréte:="Beatles")
(musique.titre:="The Beatles")
(musique.nb_morceaux:=30)
(musique.durée:=93,75)
(musique.année:=1968)

type artiste=tableau[1..Max_artistes]de type cc

mon_disque.titre:="Disuqe bleu"
mon_disque.durée:="99,34"
mon_disque.année:=1973
mon_disque.nb_morceaux:=28

mon_disque.durée[4]:=4.30