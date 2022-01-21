from typing import Final
if __name__=="__main__":
    poids:float
    taille:float
    imc:float
    taille=input("saisir votre taille en mètres:")
    taille=float(taille)
    poids=input("saisir votre poids en kilos:")
    poids=float(poids)
    imc=poids/(taille*taille)
    if imc<18.5:
        print("vous etes en insuffisance pondérale",imc)
    elif imc<=25:
        print("vous avez une corpulence normale",imc)
    elif imc<=30:
        print("vous etes en surpoids",imc)
    elif imc<=35:
        print("vous etes en obesité modérée",imc)
    else:
        print("vous etes en obésité sévere",imc)
        