### Programme Calculette ###
# Ce programme simule quelques opérations basiques d'une calculatrice.
# Le code étant inclut dans un unique programme principal,
# il est inutile d'importer ce module dans un autre.
# (Code source libre sans licence)

# Exercice : comme pour le TD correspondant, extraire les fonctions indiquées.
def addition(n1,n2):
    #cette fonction fait une addition
    return(n1+n2)

def soustraction(n1,n2):
    #cette fonction fait une soustraction
    return(n1-n2)

def multiplication(n1,n2):
    #cette fonction fait une multiplication
    return(n1*n2)

def division(n1,n2):
    #cette fonction fait une division
    return(n1/n2)

def division_reelle(n1,n2,):
    #cette procédure donne le quotient et le reste
    quotient=n1//n2
    rest=n1%n2
    return(quotient,rest)

def puissance(n1,exposant):
    #cette fonction donne la puissance d'un nombre
    result=1
    i=0
    while (i<exposant):
        result=multiplication(result,n1)
        i=i+1
    return(result)

if __name__ == "__main__":
    nombre1:float;nombre2:float;resultat:float
    nombre1str:str;nombre2str:str;operateur:str
    nombre2int:int;i:int

    print("\nCalculette : saisir deux nombres séparés par un opérateur pour obtenir le résultat.")
    print("Attention : un espace doit séparer chaque élément.")
    print("Les opérateurs reconnus sont : + (addition), - (soustraction), / (division réelle),")
    print("                               d (division entière), p (puissance) et")
    print("                               s (sortie du programme sans prendre en compte les 2 nombres).")

    operateur=''
    while operateur!='s':
        nombre1str,operateur,nombre2str=input('? ').split() # permet de lire les 3 variables séparées par des espaces
        nombre1=float(nombre1str)
        nombre2=float(nombre2str)
        if operateur=='+':
            print("=",addition(nombre1,nombre2))
        elif operateur=='-':
            print("=",soustraction(nombre1,nombre2))
        elif operateur=='*':
            print("=",multiplication(nombre1,nombre2))
        elif operateur=='/':
            print("=",division(nombre1,nombre2))
        elif operateur=='d': # division entière
            print("quotient et reste =",division_reelle(nombre1,nombre2))
        elif operateur=='p': # puissance : attention l'exposant doit être un entier
            print("=",puissance(nombre1,nombre2))
        elif operateur=='s':
            print("Sortie du programme.")
        else:
            print("L'opérateur",operateur,"n'est pas reconnu par la calculette.")
            print("\nCalculette : saisir deux nombres séparés par un opérateur pour obtenir le résultat.")
            print("Attention : un espace doit séparer chaque élément.")
            print("Les opérateurs reconnus sont : + (addition), - (soustraction), / (division réelle),")
            print("                               d (division entière), p (puissance) et")
            print("                               s (sortie du programme sans prendre en compte les 2 nombres).")