from Filiale import *
class employe(Salarie):
    def __init__(self, anneeembauche, nombrejourtravail, nom, prenom, salaire, identifiant):
        Salarie.__init__(self, nom, prenom, salaire, identifiant)
        self._anneeembauche = anneeembauche
        self._nbrjtravail = nombrejourtravail

    def afficher(self):
        pass
