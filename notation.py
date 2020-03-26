def notation(calcul):
    liste= split("calcul")
    longeurliste = len(liste)
    for i in range(-1,-longeurliste,-1):
        if isdigit(i) == False :
            liste.append(i, i-2)
    resultat = eval(liste)
    print(resultat)
