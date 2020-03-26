def newstack():
    pile = []
    return pile

def push(s,e):
    s.append(e)

def top(s):
    return s[-1]

def pop(s):  #  Retire et renvoie l’élément en haut de la pile "s" si elle est non vide
    if s!=[]:
        dernier=s[len(s)-1]
        del s[len(s)-1] #supprime toute la liste
        return dernier

def isEmpty(s):
    taille = len(s)
    if taille == 0 :
        return True
    else:
        return False

def size(s):
    return len(s)
