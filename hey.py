#Racine
NoeudRacine = Node(12,17,5)
Tree = BinaryTree(NoeudRacine)

#Gauche
Filsgauche1 = Node(NoeudRacine.getleft(),6,4)
Filsgauche2 = Node(Filsgauche1.getleft(),None,3)
Filsgauche3 = Node(Filsgauche2.getleft(),None,None)
Filsgauchedroite = Node(Filsgauche1.getright(),None,None)

#Droite
Filsdroite1 = Node(NoeudRacine.getright(), 19, None)
Filsdroite2 = Node(Filsdroite1.getright(),21,18)
Filsdroite3 = Node(Filsdroite2.getright(),None,None)
Filsdroitedroitegauche = Node(Filsdroite2.getleft(),None, None)

print(Tree.Size(Tree.getroot()))

