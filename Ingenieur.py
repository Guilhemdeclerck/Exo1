class ingenieur(Employe):
    def __init__(self, nombreheureprojet, nombreheuregestion, anneeembauche, nombrejourtravail):
        Employe.__init__(self, anneeembauche, nombrejourtravail)
        self._nbrhprojet = nombreheureprojet
        self._nbrhgestion = nombreheuregestion

    def afficher(self):
        pass
