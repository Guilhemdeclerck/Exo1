from Filiale import *
class directeur(salarie):
    def __init__(self, anneenomination, nom, prenom, salaire, identifiant):
        salarie.__init__(self, nom, prenom, salaire, identifiant)
        self.__anneenom = anneenomination

    def afficher(self):
        print("* [id=", self._id, "] Nom et Prénom :", self._nom, self._prenom, "Salaire :", self._salaire, "Statut : Directeur, Année de nomination:", self.__anneenom)
        print("Site :", self.getpays())
