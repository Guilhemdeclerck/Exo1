from pile import *

def parenthese(chaine):
    liste = [chaine]
    s = newstack()
    for elt in liste:
        if elt == "(":
            push(s, elt)
        elif elt == ")":
            pop(s,top(s))
    if isEmpty(s) == True:
        print("le calcul peut être executé")
    else: print("error")

chaine1 = "(8*(4+(3*3)))"
parenthese(chaine1)
