class multinational:
    def __init__(self, nom, paysorigine, filiale= []):
        self.__nm = nom
        self.__piorgn = paysorigine
        self.__filiale = filiale


    def ajouterfiliale(self, filiale):
        self.__filiale.append(filiale)
        return self.__filiale

    def affichagemulti(self):
        print("La multinationale RCAT est composé de", len(self.__filiale), "filiales. Son pays d'origine est", self.__piorgn)
