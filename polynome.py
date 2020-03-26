from monome import *

class polynome :
    def __init__(self, racine):
        self.__monomeracine = racine


    def evaluation(self, x, d ,c):
        degres = monome(d)
        coefficient = monome(c)
        evaluation = coefficient*(x**degres)
        return  evaluation

    def plusgrandndegres(self, c, d, nextmonome):
        newmonome = monome(c, d, self.__monomeracine)
        monomecurrent = self.__monomeracine
        while monomecurrent.getterdegres() > nextmonome.getterdegres():
            monomecurrent = monomecurrent.getterdegres()
            monomecurrent.setterdegres(newmonome)
        return monomecurrent

    def suppression(self, d):
        monome = self.__monomeracine
        degres = monome(d)
        if degres == 0 :
            del(monome)

    def affichagedecroissant(self):
        print(self.__monomeracine, "+", monome1, "+", monome2)

    def affichagecroissant(self):
        print(monome2, "+", monome1, "+", self.__monomeracine)
