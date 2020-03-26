from Filiale import *
class ingejunior(Ingenieur):
    def __init__(self, nombreanneeexperience, nombreheureprojet, nombreheuregestion):
        Ingenieur.__init__(self, nombreheureprojet, nombreheuregestion)
        self.__nbranneexp = nombreanneeexperience

    def afficher(self):
        print("* [id=", self._id, "] Nom et Prénom :", self._nom, self._prenom, "Salaire :", self._salaire, "Statut : Administratif, Année d'embauche:", self._anneeembauche)
        print("Site :", self.getpays(), ", Nombre de jour de Travail :", self._nombrejourtravail, ", Nombre heure projet :", self._nombreheureprojet, ", Nombre heure gestion :", self._nombreheuregestion,
              ", Nombre année expérience :", self.__nbranneexp)
