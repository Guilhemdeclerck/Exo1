def listetri(liste):
    liste1 = []
    for i in range(0, len(liste)):
       if liste[i]%2 == 0 :
           liste1.append(liste[i])
       else: del(liste[i])
    return liste1


list = [3, 9, 2, 4, 7, 6, 5, 1]
resultat = listetri(list)
print(resultat)
