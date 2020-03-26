class filiale:
    def __init__(self, nom, pays, datecreation = [], salarie = [], salarieplusancienne = []):
        self.__nom = nom
        self.__pays = pays
        self.__dtcrea = datecreation
        self.__salarie = salarie
        self.__salarieplusancienne = salarieplusancienne
        #self.__datecreationlaplusancienne = 0

    def getpays(self):
        return self.__pays

    def triplusancienne(self, datecreation):
        self.__nom = self.__dtcrea
        self.__dtcrea.append(datecreation)
        self.__dtcrea.sort()
        self.__dtcrea[0] = self.__nom
        return self.__dtcrea[0]

    def ajoutsalarie(self, salarie):
        self.__salarie.append(salarie)
        if self.__nom == self.__dtcrea[0] :
            self.__salarieplusancienne.append(salarie)
        return len(self.__salarieplusancienne)
        return len(self.__salarie)

    def supprimersalarie(self, salarie):
        del


    #def tridatecreation(self, datecreation):
        #self.__dtcrea.append(datecreation)
        #self.__dtcrea.sort()
        #self.__datecreationlaplusancienne = self.__dtcrea[0]


    def affichagesalarie(self):
        print("La filiale la plus ancienne de cette multinationale :", self.__dtcrea[0] , ". Elle est composée de", len(self.__salarie) ,"salariés." )
        print("RCAT est composé de", self.__salarie, "salariés :")
