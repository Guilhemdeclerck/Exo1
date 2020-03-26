from Multinationale import  *
from Filiale import  *
#from Salarie import *
#from Employe import *
from Directeur import *
from IngeJunior import *
from IngeSenior import *
from Admin import *


Multinationale = multinational("RCAT", "France")
F1 = filiale("RCTA-Belgique", "Belgique", 2000)
F2 = filiale("RCTA-Maroc", "Maroc", 2010)
F3 = filiale("RCTA-Tunisie", "Tunisie", 1950)
F4 = filiale("RCTA-Angleterre", "Angleterre", 2005)
Multinationale.ajouterfiliale(F1)
Multinationale.ajouterfiliale(F2)
Multinationale.ajouterfiliale(F3)
Multinationale.ajouterfiliale(F4)
D1 = directeur("Jambon", "Beur", 8, 210, 1960)
F3.ajoutsalarie(D1)
A1 = admin("Jean", "Michel", 2, 300, 2003, 562, "RH")
IJ1 = ingejunior("Will", "Fred", 7, 230, 2005, 809, 64, 50, 4)
F1.ajoutsalarie(A1)
F1.ajoutsalarie(IJ1)
IS1 = ingesenior("Jean", "Hugue", 9, 126, 2000, 9004, 6050, 800, "responsable prod" )
F2.ajoutsalarie(IS1)

Multinationale.affichagemulti()
F1.affichagesalarie()
F2.affichagesalarie()
F3.affichagesalarie()
F4.affichagesalarie()
