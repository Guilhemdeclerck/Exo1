from pile import *

def deque(str2):
    s = newstack()
    str1 = str2.split()
    for i in str1 :
        if i.isdigit() == True :
            push(s, i)
        else :
            a = pop(s)
            b = pop(s)
            lst = a + i + b
            tpm = eval(lst)
            push(s,str(tpm))
    return pop(s)

chaine = str(input("entrez une chaine de caracteres : "))
print(deque(chaine))
