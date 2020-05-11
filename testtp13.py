from Exo1bistp13 import *

N21 = Node(21, None, None)
N18 = Node(18, None, None)
N3 = Node(3, None, None)

N19 = Node(19, N21, N18)
N4 = Node(4, None, N3)
N6 = Node(6, None, None)

N17 = Node(17, N19, None)
N5 = Node(5, N6, N4)

N12 = Node(12, N17, N5)
Tree = BinaryTree(N12)

print(Tree.Size(Tree.getroot()))

#def size(self, node):
#if node is None:
#return 0
#else:
#return self.size(node.getLeft()) + 1 + self.size(node.getRight())
##############
#def printValues(self, node):
#if node is None:
#return ""
#else:
#return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())
