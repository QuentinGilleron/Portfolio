def valeur(x: int, y: int)-> int:
    x=x+y
    y=x-y
    y=x-y
    print("(x,y)=",x,y)
    return

if __name__=="__main__":
    x=int(input("entrer la valeur entiere: "))
    y=int(input("entrer la valeur entiere: "))
    valeur(x,y)
