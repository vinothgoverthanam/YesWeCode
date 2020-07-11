from itertools import  permutations

R=int(input("enter the target number"))
N=int(input("enter the size of the array :"))
p="enter the integer"
lista=[]

for i in range(N) :
    K=int(input(("%s %d ") % (p,i)))
    lista.append(K)

solutions = [pair for pair in permutations(lista, 2) if sum(pair) == R]
print('Solutions:', solutions)
print (set(map(frozenset, solutions)))
