from Filiale import *
class admin(employe):
    def __init__(self, service, anneeembauche, nombrejourtravail):
        Employe.__init__(self, anneeembauche, nombrejourtravail)
        self.__service = service

    def afficher(self):
        print("* [id=", self._id, "] Nom et Prénom :", self._nom, self._prenom, "Salaire :", self._salaire, "Statut : Administratif, Année d'embauche:", self._anneeembauche)
        print("Site :", self.getpays(), ", Nombre de jour de Travail :", self._nombrejourtravail, ", Service :", self.__service)

        print("* [id=", self._id, "] Nom et Prénom :", self._nom, self._prenom, "Salaire :", self._salaire, "Statut : Administratif, Année d'embauche:", self._anneeembauche)
        print("Site :", self.getpays(), ", Nombre de jour de Travail :", self._nombrejourtravail, ", Service :", self.__service)
