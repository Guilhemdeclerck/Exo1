def listSum(l, i=0):
    if i==len(l):
        return 0
    return listSum(l, i+1) + l[i]

print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11

